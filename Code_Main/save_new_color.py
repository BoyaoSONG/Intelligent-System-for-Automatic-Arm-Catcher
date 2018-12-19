import cv2
import numpy as np
def get_hsv():
    print('Please put your new object in the centre case, then press Enter to save new color')
    camera = cv2.VideoCapture(0)
    while True:
        grabbed, frame = camera.read()
        cv2.imshow("all", frame)
        imCrop = frame[220:370, 220:370]
        im = cv2.blur(imCrop, (9, 9))
        hsvRoi = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)  # get mask
        # Display cropped image
        cv2.imshow("Image", hsvRoi)

        Key = cv2.waitKey(15)
        if Key == 13:
            lower = np.array([hsvRoi[:, :, 0].min(), hsvRoi[:, :, 1].min(), hsvRoi[:, :, 2].min()])
            upper = np.array([hsvRoi[:, :, 0].max(), hsvRoi[:, :, 1].max(), hsvRoi[:, :, 2].max()])
            print(lower)
            print(upper)
            break
    camera.release()
    cv2.destroyAllWindows()
    return lower, upper