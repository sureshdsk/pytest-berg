from pynotifier import Notification
import chime


def notify(title, description):
    Notification(
        title=title,
        description=description,
        duration=5,
        urgency="normal",
    ).send()


def play_success():
    chime.success()


def play_warning():
    chime.warning()
