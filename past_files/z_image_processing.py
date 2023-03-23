# # # Import required packages
# # import cv2
# # import pytesseract

# # # Mention the installed location of Tesseract-OCR in your system
# # pytesseract.pytesseract.tesseract_cmd = 'System_path_to_tesseract.exe'

# # # Read image from which text needs to be extracted
# # img = cv2.imread("sample.jpg")

# # # Preprocessing the image starts

# # # Convert the image to gray scale
# # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # # Performing OTSU threshold
# # ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

# # # Specify structure shape and kernel size.
# # # Kernel size increases or decreases the area
# # # of the rectangle to be detected.
# # # A smaller value like (10, 10) will detect
# # # each word instead of a sentence.
# # rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

# # # Applying dilation on the threshold image
# # dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)

# # # Finding contours
# # contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
# # 												cv2.CHAIN_APPROX_NONE)

# # # Creating a copy of image
# # im2 = img.copy()

# # # A text file is created and flushed
# # file = open("recognized.txt", "w+")
# # file.write("")
# # file.close()

# # # Looping through the identified contours
# # # Then rectangular part is cropped and passed on
# # # to pytesseract for extracting text from it
# # # Extracted text is then written into the text file
# # for cnt in contours:
# # 	x, y, w, h = cv2.boundingRect(cnt)
	
# # 	# Drawing a rectangle on copied image
# # 	rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
	
# # 	# Cropping the text block for giving input to OCR
# # 	cropped = im2[y:y + h, x:x + w]
	
# # 	# Open the file in append mode
# # 	file = open("recognized.txt", "a")
	
# # 	# Apply OCR on the cropped image
# # 	text = pytesseract.image_to_string(cropped)
	
# # 	# Appending the text into file
# # 	file.write(text)
# # 	file.write("\n")
	
# # 	# Close the file
# # 	file.close

# from PIL import Image
# from pytesseract import pytesseract

# image = Image.open('ocr.png')
# image = image.resize((400,200))
# image.save('sample.png')



# # import pytesseract
# # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
# # print(pytesseract.image_to_string(r'D:\examplepdf2image.png'))

# print(0)
# import easyocr
# print(1)
# reader = easyocr.Reader(['en'])
# result = reader.readtext('ocr.png', detail=0)
# print(result)



# adds image processing capabilities
from PIL import Image
import time
# will convert the image to text string
import pytesseract
import pyautogui

# assigning an image from the source path
time.sleep(5)
filename = 'temp_screenshot.png'
myScreenshot = pyautogui.screenshot()
myScreenshot.save(f'{filename}')
img = Image.open(f'{filename}')

# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img)
print(result)

