import cv2

def fit_image_with_borders(image, output_h, output_w):
    '''
    Resize frame
    :param frame: video frame
    :return: frame resized and windowed
    '''
    width = image.shape[1]
    height = image.shape[0]
    actual_aspect = width / float(height)

    ideal_width = output_w
    ideal_height = output_h
    ideal_aspect = ideal_width / float(ideal_height)

    if actual_aspect > ideal_aspect:
        # Border on the top and bottom edges:
        new_height = int(ideal_width / actual_aspect)
        border = int((ideal_height - new_height) / 2)
        resize = (new_height, ideal_width, border, 0)
    else:
        # Border on the left and right edges:
        new_width = int(ideal_height * actual_aspect)
        border = int((ideal_width - new_width) / 2)
        resize = (ideal_height, new_width, 0, border)

    image = cv2.resize(image, (resize[1], resize[0]))
    img_with_border = cv2.copyMakeBorder(image, resize[2], resize[2], resize[3], resize[3], cv2.BORDER_CONSTANT,
                                         value=(0, 0, 0))
    return img_with_border

def image_decode(image):
    return cv2.imdecode(image, -1)