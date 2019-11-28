from camera.camera import Camera
from pymba import Vimba
import time

class VimbaCamera(Camera):

    def __init__(self, frame_retrieval, index=0, manager=None):
        Camera.__init__(self, frame_retrieval)
        self.index = index
        self.manager = manager

    def run(self):
        print('Record video process started:', self, self.is_alive())

        with Vimba() as vimba:
            print(vimba.camera_ids())
            self.camera = vimba.camera(self.index)
            self.camera.open()
            self.camera.arm('Continuous', self.frame_retrieval.frame_callback)
            self.camera.AcquisitionFrameRateAbs = 30
            self.camera.TriggerSource = 'FixedRate'
            self.camera.PixelFormat = 'BayerRG8'
            self.camera.SyncOutSelector = 'SyncOut1'
            self.camera.SyncOutSource = 'Exposing'
            self.camera.start_frame_acquisition()

            while self.manager.get_state():
                pass

            self.stop_recording()

    def stop_recording(self):
        self.camera.stop_frame_acquisition()
        self.camera.disarm()
        self.camera.close()
        Vimba().shutdown()
