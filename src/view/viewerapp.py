# -*- coding: utf-8 -*-
from view.gui import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets, QtGui
from view.imagefix import fit_image_with_borders, image_decode
import sys


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

    def append_record_action(self, function):
        self.actionParar.triggered.connect(function)

    def append_stop_action(self, function):
        self.actionIniciar.triggered.connect(function)

    def get_view_size(self):
        return self.main_view.size().height(), self.main_view.size().width()

    def view_print(self, frame):
        width_step = frame.shape[1] * 3
        img = QtGui.QImage(frame, frame.shape[1], frame.shape[0], width_step, QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap.fromImage(img)
        self.main_view.setPixmap(pix)
        self.main_view.show()

class App(QtWidgets.QApplication):

    def __init__(self, buffer, time_buffer, stop_manager, video_writer, time_writer):
        super(App, self).__init__(sys.argv)
        self.MainWindow = MainWindow()
        self.buffer = buffer
        self.time_buffer = time_buffer
        self.add_controllers()
        self.stop_manager = stop_manager
        self.video_writer = video_writer
        self.time_writer = time_writer
        self.recording = False

    def add_controllers(self):
        self.start_viewing()
        self.MainWindow.append_record_action(self.record)
        self.MainWindow.append_stop_action(self.stop)

    def record(self):
        self.recording = True

    def stop(self):
        if self.recording:
            self.video_writer.release()
            self.time_writer.release()
        self.stop_manager.set_stop()
        self.recording=False

    def show(self):
        self.MainWindow.show()
        sys.exit(self.exec_())

    def update_view(self):
        if self.buffer.qsize() > 0:

            frame = self.buffer.get()
            timestamp = self.time_buffer.get()

            if self.recording:
                self.time_writer.write(timestamp)
                self.video_writer.write(frame)

            (view_h, view_w) = self.MainWindow.get_view_size()
            frame = fit_image_with_borders(frame, view_h, view_w)
            self.MainWindow.view_print(frame)

    def start_viewing(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_view)
        self.timer.start(1)