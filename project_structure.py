import os
from pathlib import Path

project_dir = Path(__file__).resolve().parent
print(f"project_dir:{project_dir}")

file_system_list = [".github/workflows/mlpipeline.yml",
                    "abcd.py"]

for files_details in file_system_list:
    files_details = Path(files_details)
    file_dir, file_name = os.path.split(files_details)

    if file_dir != '':
        os.makedirs(file_dir, exist_ok=True)
        print(f"Directory {file_dir} created")
    
    if (not os.path.exists(files_details)) or (not files_details.is_file()) or (os.path.getsize(files_details) == 0):
        with open(file=files_details, mode='w') as f:
            pass
        print(f"File: {files_details}has been created")
    else:
        print(f"File {files_details} already exists")
