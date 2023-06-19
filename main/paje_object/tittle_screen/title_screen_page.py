from airtest.core.api import *


def button_ok_privacy():
    return Template(
        r"button_ok_privacy.png",
        record_pos=(-0.013, 0.226),
        resolution=(1080, 2340)
    )


def button_play():
    return Template(
        r"button_play.png",
        record_pos=(-0.035, 0.55),
        resolution=(1080, 2340)
    )


def button_save_my_progress():
    return Template(
        r"button_save_my_progress.png",
        record_pos=(0.001, 0.791),
        resolution=(1080, 2340)
    )


def button_settings():
    return Template(
        r"button_settings.png",
        record_pos=(-0.38, 0.959),
        resolution=(1080, 2340)
    )


def privacy_window():
    return Template(
        r"privacy_window.png",
        record_pos=(-0.004, 0.03),
        resolution=(1080, 2340)
    )


def privacy_first_link():
    return Template(
        r"privacy_first_link.png.png",
        record_pos=(0.009, 0.057),
        resolution=(1080, 2340)
    )


def privacy_second_link():
    return Template(
        r"privacy_second_link.png",
        record_pos=(0.017, 0.121),
        resolution=(1080, 2340)
    )


def first_debug():
    return Template(
        r"first_debug.png",
        record_pos=(0.405, 0.687),
        resolution=(1080, 2340)
    )


def second_debug():
    return Template(
        r"second_debug.png",
        record_pos=(0.394, 0.968),
        resolution=(1080, 2340)
    )


if __name__ == "__main__":
    print(button_ok_privacy())
    print(button_save_my_progress())
    print(button_settings())
    print(privacy_window())
    print(privacy_first_link())
    print(privacy_second_link())
    print(first_debug())
    print(second_debug())