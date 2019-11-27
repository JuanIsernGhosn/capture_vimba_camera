import os


class TimeWriter(object):

    def __init__(self, filename):
        dir_path = os.path.dirname(os.path.realpath(filename))
        file_name = os.path.basename(filename)
        filename, ext = os.path.splitext(file_name)
        self.filename = os.path.join(dir_path, filename + ".txt")
        self.file = open(self.filename, "a+")

    def write(self, timestamp):
        self.file.write("{}\n".format(str(timestamp)))

    def release(self):
        self.file.close()


