from airtest.core.api import *


def button_continue_question():
    return Template(
        "button_continue_question.png",
        record_pos=(0.019, -0.413),
        resolution=(1080, 2340)
    )


def are_you_sure():
    return Template(
        r"are_you_sure.png",
        record_pos=(-0.005, -0.326),
        resolution=(1080, 2340)
    )


def button_continue_playing():
    return Template(
        r"button_continue_playing.png",
        record_pos=(-0.011, 0.228),
        resolution=(1080, 2340)
    )


def button_no():
    return Template(
        r"button_no.png",
        record_pos=(-0.189, 0.197),
        resolution=(1080, 2340)
    )


def button_yes():
    return Template(
        r"button_yes.png",
        record_pos=(0.199, 0.197),
        resolution=(1080, 2340)
    )


def button_continue():
    return Template(
        r"button_continue.png",
        record_pos=(-0.017, 0.301),
        resolution=(1080, 2340)
    )


def moves_2_reward():
    return Template(
        r"moves_2_reward.png",
        record_pos=(-0.003, 0.707),
        resolution=(1080, 2340)
    )


def coins_900():
    return Template(
        r"coins_900.png",
        record_pos=(0.169, 0.297),
        resolution=(1080, 2340)
    )


def moves_5_icon():
    return Template(
        r"moves_5_icon.png",
        record_pos=(-0.209, -0.01),
        resolution=(1080, 2340)
    )


def add_5_moves_to_continue():
    return Template(
        r"add_5_moves_to_continue.png",
        record_pos=(0.005, -0.196),
        resolution=(1080, 2340)
    )


def coins_1900():
    return Template(
        r"coins_1900.png",
        record_pos=(0.171, 0.297),
        resolution=(1080, 2340)
    )


def coins_2900():
    return Template(
        r"coins_2900.png",
        record_pos=(0.185, 0.297),
        resolution=(1080, 2340)
    )


def coins_3900():
    return Template(
        r"coins_3900.png",
        record_pos=(0.175, 0.299),
        resolution=(1080, 2340)
    )


def coins_4900():
    return Template(
        r"coins_4900.png",
        record_pos=(0.185, 0.295),
        resolution=(1080, 2340)
    )

def comic_loose_animation():
    return Template(
        r"comic_loose_animation.png",
        record_pos=(-0.241, 0.021),
        resolution=(1080, 2340)
    )


def text_elements_will_be_lost():
    return Template(
        r"text_elements_will_be_lost.png",
        record_pos=(0.12, -0.008),
        resolution=(1080, 2340)
    )


def loose_progress_event():
    return Template(
        r"loose_progress_event.png",
        record_pos=(0.049, 0.019),
        resolution=(1080, 2340)
    )

def no_more_lives():
    return Template(
        r"no_more_lives.png",
        record_pos=(0.011, -0.581),
        resolution=(1080, 2340)
    )


def watch_ad():
    return Template(
        r"watch_ad.png",
        record_pos=(-0.004, 0.057),
        resolution=(1080, 2340)
    )


def refill():
    return Template(
        r"refill.png",
        record_pos=(-0.059, 0.252),
        resolution=(1080, 2340)
    )


def jolly_favor():
    return Template(
        r"jolly_favor.png",
        record_pos=(0.015, 0.633),
        resolution=(1080, 2340)
    )

def extra_candy():
    return Template(
        r"extra_candy.png",
        record_pos=(-0.011, 0.687),
        resolution=(1080, 2340)
    )


if __name__ == "__main__":
    print(button_continue_question())
    print(button_continue_playing())
    print(are_you_sure())
    print(button_no())
    print(button_yes())
    print(button_continue())
    print(moves_2_reward())
    print(coins_900())
    print(moves_5_icon())
    print(add_5_moves_to_continue())
    print(coins_1900())
    print(coins_2900())
    print(coins_3900())
    print(coins_4900())
    print(comic_loose_animation())
    print(text_elements_will_be_lost())
    print(loose_progress_event())
    print(no_more_lives())
    print(watch_ad())
    print(refill())
    print(jolly_favor())
    print(extra_candy())

