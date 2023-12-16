import gdown
import os

#HOW TO USE
# Simply run this file to start downloading the model file BEFORE you run the program (GUI.py)

#program to allow users to download the model file
def download_file_from_google_drive(file_id, output_file):
    url = f'https://drive.google.com/uc?id={file_id}'
    gdown.download(url, output_file, quiet=False)

#file id of the model in Google Drive
file_id = '16oFvuaz4LKLhPeXpXThmbOvHEGL_gCUI'
output_directory = 'identifier'
output_file = os.path.join(output_directory, 'keras_model.h5')

#add the output directory if the directory doesnt already exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

download_file_from_google_drive(file_id, output_file)

print(f"File '{output_file}' downloaded successfully.")

