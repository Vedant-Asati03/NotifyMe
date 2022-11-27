"""
Notifies the user
"""

import os
import time
from pygame import mixer
from plyer import notification


def main():
    """
    Calling functions
    """
    time.sleep(3 * 60)      # In minute
    notify()
    screentime()


def screentime():
    """
    Checks users screentime
    """
    alarm_file = os.path.join("alarm_sound.wav")
    mixer.init()
    mixer.music.load(alarm_file)
    mixer.music.set_volume(10)
    mixer.music.play()


def notify():
    """
    Notifies user via desktop notification
    """

    notification.notify(
        title="Take A Break!",
        message="You have exceeded your screentime",
        app_icon=None,
        timeout=10,
        toast=False,
    )


if __name__ == "__main__":
    main()
    stop_alarm = input("Press 'o' to turn off alarm: ")

    match stop_alarm:

        case "o":
            mixer.music.pause()
