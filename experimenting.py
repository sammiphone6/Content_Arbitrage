import requests

def host_file_online(downloaded_file_name):
    files= {
        'reqtype': (None, 'fileupload'),
        'time': (None, '1h'),
        'fileToUpload': open(downloaded_file_name, 'rb'),
    }
    response = requests.post('https://litterbox.catbox.moe/resources/internals/api.php', files=files)
    return response.text


for i in range(1, 5):
    print(host_file_online(f'{i}.mp4'))