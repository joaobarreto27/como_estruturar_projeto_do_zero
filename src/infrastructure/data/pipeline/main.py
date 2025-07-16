from pathlib import Path
import os
import glob
folder_name = "input"
extension_type = "xlsx"
current_dir = Path(__file__).resolve().parents[1]
path = os.path.join(current_dir,folder_name)

all_files = os.path.join(path, "*.", extension_type)
print(all_files)
all_files = glob.glob(os.path.join(path, f"*.{extension_type}"))
print(path)
print(all_files)