import cv2


class Viewer(object):
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.__create_window()

    def __create_window(self):
        cv2.namedWindow(self.name, cv2.WINDOW_NORMAL)
        print("Running, q to exit...")

    def show_frame(self, frame):
        frame = cv2.resize(frame, self.size)
        cv2.imshow(self.name, frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return True
        return False

    def finish(self):
        cv2.destroyAllWindows()