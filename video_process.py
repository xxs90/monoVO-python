import cv2
import os
import numpy as np

def video2img(file: str, outputfile):
    capture = cv2.VideoCapture(file)
    
    frameNr = 0
    
    while (True):
    
        success, frame = capture.read()
    
        if success:
            cv2.imwrite(f'./{outputfile}/{str(frameNr).zfill(6)}.png', frame)
    
        else:
            break
    
        frameNr = frameNr+1
    
    capture.release()

def video2gray(file: str, outputfile):
    capture = cv2.VideoCapture(file)
    
    frameNr = 0
    
    while (True):
    
        success, frame = capture.read()
    
        if success:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(f'./{outputfile}/{str(frameNr).zfill(6)}.png', frame)
    
        else:
            break
    
        frameNr = frameNr+1
    
    capture.release()

def imageResize(input_dir:str, output_dir:str):
    file_list = os.listdir(input_dir)
    if len(os.listdir(output_dir)):
        raise Exception('The destination dir is not empty!')
    for i in file_list:
        img = cv2.imread(os.path.join(input_dir,i))
        resized_img = cv2.resize(img, (640, 480))
        cv2.imwrite(f'{output_dir}/'+i, resized_img)


def generatePseudoTimeStamp(time_duration_second:int, sampled_hz:int, input_dir:str, output_dir:str):
    file_list = os.listdir(output_dir)
    if 'times.txt' in file_list:
        raise Exception('There is a existing times.txt!')
    file_list_num = len(os.listdir(input_dir))
    timeStamp = np.arange(0, time_duration_second, 1/sampled_hz)
    np.savetxt(f'{output_dir}/times.txt', timeStamp)
    


if __name__ == "__main__":
    # video2gray('../my_data/house1.mp4', 'output')
    # imageResize("../my_data/house1_gray","../my_data/house1_gray_resized")
    generatePseudoTimeStamp(90, 10, '/home/mingxi/ws/final_proj_5554/my_data/test_data/image_0', '/home/mingxi/ws/final_proj_5554/my_data/test_data')