import cv2
import numpy as np


class FrameFixer(object):

    def __init__(self, window_h, window_w):
        self.window_h = window_h
        self.window_w = window_w

    def fix_frames(self, data):
        '''
        Resize video depending of window wanted
        :param data: video
        :return: video resized
        '''
        data_new = []
        for i in range(0, data.shape[0]):
            frame_resized = self.fix_frame(data[i])
            data_new.append(frame_resized)
        data_new = np.array(data_new)
        return data_new

    def fix_frame(self, frame):
        '''
        Resize frame
        :param frame: video frame
        :return: frame resized and windowed
        '''
        width = frame.shape[1]
        height = frame.shape[0]
        actual_aspect = width / float(height)

        ideal_width = self.window_w
        ideal_height = self.window_h
        ideal_aspect = ideal_width / float(ideal_height)

        if actual_aspect > ideal_aspect:
            # Crop the left and right edges:
            new_width = int(ideal_aspect * height)
            offset = int((width - new_width) / 2)
            resize = (offset, 0, width - offset, height)
        else:
            # Crop the top and bottom edges:
            new_height = int(width / ideal_aspect)
            offset = int((height - new_height) / 2)
            resize = (0, offset, width, height - offset)

        frame = frame[resize[1]:resize[3], resize[0]:resize[2], :]
        return cv2.resize(frame, (ideal_width, ideal_height))