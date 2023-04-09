import cv2
import urllib.request
import numpy as np
import barcode
from barcode import EAN13
from barcode.reader import ImageReader

# Define a function to read barcodes from a video stream
def read_barcodes(camera):
    # Initialize video capture object for the camera
    cap = cv2.VideoCapture(int(camera), cv2.CAP_DSHOW)
    # Loop over frames from the video stream
    while True:
        # Read a frame from the video stream
        ret, frame = cap.read()
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Load the barcode image from the grayscale frame
        pil_img = Image.fromarray(gray)
        # Use the python-barcode library to read the barcode
        barcode = None
        try:
            barcode = EAN13(pil_img, reader=ImageReader())
        except:
            pass
        # If a barcode is detected, print the product name and manufacturer
        if barcode is not None:
            product_name, manufacturer = barcode.name.split(" ")
            print("Product Name: ", product_name)
            print("Manufacturer: ", manufacturer)
        # Show the video stream in a window
        cv2.imshow("Barcode Scanner", frame)
        # Wait for a key press
        key = cv2.waitKey(1) & 0xFF
        # Exit the loop if the 'q' key is pressed
        if key == ord("q"):
            break
    # Release the video capture object and close the window
    cap.release()
    cv2.destroyAllWindows()

# Call the read_barcodes function with the camera index as an argument
read_barcodes(0)




