from pexelsapi.pexels import Pexels
import os
import requests

# Function to download and save an image
def download_and_save_image(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)

# Initialize Pexels API
pexel = Pexels('bdtHuI2PpcFVa2z3DuJUZITxnQZ2VWouoNrxzvC6rMD28tWyLTFb2FSC')

# Search for photos
query= input("Enter the prompt :")
search_photos = pexel.search_photos(query, per_page=4)

# Specify the directory to save images
save_directory = 'downloaded_images1'

# Create the directory if it doesn't exist
os.makedirs(save_directory, exist_ok=True)

# Download and save each image
for photo in search_photos['photos']:
    image_url = photo['src']['original']
    image_name = f"{photo['id']}.jpg"  # You can adjust the naming convention
    image_path = os.path.join(save_directory, image_name)

    download_and_save_image(image_url, image_path)
    print(f"Image '{image_name}' saved to '{save_directory}'")