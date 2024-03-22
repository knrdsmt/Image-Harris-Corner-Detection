import cv2
import numpy as np

image_path = 'pg.jpg'
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

img_color = cv2.imread(image_path)

img = cv2.medianBlur(img, 5)

dx = np.array([1, 0, -1])
dy = np.array([[1], [0], [-1]])

img_dx = np.zeros_like(img, dtype=np.float32)
for i in range(1, img.shape[0] - 1):
    for j in range(img.shape[1]):
        img_dx[i, j] = np.sum(dx * img[i - 1:i + 2, j])

img_dy = np.zeros_like(img, dtype=np.float32)
for i in range(1, img.shape[0] - 1):
    for j in range(1, img.shape[1] - 1):
        img_dy[i, j] = np.sum(dy * img[i - 1:i + 2, j - 1:j + 2])


img_dx += 128
img_dy += 128

img_dx = img_dx.astype(np.uint8)
img_dy = img_dy.astype(np.uint8)

kernel = np.ones((5, 5), np.uint8)
img_dx = cv2.dilate(img_dx, kernel, iterations=1)
img_dy = cv2.dilate(img_dy, kernel, iterations=1)

cv2.imwrite('img_dx.png', img_dx)
cv2.imwrite('img_dy.png', img_dy)

cv2.imshow('Derivative of X', img_dx)
cv2.imshow('Derivative of Y', img_dy)

cv2.waitKey(0)
cv2.destroyAllWindows()

img_dx2 = img_dx ** 2
img_dy2 = img_dy ** 2
img_dxdy = img_dx * img_dy

window_size = 3
half_size = window_size // 2
height, width = img.shape

dx2_sum = np.zeros_like(img, dtype=np.float64)
dy2_sum = np.zeros_like(img, dtype=np.float64)
dxdy_sum = np.zeros_like(img, dtype=np.float64)

for y in range(half_size, height - half_size):
    for x in range(half_size, width - half_size):
        dx2_sum[y, x] = np.sum(img_dx2[y - half_size:y + half_size + 1, x - half_size:x + half_size + 1])
        dy2_sum[y, x] = np.sum(img_dy2[y - half_size:y + half_size + 1, x - half_size:x + half_size + 1])
        dxdy_sum[y, x] = np.sum(img_dxdy[y - half_size:y + half_size + 1, x - half_size:x + half_size + 1])

k = 0.04
det_M = dx2_sum * dy2_sum - dxdy_sum ** 2
trace_M = dx2_sum + dy2_sum
harris_response = det_M - k * trace_M ** 2

corners = harris_response > 0.15 * harris_response.max()

img_color[corners] = [0, 255, 0]
cv2.imwrite('corners_pg.jpg', img_color)
cv2.imshow('Corners', img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()
