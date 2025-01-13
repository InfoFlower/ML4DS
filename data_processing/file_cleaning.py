#Fait par IA
import os

def delete_empty_txt_files(directory,info=False):
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            if os.path.getsize(file_path) == 0:
                os.remove(file_path)
                if info:
                    print(f"{filename} deleted")