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


def window_connect():
    return Template(
        r"window_connect.png",
        record_pos=(-0.003, -0.181),
        resolution=(1080, 2340)
    )


def account_test_9():
    return Template(
        r"account_test9.png",
        record_pos=(-0.079, -0.315),
        resolution=(1080, 2340)
    )


def button_settings():
    return Template(
        r"button_settings.png",
        record_pos=(-0.38, 0.959),
        resolution=(1080, 2340)
    )


def music_on():
    return Template(
        r"music_on.png",
        record_pos=(0.109, -0.322),
        resolution=(1080, 2340)
    )


def sound_on():
    return Template(
        r"sound_on.png",
        record_pos=(0.115, -0.231),
        resolution=(1080, 2340)
    )


def swipe_on():
    return Template(
        r"swipe_on.png",
        record_pos=(0.248, -0.091),
        resolution=(1080, 2340)
    )


def swipe_off():
    return Template(
        r"swipe_off.png",
        record_pos=(0.244, 0.023),
        resolution=(1080, 2340)
    )


def button_connection():
    return Template(
        r"button_connection.png",
        record_pos=(-0.166, 0.181),
        resolution=(1080, 2340)
    )


def russian():
    return Template(
        r"russian.png",
        record_pos=(0.175, 0.183),
        resolution=(1080, 2340)
    )


def all_languages():
    return Template(
        r"all_languages.png",
        record_pos=(0.013, 0.039),
        resolution=(1080, 2340)
    )


def english():
    return Template(
        r"english.png",
        record_pos=(-0.197, -0.1),
        resolution=(1080, 2340)
    )


def english_selected():
    return Template(
        r"english_selected.png",
        record_pos=(-0.171, -0.105),
        resolution=(1080, 2340)
    )


def cross():
    return Template(
        r"cross.png",
        record_pos=(0.369, -0.314),
        resolution=(1080, 2340)
    )


if __name__ == "__main__":
    print(button_ok_privacy())
    print(button_ok_privacy())
    print(button_save_my_progress())
    print(account_test_9())
    print(button_settings())
    print(music_on())
    print(sound_on())
    print(swipe_on())
    print(swipe_off())
    print(button_connection())
    print(russian())
    print(all_languages())
    print(english())
    print(english_selected())
    print(cross())
