# this is a fitness_alarm code

# importing all the essential modules
from pygame import mixer
from datetime import datetime
from time import time


# function for play the tune/sound
def sound_loop(stopper):
    mixer.init()
    mixer.music.load("sound.wav")
    mixer.music.play()
    while True:
        user_input = input()
        if user_input == stopper:
            mixer.music.stop()
            break


# function for wrtite the message and activiity log as a txt file
def log_file(msg):
    with open("fitness_alarm.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")


# main function

if __name__ == '__main__':
    init_water = time()
    init_physical = time()
    init_eye = time()
    water_time =5 #30 * 60
    physical_time = 30#60 * 60
    eye_time =50  #40 * 60

    while True:

        # for water
        if time() - init_water > water_time:
            print("This is water time. Time for drining water.Write 'drank' in order to stop the sound")
            sound_loop("drank")
            init_water = time()
            log_file("last water drinking time")

        # for eye
        if time() - init_eye > eye_time:
            print("Time for some eye exercise. After finishing the eye exercise write 'done' to stop the sound")
            sound_loop("done")
            init_eye = time()
            log_file("last eye rest time")

        # for physical exercise
        if time() - init_physical > physical_time:
            print(
                "time to off the monitor and do some physical exercise. After finished write down 'physical' to stop the sound")
            sound_loop("physical")
            init_physical = time()
            log_file("last physical exercise time")
