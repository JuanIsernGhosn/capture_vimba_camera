
from abc import ABC
from multiprocessing import Process

class Camera(ABC, Process):

    def __init__(self, frame_retrieval):
        super(Camera, self).__init__()
        self.frame_retrieval = frame_retrieval