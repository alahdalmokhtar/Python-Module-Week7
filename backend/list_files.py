
# backend/list_files.py
from googleapiclient.discovery import build
from .auth import auth
import sys

def list_files():
    try:
        creds = auth()
        if not creds:
            print("Authentication failed", file=sys.stderr)
            return []  # Return empty list instead of None
            
        service = build('drive', 'v3', credentials=creds)
        
        # Call the Drive API
        results = service.files().list(
            pageSize=10,
            fields="nextPageToken, files(id, name)"
        ).execute()
        
        files = results.get('files', [])
        print("Debug: Files retrieved from API:", files)  # Debug output
        return files
        
    except Exception as e:
        print(f"Error in list_files: {e}", file=sys.stderr)
        return []  # Always return a list, never None