from picamera import PiCamera
from time import sleep

while 1 == 1:
    print('awaiting input') #input a empty string to take the shot
    result = input()

    if result == '':
        print('taking the shot in 2 sec')
        camera = PiCamera()

        camera.start_preview()
        sleep(2)
        save_location = '/home/pi/Desktop/image.jpg'
        camera.capture(save_location)
        camera.stop_preview()
        print('shot taken, saved at ' + save_location)
