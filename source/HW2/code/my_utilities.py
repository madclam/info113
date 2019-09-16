from utilities import *

### BEGIN SOLUTION
def crop_image(img, crop_size = 32):
    ''' Extract the `crop_size` x `crop_size` pixels from the center of the PIL image `img`.'''
    # First determine the bounding box
    width, height = img.size
    left = round((width - crop_size)/2.)
    top = round((height - crop_size)/2.)
    right = round((width + crop_size)/2.)
    bottom = round((height + crop_size)/2.)
    # Then crop the image to that box
    cropped_img = img.crop((left, top, right, bottom))
    return cropped_img

def difference_filter(img):
    '''Extract a numpy array D = R-(G+B)/2 from the PIL image `img`.'''
    M = np.array(img)
    R = M[:,:,0] * 1.0
    G = M[:,:,1] * 1.0
    B = M[:,:,2] * 1.0
    D = R-(G+B)/2
    return D

def value_filter(img):
    '''Extract a numpy array V = (R+G+B)/3 from a PIL image `img`.'''
    M = np.array(img)
    R = M[:,:,0] * 1.0
    G = M[:,:,1] * 1.0
    B = M[:,:,2] * 1.0
    V = (R+G+B)/3
    return V

def foreground_filter(img, theta = 2/3):
    '''Extract a numpy array with True as foreground 
    and False as background from a PIL image.
    Parameter theta is a relative binarization threshold.'''
    D = difference_filter(img)
    V = value_filter(img) 
    F0 = np.maximum(D, V)
    threshold = theta*(np.max(F0) - np.min(F0))
    F = F0 > threshold
    return F

def transparent_background_filter(img, theta = 2/3):
    '''Return the PIL image `img` with its background set to transparent.'''
    M = np.array(img)
    R = M[:,:,0]
    G = M[:,:,1]
    B = M[:,:,2]
    T = foreground_filter(img) * 255
    return Image.fromarray(np.array(np.stack([R,G,B,T], axis=2), dtype='uint8'))

def get_redness(img):
    '''Extract the scalar value redness from a PIL image.'''
    D = difference_filter(img)
    F = foreground_filter(img)
    return np.mean(D[F])

# This code is given to you, you can study it to understand how it works
def get_elongation(img):
    '''Extract the scalar value elongation from a PIL image.'''
    F = foreground_filter(img)
    # Find the array indices of the foreground image pixels
    xy = np.argwhere(F)
    # We first center the data
    C = np.mean(xy, axis=0)
    Cxy = xy - np.tile(C, [xy.shape[0], 1])
    # We now apply singular value decomposition
    U, s, V = np.linalg.svd(Cxy)
    elongation = s[0]/s[1]
    return elongation

def extract_features(img, verbose = True):
    '''Take a PIL image and return two features of the foreground: redness and elongation.'''
    redness = get_redness(img)
    if verbose: print('redness={0:5.2f}'.format(redness))
    elongation = get_elongation(img)
    if verbose: print('elongation={0:5.2f}'.format(elongation))
    return [redness, elongation]

### END SOLUTION
