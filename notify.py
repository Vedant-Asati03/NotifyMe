"""
Notifies the user
"""

import time
from plyer import notification


def main():
    """
    Calling functions
    """
    print("\nOK, You will be notified in every 1/2 hour\n")
    for _ in range(10):
        time.sleep(1800)  # In minute
        notify()


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
