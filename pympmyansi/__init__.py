import sys


def pymp(input: str, code: str) -> str:
    """Returns a string enclosed within the necessary ANSI escape codes.

    Args:
        input (str): The input string.
        color (str): The desired code.

    Returns:
        str
    """
    if not sys.stdout.isatty():
        return input
    else:
        return codes[code] + input + codes['end']


# TODO use an enum
codes = {
    'black':        "\033[0;30m",
    'red':          "\033[0;31m",
    'green':        "\033[0;32m",
    'brown':        "\033[0;33m",
    'blue':         "\033[0;34m",
    'purple':       "\033[0;35m",
    'cyan':         "\033[0;36m",
    'light_gray':   "\033[0;37m",
    'dark_gray':    "\033[1;30m",
    'light_red':    "\033[1;31m",
    'light_green':  "\033[1;32m",
    'yellow':       "\033[1;33m",
    'light_blue':   "\033[1;34m",
    'light_purple': "\033[1;35m",
    'light_cyan':   "\033[1;36m",
    'light_white':  "\033[1;37m",
    'bold':         "\033[1m",
    'faint':        "\033[2m",
    'italic':       "\033[3m",
    'underline':    "\033[4m",
    'blink':        "\033[5m",
    'negative':     "\033[7m",
    'crossed':      "\033[9m",
    'end':          "\033[0m",
}
