# Exam 2


## 1. INTRODUCTORY CONCEPTS 

### 1.1 Give an intuitive explanation for the fact that a pinhole camera has an infinite depth of field.

- A pinhole camera works by projecting an image of the scene onto a photosensitive surface (such as film or a digital sensor) through a small aperture, or pinhole. The size of the pinhole determines the amount of light that enters the camera, and also affects the sharpness of the resulting image.

- The smaller the aperture (and hence the smaller the pinhole), the greater the depth of field. This is because a smaller aperture causes light rays to diverge less as they pass through the aperture, which means that objects at different distances from the camera will still project relatively sharp images onto the surface.

- As the aperture becomes smaller and smaller, the depth of field approaches infinity, because almost all light rays from the scene will converge to a point on the surface. This means that objects at any distance from the camera will still be relatively sharp in the resulting image.

- Therefore, a pinhole camera has an infinite depth of field because the tiny aperture causes light rays to converge from a wide range of distances, allowing objects at different depths to be in focus simultaneously.


### 1.2 What is the effect of adding the same value to the three components of a colour image, represented in the RGB space?

- Adding the same value to each of the three color channels (red, green, and blue) in an RGB color image results in a uniform increase in the brightness of the image. This is because each pixel in the image is represented as a combination of red, green, and blue values, and adding the same value to each channel results in a uniform increase in the intensity of all colors.


## 2. IMAGE ENHANCEMENT AND FEATURE DETECTION (EDGES, CORNERS, LINES, ...) 

### 2.1 

#### a. The Gaussian filters are, in general, preferable when compared to simple mean filters. Why?

- Gaussian filters are generally preferable to simple mean filters for several reasons:

    - Smoothing properties: Gaussian filters have better smoothing properties compared to simple mean filters. This is because the Gaussian filter weights the pixels according to their distance from the center pixel, with closer pixels being weighted more heavily. This results in a smoother output image with reduced noise and edge preservation.

    - Edge preservation: Gaussian filters better preserve edges than simple mean filters. This is because the Gaussian filter has a bell-shaped response, which means that it assigns smaller weights to pixels that are farther from the center pixel. This helps to preserve the edges in the image.

    - Non-linear operation: Gaussian filters are non-linear filters, whereas simple mean filters are linear filters. Non-linear filters are more effective in removing noise and preserving edges in images.

    - Flexibility: Gaussian filters are more flexible than simple mean filters in terms of the size of the filter kernel. Gaussian filters can be easily adjusted to different sizes and standard deviations, allowing them to be used for a wide range of image processing tasks.


#### b. One important feature of the Gaussian filters is that they are “separable filters”. Explain the concept of “separable filters” and justify the advantage of using it

- A separable filter is a type of filter that can be expressed as a product of two or more one-dimensional filters. In the case of a Gaussian filter, this means that the 2D Gaussian filter can be expressed as a product of two 1D Gaussian filters, one applied in the horizontal direction and the other applied in the vertical direction.

- The advantage of using separable filters is that they can greatly reduce the computational complexity of the filtering operation. When applying a separable filter to an image, the filter can be applied to each row of the image separately using the 1D filter in the horizontal direction. Then, the resulting image can be filtered again using the 1D filter in the vertical direction. This requires fewer computations compared to applying the full 2D filter directly to the image.


### 2.2 Consider the original image in Fig. 1 and the images in Fig. 2 and Fig. 3, which have resulted from transformation operations to the former image’s histogram. It is known that one of those operations was histogram equalization.

#### a. Which of the two images is the result of that operation? Justify.

- The image 3 because histogram equalization is a technique used in image processing to enhance the contrast of an image. The basic idea behind histogram equalization is to redistribute the intensity values of an image so that they are spread more evenly across the available intensity range.

#### b. Indicate a possible operation that the other image is a result of.

- Histogram stretching

### 2.3 A SIFT descriptor has typically 128 values. What is the meaning of these values?

- SIFT (Scale-Invariant Feature Transform) descriptors are a way of representing key points in an image. Each key point is described by a 128-dimensional vector, which encodes information about the local image structure around the key point.

- The values in the SIFT descriptor represent the relative strengths and orientations of the gradients in a 16x16 pixel patch around the key point. Specifically, the patch is divided into 16 sub-regions, and for each sub-region, a histogram of gradient orientations is computed. The histogram bins are weighted by the magnitudes of the gradients, and the resulting 128 values in the descriptor represent the concatenation of these weighted histogram values.

- Overall, the SIFT descriptor captures information about the texture, shape, and orientation of the local image patch around each key point, and can be used for tasks such as image matching, object recognition, and image retrieval.


## 3. SEGMENTATION AND POST-PROCESSING

### 3.1  Describe the general effect of an opening operation.

- Opening is the compound operation of erosion followed by dilation (with the same structuring element) open(B,S) = dilate(erode(B,S),S)
- Morphological opening: the upward outliers are eliminated as a result
- Results of opening on an image: small bright regions are removed, and the remaining bright regions are isolated but retain their size


## 4. GEOMETRICAL MODELLING OF A CAMERA / STEREOSCOPY

### 4.1 Justify the following sentence: “The accuracy of a depth estimate based on stereoscopy varies with the depth itself.”

- The sentence "The accuracy of a depth estimate based on stereoscopy varies with the depth itself" is justified because the accuracy of depth estimation using stereoscopy is affected by various factors, one of which is the depth of the object being viewed.

- Stereoscopy works by analyzing the disparity between two images captured from different viewpoints to determine the distance of objects from the observer. The greater the disparity between the two images, the greater the distance of the object from the observer. However, as the depth of the object increases, the disparity between the two images decreases, making it harder to estimate the depth accurately.


