from airtest.core.api import *


def settings():
    return Template(
        r"settings.png",
        record_pos=(0.375, -0.872),
        resolution=(1080, 2340)
    )


def minus_5_steps():
    return Template(
        r"minus_5_steps.png",
        record_pos=(-0.411, -0.902),
        resolution=(1080, 2340)
    )


def plus_5_steps():
    return Template(
        r"plus_5_steps.png",
        record_pos=(-0.237, -0.901),
        resolution=(1080, 2340)
    )


def pick():
    return Template(
        r"pick.png",
        record_pos=(0.013, 0.921),
        resolution=(1080, 2340)
    )


def whirly_mill():
    return Template(
        r"whirly_mill.png",
        record_pos=(0.187, 0.921),
        resolution=(1080, 2340)
    )


def hand():
    return Template(
        r"hand.png",
        record_pos=(0.358, 0.928),
        resolution=(1080, 2340)
    )


def prankster_gameplay():
    return Template(
        r"prankster_gameplay.png",
        record_pos=(-0.306, 0.881),
        resolution=(1080, 2340)
    )


def comic_gameplay():
    return Template(
        r"comic_gameplay.png",
        record_pos=(-0.281, 0.871),
        resolution=(1080, 2340)
    )


def clumsy_gameplay():
    return Template(
        r"clumsy_gameplay.png",
        record_pos=(-0.303, 0.88),
        resolution=(1080, 2340)
    )


def loafer_gameplay():
    return Template(
        r"loafer_gameplay.png",
        record_pos=(-0.292, 0.863),
        resolution=(1080, 2340)
    )


def white_element():
    return Template(
        r"white_element.png",
        record_pos=(-0.318, -0.429),
        resolution=(1080, 2340)
    )


def red_element():
    return Template(
        r"red_element.png",
        record_pos=(-0.113, -0.429),
        resolution=(1080, 2340)
    )


def blue_element():
    return Template(
        r"blue_element.png",
        record_pos=(0.001, -0.427),
        resolution=(1080, 2340)
    )


def orange_element():
    return Template(
        r"orange_element.png",
        record_pos=(-0.111, -0.425),
        resolution=(1080, 2340)
    )


def green_element():
    return Template(
        r"green_element.png",
        record_pos=(-0.107, -0.327),
        resolution=(1080, 2340)
    )


def purple_element():
    return Template(
        r"purple_element.png",
        record_pos=(-0.321, -0.105),
        resolution=(1080, 2340)
    )


if __name__ == "__main__":
    print(settings())
    print(minus_5_steps())
    print(plus_5_steps())
    print(pick())
    print(whirly_mill())
    print(hand())
    print(prankster_gameplay())
    print(comic_gameplay())
    print(clumsy_gameplay())
    print(loafer_gameplay())
    print(white_element())
    print(red_element())
    print(blue_element())
    print(orange_element())
    print(green_element())
    print(purple_element())
