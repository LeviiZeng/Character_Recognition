import cv2
import recognition #the recognition part of our program.


if __name__ == "__main__":

    #create a window named 'camara' (1 means we can't change the size of the window）
    cv2.namedWindow("camera",1)
    # 0 means call camera of our laptop; 1 means call the camera with an usb projector which can be connected to laptop
    #cv2.VideoCapture(0)

    #ip camera: if you have the app, then you can use your ip of your camera to call your phone camera.
    #video = 'http://admin:admin@122.239.219.18:8081/video'     #admin:admin are username and passowrd. 122.239.219.18:8081 is ip.
    capture = cv2.VideoCapture(0) # capture the camera of laptop

    # we use an unending loop to keep the window, or it will appear for a while and then disappear.
    while True: # the idea that we get from the Internet(Only the while loop, the codes in loop is our own codes).
        success,img = capture.read()
        cv2.imshow("camera",img)
        #set keys of start and stop.
        key = cv2.waitKey(1)
        if key == 27: # 27 is the 'esc' key, if we type 'esc', then the loop will stop and the window will disappear.

            break
        if key == 32: # 32 is the 'space' key. if we type 'space', then it will take a picture.

            filename = 'frames.jpg' # create a file named frames.jpg to store the pictures that our camera take.
            cv2.imwrite(filename,img) # save images
            s = recognition.img_to_str(filename) # transform the image to texts.
            print(s)

    #release the camera
    capture.release()
    #close the window
    cv2.destroyWindow("camera")