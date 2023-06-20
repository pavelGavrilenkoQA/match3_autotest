from airtest.core.api import *


def core_settings_popup():
    return Template(
        r"core_settings_popup.py",
        record_pos=(0.031, -0.024),
        resolution=(1080, 2340)
    )


def cross():
    return Template(
        r"cross.png",
        record_pos=(0.371, -0.336),
        resolution=(1080, 2340)
    )


def sounds():
    return Template(
        r"sounds.png"
    )


def music():
    return Template(
        r"music.png"
    )


def vibration_on():
    return Template(
        r"vibration_on.png",
        record_pos=(0.261, 0.05),
        resolution=(1080, 2340)
    )


def vibration_off():
    return Template(
        r"vibration_off.png",
        record_pos=(0.245, 0.054),
        resolution=(1080, 2340)
    )


def button_exit():
    return Template(
        r"button_exit.png",
        record_pos=(-0.185, 0.237),
        resolution=(1080, 2340)
    )


def button_continue():
    return Template(
        r"button_continue.png",
        record_pos=(0.195, 0.231),
        resolution=(1080, 2340)
    )


def lose():
    return Template(
        r"lose.png",
        record_pos=(-0.281, 0.435),
        resolution=(1080, 2340)
    )


def fatal():
    return Template(
        r"fatal.png",
        record_pos=(-0.269, 0.538),
        resolution=(1080, 2340)
    )


def restart():
    return Template(
        r"restart.png",
        record_pos=(-0.271, 0.636),
        resolution=(1080, 2340)
    )


def win():
    return Template(
        r"win.png",
        record_pos=(0.26, 0.428),
        resolution=(1080, 2340)
    )


def cheater_panel():
    return Template(
        r"cheater_panel.png",
        record_pos=(0.275, 0.641),
        resolution=(1080, 2340)
    )


if __name__ == "__main__":
    print(core_settings_popup())
    print(cross())
    print(sounds())
    print(music())
    print(vibration_on())
    print(vibration_off())
    print(button_exit())
    print(button_continue())
    print(lose())
    print(fatal())
    print(restart())
    print(win())
    print(cheater_panel())