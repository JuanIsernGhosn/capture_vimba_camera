from frameretrieval import FrameRetrieval
from framefixer import FrameFixer
from camera.vimbacamera import VimbaCamera
from videowriter import VideoWriter
from stopmanager import StopManager
from timewriter import TimeWriter
from multiprocessing.managers import BaseManager
import os
from multiprocessing import Queue
from view.viewerapp import App

def capture(camera_index, file_path, codec):

    buffer = Queue(128)
    time_buffer = Queue(128)

    BaseManager.register('StopManager', StopManager)
    manager = BaseManager()
    manager.start()
    stop_manager = manager.StopManager()

    frame_fixer = FrameFixer(964, 1292)
    frame_retrieval = FrameRetrieval(frame_fixer, buffer, time_buffer)
    stop_manager.set_start()
    process_capturer = VimbaCamera(frame_retrieval, index=camera_index, manager=stop_manager)
    process_capturer.start()

    filename = correct_filepath(file_path)

    video_writer = VideoWriter(filename=filename, fps=30, height=964, width=1292, codec=codec)
    time_writer = TimeWriter(filename=filename)

    viewer = App(buffer, time_buffer, stop_manager, video_writer, time_writer)
    viewer.show()


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

