import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from auth import auth

def list_files():
  """Shows basic usage of the Drive Labels API.

    Prints the first page of the customer's Labels.
  """
  creds = auth()
  
  try:
    service = build('drivelabels', 'v2', credentials=creds)
    response = service.labels().list(
        view='LABEL_VIEW_FULL').execute()
    labels = response['labels']

    if not labels:
      print('No Labels')
    else:
      for label in labels:
        name = label['name']
        title = label['properties']['title']
        print(u'{0}:\t{1}'.format(name, title))
      return labels
  except HttpError as error:
    # TODO (developer) - Handle errors from Labels API.
    print(f'An error occurred: {error}')

if __name__ == '__main__':
  list_files()