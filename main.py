import cv2
import webbrowser

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
while True:
    _,img=cap.read()
    data,one, _=detector.detectAndDecode(img)
    if data:
        avg=data
        break
    cv2.imshow('qrcodescanner app', img)
    if cv2.waitKey(1)==ord('q'):
        break
b = webbrowser.open(str(avg))
cap.release(avg)
cv2.destroyAllWindows()