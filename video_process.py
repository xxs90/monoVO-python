import cv2
 


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


if __name__ == "__main__":
    video2gray('../my_data/house1.mp4', 'output')