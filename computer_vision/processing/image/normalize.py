def normalize_image(image):
    """
    Normalizes an input image to a range of [0, 1].

    Args:
        image (numpy.ndarray): Input image.

    Returns:
        numpy.ndarray: Normalized image.
    """
    return (image / 255.0).astype(np.float32)
