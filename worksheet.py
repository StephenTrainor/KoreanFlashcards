import constants
from fpdf import FPDF
from parseInput import retrieve_flashcard_contents, get_input


def create_worksheet(korean_words):
    output_filename = get_input("Enter the desired filename of your worksheet: ")

    pdf = FPDF()
    pdf.add_font('f', '', f'{constants.DEFAULT_FONT_DIRECTORY}{constants.DEFAULT_PDF_FONT}', uni=True)
    pdf.set_font('f', '', constants.DEFAULT_PDF_FONT_SIZE)

    for i in range(0, len(korean_words), constants.DEFAULT_PDF_WORDS_PER_PAGE):
        pdf.add_page()

        max_word_index = lambda x: x + constants.DEFAULT_PDF_WORDS_PER_PAGE \
            if (x + constants.DEFAULT_PDF_WORDS_PER_PAGE < len(korean_words)) else (len(korean_words))
        longest_word = len(max(korean_words[i: max_word_index(i)], key=len))
        line_y_pos = constants.DEFAULT_PDF_SECTION_HEIGHT

        for j in range(i, max_word_index(i)):
            pdf.write(10, korean_words[j].encode(constants.DEFAULT_FILE_ENCODING).decode(constants.DEFAULT_FILE_ENCODING))
            pdf.line(0, line_y_pos, 220, line_y_pos)
            pdf.ln(10)
            line_y_pos += 10

        for j in range(10, 220, (longest_word + 1) * 7):
            pdf.line(j, 0, j, line_y_pos)

    pdf.output(f"{constants.DEFAULT_WORKSHEET_DIRECTORY}{output_filename}.pdf", 'F')


if __name__ == '__main__':
    korean_vocabulary_words = retrieve_flashcard_contents()

    create_worksheet([pair[0] for pair in korean_vocabulary_words])
