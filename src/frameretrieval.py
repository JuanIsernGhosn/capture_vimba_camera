from typing import Optional
import cv2
from pymba import Frame

PIXEL_FORMATS_CONVERSIONS = {
    'BayerRG8': cv2.COLOR_BAYER_RG2RGB,
}

class FrameRetrieval(object):

    def __init__(self, frame_fixer, buffer):
        self.frame_fixer = frame_fixer
        self.buffer = buffer

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
            image = self.frame_fixer.fix_frame(image)

            self.buffer.put(image)
        except KeyError:
            pass


