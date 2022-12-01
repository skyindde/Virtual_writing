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

the screen is being cleared by waving hand.
For this mask of palm color is being used.
When the exposed area of palm is greater than a given value the set of red dots is being emptied and in next frame there is no red dots.
Part of palm is always exposed and sometimes may exceed the given value.
Therefore, the value should be set carefully.

Use track bars to create mask for the pencil or anything which will be used for writing.
The track bars window has 6 scales on which minimum and maximum values of hue, saturation and value of HSV format can be set.
The marker on the scale is moved in left right direction to find a place where reqyured mask part starts to get black.
The values are supposed to be set in such a way that in the mask window only mask of pen/pencil is visible and rest everything is black.
Depending upon the area of exposure, a suitable value can be set in the program.
Also remember that the area of exposure depends on the distance from the camera and is inversely proportional.
Also the area of exposure of the mask can be controlled using fingers and holding it accordingly.
There is a practical limit on the speed of writing due to fixed value of frame rate of the camera and processing speed of the algorithm.
