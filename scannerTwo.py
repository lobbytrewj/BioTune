import cv2
import pytesseract
import numpy as np
import requests
from bs4 import BeautifulSoup

# Ask the user to upload an image file
image_path = input("Enter the path to the image file: ")

# Read the image file
img = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Extract text from the image
text = pytesseract.image_to_string(gray)

# Clean the extracted text
text = text.replace("\n", " ")
text = "".join(c for c in text if c.isalnum() or c.isspace())
text = " ".join(text.split())

# Search for products on Amazon
url = f"https://www.amazon.com/s?k={text}"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

# Extract the product titles and prices from the search results
products = soup.find_all("div", {"class": "s-result-item"})
for product in products:
    title = product.find("h2", {"class": "a-size-mini"}).text.strip()
    price = product.find("span", {"class": "a-offscreen"}).text.strip()
    print(f"{title} - {price}")