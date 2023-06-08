#!/usr/bin/env python3

from colored import fg, attr, stylize
import re


class Color(object):

    ''' Helpers for printing to terminal '''

    colors = {
        'W' : 15,  # white (normal)
        'R' : 1,
        'G' : 2,
        'O' : 214,
        'B' : 4,
        'P' : 141,
        'C' : 81,
        'GR': 245,
        'Y' : 226
    }

    '''
    Prints text using colored format on same line.
    Example:
        Color.p('{R}This text is red. {W}This text is white')
    '''
    @staticmethod
    def s(text):
        base = text
        output = ''
        start = 0

        match_pattern = r"\{([A-Z])\}"
        matches = re.findall(match_pattern, text)

        for match in matches:
            color_key = match
            color_code = Color.colors[color_key]
            r_code = "{" + color_key + "}"

            base = base.replace(r_code, '')
            regex = re.search(match_pattern, base)

            if regex:
                end = regex.start()
                substring = base[start:end]
                start = end
            else:
                substring = base[start:]


            c_string = Color.color(substring, color_code) + ' '
            output = ''.join([output, c_string])

        return output

    @staticmethod
    def color(text, code):
        colored_text = stylize(text, fg(code))
        return colored_text

    @staticmethod
    def print(text):
        output = Color.s(text)
        print(output)


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

    @staticmethod
    def p(text, color, attrib=None):
        '''
        Prints text using colored format on same line.
        Usage = Color.p('Text.', 'Color Code', Style code)
        '''
        output = Color.set(text, color, attrib)
        print(output)