import gdown
import os

def download_file_from_google_drive(file_id, output_file):
    url = f'https://drive.google.com/uc?id={file_id}'
    gdown.download(url, output_file, quiet=False)

# Replace 'YOUR_GOOGLE_DRIVE_FILE_ID' with the actual file ID of the file you want to download
file_id = '16oFvuaz4LKLhPeXpXThmbOvHEGL_gCUI'
output_directory = 'identifier'
output_file = os.path.join(output_directory, 'keras_model.h5')

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

download_file_from_google_drive(file_id, output_file)

print(f"File '{output_file}' downloaded successfully.")
