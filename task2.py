import cv2

image = cv2.imread('img.png')

height, width = image.shape[:2]
rotation_center = (width // 2, height // 2)
angle = 75
scale = 1.0

rot_matrix = cv2.getRotationMatrix2D(rotation_center, angle, scale)
rotated_image = cv2.warpAffine(image, rot_matrix, (width, height))

resize_factor = 0.75
resized_image = cv2.resize(rotated_image, (int(width * resize_factor), int(height * resize_factor)))

new_height, new_width = resized_image.shape[:2]
line_color = (0, 0, 255)
line_thickness = 2
cv2.line(resized_image, (new_width // 2, 0), (new_width // 2, new_height), line_color, line_thickness)

display_text = "%#?!!a1T"
text_position = (150, new_height - 10)
font_type = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
text_color = (0, 0, 255)
text_thickness = 2
cv2.putText(resized_image, display_text, text_position, font_type, font_scale, text_color, text_thickness)

cv2.imshow("Transformed Image", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
