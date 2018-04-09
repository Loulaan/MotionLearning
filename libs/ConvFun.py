from imutils.object_detection import non_max_suppression
import numpy as np
import cv2


def ConvPilot(frame, mode):
    if mode == 0:
        # Gray Scale
        gr = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        doneFrame = cv2.cvtColor(gr, cv2.COLOR_GRAY2BGR)

    if mode == 1:
        # Negative
        doneFrame = cv2.bitwise_not(frame)

    if mode == 2:
        # Sepia
        kernel = np.asarray( [
    [0.272, 0.534, 0.131],
    [0.349, 0.686, 0.168],
    [0.393, 0.769, 0.189]] )
        doneFrame = cv2.transform(frame, kernel)

    if mode == 3:
        # Blue Sepia
        kernel = np.asarray( [ 
[0.393, 0.769, 0.189], 
[0.349, 0.686, 0.168], 
[0.272, 0.534, 0.131]] )
        doneFrame = cv2.transform(frame, kernel)

    if mode == 4:
        kernel = np.ones((5,5),np.uint8)
        doneFrame = cv2.morphologyEx(frame, cv2.MORPH_GRADIENT, kernel)

    if mode == 5:
        s_vs_p = 0.5
        amount = 0.1  # Менять количество шумов тут
        doneFrame = np.copy(frame)
        # Salt mode
        num_salt = np.ceil(amount * frame.size * s_vs_p)
        coords = [np.random.randint(0, i - 1, int(num_salt))
        for i in frame.shape]
        doneFrame[coords] = 1

        # Pepper mode
        num_pepper = np.ceil(amount* frame.size * (1. - s_vs_p))
        coords = [np.random.randint(0, i - 1, int(num_pepper))
        for i in frame.shape]
        doneFrame[coords] = 0

    if mode == 6:
        pass

    if mode == 7:
        edges = cv2.Canny(frame, 100, 200)
        doneFrame = frame
        for i in range(edges.shape[0]):
            for j in range(edges.shape[1]):
                if edges[i][j] != 0:
                    doneFrame[i][j] = [0, 0, 255]

    if mode == 8:
        hog = cv2.HOGDescriptor()
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        orig = frame.copy()
        (rects, weights) = hog.detectMultiScale(frame, winStride=(4, 4), padding=(0, 0), scale=1.1)
        for (x, y, w, h) in rects:
            cv2.rectangle(orig, (x, y), (x + w, y + h), (255, 0, 0), 1)
        rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
        pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

        doneFrame = frame
        for (xA, yA, xB, yB) in pick:
            cv2.rectangle(doneFrame, (xA, yA), (xB, yB), (255, 0, 0), 1)

    if mode == 9:
        hog = cv2.HOGDescriptor()
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        orig = frame.copy()
        (rects, weights) = hog.detectMultiScale(frame, winStride=(4, 4), padding=(0, 0), scale=1.1)
        for (x, y, w, h) in rects:
            cv2.rectangle(orig, (x, y), (x + w, y + h), (255, 0, 0), 1)
        rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
        pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
        max = -1
        max_coord = (0, 0, 0, 0)
        for (xA, yA, xB, yB) in pick:
            if abs(xA - xB) + abs(yA - yB) > max:
                max_coord = (yA, yB, xA, xB)
                max = abs(xA - xB) + abs(yA - yB)

        cropped = frame[max_coord[0] + 1:max_coord[1] - 1, max_coord[2] + 1:max_coord[3] - 1]
        imgray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY).copy()
        blur = cv2.GaussianBlur(imgray, (13, 13), 0)
        edges = cv2.Canny(blur, 100, 200)
        __, contours, __ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            cv2.drawContours(cropped, [cnt], 0, (0, 0, 255), 1)
        doneFrame = frame

    if mode == 10:
        doneFrame = frame

    return doneFrame


def setFlag(GUI):
    if GUI.settings.ui.radioButton.isChecked():
        mode = 0
    if GUI.settings.ui.radioButton_2.isChecked():
        mode = 1
    if GUI.settings.ui.radioButton_3.isChecked():
        mode = 2
    if GUI.settings.ui.radioButton_4.isChecked():
        mode = 3
    if GUI.settings.ui.radioButton_5.isChecked():
        mode = 4
    if GUI.settings.ui.radioButton_6.isChecked():
        mode = 5
    if GUI.settings.ui.radioButton_8.isChecked():
        mode = 6
    if GUI.settings.ui.radioButton_7.isChecked():
        mode = 7
    if GUI.settings.ui.radioButton_9.isChecked():  # Поиск людей
        mode = 8
    if GUI.settings.ui.radioButton_12.isChecked():  # Контур тренера
        mode = 9
    if GUI.settings.ui.radioButton_16.isChecked():  # None
        mode = 10

    return mode