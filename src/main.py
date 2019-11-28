import argparse
import capturer

parser = argparse.ArgumentParser()

parser.add_argument('-I', type=int, action='store',
                    dest='camera_index',
                    help='Choose camera device index')

parser.add_argument('-P', action='store',
                    dest='file_path',
                    help='Path for saving recorded video file')

parser.add_argument('-C', action='store',
                    dest='codec',
                    help='Resulting codec for video file')


results = parser.parse_args()

if __name__ == '__main__':
    camera_index = results.camera_index if results.camera_index is not None else 0
    file_path = results.file_path if results.file_path is not None else './untitle.mp4'
    codec = results.codec if results.codec is not None else 'DIVX'
    capturer.capture(camera_index=camera_index, file_path=file_path, codec=codec)