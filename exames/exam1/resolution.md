# Exam 1


## 1. INTRODUCTORY CONCEPTS 

### 1.1 What Is Depth Of Field?

- Depth of field is one of the essential concepts in photography.  The depth of field in a photo refers to the distance between the closest and farthest objects that appears acceptably sharp. Depth of field differs based on camera type, aperture, and focusing distance. In addition, the viewing distance and print size can contribute to the perception of depth of field.
- The depth of field does not change from sharp to unsharp abruptly. Instead, there is a gradual transition. Everything in front of or in the back of the focusing distance starts to lose sharpness. Our eyes or the resolution of the camera do not perceive this. This is based on a scientific phenomenon called the circle of confusion.
- Depth of field is mainly concerned with the lens’s aperture used for photography, while camera distance is also vital. The distance between your camera and the subject where your focus point is located has a significant effect. The lower the depth of field, the closer you are to your subject. As a result, the more distant from the subject, the greater the depth of field.


### 1.2 What is, in general, the expected result of an operation to equalize the histogram of an image represented in gray levels? Is it possible to predict the general effect of equalizing the histogram of each of the components, R, G and B, of a color image? Justify the answer.

- The contrast enhancement is better after the histogram equalization, which more easily detects structures located in the shade. In fact any strongly represented gray-level is stretched while any weakly represented graylevel is merged with other close levels
- No, in color images, only the luminance channel is usually equalized as otherwise the colors can become distorted.


## 2. - IMAGE ENHANCEMENT AND FEATURE DETECTION (EDGES, CORNERS, LINES, ...) 

### 2.1 Explain how to attenuate this noise in order to  obtain an image similar to that of Fig. 2. Justify the answer.

- The best method to eliminate salt-and-pepper noise is median filtering, as it preserves the edges while removing the noise
- The median filter works by replacing each pixel in the image with the median of the value of its neighboring pixels, which makes it less sensitive to extreme values (such as the ones we see in salt-and-pepper noise) than other filtering methods such as mean filtering

### 2.2 2.2 In relation to Canny edges detector, tell what is the purpose of the non-maximum suppression and thresholding hysteresis steps. If an image contains a long vertical edge, what are the neighbors of a pixel in that edge that are analyzed when performing each of these steps?

- The Canny operator uses the so-called “hysteresis” thresholding. Most thresholders use a single threshold limit,
which means that if the edge values fluctuate above and below this value, the line appears broken. This phenomenon is commonly referred to as “streaking”. Hysteresis counters streaking by setting an upper and lower edge value limit.
- Considering a line segment,
    - If a value lies above the upper threshold limit it is immediately accepted.
    - If the value lies below the low threshold it is immediately rejected.
    - Points which lie between the two limits are accepted if they are connected to pixels which exhibit strong response.
- The edges can be located at the points of local maximum gradient magnitude. It is done via suppression of non-maxima, that is, points, whose gradient magnitudes are not local maxima. Non-maxima perpendicular to the edge direction, rather than those in the edge direction, have to be suppressed. The algorithm starts off by reducing the angle of gradient to one of the four sectors shown in Figure.The algorithm passes the 3x3 neighborhood
across the magnitude array. At each point the center element of the neighborhood is compared with its two neighbors along line of the gradient given by the sector value. If the central value is non-maximum, that is, not greater than the neighbors, it is suppressed.

### 2.3 Is it possible to change the sensitivity of the Harris corner detector in order to detect more or fewer corners? If yes, please indicate how.

- Yes, it is possible to change the sensitivity of the Harris corner detector in order to detect more or fewer corners.

- The sensitivity of the Harris corner detector is controlled by a parameter called the threshold. This threshold determines the minimum value of the corner response function that will be considered as a corner.

- If the threshold is set to a high value, only the most prominent corners will be detected, and many weaker corners will be missed. On the other hand, if the threshold is set to a low value, more corners will be detected, including weaker corners that may not be relevant to the task at hand.

- In general, if you want to detect more corners, you can lower the threshold. Conversely, if you want to detect fewer corners, you can increase the threshold. However, it is important to note that adjusting the threshold can also affect the accuracy and repeatability of the detected corners, so it is important to choose an appropriate threshold based on the specific requirements of the application.


## 3. SEGMENTATION AND POST-PROCESSING

### 3.1 Thresholding techniques are widely used in image segmentation. Indicate two factors.

- Image Contrast: In images with low contrast, there may not be a clear distinction between the object of interest and the background. In such cases, using a single threshold may result in a poor segmentation of the object, as the threshold will not be able to separate the object from the background effectively.

- Variation in Object Intensity: Objects in an image may have varying intensity values, and a single threshold may not be able to accurately segment these objects. For example, in an image with an object that has both bright and dark regions, a single threshold may result in either over-segmentation or under-segmentation of the object, as the threshold cannot differentiate between the different regions of the object.

### 3.2 Consider the pulmonary X-ray images of Fig.3. The segmentation of pulmonary regions, shown in the figure, is frequently performed using Active Shape Models. How do you justify this option? What is the possibility of applying this type of segmentation technique?


- The ASM algorithm aims to match the model to a new image.
It works by alternating the following steps:
    - Look in the image around each point for a better position for that point
    - Update the model parameters to best match to these new found positions
- To locate a better position for each point one can:
    - look for strong edges, or
    - a match to a statistical model of what is expected at the point
- Application examples:
    - analyse images of faces,
    - medical image segmentation (in 2D and 3D; ex: lung segmentation).


### 3.3  Consider the images in Figs. 4 and 5. Describe a processing sequence based on morphological operators, starting from the binary image of Fig. 4, to obtain the image of Fig. 5, where the edges of the objects of Fig. 4 are detected.

- The morphological operators are used in image processing to extract or enhance certain features of an image such as edges, boundaries, and shapes. To obtain the edges of an image using morphological operators, we can follow the following processing sequence:

    - Convert the image to grayscale: To obtain the edges, we do not need the color information of the image. So, we can convert the image to grayscale using any standard method.

    - Apply morphological gradient: Morphological gradient is a combination of dilation and erosion operations. It highlights the edges of an image by subtracting the eroded image from the dilated image. The morphological gradient can be obtained by performing the following steps:

        - Dilate the grayscale image using a structuring element (e.g., a square or circle) of a certain size.
        - Erode the grayscale image using the same structuring element.
        - Subtract the eroded image from the dilated image to obtain the morphological gradient.

    - Threshold the gradient image: The morphological gradient image obtained in step 2 will have values ranging from negative to positive. We can threshold the image to obtain a binary image where the edges are represented by white pixels and the rest of the image is represented by black pixels.

    - Perform morphological thinning: The edges obtained in step 3 may not be very thin and may have multiple pixels. To obtain a one-pixel thick edge, we can perform morphological thinning using the binary image obtained in step 3. Morphological thinning removes pixels from the edges until they are one-pixel wide.

- The resulting image after these steps will contain the edges of the original image. The morphological operators are powerful tools in image processing and can be used in various applications such as object recognition, segmentation, and tracking.


## 4. GEOMETRICAL MODELLING OF A CAMERA / STEREOSCOPY 

### 4.1 A camera can be modeled, geometrically, by a matrix of 3x4 elements, commonly referred to as a "perspective projection matrix". Give a physical, intuitive explanation for the fact that this matrix is not invertible.

- The perspective projection matrix is used to map the 3D coordinates of a scene onto a 2D image plane. This matrix takes into account the camera's intrinsic and extrinsic parameters, such as focal length, image sensor size, and the camera's position and orientation in the scene.

- The matrix is not invertible because the projection from 3D to 2D is not a one-to-one mapping. This means that multiple 3D points can project onto the same 2D point, resulting in a loss of information. This phenomenon is known as perspective distortion, and it is caused by the fact that objects that are farther away from the camera appear smaller in the image.

- As a result of this loss of information, the inverse of the perspective projection matrix cannot be uniquely determined. In other words, it is not possible to recover the exact 3D coordinates of a scene point from its 2D projection in the image. Instead, techniques such as triangulation or photogrammetry are used to estimate the 3D coordinates of a point from multiple 2D images taken from different viewpoints.

- In summary, the perspective projection matrix is not invertible because the projection from 3D to 2D is a non-injective mapping, resulting in a loss of information about the 3D coordinates of the scene.

### 4.2 Briefly describe the rectification of a pair of stereo images and the reason for their use

- Rectification is a process in stereo vision that transforms a pair of stereo images so that their corresponding epipolar lines become parallel to each other, simplifying the process of finding the correspondences between the images. The rectification process is typically performed as a preprocessing step before stereo matching.

- The reason for rectification is to simplify the computation of stereo correspondence by reducing it from a 2D search problem to a 1D search problem. Without rectification, finding the correspondences between a pair of stereo images can be difficult and computationally expensive, as every pixel in one image needs to be compared with every pixel in the other image. Rectification simplifies this task by ensuring that the epipolar lines, which represent the projection of a 3D point onto the image plane of the other camera, are parallel in both images. This reduces the search space from a 2D area to a 1D line, making the process much faster and more accurate.

- The rectification process involves finding a pair of transformation matrices that map each stereo image onto a common rectified coordinate system. The rectification is usually performed based on the fundamental matrix of the stereo pair, which represents the relationship between the epipolar lines in the two images. The rectification matrices ensure that the epipolar lines in the rectified images are parallel to each other and aligned with the horizontal image axis.
