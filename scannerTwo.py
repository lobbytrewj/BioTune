import cv2
from pyzbar.pyzbar import decode

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
        # Find barcodes in the grayscale frame
        barcodes = decode(gray)
        # Loop over detected barcodes
        for barcode in barcodes:
            # Extract the barcode data as a string
            barcode_data = barcode.data.decode("utf-8")
            # Check if the barcode is a UPC code
            if barcode.type == "UPC-A":
                # Get the product name and manufacturer from the barcode data
                manufacturer = barcode_data[:6]
                product_code = barcode_data[6:11]
                # Print the product name and manufacturer
                print("Product Name: ", product_code)
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