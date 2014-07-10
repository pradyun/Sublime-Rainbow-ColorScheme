#!usr/bin/python
# -*- coding: utf8 -*-
"""Generates the color scheme from a Python definition of the color schemes

Makes possible to use all kinds of nice functions in color schemes
"""

import os
import sys
import json
import colorsys
import plistlib

AUTHOR = "Pradyun"
PACKAGE_NAME = "Color Scheme - Rainbow"


def get_packages_path():
    if sys.platform.startswith("darwin"):
        ret = os.path.expanduser("~/Library/Application Support/Sublime Text 3")
    elif sys.platform.startswith("win"):
        ret = os.path.join(os.environ["APPDATA"], "Sublime Text 3")
    elif sys.platform.startswith("linux"):
        ret = os.path.expanduser("~/.config/sublime-text-3")
    else:
        raise Exception("Unknown OS!")
    return os.path.join(ret, "Packages")


def generate_color_scheme(scheme_name, color_scheme_dict):
    fname = scheme_name + ".tmTheme"
    path = os.path.join(get_packages_path(), PACKAGE_NAME, fname)
    plistlib.writePlist(color_scheme_dict, path)
    print("Generated: " + fname)


#-------------------------------------------------------------------------------
# Color representation schemes
#-------------------------------------------------------------------------------
# hex    : "#000000" - "#FFFFFF"
# rgb_int: (0, 0, 0) - (255, 255, 255)
# rgb    : (0, 0, 0) - (1.0, 1.0, 1.0)
# hsv    : (0, 0, 0) - (1.0, 1.0, 1.0)


def split_hex(hex_str):
    if hex_str[0] == "#":
        hex_str = hex_str[1:]
    return [hex_str[i-2:i] for i in range(2, len(hex_str) + 1, 2)]


def hex2rgb(hex_val):
    parts = split_hex(hex_val)
    assert len(parts) == 3, hex_val
    return tuple(int(i, 16)/255.0 for i in parts)

assert hex2rgb("#000000") == (0, 0, 0)
assert hex2rgb("#FFFFFF") == (1, 1, 1)


def rgb2hex(r, g, b):
    rgb = (int(round(num*255)) for num in (r, g, b))
    return "#" + "".join(hex(i)[2:].rjust(2, "0") for i in rgb).upper()

assert rgb2hex(0, 0, 0) == "#000000"
assert rgb2hex(1, 1, 1) == "#FFFFFF"


def hex2rgb_int(hex_val):
    parts = split_hex(hex_val)
    assert len(parts) == 3, hex_val
    return tuple(int(i, 16) for i in parts)

assert hex2rgb_int("#000000") == (0, 0, 0)
assert hex2rgb_int("#FFFFFF") == (255, 255, 255)


def hsv2rgb(h, s, v):
    return colorsys.hsv_to_rgb(h, s, v)

assert hsv2rgb(0, 0, 0) == (0, 0, 0)
assert hsv2rgb(0, 1, 1) == (1, 0, 0)
assert hsv2rgb(0.5, 0.5, 0.5) == (0.25, 0.5, 0.5)


def rgb2hsv(r, g, b):
    return colorsys.rgb_to_hsv(r, g, b)

assert rgb2hsv(0, 0, 0) == (0, 0, 0)
assert rgb2hsv(1, 0, 0) == (0, 1, 1)
assert rgb2hsv(0.25, 0.5, 0.5) == (0.5, 0.5, 0.5)


def hex2hsv(hex_val):
    r, g, b = hex2rgb(hex_val)
    return rgb2hsv(r, g, b)


def hsv2hex(h, s, v):
    r, g, b = hsv2rgb(h, s, v)
    return rgb2hex(r, g, b)


#-------------------------------------------------------------------------------
# Color modifiers
#-------------------------------------------------------------------------------
def grey(amount):
    amount /= 100.0
    return rgb2hex(amount, amount, amount)

assert grey(0) == "#000000", grey(0)
assert grey(6.5) == "#111111", grey(6.5)
assert grey(100) == "#FFFFFF", grey(100)


def shade(color, amount=50):
    h, s, v = hex2hsv(color)
    # print(h, s, v)
    v += amount/100.0  # Convert from percent
    if v > 1.0:
        v = 1.0
    if v < 0.0:
        v = 0.0
    # print(h, s, v)
    return hsv2hex(h, s, v)

assert shade("#000000", 50), "#808080"
assert shade("#808080", -50), "#000000"


def saturate(color, amount=50):
    h, s, v = hex2hsv(color)
    s += amount/100.0  # Convert from percent
    if s > 1.0:
        s = 1.0
    if s < 0.0:
        s = 0.0
    # print(h, s, v)
    # print(hsv2rgb(h, s, v))
    return hsv2hex(h, s, v)

assert saturate("#111100", -100) == "#111111"


def blend(color1, color2, amount=50):
    amount /= 100.0  # Convert from percent
    r1, g1, b1 = hex2rgb(color1)
    r2, g2, b2 = hex2rgb(color2)
    return rgb2hex(
        (r2 - r1)*amount + r1,
        (g2 - g1)*amount + g1,
        (b2 - b1)*amount + b1,
    )

assert blend("#000000", "#FFFFFF", 0) == "#000000"
assert blend("#000000", "#FFFFFF", 25) == "#404040"
assert blend("#000000", "#FFFFFF", 50) == "#808080"
assert blend("#000000", "#FFFFFF", 100) == "#FFFFFF"


def transparency(color, amount):
    if len(color) != 7:
        raise ValueError("`color` should be 7 chars long")
    transparency = int(round((255.0/100.0) * amount))
    return color + hex(transparency)[2:].rjust(2, "0")

assert transparency("#222222", 1) == "#22222203"
assert transparency("#222222", 6.55) == "#22222211"
