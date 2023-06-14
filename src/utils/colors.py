#!/usr/bin/env python3

import re
from colored import fg, attr, stylize


class Color(object):

    """Helpers for printing to terminal"""

    colors = {
        "W": 15,  # white (normal)
        "R": 1,
        "G": 2,
        "O": 214,
        "B": 4,
        "P": 141,
        "C": 81,
        "X": 245, # Gray
        "Y": 226,
        "L": 121, # Light Green
    }

    @staticmethod
    def print(text):
        """
        Prints text using colored format on same line.
        Example:
            Color.print('{R}This text is red. {W}This text is white')
        """
        output = Color.s(text)
        print(output)

    @staticmethod
    def s(text):
        base = text
        output = ""
        start = 0

        match_pattern = r"\{([A-Z])\}"
        matches = re.findall(match_pattern, text)

        for match in matches:
            color_key = match
            color_code = Color.colors[color_key]
            r_code = "{" + color_key + "}"

            base = base.replace(r_code, "")
            regex = re.search(match_pattern, base)

            if regex:
                end = regex.start()
                substring = base[start:end]
                start = end
            else:
                substring = base[start:]

            c_string = Color.color(substring, color_code) + " "
            output = "".join([output, c_string])

        return output

    @staticmethod
    def color(text, code):
        colored_text = stylize(text, fg(code))
        return colored_text

    @staticmethod
    def p_error(error):
        '''Prints an exception. Includes stack trace if necessary.'''
        error_style = fg(1) + attr(1)
        msg_style = fg(15) + attr(0)
        error_message = f"{stylize('Error:', error_style)} {stylize(str(error), msg_style)}"
        print(error_message)