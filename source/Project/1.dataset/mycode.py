# Replace this code by your OWN code!!

# Load general libraries
import os, re, sys
from glob import glob as ls
from PIL import Image, ImageOps
import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns; sns.set()
from PIL import Image
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import StratifiedShuffleSplit
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis


def resize_image(img, desired_size = 32):
	''' Resize a PIL image to dimension img_size x img_size.'''
	old_size = img.size 
	ratio = float(desired_size)/max(old_size)
	new_size = tuple([int(x*ratio) for x in old_size])
	img = img.resize(new_size, Image.ANTIALIAS)
	delta_w = desired_size - new_size[0]
	delta_h = desired_size - new_size[1]
	padding = (delta_w//2, delta_h//2, delta_w-(delta_w//2), delta_h-(delta_h//2))
	new_img = ImageOps.expand(img, padding, fill = '#ffffff')
	return new_img
	
def extract_resized_image(img, verbose = False):
    '''Take a PIL image and return a vector of flattened pixel values of a cropped image.'''
    img = resize_image(img)
    if verbose: print(img.size)
    return np.array(img).ravel()
    
def get_luminosity(img, verbose = False):
    '''Extract the scalar value luminosity from a PIL image.'''
    luminosity = np.mean(img)
    if verbose: print(luminosity)
    return luminosity

def my_foreground_filter(img, theta = 3/4):
    '''Extract a numpy array V = (R+G+B)/3 from a PIL image.'''
    # First resize the image
    img = resize_image(img)
    # Then extract the value of the image
    M = np.array(img)
    R = 1.*M[:,:,0]; G = 1.*M[:,:,1]; B = 1.*M[:,:,2]
    V = (R+G+B)/3
    # Finally, threshold it
    threshold = theta*(np.max(V) - np.min(V))
    F = V<threshold
    return F
    return V
    
def get_elongation(img, verbose = False):
    '''Extract the scalar value elongation from a PIL image.'''
    F = my_foreground_filter(img)
    # Find the array indices of the foreground image pixels
    xy = np.argwhere(F)
    # We first center the data
    C = np.mean(xy, axis=0)
    Cxy = xy - np.tile(C, [xy.shape[0], 1])
    # We now apply singular value decomposition
    U, s, V = np.linalg.svd(Cxy)
    elongation = s[0]/s[1]
    if verbose: print(elongation)
    return elongation
    
def extract_features(img, verbose = False):
    '''Take a PIL image and return two features of the foreground: redness and elongation.'''
    luminosity = get_luminosity(img)
    if verbose: print('luminosity={0:5.2f}'.format(redness))
    elongation = get_elongation(img)
    if verbose: print('elongation={0:5.2f}'.format(elongation))
    return [luminosity, elongation]

def standardize_df(df):
    '''Standardize all the columns except the last one (target values).'''
    df_scaled = (df-df.mean())/(sys.float_info.epsilon + df.std())
    df_scaled.iloc[:, -1] = df.iloc[:, -1]
    return df_scaled