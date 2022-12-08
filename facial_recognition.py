import cv2

def face(img):
     #준비
    hog = cv2.HOGDescriptor() #객체
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector()) #모델지정 
    hogParams = {'winStride': (8,8), 'padding': (32,32), 'scale': 1.05, 'hitThreshold': 0} #파라미터 설정 

    #검출
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #흑백변환 
    human, r = hog.detectMultiScale(gray, **hogParams) #사람 검출 - human에는 사람의 위치정보가 들어감 

    if (len(human)> 0): #사람으로 인식한게 1개 이상이라면 
        for (x, y, w, h) in human:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 255), 3) #사각형을 그려! (여기서 255,255,255는 white 색)
        
    return img
