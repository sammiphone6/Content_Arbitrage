import cv2  
import numpy as np  
import scipy.ndimage as sp
import pyautogui
import PIL.ImageGrab
from account_adding.fsm_functions import pause_for
snapshot = PIL.ImageGrab.grab()
snapshot.save('pilsc.png')

image = cv2.imread("Facebook.png")  
template = cv2.imread("Phone number.png")  

image = cv2.imread("pilsc.png")  
template = cv2.imread("cc.png")  

# methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
#             'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
# for method in methods:
#     result = cv2.matchTemplate(image,template,cv2.TM_CCOEFF_NORMED)  
#     loc = np.unravel_index(result.argmax(),result.shape)
#     print (method, loc)
#     pyautogui.click(loc)


directory = 'account_adding/button_icons/facebook'
# pause_for([f'{directory}/Next.png', f'{directory}/Next2.png'], 10)
pause_for([f'{directory}/Skip.png', f'{directory}/Next2.png'], 5)


def find_subimages(primary, subimage, confidence=0.60):
  primary_edges = cv2.Canny(primary, 32, 128, apertureSize=3)
  subimage_edges = cv2.Canny(subimage, 32,128, apertureSize=3)

  result = cv2.matchTemplate(primary_edges, subimage_edges, cv2.TM_CCOEFF_NORMED)
  (y, x) = np.unravel_index(result.argmax(),result.shape)

  result[result>=confidence]=1.0
  result[result<confidence]=0.0
  
  ccs = get_connected_components(result)
  y,x = correct_bounding_boxes(subimage, ccs)[0]
  return ((x[0]+x[1])/2, (y[0]+y[1])/2)

def cc_shape(component):
  x = component[1].start
  y = component[0].start
  w = component[1].stop-x
  h = component[0].stop-y
  return (x, y, w, h)

def correct_bounding_boxes(subimage, connected_components):
  (image_h, image_w)=subimage.shape[:2]
  corrected = []
  for cc in connected_components:
    (x, y, w, h) = cc_shape(cc)
    presumed_x = x+w/2
    presumed_y = y+h/2
    corrected.append(((presumed_y, presumed_y+image_h), (presumed_x, presumed_x+image_w)))
  return corrected

def get_connected_components(image):
  s = sp.morphology.generate_binary_structure(2,2)
  labels,n = sp.measurements.label(image)#,structure=s)
  objects = sp.measurements.find_objects(labels)
  return objects


# x,y = find_subimages(image, template)[0]
x = find_subimages(image, template)
print(x)
r = 2
pyautogui.click((x[0]/r, x[1]/r))
# print(((x[0]+x[1])/2, (y[0]+y[1])/2))


# def draw_bounding_boxes(img,connected_components,max_size=0,min_size=0,color=(0,0,255),line_size=2):
#   for component in connected_components:
#     if min_size > 0 and area_bb(component)**0.5<min_size: continue
#     if max_size > 0 and area_bb(component)**0.5>max_size: continue
#     (ys,xs)=component[:2]
#     cv2.rectangle(img,(xs.start,ys.start),(xs.stop,ys.stop),color,line_size)

# def save_output(infile, outfile, connected_components):
#   img = cv2.imread(infile)
#   draw_bounding_boxes(img, connected_components)
#   cv2.imwrite(outfile, img)

# def  find_subimages_from_files(primary_image_filename, subimage_filename, confidence):
#   '''
#   2d cross correlation we'll run requires only 2D images (that is color images
#   have an additional dimension holding parallel color channel info). So we 'flatten'
#   all images loaded at this time, in effect making them grayscale.
#   There is certainly a lot of info that will be lost in this process, so a better approach
#   (running separately on each channel and combining the cross correlations?) is probably
#   necessary.  
#   '''
#   primary = cv2.imread(primary_image_filename, cv2.CV_LOAD_IMAGE_GRAYSCALE)
#   subimage = cv2.imread(subimage_filename, cv2.CV_LOAD_IMAGE_GRAYSCALE)
#   return find_subimages(primary, subimage, confidence)


