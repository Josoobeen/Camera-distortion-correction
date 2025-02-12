def circular_distortion(image: np.ndarray, k1 = -0.05, k2 = 0.005, k3 = 0) -> np.ndarray:
    """
    The Circular distortion correction for wide camera image. 

    Args
        image : image array
    """
    h, w = image.shape[:2]
    h_middle = h // 2
    w_middle = w // 2

    # Output image base
    new_image = np.zeros_like(image)

    for i in range(h):
        for j in range(w):
            # regulate point
            x = (j - w_middle) / w_middle
            y = (i - h_middle) / h_middle

            # get distortion factor
            r2 = x * x + y * y
            distortion_factor = 1 + k1 * r2 + k2 * r2 ** 2 + k3 * r2 ** 3

            # mapping (destination → source mapping)
            x_corrected = int(w_middle + x * distortion_factor * w_middle)
            y_corrected = int(h_middle + y * distortion_factor * h_middle)

            # copy if the image index is exist
            if 0 <= x_corrected < w and 0 <= y_corrected < h:
                new_image[i, j] = image[y_corrected, x_corrected]
              
    return new_image
