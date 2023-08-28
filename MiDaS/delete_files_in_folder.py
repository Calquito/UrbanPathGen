import os

def delete_files_in_folder(folder_path):
    try:
        # Get list of files in folder
        files = os.listdir(folder_path)

        for file in files:
            file_path = os.path.join(folder_path, file)
            
            # Check if is file (no directory)
            if os.path.isfile(file_path):
                os.remove(file_path)
    except Exception as e:
        print(f"Error deleting files: {e}")