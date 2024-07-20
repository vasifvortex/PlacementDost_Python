import requests
def download_image(url, file_name):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(file_name, 'wb') as file:
                file.write(response.content)
            print(f"Image successfully downloaded: {file_name}")
        else:
            print(f"Failed to retrieve image. HTTP Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

image_url = 'https://static1.cbrimages.com/wordpress/wp-content/uploads/2019/12/Hisoka-Featured-Image.jpg'
file_name = 'downloaded_image.jpg'
download_image(image_url, file_name)