import cv2
 
#Variable untuk VideoCapture
cap = cv2.VideoCapture(0)
 
#Fungsi untuk membuat frame pengaturan pada video
while(True):
    #Membaca video
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    abu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('membuka camera', abu)
    cv2.imshow('membuka kamera',frame)
    #Pengaturan frame
    if cv2.waitKey(1) == ord('v'):
        break
cap.release()
cv2.destroyAllWindows()