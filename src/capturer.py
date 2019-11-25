from frameretrieval import FrameRetrieval
from framefixer import FrameFixer
from camera.vimbacamera import VimbaCamera
from videowriter import VideoWriter
import os

def capture(camera_index, file_path, codec):


    frame_fixer = FrameFixer(720, 1280)
    video_writer = VideoWriter(filename=correct_filepath(file_path), fps=30, height=720, width=1280, codec=codec)
    frame_retrieval = FrameRetrieval(frame_fixer, video_writer)
    process_capturer = VimbaCamera(frame_retrieval, index=camera_index)

    process_capturer.start()
    process_capturer.join()
    video_writer.release()

    print(correct_filepath(file_path))


def correct_filepath(file_path):

    if os.path.exists(file_path):
        dir_path = os.path.dirname(os.path.realpath(file_path))
        file_name = os.path.basename(file_path)
        file_name, ext = os.path.splitext(file_name)

        index = 1

        while True:
            file_path = os.path.join(dir_path, file_name+"_"+str(index)+ext)
            if not os.path.exists(file_path): break
            index = index + 1

    return file_path

