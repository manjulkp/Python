import os
import shutil

desktop_path = os.path.expanduser("~/Desktop")
print("desktop path " , desktop_path)

folders = {
    "Images" : [".jpeg" , ".jpg" , ".png"],
    "Documents" : [".doc" , ".pdf"],
    "Archives" : [".zip" , ".rar"] 
}

# create folders for Image , Document , Archives if they are not present
for folder_name in folders:
    folder_path = os.path.join(desktop_path , folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        
for file_name in os.listdir(desktop_path):
     original_file_path = os.path.join(desktop_path , file_name)
     
     if os.path.isfile(original_file_path):
         for folder_name , extension in folders.items():
             for ext in extension :
                 if file_name.endswith(ext):
                    dest_path = os.path.join(desktop_path , folder_name)
                    shutil.move(original_file_path , dest_path)
                 
     
     
        

    