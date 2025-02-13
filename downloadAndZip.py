import requests
from zipfile import ZipFile 


dataUrl = "https://upload.itcollege.ee/~aleksei/random_files_without_extension.zip"


response = requests.get(dataUrl)
filePath = './downloaded_random_files'
zipFilePath = filePath + ".zip"


if response.status_code == 200:
    with open(zipFilePath, 'wb') as file:
        file.write(response.content)
    print('File downloaded successfully')
    with ZipFile(zipFilePath, 'r') as zip:
        zip.extractall(filePath)
        zip.close()
        print('File unpacked successfully')
else:
    print('Failed to download file')

