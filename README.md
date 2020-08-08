# Comparing Traditional Method with Deep Learning in fMRI Pattern Recognition
## Abstract
Deep Learning achieves huge success in various image processing tasks. It is, there-
fore, a popular candidate for processing fMRI data which encodes rich information
of the neural activity and is hard to be interpreted directly with human eyes. We
explore the performance of deep learning models compared with traditional machine
learning methods on 125 fMRI samples from the ADHD-200 dataset. Concretely, we
compare the results of pixel-wise KL Divergence and Deep Learning models in pat-
tern recognition and localization of the fMRI data. We nd that the pixel-wise KL
Divergence based model consistently outperforms deep learning models in all tasks.
We expect that a larger amount of data and more sophisticated data pre-processing
would help deep learning models in the future.

## Description

The github resiportory documents all codes for the project including implementation of the metrics and preprocessing of the FMRI data. The paper is also attached where one can look at the methods. Read the paper first to know more about it.


## Phenotypic Analysis of the selected data from ADHD-200 dataset

![Verbal IQ vs. ADHD type](plots/verbal.png)

![Performance IQ vs. ADHD type](plots/performance.png)

![Performance IQ vs. Verbal IQ](plots/performance_verbal.png)


## Visualization of the FMRI data

![visualization](plots/t_0.png)
![average](plots/average_image.png)



One can use the notebook FMRI data visualization in the notebook file to animate the FMRI data.

## Traditional Methods Analysis
![pixel_wise_difference](plots/pdifference.png)

![variance](plots/variance.png)

The first is the KL Divergence of time evolution of all FMRI pixels of type 1 ADHD kids compared with healthy kids 
The second is the top 10000 pixels of the result.

![KL](plots/kl_all.png)
![KL_sparse](plots/kl_sparse.png)

For more information, please look at the KL test notebook and the paper.



## Neural Network Models
### Architecture
![arch](plots/arch.png)
### Feature Maps in Convolution Filter
The first is low level feature and the second is higher level feature in the CNN.
![low](plots/low-level.png)
![high](plots/high-level.png)

For more implementation detail there is a neural network notebook in the notebook file as well.
