import numpy as np
import nibabel as nib
from scipy.stats import entropy

def averaging_slide(image_data):
    average_image = np.zeros((image_data.shape[0],image_data.shape[1],image_data.shape[2]))
    for i in range(image_data.shape[0]):
        for j in range(image_data.shape[1]):
            for k in range(image_data.shape[2]):
                average_image[i,j,k] = np.average(image_data[i,j,k,:])
    return average_image

def variance_to_average(image_data,average_im):
    variance_matrix = np.zeros(image_data.shape)
    for i in range(image_data.shape[3]):
        variance_matrix[:,:,:,i] = image_data[:,:,:,i] - average_im
    return variance_matrix

def variance(image_data):
    return np.var(image_data, axis = 3)

def average_variance_along(var_matrix, axis):
    shape = var_matrix.shape
    if axis == 0:
        average_matrix = np.zeros((shape[0],shape[2],shape[3]))
        for i in range(shape[0]):
            for j in range(shape[2]):
                for k in range(shape[3]):
                    average_matrix[i,j,k] = np.mean(var_matrix[i,:,j,k])
    elif axis == 1:
        average_matrix = np.zeros((shape[0],shape[1],shape[3]))
        for i in range(shape[0]):
            for j in range(shape[1]):
                for k in range(shape[3]):
                    average_matrix[i,j,k] = np.mean(var_matrix[i,j,:,k])
    elif axis == 2:
        average_matrix = np.zeros((shape[0],shape[1],shape[2]))
        for i in range(shape[0]):
            for j in range(shape[1]):
                for k in range(shape[2]):
                    average_matrix[i,j,k] = np.mean(var_matrix[i,j,k,:])
    else:
        print("please enter digit between 0 to 2")
        return shape
    return average_matrix

def img_get_data(filename):
    data = nib.load(filename)
    return data.get_fdata()

def kl_divergence(s1, s2):
    shape = s1.shape
    kl_matrix = np.zeros((shape[1], shape[2], shape[3]))
    for i in range(shape[1]):
        for j in range(shape[2]):
            for k in range(shape[3]):
                s1_pixel = s1[:,i,j,k]
                s2_pixel = s2[:,i,j,k]
                s1_hist = np.histogram(s1_pixel, bins = [0.5,1,3,5,7,9,13,17,20], range = (0, 20))
                s2_hist = np.histogram(s2_pixel, bins = [0.5,1,3,5,7,9,13,17,20], range = (0, 20))
                kl = entropy(s1_hist, s2_hist)
                kl_matrix[i,j,k] = kl
    return kl_matrix