import cv2 as cv
import os

def save_frame(video_path, save_dir, basename):
    frame_skip = 10 # Every ? frames is saved
    frame_num = 1 # The number of frame in the total video
    vc = cv.VideoCapture(video_path)

    if vc.isOpened():
        rval, frame = vc.read()
        while rval:
            rval, frame = vc.read()
            if frame_num % frame_skip == 0:
                frame_savename = basename + '_' + str(frame_num) + '.jpg'
                cv.imwrite(os.path.join(save_dir, frame_savename), frame)
            frame_num += 1
            # cv.waitKey(1)
        print('Passed: ', video_path)
    else:
        print('Failed: ', video_path)

    vc.release()


if __name__ == '__main__': 

    PATH = 'C:\\MyProject\\MarkFile\\03'
    input_dir = True  # True: PATH is a dir of several video files. False: PATH is only a video file

    if (input_dir):
        for video_name in os.listdir(PATH):
            video_path = os.path.join(PATH, video_name)
            if os.path.isfile(video_path):
                basename, _ = video_name.split('.')
                save_dir = os.path.join(PATH, basename)
                if not os.path.isdir(save_dir):
                    os.makedirs(save_dir)    
                    save_frame(video_path, save_dir, basename)
    else:
        path_dir, video_name = PATH.rsplit('\\', 1) # on Linux, / instead of //
        basename, _ = video_name.split('.')
        save_dir = os.path.join(path_dir, basename)
        if not os.path.isdir(save_dir):
            os.makedirs(save_dir) 
        save_frame(PATH, save_dir, basename)
