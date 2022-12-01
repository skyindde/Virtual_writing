# Virtual_writing
A program for writing virtually on screen using just anything around.

Using OpenCV, an application has been created in Python to write virtually on the screen.
One can use practically anything for writing.
a color paatch is  tracked using a mask in HSV format of image input from webcam.
CV2.findContours is applied to get the contour of blue part and CV2.drawContours is  used to draw it
the exposure area of the patch is controlled by the fingers.
While writing it is being exposed and when you don't need to write, cover most part of it behind the fingers.
This changes the area of the blue contour.
There is a minimum contour area required in order to write which can be tuned as needed.
For writing, red dots are being added in a set of already existing red dots.
The positions of the red dots have been related to the position of the contour.
In each progressing frame, new larger set of red dots is drawn.
You would need to tune some parameters in the code according to the ambient light conditions and your skin color.
