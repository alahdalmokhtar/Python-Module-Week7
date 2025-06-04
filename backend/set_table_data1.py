from .list_files_oldwerk import list_files
from .download_file import download_file
from .read_xlsx import read_excel
""" def set_table_date(window,file_name):
    drive_files=list_files()
    file_id=None
    for file in drive_files:
        if file['name']==file_name:
            file_id=file['id']
            download_file(file_id)
            break
    rows=read_xlsx(file_name)
  
    headers=[header for header in rows[0] if header is not None]
    window.tableWidget.clear()
    window.tableWidget.setColumnCount(len(headers))
    window.tableWidget.setRowCount(len(rows)-1)  # Exclude header row -1 

    for col, header in enumerate(headers):
        if header == 'None' or header in [None]:
            continue
        item=QTWidgets.QTableWidgetItem()
        item.setText(header)
        window.tableWidget.setHorizontalHeaderItem(col, item) """
# backend/set_table_data.py
from backend.list_files_oldwerk import list_files

def set_table_date(application, filename):
    try:
        # Get files with proper error handling
        drive_files = list_files()
        
        # Debug print to verify files
        print("Files in set_table_date:", drive_files)
        
        # Check if we got valid results
        if not drive_files:
            print("Warning: No files returned from list_files()")
            return False
            
        # Process files
        processed_files = []
        for file in drive_files:
            print(f"Processing file: {file['name']}")
            # Add your file processing logic here
            processed_files.append(file)
            
            # Special handling for target filename
            if file['name'] == filename:
                print(f"Found target file: {filename}")
                # Add your specific processing here
                
        return bool(processed_files)  # Return True if files processed
        
    except Exception as e:
        print(f"Error in set_table_date: {e}")
        return False
    """ # backend/set_table_data.py
from backend.list_files_oldwerk import list_files

def set_table_date(application, filename):
    try:
        # Get files with proper error handling
        drive_files = list_files()
        
        # Debug print to verify files
        print("Files in set_table_date:", drive_files)
        
        # Check if we got valid results
        if not drive_files:
            print("Warning: No files returned from list_files()")
            return False
            
        # Process files
        processed_files = []
        for file in drive_files:
            print(f"Processing file: {file['name']}")
            # Add your file processing logic here
            processed_files.append(file)
            
            # Special handling for target filename
            if file['name'] == filename:
                print(f"Found target file: {filename}")
                # Add your specific processing here
                
        return bool(processed_files)  # Return True if files processed
        
    except Exception as e:
        print(f"Error in set_table_date: {e}")
        return False
# backend/set_table_data.py
from .list_files import list_files
import sys

def set_table_date(application, filename):
    try:
        # Explicitly get the files
        drive_files = list_files()
        print("Debug: Received files in set_table_date:", drive_files, file=sys.stderr)
        
        if not drive_files:  # Checks for both None and empty list
            print("Warning: No files available to process", file=sys.stderr)
            return False
            
        # Process files
        for file in drive_files:
            print(f"Processing file: {file['name']} (ID: {file['id']})", file=sys.stderr)
            if file['name'] == filename:
                print(f"Found target file: {filename}", file=sys.stderr)
                # Add your file processing logic here
                return True
                
        print(f"Target file {filename} not found", file=sys.stderr)
        return False
        
    except Exception as e:
        print(f"Error in set_table_date: {e}", file=sys.stderr)
        return False
        """
