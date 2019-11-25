from typing import Optional
import cv2
from pymba import Frame
import time

PIXEL_FORMATS_CONVERSIONS = {
    'BayerRG8': cv2.COLOR_BAYER_RG2RGB,
}

class FrameRetrieval(object):

    def __init__(self, frame_fixer, video_writer):
        self.frame_fixer = frame_fixer
        self.video_writer = video_writer

    def frame_callback(self, frame: Frame, delay: Optional[int] = 1) -> None:
        """
        Displays the acquired frame.
        :param frame: The frame object to display.
        :param delay: Display delay in milliseconds, use 0 for indefinite.
        """
        # get a copy of the frame data
        image = frame.buffer_data_numpy()

        # convert colour space if desired
        try:
            image = cv2.cvtColor(image, PIXEL_FORMATS_CONVERSIONS[frame.pixel_format])
        except KeyError:
            pass

        image = self.frame_fixer.fix_frame(image)
        print(image)

        # self.video_writer.write(image)
