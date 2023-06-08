#!/usr/bin/env python3

from colored import fg, attr, stylize


class Color(object):

    ''' Helpers for printing to terminal '''

    '''
    Color Keys:
    red = 1
    orange = 214
    yellow = 220
    green = 2
    blue = 4
    cyan = 81
    purple = 141
    gray = 245
    white = 15

    Attributes keys:
    0 = reset
    1 = bold
    2 = dim
    21 = reset bold
    22 = rest dim

    Extra colors:
    33 = dog blue
    226 = bright yellow
    212 = nice purple
    171 = purple
    141 = cool purple
    '''

    @staticmethod
    def set(text, color, attrib=None):
        r = 1
        orng = 214
        y = 220
        g = 2
        b = 4
        cy = 81
        purp = 141
        gr = 245
        wh = 15

        if color == 'r':
            color_code = r

        if color == 'orng':
            color_code = orng

        if color == 'y':
            color_code = y

        if color == 'g':
            color_code = g

        if color == 'b':
            color_code = b

        if color == 'cy':
            color_code = cy

        if color == 'purp':
            color_code = purp

        if color == 'gr':
            color_code = gr

        if color == 'wh':
            color_code = wh


        if attrib is None:
            output = stylize(text, fg(color_code))
        else:
            style = fg(color_code) + attr(attrib)
            output = stylize(text, style)

        return output