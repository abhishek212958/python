import cv2 as cv

# Take image path as input from the user
image_path = input("Enter the full path of the image: ")

# Read the image
img = cv.imread(image_path)

# Check whether the image was loaded successfully
if img is None:
    print("Error: Invalid image path or image not found.")
else:
    print("Image loaded successfully!")

    # Display the image in a separate window
    cv.imshow("Selected Image", img)

    # Wait until any key is pressed
    cv.waitKey(0)

    # Close the image window
    cv.destroyAllWindows()