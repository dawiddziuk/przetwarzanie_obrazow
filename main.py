import urllib.request
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO


# LINK ZDJECIA
IMAGE_URL = "https://raw.githubusercontent.com/opencv/opencv/master/samples/data/lena.jpg"


# WCZYTANIE OBRAZU Z INTERNETU
request = urllib.request.Request(
    IMAGE_URL,
    headers={"User-Agent": "Mozilla/5.0"}
)

with urllib.request.urlopen(request) as response:
    image_data = response.read()

image = Image.open(BytesIO(image_data))
image = image.convert("RGB")


# WYŚWIETLENIE OBRAZU ORYGINALNEGO
plt.imshow(image)
plt.title("Obraz oryginalny")
plt.axis("off")
plt.show()


# ZMNIEJSZENIE ROZDZIELCZOŚCI O 50%
width, height = image.size
image_small = image.resize((width // 2, height // 2))


# KONWERSJA DO GRAYSCALE
gray = image_small.convert("L")


# OBRÓT O 90 STOPNI
rotated = gray.rotate(90, expand=True)

# WYŚWIETLENIE OBRAZU
plt.imshow(rotated, cmap="gray")
plt.title("Obraz wynikowy")
plt.axis("off")
plt.show()


# MACIERZ OBRAZU
matrix = np.array(rotated)

print("Rozmiar macierzy (wysokosc, szerokosc):", matrix.shape)
print("Fragment macierzy 20x20:")
print(matrix[:20, :20])