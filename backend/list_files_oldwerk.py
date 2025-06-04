import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from .auth import auth

def list_files():
    """Lists the first 10 files in the user's Google Drive."""
    creds = auth()

    try:
        # الاتصال بخدمة Google Drive API
        service = build('drive', 'v3', credentials=creds)

        # جلب أول 10 ملفات
        results = service.files().list(
            pageSize=10,
            fields="nextPageToken, files(id, name)"
        ).execute()

        items = results.get('files', [])
        #return items

        if not items:
            print('No files found.')
        else:
            print('Files:')
            for item in items:
                print(f"{item['name']} (ID: {item['id']})")

    except HttpError as error:
        print(f'An error occurred: {error}')

if __name__ == '__main__':
    list_files()
