"""
Text Formatting Module for Python Games
Provides various color and text styling functions using ANSI escape codes.
"""

# Define what gets imported with "from text_formatting import *"
__all__ = [
    # Basic colors
    'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'black',
    # Bright colors
    'bright_red', 'bright_green', 'bright_yellow', 'bright_blue', 
    'bright_magenta', 'bright_cyan', 'bright_white',
    # Background colors
    'bg_red', 'bg_green', 'bg_yellow', 'bg_blue', 'bg_magenta', 
    'bg_cyan', 'bg_white', 'bg_black',
    # Text styles
    'bold', 'italic', 'underline', 'strikethrough', 'dim', 'blink', 'reverse', 'hidden',
    # Combination functions
    'bold_red', 'bold_green', 'bold_yellow', 'bold_blue', 'bold_magenta', 'bold_cyan', 'bold_white',
    'underline_red', 'underline_green', 'underline_yellow', 'underline_blue',
    # Utility functions
    'rainbow', 'reset', 'clear_line', 'move_cursor_up', 'move_cursor_down', 
    'move_cursor_right', 'move_cursor_left', 'rgb_color', 'rgb_bg_color',
    # Game-specific functions
    'success', 'error', 'warning', 'info', 'title', 'subtitle', 'highlight', 
    'game_over', 'winner'
]

# Color Functions
def red(text):
    """Return text in red color"""
    return f"\033[31m{text}\033[0m"

def green(text):
    """Return text in green color"""
    return f"\033[32m{text}\033[0m"

def yellow(text):
    """Return text in yellow color"""
    return f"\033[33m{text}\033[0m"

def blue(text):
    """Return text in blue color"""
    return f"\033[34m{text}\033[0m"

def magenta(text):
    """Return text in magenta color"""
    return f"\033[35m{text}\033[0m"

def cyan(text):
    """Return text in cyan color"""
    return f"\033[36m{text}\033[0m"

def white(text):
    """Return text in white color"""
    return f"\033[37m{text}\033[0m"

def black(text):
    """Return text in black color"""
    return f"\033[30m{text}\033[0m"

# Bright Colors
def bright_red(text):
    """Return text in bright red color"""
    return f"\033[91m{text}\033[0m"

def bright_green(text):
    """Return text in bright green color"""
    return f"\033[92m{text}\033[0m"

def bright_yellow(text):
    """Return text in bright yellow color"""
    return f"\033[93m{text}\033[0m"

def bright_blue(text):
    """Return text in bright blue color"""
    return f"\033[94m{text}\033[0m"

def bright_magenta(text):
    """Return text in bright magenta color"""
    return f"\033[95m{text}\033[0m"

def bright_cyan(text):
    """Return text in bright cyan color"""
    return f"\033[96m{text}\033[0m"

def bright_white(text):
    """Return text in bright white color"""
    return f"\033[97m{text}\033[0m"

# Background Colors
def bg_red(text):
    """Return text with red background"""
    return f"\033[41m{text}\033[0m"

def bg_green(text):
    """Return text with green background"""
    return f"\033[42m{text}\033[0m"

def bg_yellow(text):
    """Return text with yellow background"""
    return f"\033[43m{text}\033[0m"

def bg_blue(text):
    """Return text with blue background"""
    return f"\033[44m{text}\033[0m"

def bg_magenta(text):
    """Return text with magenta background"""
    return f"\033[45m{text}\033[0m"

def bg_cyan(text):
    """Return text with cyan background"""
    return f"\033[46m{text}\033[0m"

def bg_white(text):
    """Return text with white background"""
    return f"\033[47m{text}\033[0m"

def bg_black(text):
    """Return text with black background"""
    return f"\033[40m{text}\033[0m"

# Text Styles
def bold(text):
    """Return text in bold"""
    return f"\033[1m{text}\033[0m"

def italic(text):
    """Return text in italic"""
    return f"\033[3m{text}\033[0m"

def underline(text):
    """Return text with underline"""
    return f"\033[4m{text}\033[0m"

def strikethrough(text):
    """Return text with strikethrough"""
    return f"\033[9m{text}\033[0m"

def dim(text):
    """Return text with dim/faint appearance"""
    return f"\033[2m{text}\033[0m"

def blink(text):
    """Return text with blinking effect"""
    return f"\033[5m{text}\033[0m"

def reverse(text):
    """Return text with reversed colors (swap foreground and background)"""
    return f"\033[7m{text}\033[0m"

def hidden(text):
    """Return hidden text (invisible but still there)"""
    return f"\033[8m{text}\033[0m"

# Combination Functions
def bold_red(text):
    """Return text in bold red"""
    return f"\033[1;31m{text}\033[0m"

def bold_green(text):
    """Return text in bold green"""
    return f"\033[1;32m{text}\033[0m"

def bold_yellow(text):
    """Return text in bold yellow"""
    return f"\033[1;33m{text}\033[0m"

def bold_blue(text):
    """Return text in bold blue"""
    return f"\033[1;34m{text}\033[0m"

def bold_magenta(text):
    """Return text in bold magenta"""
    return f"\033[1;35m{text}\033[0m"

def bold_cyan(text):
    """Return text in bold cyan"""
    return f"\033[1;36m{text}\033[0m"

def bold_white(text):
    """Return text in bold white"""
    return f"\033[1;37m{text}\033[0m"

def underline_red(text):
    """Return text in underlined red"""
    return f"\033[4;31m{text}\033[0m"

def underline_green(text):
    """Return text in underlined green"""
    return f"\033[4;32m{text}\033[0m"

def underline_yellow(text):
    """Return text in underlined yellow"""
    return f"\033[4;33m{text}\033[0m"

def underline_blue(text):
    """Return text in underlined blue"""
    return f"\033[4;34m{text}\033[0m"

# Utility Functions
def rainbow(text):
    """Return text with rainbow colors (each character different color)"""
    colors = [red, green, yellow, blue, magenta, cyan]
    result = ""
    for i, char in enumerate(text):
        if char == ' ':
            result += char
        else:
            result += colors[i % len(colors)](char)
    return result

def reset():
    """Return reset sequence to clear all formatting"""
    return "\033[0m"

def clear_line():
    """Return sequence to clear current line"""
    print(f"\033[2K", end='', flush=True)
   # return "\033[2K"

def move_cursor_up(lines=1):
    """Move cursor up by specified lines"""
    print(f"\033[{lines}A", end='', flush=True)

def move_cursor_down(lines=1):
    """Move cursor down by specified lines"""
    print(f"\033[{lines}B", end='', flush=True)

def move_cursor_right(columns=1):
    """Move cursor right by specified columns"""
    print(f"\033[{columns}C", end='', flush=True)

def move_cursor_left(columns=1):
    """Move cursor left by specified columns"""
    print(f"\033[{columns}D", end='', flush=True)

# Custom color function using RGB values (for terminals that support it)
def rgb_color(r, g, b, text):
    """Return text with custom RGB color (for supported terminals)"""
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

def rgb_bg_color(r, g, b, text):
    """Return text with custom RGB background color (for supported terminals)"""
    return f"\033[48;2;{r};{g};{b}m{text}\033[0m"

# Predefined color combinations for game elements
def success(text):
    """Return text formatted for success messages"""
    return bold_green(text)

def error(text):
    """Return text formatted for error messages"""
    return bold_red(text)

def warning(text):
    """Return text formatted for warning messages"""
    return bold_yellow(text)

def info(text):
    """Return text formatted for info messages"""
    return bold_blue(text)

def title(text):
    """Return text formatted for titles"""
    return bold(underline(bright_cyan(text)))

def subtitle(text):
    """Return text formatted for subtitles"""
    return bold(bright_magenta(text))

def highlight(text):
    """Return text with highlighted appearance"""
    return bg_yellow(black(text))

def game_over(text):
    """Return text formatted for game over messages"""
    return bold_red(blink(text))

def winner(text):
    """Return text formatted for winner announcements"""
    return bold_green(underline(text))

# Test function to demonstrate all colors and styles
def test_all_formats():
    """Test function to display all available formatting options"""
    print("=== Colors ===")
    print(red("Red text"))
    print(green("Green text"))
    print(yellow("Yellow text"))
    print(blue("Blue text"))
    print(magenta("Magenta text"))
    print(cyan("Cyan text"))
    print(white("White text"))
    print(black("Black text"))
    
    print("\n=== Bright Colors ===")
    print(bright_red("Bright Red text"))
    print(bright_green("Bright Green text"))
    print(bright_yellow("Bright Yellow text"))
    print(bright_blue("Bright Blue text"))
    print(bright_magenta("Bright Magenta text"))
    print(bright_cyan("Bright Cyan text"))
    print(bright_white("Bright White text"))
    
    print("\n=== Text Styles ===")
    print(bold("Bold text"))
    print(italic("Italic text"))
    print(underline("Underlined text"))
    print(strikethrough("Strikethrough text"))
    print(dim("Dim text"))
    print(reverse("Reversed text"))
    
    print("\n=== Combinations ===")
    print(bold_red("Bold Red text"))
    print(underline_blue("Underlined Blue text"))
    print(rainbow("Rainbow text!"))
    
    print("\n=== Game Formatting ===")
    print(success("Success message"))
    print(error("Error message"))
    print(warning("Warning message"))
    print(info("Info message"))
    print(title("TITLE TEXT"))
    print(subtitle("Subtitle Text"))
    print(highlight("Highlighted text"))
    print(winner("WINNER!"), end="")
    clear_line()
    print("w")
    move_cursor_down(3)

if __name__ == "__main__":
    test_all_formats()