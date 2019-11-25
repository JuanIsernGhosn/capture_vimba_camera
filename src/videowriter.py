import os
import cv2
import numpy as np
import shutil


class VideoWriter(object):

    def __init__(self, filename, fps, height, width, codec=None):

        if codec == 'png':
            out = VideoWriterPNG(filename, fps, height, width)
        else:
            out = VideoWriterRGB(filename, fps, height, width, codec)

        self.v_out = out

    def write(self, image):
        self.v_out.write(image)

    def release(self):
        self.v_out.release()


class VideoWriterRGB(object):

    def __init__(self, filename, fps, height, width, codec=None):
        if codec is None:
            fourcc = 0
        else:
            fourcc = cv2.VideoWriter_fourcc(*codec)
        out = cv2.VideoWriter(filename=filename,
                              apiPreference=cv2.CAP_GSTREAMER,
                              fourcc=fourcc,
                              fps=fps,
                              frameSize=(width, height))
        self.out = out

    def write(self, image):
        image = utils.convert_to_cv8uc3(image)
        self.out.write(image)

    def release(self):
        self.out.release()


class VideoWriterPNG(object):

    def __init__(self, basedir, fps, height, width):
        self.basedir = basedir
        self.fps = int(fps)
        self.height = height
        self.width = width
        self.current_frame_id = 0
        self.create_base_dir()

    def create_base_dir(self):
        if os.path.isdir(self.basedir):
            shutil.rmtree(self.basedir)
        os.makedirs(self.basedir, exist_ok=True)

    def write(self, image):
        image = cv2.resize(image, (self.width, self.height))
        image = image.astype(np.uint16)
        filename = os.path.join(self.basedir, "frame_{}_fps_{}.png".format(self.current_frame_id, self.fps))
        cv2.imwrite(filename, image)
        self.current_frame_id = self.current_frame_id + 1

    def release(self):
        self.current_frame_id = 0