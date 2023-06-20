from airtest.core.api import *


def level_start_popup_window():
    return Template(
        r"level_start_popup_page.py",
        record_pos=(-0.003, 0.088),
        resolution=(1080, 2340)
    )


def locked_character():
    return Template(
        r"locked_character.png",
        record_pos=(-0.081, 0.314),
        resolution=(1080, 2340)
    )


def text_available_at():
    return Template(
        r"text_available_at.png",
        record_pos=(0.051, 0.097),
        resolution=(1080, 2340)
    )


def comic():
    return Template(
        r"comic.png",
        record_pos=(-0.279, 0.319),
        resolution=(1080, 2340)
    )


def Prankster():
    return Template(
        r"Prankster.png",
        record_pos=(0.094, 0.318),
        resolution=(1080, 2340)
    )


def loafer():
    return Template(
        r"loafer.png",
        record_pos=(0.294, 0.314),
        resolution=(1080, 2340)
    )


def clumsy():
    return Template(
        r"clumsy.png",
        record_pos=(-0.081, 0.325),
        resolution=(1080, 2340)
    )


def comic_selected():
    return Template(
        r"comic_selected.png",
        record_pos=(-0.279, 0.271),
        resolution=(1080, 2340)
    )


def clumsy_selected():
    return Template(
        r"clumsy_selected.png",
        record_pos=(-0.099, 0.263),
        resolution=(1080, 2340)
    )


def prankster_selected():
    return Template(
        r"prankster_selected.png",
        record_pos=(0.106, 0.257),
        resolution=(1080, 2340)
    )


def loafer_selected():
    return Template(
        r"loafer_selected.png",
        record_pos=(0.281, 0.256),
        resolution=(1080, 2340)
    )


def comic2():
    return Template(
        r"comic2.png.png",
        record_pos=(0.013, -0.189),
        resolution=(1080, 2340)
    )


def clumsy2():
    return Template(
        r"clumsy_2.png",
        record_pos=(-0.021, -0.167),
        resolution=(1080, 2340)
    )


def prankster2():
    return Template(
        r"prankster_2.png",
        record_pos=(0.008, -0.196),
        resolution=(1080, 2340)
    )


def loafer2():
    return Template(
        r"loafer2.png",
        record_pos=(0.008, -0.222),
        resolution=(1080, 2340)
    )


if __name__ == "__main__":
    print(level_start_popup_window())
    print(locked_character())
    print(text_available_at())
    print(comic())
    print(Prankster())
    print(loafer())
    print(clumsy())
    print(clumsy_selected())
    print(comic_selected())
    print(prankster_selected())
    print(loafer_selected())
    print(comic2())
    print(clumsy2())
    print(prankster2())
    print(loafer2())

