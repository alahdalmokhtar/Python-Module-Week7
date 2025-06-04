import datetime
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Full calendar access scope
SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_authenticated_service():
    """Authenticate and return the calendar service"""
    creds = None
    
    # The file token.json stores the user's access and refresh tokens
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # If there are no (valid) credentials available, let the user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    return build('calendar', 'v3', credentials=creds)

def list_calendars(service):
    """List all accessible calendars for debugging"""
    print("\nListing all calendars:")
    calendars = service.calendarList().list().execute()
    for calendar in calendars.get('items', []):
        print(f"ID: {calendar['id']}, Name: {calendar['summary']}")

def get_upcoming_events(service, max_results=10):
    """Get upcoming events from primary calendar"""
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    print(f"\nGetting the upcoming {max_results} events from primary calendar")
    
    events_result = service.events().list(
        calendarId='primary',
        timeMin=now,
        maxResults=max_results,
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    
    events = events_result.get('items', [])
    
    if not events:
        print("No upcoming events found.")
        return
    
    print("\nUpcoming events:")
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(f"{start} - {event.get('summary', 'No title')}")

def main():
    try:
        service = get_authenticated_service()
        
        # Debugging: List all accessible calendars
        list_calendars(service)
        
        # Get upcoming events
        get_upcoming_events(service)
        
    except HttpError as error:
        print(f'\nAn error occurred: {error}')
    except Exception as error:
        print(f'\nUnexpected error: {error}')

if __name__ == '__main__':
    # First delete old token file if exists
    if os.path.exists('token.json'):
        os.remove('token.json')
    main()