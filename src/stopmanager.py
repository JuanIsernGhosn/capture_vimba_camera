
class StopManager(object):

    def __init__(self):
        self.working = False

    def set_start(self):
        self.working = True

    def set_stop(self):
        self.working = False

    def get_state(self):
        return self.working
