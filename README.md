
# Image Processing with Harris Corner Detection

This project is an implementation of the Harris Corner Detection algorithm, a popular method used in computer vision for corner detection. The algorithm works by detecting regions in the image with significant changes in all directions, which are typically interpreted as corners.

## Example
##### Original image,     Derivative of X,   Derivative of Y      
<p>
<img src="https://github.com/knrdsmt/Image-Harris-Corner-Detection/blob/main/pg.jpg?raw=true" alt="Original" width="32%" height="auto" align="left" />
<img src="https://github.com/knrdsmt/Image-Harris-Corner-Detection/blob/main/img_dx.png?raw=true" alt="DX" width="32%" height="auto" float="center" />
<img src="https://github.com/knrdsmt/Image-Harris-Corner-Detection/blob/main/img_dy.png?raw=true" alt="DY" width="31.5%" height="auto" align="right" />
</p>

#### Harris Corner Detectioned image
<p align="center">
<img src="https://github.com/knrdsmt/Image-Harris-Corner-Detection/blob/main/corners_pg.jpg?raw=true" alt="Harris Corner Detectioned" width="100%" height="auto"/>
</p>

# Harris Corner Detection Process

1. **Image Input**: The program reads an image in grayscale format using OpenCV's `imread` function.

2. **Image Smoothing**: The image is smoothed using a median filter to reduce noise.

3. **Gradient Calculation**: The program calculates the image gradients in the x and y directions. This is done by convolving the image with a 1D kernel in both directions. The result is two images representing the x and y derivatives of the original image.

4. **Structure Tensor Calculation**: The structure tensor (also known as the second moment matrix) is calculated for each pixel. This involves squaring the x and y derivatives and also calculating the product of the x and y derivatives.

5. **Window Function Application**: A window function (in this case, a simple box window) is applied to the structure tensor. This is equivalent to summing the values of the structure tensor over a local neighborhood around each pixel.

6. **Corner Response Calculation**: The Harris corner response is calculated for each pixel. This involves computing the determinant and trace of the structure tensor, and combining them in a specific way.

7. **Corner Detection**: Finally, corners are detected by thresholding the Harris response. Pixels with a response above a certain threshold are marked as corners.

8. **Output**: The corners are highlighted in the original image and the image is saved to disk. The corners are also displayed to the user using OpenCV's `imshow` function.

## Implementation Note
This program has been implemented without the use of the OpenCV library, except for image input/output operations. All the image processing tasks, including the computation of image derivatives and the Harris response function, are implemented from scratch using only the NumPy library.

## Applications of Harris Corner Detection

Harris Corner Detection has a wide range of applications in the field of computer vision and image processing. Some of the key applications include:

- **Image Stitching**: Harris corners are used to find corresponding points between different images for image stitching, which is the process of combining multiple images with overlapping fields of view to produce a high-resolution panorama.

- **Object Recognition**: Corners are often used as features for object recognition algorithms because they provide unique and robust features that can be used to match different views of an object.

- **3D Reconstruction**: Harris corners can be used to find corresponding points between stereo images, which can then be used to reconstruct the 3D structure of a scene.

- **Motion Tracking**: In video processing, Harris corners can be tracked across frames to estimate the motion of objects or the camera.
