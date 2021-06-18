
def main():
    hello()
    hello()
    c = get_word_count_by_line('bird', 'DATA/parrot.txt', True)
    print(f"bird occurs on {c} lines")

def hello():
    print("Hello, JPMC world")

def get_word_count_by_line(word: str, file_name: str, ignore_case: bool=False) -> int:
    """
    Retrieve number of lines containing a word in a specified file.

    :param word: Word to find (string)
    :param file_name: File name to search
    :param ignore_case: If True, ignore case on search
    :return: Number of lines containing word
    """
    count = 0
    if ignore_case:
        word = word.lower()
    with open(file_name) as file_in:
        for line in file_in:
            if ignore_case:
                line = line.lower()
            if word in line:
                count += 1
    return count

if __name__ == '__main__':
    main()










