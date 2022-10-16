import sys
import constants
from flashcard import flashcard
from worksheet import create_worksheet
from parseInput import retrieve_flashcard_contents, get_korean, get_english, get_input


def main():
    mode = get_input(constants.START_MODE_PROMPT)

    while mode.lower() not in constants.START_MODE_QUIT_OPTIONS:
        if mode == '1':
            add_to_flashcard_set()
        elif mode == '2':
            study_flashcard_set()
        elif mode == '3':
            convert_flashcard_set_to_worksheet()
        else:
            print(constants.UNKNOWN_OPTION_ERROR)

        mode = get_input(constants.START_MODE_PROMPT)


def add_to_flashcard_set():
    filename = get_input(constants.FLASHCARD_FILENAME_PROMPT)

    with open(f"{constants.DEFAULT_FLASHCARD_DIRECTORY}{filename}.txt", "a+", encoding=constants.DEFAULT_FILE_ENCODING) as f:
        korean_word = get_korean(constants.GET_KOREAN_PROMPT)
        english_translation = get_english(constants.GET_ENGLISH_PROMPT)

        while korean_word and english_translation:
            f.write(f"{korean_word};{english_translation}\n")

            korean_word = get_korean(constants.GET_KOREAN_PROMPT)
            english_translation = get_english(constants.GET_ENGLISH_PROMPT)

    print()


def study_flashcard_set():
    korean_vocabulary_words = retrieve_flashcard_contents()
    flashcard_set = flashcard(korean_vocabulary_words)

    mode = get_input(constants.STUDY_FLASHCARD_SET_PROMPT)

    while mode.lower() not in constants.STUDY_FLASHCARD_SET_QUIT_OPTIONS:
        if mode == '1':
            flashcard_set.display()

        elif mode == '2':
            flashcard_set.mock_test()

        elif mode == '3':
            flashcard_set.random_test()

        elif mode == '4':
            flashcard_set.mock_test(limited=True)

        mode = get_input(constants.STUDY_FLASHCARD_SET_PROMPT)

    print()


def convert_flashcard_set_to_worksheet():
    korean_vocabulary_words = retrieve_flashcard_contents()

    create_worksheet([pair[0] for pair in korean_vocabulary_words])


if __name__ == '__main__':
    main()
    sys.exit(0)
