import cv2
from pyzbar.pyzbar import decode
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Define a function to read barcodes from a video stream
def read_barcodes(camera):
    # Initialize video capture object for the camera
    cap = cv2.VideoCapture(int(camera), cv2.CAP_DSHOW)
    # Initialize web driver for Amazon search
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.com/")
    # Loop over frames from the video stream
    while True:
        # Read a frame from the video stream
        ret, frame = cap.read()
        # Find barcodes in the frame
        barcodes = decode(frame)
        # Loop over detected barcodes
        for barcode in barcodes:
            # Extract the barcode data as a byte string
            barcode_data = barcode.data.decode("utf-8")
            # Print the barcode data
            print("Barcode Data: ", barcode_data)
            # Search for the product on Amazon
            search_input = driver.find_element_by_id("twotabsearchtextbox")
            search_input.send_keys(barcode_data)
            search_input.send_keys(Keys.RETURN)
            # Wait for the search results to load
            driver.implicitly_wait(10)
            # Get the title and price of the first search result
            try:
                first_result_title = driver.find_element_by_css_selector(".s-result-item h2 a").text
                first_result_price = driver.find_element_by_css_selector(".s-result-item .a-price-whole").text
                # Print the title and price
                print("First Result Title: ", first_result_title)
                print("First Result Price: $", first_result_price)
            except:
                print("No results found")
        # Show the video stream in a window
        cv2.imshow("Barcode Scanner", frame)
        # Wait for a key press
        key = cv2.waitKey(1) & 0xFF
        # Exit the loop if the 'q' key is pressed
        if key == ord("q"):
            break
    # Release the video capture object, close the window, and quit the web driver
    cap.release()
    cv2.destroyAllWindows()
    driver.quit()

# Call the read_barcodes function with the camera index as an argument
read_barcodes(0)