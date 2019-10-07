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

