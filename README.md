# EdgeDetection_usingOpenCV
Edge detection is one of the fundamental image-processing tasks used in various Computer Vision tasks to identify the boundary or sharp changes in the pixel intensity. It plays a crucial role in object detection, image segmentation and feature extraction from the image. In Real-time edge detection, the image frame coming from a live webcam or video is continuously captured and each frame is processed by edge detection algorithms which identify and highlight these edges continuously.
## Canny Edge Detection
Canny Edge Detection is one of the most widely used edge detection algorithms developed by John F. Canny in 1986. It works in four stages i.e Noise reduction, Finding the intensity gradient, Non-maximum suppression, and Hysteresis thresholding.

Let’s understand each stage one by one:
### Step 1: Noise Reduction
First, the noise in the image is reduced by blurring the image. To blur the image we apply the Gaussian filter. It applies a weighted average to each pixel, which reduces the sensitivity with the slight changes in intensity caused by noise. The larger the kernel size, the more significant the smoothing effect. 
### Step 2: Finding the intensity gradient
In this step, the intensity gradient of the image is found, which helps to locate the areas of sudden intensity shifts that correspond to edges in the image. The technique, known as Sobel algorithms are used to compute the first derivative of the image in both the horizontal (Gx) and vertical (Gy) directions. 
### Step 3: Non-maximum Suppression
We use non-maximum suppression to get thin edges. Each pixel is looked at in the gradient direction to see if there is a local maximum. If it isn’t, the pixel is suppressed (its value is set to 0) because it probably isn’t a component of an edge.
### Step 4: Hysteresis Thresholding
Hysteresis thresholding is used to finalize the edges. We set the minVal and maxVal threshold values. Pixels with gradient magnitudes above maxVal are considered strong edges, while those below minVal are considered non-edges and discarded. Pixels with magnitudes between minVal and maxVal are considered weak edges.

To identify the final edges, we follow the strong edges and consider weak edges connected to them as part of the edge. If a weak edge is not connected to any strong edge, it is discarded as noise.
