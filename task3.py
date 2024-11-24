import cv2


def apply_positive_filter(image):
    """
    Применяет положительный фильтр: повышает яркость и контрастность.
    """
    alpha = 1.5
    beta = 50
    positive = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return positive


def apply_negative_filter(image):
    """
    Применяет отрицательный фильтр: инвертирует цвета.
    """
    negative = cv2.bitwise_not(image)
    return negative


def main():
    image = cv2.imread("img.png")
    if image is None:
        print("Ошибка: не удалось загрузить изображение.")
        return

    positive_image = apply_positive_filter(image)
    negative_image = apply_negative_filter(image)
    cv2.imshow("Original Image", image)
    cv2.imshow("Positive Filter", positive_image)
    cv2.imshow("Negative Filter", negative_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
