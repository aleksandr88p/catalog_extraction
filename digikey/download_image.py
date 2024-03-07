import requests
import base64


def download_image(image_url: str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Alt-Used': 'mm.digikey.com',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'If-Modified-Since': 'Wed, 28 Dec 2022 17:03:20 GMT',
        'If-None-Match': '"6af19549de1ad91:0"',

    }

    response = requests.get(f'https:{image_url}', headers=headers)
    if response.status_code == 200:
        image_name = image_url.split('/')[-1]
        # Сохранение изображения в файл
        with open(f"{image_name}.jpg", "wb") as file:
            file.write(response.content)
        print("Image saved.")

        # Конвертация изображения в base64
        image_base64 = base64.b64encode(response.content).decode('utf-8')
        print("Image converted to base64.")

        # Сохранение base64 в файл для демонстрации
        image_base_65_name = image_url.split('/')[-1].replace('.jpg', '-').replace('png', '_')
        with open(f"{image_base_65_name}.txt", "w") as file:
            file.write(image_base64)
        print("Base64 saved to file.")

        return image_base64
    else:
        print("Failed to download image.")
        return None


img1 = '//mm.digikey.com/Volume0/opasdata/d220001/medias/images/650/MFG_AI-4328-P-C120-R.jpg'


download_image(img1)

def save_image_from_base64_file(image_base64_file_path, output_file_path):
    with open(image_base64_file_path, 'r') as file:
        image_base64 = file.read().strip()  # Убираем лишние пробельные символы, если они есть
    image_data = base64.b64decode(image_base64)
    with open(output_file_path, 'wb') as file:
        file.write(image_data)
    print(f"Image saved as {output_file_path}.")

# save_image_from_base64_file('image_base64.txt', 'NEW.jpg')