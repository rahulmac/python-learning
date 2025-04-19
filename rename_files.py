import os

folder_path="files"

# os for file handling
# enumerate for indexing

files = sorted(os.listdir(folder_path))

for index, filename in enumerate(files, start=1):
    if(filename.endswith(".txt")):
        new_name = f"text_{str(index).zfill(5)}.txt"
        # zfill to pad the number
        src = os.path.join(folder_path,filename)
        dst = os.path.join(folder_path, new_name)
        os.rename(src,dst)
        print(f"Renamed: {filename} → {new_name}")
                