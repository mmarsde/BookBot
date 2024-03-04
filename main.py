import os, string

def get_book_path(book: str) -> str:
    book_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "books")
    return os.path.join(book_directory, book)  

def get_book_text(book_path : str) -> str:
    with open(book_path, 'r') as file:
        content = file.read()
        return content

def get_word_count(text: str) -> int:
    return len(text.split())
    
def get_letter_dict(text: str) -> dict:
    letters_dict = {}
    letters = list(string.ascii_lowercase)
    for letter in letters:
        letters_dict[letter] = text.lower().count(letter)       
    return letters_dict

def sort_on(dict):
    return dict["count"]

def build_sorted_report(letter_dict: dict) -> list:
    report = []
    for key, value in letter_dict.items():
        report_value = {
            "letter" : key,
            "count" : value
        }
        report.append(report_value)
    report.sort(reverse=True, key=sort_on)
    return report

def display_report(word_count: int, report: list, book: str ):
    print(f"--- Begin report of books/{book} ---\n")
    print(f"{word_count} words found in the document\n")

    for letter_report in report:
        letter = letter_report["letter"]
        count = letter_report["count"]
        print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")

def main():
    BOOK = "frankenstein.txt"
    book_path = get_book_path(BOOK)
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    letter_dict = get_letter_dict(text)
    report = build_sorted_report(letter_dict)
    display_report(word_count, report, BOOK)

if __name__ == "__main__":
    main()