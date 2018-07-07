import pygame

import subprocess

pygame.init()

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while done==False:
    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

    joystick = pygame.joystick.Joystick(0)

    joystick.init()

    drowis = joystick.get_button( 6 )
    faceRecognation = joystick.get_button( 7 )
    if drowis:
        print("drowis", drowis)
        subprocess.call("./eye_detection.sh", shell=True)
    if faceRecognation:
        print("faceRecognation", faceRecognation)
        subprocess.call("./face_recognition.sh", shell=True)

    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

    # Limit to 20 frames per second
    clock.tick(2)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit ()
