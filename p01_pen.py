import cv2
import numpy as np

# virtual pen and wiping with OpenCV
# orange pen - 23 179 67 127 255 255
# blue refill  89 163 100 255 92 255
# green_cap -  33 39  51 88 160 255
# red pen      172 179 118 222 103 202

def empty(a):
    pass

def wipe(imgg):
    contours, hierarchy = cv2.findContours(imgg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_KCOS)
    for cnt in contours:
        area2 = cv2.contourArea(cnt)
        print(area2)
        if area2 > 30000:    # for work for only valid shapes
            # np.empty(points)
            points.clear()
        # elif area2 > 8000:
            # points = points[:len(points)-10]
            # del points[-1:]


def getCountours(imgg):
    contours, hierarchy = cv2.findContours(imgg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_KCOS)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # print(area)
        if area > 400:    # for work for only valid shapes
            cv2.drawContours(img2, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.01*peri, True)
            x, y, w, h = cv2.boundingRect(approx)
            # cv2.rectangle(img2, (x, y), (x+w, y+h), (0, 255, 0), 1)
            # cv2.circle(img2, (x, y), 5, (0, 0, 255), cv2.FILLED)
            points.append([x+w, y])

cv2.namedWindow("Track Bars")
cv2.resizeWindow("Track Bars", 600, 300)
cv2.createTrackbar("Hue Min", "Track Bars", 33, 179, empty)
cv2.createTrackbar("Hue Max", "Track Bars", 39, 179, empty)
cv2.createTrackbar("Sat Min", "Track Bars", 51, 255, empty)
cv2.createTrackbar("Sat Max", "Track Bars", 88, 255, empty)
cv2.createTrackbar("Val Min", "Track Bars", 160, 255, empty)
cv2.createTrackbar("Val Max", "Track Bars", 255, 255, empty)


vid = cv2.VideoCapture(0)   # o for default webcam, 1 or 2 for additional webcam
vid.set(3, 800)  # 3 for widthq
vid.set(4, 600)  # 4 for height
vid.set(10, 100) # 10 for brightness

points = []

while True:
    success, img = vid.read()
    # img = cv2.resize(img, (400, 300))
    img2 = img.copy()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue Min", "Track Bars")
    h_max = cv2.getTrackbarPos("Hue Max", "Track Bars")
    s_min = cv2.getTrackbarPos("Sat Min", "Track Bars")
    s_max = cv2.getTrackbarPos("Sat Max", "Track Bars")
    v_min = cv2.getTrackbarPos("Val Min", "Track Bars")
    v_max = cv2.getTrackbarPos("Val Max", "Track Bars")

    # print(h_min, h_max, s_min, s_max, v_min, v_max)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    lower2 = np.array([5, 31, 207])
    upper2 = np.array([27, 135, 255])
    mask = cv2.inRange(imgHSV, lower, upper)
    mask2 = cv2.inRange(imgHSV, lower2, upper2)
    imgResult = cv2.bitwise_and(img, img, mask=mask)
    getCountours(mask)
    wipe(mask2)

    for pt in points:
        cv2.circle(img2, (pt[0], pt[1]), 5, (0, 0, 255), cv2.FILLED)
    img2 = cv2.flip(img2, 1)
    cv2.imshow("H5", img2)

    # cv2.imshow("Original", img)
    # cv2.imshow("HSV", imgHSV)
    # cv2.imshow("Mask", mask)
    cv2.imshow("Result", imgResult)

    # cv2.imshow("Virtual Board", img2)

    hor1 = np.hstack((img, imgHSV))
    # cv2.imshow("fff", hor1)
    hor2 = np.hstack((img2, imgResult))
    # Result = np.vstack((hor2, hor1))
    # cv2.imshow("Results", Result)
    # cv2.imshow("H2", hor2)
    # cv2.waitKey(1)


    # cv2.imshow("Faces", img)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    if cv2.waitKey(1) == 27: # ESC key
        break