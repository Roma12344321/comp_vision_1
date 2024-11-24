import cv2
import numpy as np


def convert_rgb_to_cmyk(r, g, b):
    if r == 0 and g == 0 and b == 0:
        return 0, 0, 0, 255
    r_norm, g_norm, b_norm = r / 255.0, g / 255.0, b / 255.0
    k = 1 - max(r_norm, g_norm, b_norm)
    c = (1 - r_norm - k) / (1 - k)
    m = (1 - g_norm - k) / (1 - k)
    y = (1 - b_norm - k) / (1 - k)
    return int(c * 255), int(m * 255), int(y * 255), int(k * 255)


def convert_rgb_to_hsv(r, g, b):
    pixel = np.uint8([[[b, g, r]]])
    hsv_pixel = cv2.cvtColor(pixel, cv2.COLOR_BGR2HSV)
    return hsv_pixel[0][0][0], hsv_pixel[0][0][1], hsv_pixel[0][0][2]


def mouse_event_handler(event, x, y, flags, image_data):
    global cmyk_window_opened, hsv_window_opened

    if event == cv2.EVENT_LBUTTONDOWN:
        b, g, r = map(int, image_data["image"][y, x])
        c, m, y1, k = convert_rgb_to_cmyk(r, g, b)
        h, s, v = convert_rgb_to_hsv(r, g, b)
        print(f"Координаты: ({x}, {y}) | RGB: ({r}, {g}, {b}) | CMYK: ({c}, {m}, {y1}, {k}) | HSV: ({h}, {s}, {v})")
        image_data["cmyk_image"][:, :] = [k, y1, m]
        image_data["hsv_image"][:, :] = [h, s, v]
        if not cmyk_window_opened:
            cv2.imshow("CMYK Preview", image_data["cmyk_image"])
            cmyk_window_opened = True
        else:
            cv2.imshow("CMYK Preview", image_data["cmyk_image"])

        if not hsv_window_opened:
            cv2.imshow("HSV Preview", image_data["hsv_image"])
            hsv_window_opened = True
        else:
            cv2.imshow("HSV Preview", image_data["hsv_image"])


image_path = "img.png"

original_image = cv2.imread(image_path)
if original_image is None:
    raise FileNotFoundError("Изображение не найдено!")

cmyk_window_opened = False
hsv_window_opened = False

img_height, img_width = original_image.shape[:2]
cmyk_preview = np.zeros((img_height, img_width, 3), dtype=np.uint8)
hsv_preview = np.zeros((img_height, img_width, 3), dtype=np.uint8)

image_data = {
    "image": original_image,
    "cmyk_image": cmyk_preview,
    "hsv_image": hsv_preview,
}

cv2.imshow("Original Image", original_image)
cv2.setMouseCallback("Original Image", mouse_event_handler, image_data)

cv2.waitKey(0)
cv2.destroyAllWindows()
