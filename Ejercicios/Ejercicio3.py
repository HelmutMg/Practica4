import requests
import zipfile
from io import BytesIO
from PIL import Image

url = "https://images.unsplash.com/photo-1560807707-8cc77767d783"

# Descargar la imagen desde la URL
response = requests.get(url)
if response.status_code == 200:
    image_data = response.content
else:
    print("No se pudo descargar la imagen.")
    exit()


zip_filename = "imagen.zip"

with zipfile.ZipFile(zip_filename, "w") as zipf:
    zipf.writestr("imagen.jpg", image_data)

print(f"La imagen se ha guardado en '{zip_filename}'")

with zipfile.ZipFile(zip_filename, "r") as zipf:
    zipf.extractall()

print("La imagen se ha extraído del archivo ZIP.")

imagen_extraida = Image.open("imagen.jpg")
imagen_extraida.show()

