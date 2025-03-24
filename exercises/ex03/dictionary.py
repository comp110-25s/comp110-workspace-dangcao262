"""Dictionary Assignment"""

__author__ = "730747262"


def invert(a: dict[str, str]) -> dict[str, str]:
    new_dict = {}
    used_values = set()

    for key in a:
        value = a[key]

        if value in used_values:
            raise KeyError("There are two of the same key and THAT CANNOT HAPPEN")

        """x[key] = value so saying you're basically saying new_dict[value] = key"""
        new_dict[a[key]] = key
        used_values.add(value)

    return new_dict


def count(b: list[str]) -> dict[str, int]:
    new_dict = {}
    """making a new dictionary and counting how many times an item is seen in a list"""
    for item in b:
        """because you labeled the elements of the list "item"  it refers the list"""
        if item in new_dict:
            """if an item is seen in the key already it adds one to the value"""
            new_dict[item] += 1
        else:
            new_dict[item] = 1

    return new_dict


def favorite_color(c: dict[str, str]) -> str:
    """this function records the colors and the amount of times they're seen"""
    """then it prints the most seen one"""
    colors = []

    for name in c:
        colors.append(c[name])
    color_count = count(colors)

    greatest = 0
    fav_color = ""

    for color in color_count:
        if color_count[color] > greatest:
            greatest = color_count[color]
            fav_color = color

    return fav_color


def bin_len(d: list) -> dict[int, str]:
    """this function records lengths of each word in a list and make those keys"""
    """then as the value it makes a set of the words that are those lengths """
    new_dict = {}

    for item in d:
        length = len(item)

        if item not in new_dict:
            new_dict[length] = set()

        new_dict[length].add(item)

    return new_dict
