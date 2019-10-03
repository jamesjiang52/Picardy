import os
import sys
import lut
import utils

os.system("color")

EBONY = "\033[100m"
IVORY = "\033[47m"
GREEN = "\033[102m"
PURPLE = "\033[105m"


def clear():
    os.system("cls")


def print_lines(lines):
    out = "\n".join(lines)
    print(out + "\x1b[0m")


def draw_keyboard(notes):
    """
    notes is a list of indices:
    [C1, C#1, D1, D#1, E1, F1, F#1, G1, G#1, A1, A#1, B1, C2, C#2, D2, D#2, E2, F2, F#2, G2, G#2, A2, A#2, B2]
    """
    colors = [IVORY, EBONY, IVORY, EBONY, IVORY, IVORY, EBONY, IVORY, EBONY, IVORY, EBONY, IVORY, IVORY, EBONY, IVORY, EBONY, IVORY, IVORY, EBONY, IVORY, EBONY, IVORY, EBONY, IVORY]
    
    for note in notes:
        colors[note] = GREEN
        
    print_lines([
        "\033[90m{0}   {1}   {2}  {3}   {4}   \033[47m|{5}   {6}   {7}  {8}   {9}  {10}   {11}   \033[47m|{12}   {13}   {14}  {15}   {16}   \033[47m|{17}   {18}   {19}  {20}   {21}  {22}   {23}   ".format(*colors),
        "\033[90m{0}   {1}   {2}  {3}   {4}   \033[47m|{5}   {6}   {7}  {8}   {9}  {10}   {11}   \033[47m|{12}   {13}   {14}  {15}   {16}   \033[47m|{17}   {18}   {19}  {20}   {21}  {22}   {23}   ".format(*colors),
        "\033[90m{0}   {1}   {2}  {3}   {4}   \033[47m|{5}   {6}   {7}  {8}   {9}  {10}   {11}   \033[47m|{12}   {13}   {14}  {15}   {16}   \033[47m|{17}   {18}   {19}  {20}   {21}  {22}   {23}   ".format(*colors),
        "\033[90m{0}   {1}   {2}  {3}   {4}   \033[47m|{5}   {6}   {7}  {8}   {9}  {10}   {11}   \033[47m|{12}   {13}   {14}  {15}   {16}   \033[47m|{17}   {18}   {19}  {20}   {21}  {22}   {23}   ".format(*colors),
        "\033[90m{0}   {1}   {2}  {3}   {4}   \033[47m|{5}   {6}   {7}  {8}   {9}  {10}   {11}   \033[47m|{12}   {13}   {14}  {15}   {16}   \033[47m|{17}   {18}   {19}  {20}   {21}  {22}   {23}   ".format(*colors),
        "\033[90m{0}    \033[47m|{2}    \033[47m|{4}    \033[47m|{5}    \033[47m|{7}    \033[47m|{9}    \033[47m|{11}    \033[47m|{12}    \033[47m|{14}    \033[47m|{16}    \033[47m|{17}    \033[47m|{19}    \033[47m|{21}    \033[47m|{23}    ".format(*colors),
        "\033[90m{0}    \033[47m|{2}    \033[47m|{4}    \033[47m|{5}    \033[47m|{7}    \033[47m|{9}    \033[47m|{11}    \033[47m|{12}    \033[47m|{14}    \033[47m|{16}    \033[47m|{17}    \033[47m|{19}    \033[47m|{21}    \033[47m|{23}    ".format(*colors),
        "\033[90m{0}    \033[47m|{2}    \033[47m|{4}    \033[47m|{5}    \033[47m|{7}    \033[47m|{9}    \033[47m|{11}    \033[47m|{12}    \033[47m|{14}    \033[47m|{16}    \033[47m|{17}    \033[47m|{19}    \033[47m|{21}    \033[47m|{23}    ".format(*colors)
    ])


def draw_blank_keyboard():
    draw_keyboard([])


def main(argv):
    draw_keyboard(utils.get_indices(lut.lut[utils.get_canonical_name(argv[1])]))


if __name__ == "__main__":
    main(sys.argv)
