from _pytest.config.argparsing import Parser as PytestParser
import pytest
from .notification import notify, play_success, play_warning


def pytest_addoption(parser: PytestParser):
    parser.addoption(
        "--notify",
        action="store_true",
        help="Sends a desktop notification when pytest is finished.",
    )

    parser.addoption(
        "--sound",
        "--play-sound",
        action="store_true",
        help="Plays a sound when pytest is finished.",
    )


def pytest_sessionfinish(session: pytest.Session, exitstatus: int):
    notify_on = session.config.getoption("notify")
    sound_on = session.config.getoption("sound")

    if notify_on:
        if exitstatus == 0:
            notify("Pytest", "All tests are succesfull!")
        else:
            notify("Pytest", "Failing tests detected!")

    if sound_on:
        if exitstatus == 0:
            play_success()
        else:
            play_warning()
