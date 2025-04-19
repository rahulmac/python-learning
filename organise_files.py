import os
import shutil

folder_path="myfiles"
files = os.listdir(folder_path)

files_extensions = {
"Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Spreadsheets": [".xlsx", ".xls", ".csv"],
    "Music": [".mp3", ".wav"],
    "Code": [".py", ".js", ".html", ".css"]
}

for file_name in files:
    file_ext = os.path.splitext(file_name)[1]
    src_path = os.path.join(folder_path, file_name)
    
    if os.path.isdir(src_path):
        continue
    
    for folder, extension in files_extensions.items():
        if file_ext.lower() in extension:
            dest_folder = os.path.join(folder_path, folder)
            os.makedirs(dest_folder, exist_ok=True)
            
            
            dst_path = os.path.join(dest_folder, file_name)
            shutil.move(src_path, dest_folder)
            print(f"Moved: {file_name} → {folder}/")
            
            