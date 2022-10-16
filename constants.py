UNKNOWN_OPTION_ERROR = "Unknown Option. Please select a valid option from the given list."
UNKNOWN_FILENAME_ERROR = "Could not find the specified file, please try again or enter q to quit"

DEFAULT_PDF_FONT = "Guseul.ttf"
DEFAULT_PDF_FONT_SIZE = 20
DEFAULT_PDF_SECTION_HEIGHT = 20
DEFAULT_PDF_WORDS_PER_PAGE = 26

DEFAULT_LANGUAGE = "english"
DEFAULT_YES_OPTIONS = ['y', 'yes', '네', 'ㅛ', 'ㅛㄷㄴ']
DEFAULT_QUIT_OPTIONS = ['', 'q', 'quit']
DEFAULT_FILE_ENCODING = "utf-8"
DEFAULT_FONT_DIRECTORY = "fonts/"
DEFAULT_FLASHCARD_DIRECTORY = "flashcards/"
DEFAULT_WORKSHEET_DIRECTORY = "worksheets/"
DEFAULT_KOREAN_MODE_OPTIONS = ['k', 'kor', 'korean']

START_MODE_QUIT_OPTIONS = DEFAULT_QUIT_OPTIONS + ['3']
START_MODE_PROMPT = "Enter mode:\n" \
                    "1: Add flashcards\n" \
                    "2: Study flashcards\n" \
                    "3: Quit the program\n" \
                    "\n" \
                    "Mode: "

STUDY_FLASHCARD_SET_QUIT_OPTIONS = DEFAULT_QUIT_OPTIONS + ['5']
STUDY_FLASHCARD_SET_PROMPT = "\nEnter mode:\n" \
                             "1: Display entire list\n" \
                             "2: Mock test\n" \
                             "3: Study random\n" \
                             "4: Study limited\n" \
                             "5: Quit study mode\n" \
                             "\n" \
                             "Mode: "

FLASHCARD_TEST_LANGUAGE_MODE_PROMPT = "\nWould you like to answer in (e)nglish or (k)orean: "
FLASHCARD_TEST_DIRECTIONS = "A word/definition will be displayed, provide the equivalent in the opposite language. To stop, enter q or nothing.\n"

FLASHCARD_FILENAME_PROMPT = "\nEnter the name of the flashcard set or file: "

GET_KOREAN_PROMPT = u"\n한글: "
GET_ENGLISH_PROMPT = u"\n영어: "
