import copy
import random
import constants
from parseInput import get_input


def filterShortLists(lst):
    if len(lst) < 2:
        return False
    return True


class flashcard:
    def __init__(self, words: list):
        self.pairs = list(filter(filterShortLists, words))

    @staticmethod
    def my_enumerate(objs, start, stop):
        try:
            if start < 0:
                start = 0
            if stop > len(objs):
                stop = len(objs)
            for i in range(start, stop):
                yield i, objs[i]

        except IndexError:
            return

    @staticmethod
    def display_test_results(correct, missed, total=0, start=0, stop=0):
        if stop - start != 0:
            print(f"\nCorrect: {correct}\n"
                  f"Incorrect: {len(missed)}\n"
                  f"Accuracy: {(correct / (stop - start) * 100):.2f}%\n")
        elif total != 0:
            print(f"\nCorrect: {correct}\n"
                  f"Incorrect: {len(missed)}\n"
                  f"Accuracy: {(correct / total * 100):.2f}%")

        results = get_input("See full results (y/n): ").lower().strip()

        if results in constants.DEFAULT_YES_OPTIONS:
            for i, miss in enumerate(missed):
                print(f"{i}: {miss[0]} > (O) {miss[1]} (X) {miss[2]}")

    def display(self):
        for pair in self.pairs:
            print(f"{pair[0]} - {pair[1]}")

    def random(self, mode=constants.DEFAULT_LANGUAGE):
        pair = self.pairs[random.randint(0, len(self.pairs) - 1)]

        if mode in constants.DEFAULT_KOREAN_MODE_OPTIONS:
            return pair[1], pair[0]

        return pair

    def random_test(self):
        total = 0
        correct = 0
        missed = []

        language_mode = get_input(constants.FLASHCARD_TEST_LANGUAGE_MODE_PROMPT)
        print(constants.FLASHCARD_TEST_DIRECTIONS)

        total += 1
        random_word = self.random(language_mode)
        answer = get_input(f"{random_word[0]} > ", language_mode)

        if not answer:
            return
        elif answer == random_word[1]:
            correct += 1
            print("O\n")
        else:
            missed.append([random_word[0], random_word[1], answer])
            print(f"X {random_word[1]}\n")

        while answer:
            random_word = self.random(language_mode)
            answer = get_input(f"{random_word[0]} > ", language_mode)

            if not answer:
                break
            elif answer == random_word[1]:
                correct += 1
                print("O\n")
            else:
                missed.append([random_word[0], random_word[1], answer])
                print(f"X {random_word[1]}\n")

            total += 1

        flashcard.display_test_results(correct, missed, total=total)

    def mock_test(self, limited=False, randomize=True):
        words = copy.deepcopy(self.pairs)

        correct = 0
        missed = []

        start = 0
        stop = len(words)

        if limited:
            try:
                start = int(input("\nStart: "))
                stop = int(input("Stop: "))

                words = words[start: stop]

            except (ValueError, IndexError):
                self.mock_test(limited=limited, randomize=randomize)
                return

        if randomize:
            for _ in range(len(words) * 3):
                words.append(words.pop(random.randint(0, len(words) - 1)))

        language_mode = get_input(constants.FLASHCARD_TEST_LANGUAGE_MODE_PROMPT)
        print(constants.FLASHCARD_TEST_DIRECTIONS)

        for i, pair in enumerate(words):
            if language_mode in constants.DEFAULT_KOREAN_MODE_OPTIONS:
                pair[0], pair[1] = pair[1], pair[0]

            answer = get_input(f"{i + 1}: {pair[0]} -> ", language_mode)

            if answer in ['q', 'quit']:
                break
            elif answer == pair[1]:
                correct += 1
            else:
                missed.append([pair[0], pair[1], answer])

        flashcard.display_test_results(correct, missed, start=start, stop=stop)
