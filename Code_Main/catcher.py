import cv2
import numpy as np
from sklearn.externals import joblib

def give_position(red):

    find_object_color = str(red)
    capture = cv2.VideoCapture(0)
    Lower = []
    Upper = []

    if find_object_color == 'orange':
        Lower = np.array([0, 100, 100])
        Upper = np.array([10, 255, 255])
    if find_object_color == 'green':
        Lower = np.array([50, 50, 50])
        Upper = np.array([75, 255, 255])
    if find_object_color == 'blue':
        Lower = np.array([110, 65, 65])
        Upper = np.array([130, 255, 255])
    if find_object_color == 'yellow':
        Lower = np.array([20, 35, 35])
        Upper = np.array([30, 255, 255])
    if find_object_color == 'red':
        Lower = np.array([156, 40, 40])
        Upper = np.array([180, 255, 255])
    while (1):  # get a frame and show
        ret, frame = capture.read()
        cv2.imshow('Original', frame)  # change to hsv model
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite("result.png", frame)
            break
    capture.release()

    image = cv2.imread("result.png")
    frame = cv2.blur(image, (5, 5))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # get mask
    mask = cv2.inRange(hsv, Lower, Upper)
    cv2.imshow('Mask for detect red', mask)  # detect red

    target = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('Shift out background', target)
    gray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
    th, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)
    _, contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    p = 0
    position = []
    for cnt in contours:
        X, Y, w, h = cv2.boundingRect(cnt)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image, str(p), (X - 10, Y + 10), font, 1, (0, 0, 255), 2)

        (x, y), radius = cv2.minEnclosingCircle(cnt)
        center = (int(x), int(y))
        radius = int(radius)
        cv2.circle(image, center, radius, (0, 255, 0), 2)
        print("Center ", p, " :", center)
        position.append(center)
        p = p + 1

    print('Total number of objects', p)
    print(position)
    cv2.imshow('imm', image)

    while True:
        Key = chr(cv2.waitKey(15) & 255)
        if Key == 'q':
            capture.release()
            cv2.destroyAllWindows()
            break

    sum_x = 0
    sum_y = 0
    for x in range(len(position)):
        sum_x = sum_x + position[x][0]
        sum_y = sum_y + position[x][1]
    x_test = int(sum_x/p)
    y_test = int(sum_y/p)
    print(x_test,y_test)

    model = joblib.load('save/model.pkl')
    print(model.predict([[x_test,y_test]]))

    result = str(int(model.predict([[x_test, y_test]])[0]))
    big_case = int(result[0])
    small_case = int(result[1:])
    return big_case,small_case

