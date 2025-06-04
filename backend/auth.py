import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# الصلاحيات المطلوبة: صلاحية كاملة على Google Drive
SCOPES = ['https://www.googleapis.com/auth/drive',
          'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/drive.metadata.readonly']

def auth():
    """تنفيذ المصادقة وإرجاع الاعتماد (credentials)."""
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def list_drive_files():
    """يعرض قائمة بأسماء الملفات الموجودة في Google Drive."""
    creds = auth()
    try:
        service = build('drive', 'v3', credentials=creds)

        # طلب الملفات
        results = service.files().list(
            pageSize=10,  # عدد الملفات التي سيتم عرضها
            fields="files(id, name)"
        ).execute()
        items = results.get('files', [])

        if not items:
            print('❌ لا توجد ملفات.')
            return

        print('📂 الملفات الموجودة على Google Drive:')
        for item in items:
            print(f"- {item['name']} (ID: {item['id']})")

    except HttpError as error:
        print(f"حدث خطأ: {error}")

if __name__ == '__main__':
    list_drive_files()
