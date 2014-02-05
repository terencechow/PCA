This project is an attempt to convert the main functions from missMDA in R into Python so that one can impute missing values using a PCA iterative approach. It is also known as the EM-PCA algorithm. You can read more about the functions if you read the R documents.

Please use at your own risk. Feel free to review my code for errors.

Usage

from missMDA import *
estim_ncpaPCA(data)

This will give you a tupple with the first element being the number of components retained and the second element showing the mean squared error of prediction (MSEP) for different number of components. The 1st element of this tuple will be the smallest MSEP found.

imputePCA(data,ncp=q) 

Where q is the number of components retained from estim_ncpPCA(data). This will return a list of 2 numpy arrays. The first array is what the data is with imputed values replacing the missing values and the second numpy array is what the data would look like if all values were imputed.

From here you can take the first element of imputePCA and use that as your new data set and run a regular PCA on it