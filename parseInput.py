import os
import constants


def retrieve_flashcard_contents():
    filename = get_input(constants.FLASHCARD_FILENAME_PROMPT)

    while not os.path.isfile(f"{constants.DEFAULT_FLASHCARD_DIRECTORY}{filename}.txt"):
        if filename in constants.DEFAULT_QUIT_OPTIONS:
            return

        print(constants.UNKNOWN_FILENAME_ERROR)
        filename = get_input(constants.FLASHCARD_FILENAME_PROMPT)

    with open(f"{constants.DEFAULT_FLASHCARD_DIRECTORY}{filename}.txt", "r", encoding=constants.DEFAULT_FILE_ENCODING) as f:
        flashcard_set_contents = f.read().strip()

    flashcard_pairs = flashcard_set_contents.split('\n')
    vocabulary_words = [x.split(';') for x in flashcard_pairs]

    return vocabulary_words


def parse_raw_hangeul_string(raw_hangeul):
    blocks = list(raw_hangeul.strip())
    filtered_hangeul = list(filter(filter_unknowns, blocks))

    return "".join(filter_double_space(filtered_hangeul)).strip()


def filter_unknowns(block):
    try:
        if block in ['·', '<', ',', '>', '.', '?', '/', '}', ']', '{', '[', ':', ';', "'", '"', '\\', '|', '+', '=',
                     '_', '-', ')', '(', '*', '&', '^', '%', '$', '#', '@', '!', '~', '`', '1', '2', '3', '4', '5', '6',
                     '7', '8', '9', '0']:
            return False
        else:
            return True

    except (ValueError, UnicodeEncodeError):
        return True


def filter_unknowns_korean(block):
    try:
        if block in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                     'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z', '<', ',', '>', '.', '?', '/', '}', ']', '{',
                     '[', ':', ';', "'", '"', '\\', '|', '+', '=', '_', '-', ')', '(', '*', '&', '^', '%', '$', '#',
                     '@', '!', '~', '`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '·']:
            return False
        else:
            return True

    except (ValueError, UnicodeEncodeError):
        return True


def filter_double_space(string):
    out = []

    for i in range(len(string) - 1):
        if string[i] is " ":
            if string[i + 1] is not " ":
                out.append(string[i])
        else:
            out.append(string[i])

    return out


def get_input(prompt, mode=constants.DEFAULT_LANGUAGE):
    if mode in constants.DEFAULT_KOREAN_MODE_OPTIONS:
        return get_korean(prompt)
    return get_english(prompt)


def get_korean(prompt):
    raw_korean = input(prompt).strip()
    return "".join(filter(filter_unknowns_korean, raw_korean))


def get_english(prompt):
    return input(prompt).strip()


# if __name__ == '__main__':
#     s = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvxyz<,>.?/}]{[:;\'\"\\|+=_-)(*&^%$#@!~`1234567890·"
#     print(list(s))
#     temps = range(0, 100)
#     for i in range(0, len(temps), 26):
#         cap = lambda x: x + 26 if (x + 26 < len(temps)) else (len(temps) - 1)
#
#         for j in range(i, cap(i)):
#             print(j, end=' ')
#
#         print()
