# Import the OpenCV library version 2 (cv2) for image processing
import cv2

# Read the image from the file "logo.png" and store it in the variable `image`
image = cv2.imread("logo.png")

# Display the original image in a window titled 'Original Image'
cv2.imshow('Original Image', image)

# Save the original image as "Original Image.jpg" in the current directory
cv2.imwrite('Original Image.jpg', image)

# Print the entire image matrix (NumPy array representation of the image)
# This will print all the pixel values (BGR channels for each pixel in the image)
print(image)

# Print the pixel value at position (100, 100) in the image
# This is the BGR value of the pixel at row 100, column 100
print(image[100, 100])

# Print the pixel value at position (33, 200)
# This prints the BGR value of the pixel at row 33, column 200
print(image[33, 200])

# Print the maximum pixel value in the image
# The max value will be 255 if the image contains any fully saturated color channel
print(image.max())

# Print the minimum pixel value in the image
# The min value will be 0 if the image contains any pixel with no color intensity in any channel
print(image.min())

# Print the shape of the image (height, width, channels)
# This shows the number of rows (height), columns (width), and color channels in the image
print(image.shape)

# Print the number of rows (height) in the image
print(image.shape[0])

# Print the number of columns (width) in the image
print(image.shape[1])

# Print the number of color channels in the image (3 for BGR image)
print(image.shape[2])

# Print the first two dimensions (height and width) of the image (ignoring channels)
print(image.shape[:2])

# Convert the image from BGR to grayscale
# The resulting image contains intensity values only (single channel)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the grayscale image in a window titled 'Gray Image'
cv2.imshow('Gray Image', gray_image)

# Convert (cvt) the image from BGR to RGB
# This is often used when working with libraries like Matplotlib that expect RGB images
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display the RGB image in a window titled 'Gray Image'
# This title should ideally be changed to something like 'RGB Image' for clarity
cv2.imshow('RGB Image', rgb_image)

# Wait for a key press indefinitely and then close the windows
cv2.waitKey(0)

# Close all OpenCV windows after a key is pressed
cv2.destroyAllWindows()
