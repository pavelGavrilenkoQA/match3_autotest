from airtest.core.api import *

def shop_main():
    return Template(
        r"shop_main.png",
        record_pos=(0.013, 0.092),
        resolution=(1080, 2340)
    )


def more_offers():
    return Template(
        r"more_offers.png",
        record_pos=(-0.006, 0.978),
        resolution=(1080, 2340)
    )


def coins_2000():
    return Template(
        r"coins_2000.png",
        record_pos=(-0.001, -0.363),
        resolution=(1080, 2340)
    )

def coins_5500():
    return Template(
        r"coins_5500.png",
        record_pos=(-0.003, -0.115),
        resolution=(1080, 2340)
    )

def coins_12000():
    return Template(
        r"coins_12000.png",
        record_pos=(0.017, 0.115),
        resolution=(1080, 2340)
    )


def coins_25000():
    return Template(
        r"coins_25000.png",
        record_pos=(0.005, 0.347),
        resolution=(1080, 2340)
    )


def coins_80000():
    return Template(
        r"coins_80000.png",
        record_pos=(0.003, 0.568),
        resolution=(1080, 2340)
    )


def small_chest():
    return Template(
        r"small_chest.png",
        record_pos=(0.001, -0.439),
        resolution=(1080, 2340)
    )


def welcome_pack():
    return Template(
        r"welcome_pack.png",
        record_pos=(0.029, -0.015),
        resolution=(1080, 2340)
    )


def starter_pack():
    return Template(
        r"starter_pack.png",
        record_pos=(0.005, 0.406),
        resolution=(1080, 2340)
    )


def special_chest():
    return Template(
        r"special_chest.png",
        record_pos=(0.225, -0.105),
        resolution=(1080, 2340)
    )

def large_chest():
    return Template(
        r"large_chest.png",
        record_pos=(0.007, 0.294),
        resolution=(1080, 2340)
    )


def royal_chest():
    return Template(
        r"royal_chest.png",
        record_pos=(0.243, 0.656),
        resolution=(1080, 2340)
    )

def ads_coins():
    return Template(
        r"ads_coins.png",
        record_pos=(0.021, 0.771),
        resolution=(1080, 2340)
    )

if __name__ == "__main__":
    print(shop_main())
    print(more_offers())
    print(coins_2000())
    print(coins_5500())
    print(coins_12000())
    print(coins_25000())
    print(coins_80000())
    print(small_chest())
    print(welcome_pack())
    print(starter_pack())
    print(special_chest())
    print(large_chest())
    print(royal_chest())
    print(ads_coins())
