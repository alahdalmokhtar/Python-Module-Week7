import io

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
from .auth import auth

def download_file(real_file_id):
  """Downloads a file
  Args:
      real_file_id: ID of the file to download
  Returns : IO object with location.

  Load pre-authorized user credentials from the environment.
  TODO(developer) - See https://developers.google.com/identity
  for guides on implementing OAuth2 for the application.
  """
  creds= auth()

  try:
    # create drive api client
    service = build("drive", "v3", credentials=creds)
    file_id = real_file_id
    file_metadata = service.files().get(fileId=file_id).execute()
    name= file_metadata.get("name")
    

    # pylint: disable=maybe-no-member
    request = service.files().get_media(fileId=file_id)
    file = io.BytesIO()
    downloader = MediaIoBaseDownload(file, request)
    done = False
    #  Download the file 
    while done is False:
      status, done = downloader.next_chunk()
      print(f"Download {int(status.progress() * 100)}.")
    #save file
    with open(name, "wb") as f:
      f.write(file.getvalue())
    

  except HttpError as error:
    print(f"An error occurred: {error}")
    file = None

  if file is not None:
    return file.getvalue()
  else:
    print("Download failed. No content returned.")
    return None



if __name__ == "__main__":
  download_file(real_file_id="1FJjIzyrK5D8uPVB95nRyyMlnnncVO7P1") # applocation.xlsx
  #download_file(real_file_id="1-6FvC5dIP8A2WoUAWJIAG5n-7H48AO5z") # user.xlsx
  #download_file(real_file_id="1aaffd7rrjHmytov91D36xd1vViEJJlqW") # interview.xlsx
  #download_file(real_file_id="1yOq_Yn1081l2eAJyYCqp1AOJDuFssOEB") # mentor.xlsx
 