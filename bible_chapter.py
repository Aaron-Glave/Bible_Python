from random import randint
biblebooks =[
    ("Genesis", 50),
    ("Exodus", 40),
    ("Leviticus", 27),
    ("Numbers", 36),
    ("Deuteronomy", 34),
    ("Joshua", 24),
    ("Judges", 21),
    ("Ruth", 4),
    ("1 Samuel", 31),
    ("2 Samuel", 24),
    ("1 Kings", 22),
    ("2 Kings", 25),
    ("1 Chronicles", 29),
    ("2 Chronicles", 36),
    ("Ezra", 10),
    ("Nehemiah", 13),
    ("Esther", 10),
    ("Job", 42),
    ("Psalms", 150),
    ("Proverbs", 31),
    ("Ecclesiastes", 12),
    ("Song of Solomon", 8),
    ("Isaiah", 66),
    ("Jeremiah", 52),
    ("Lamentations", 5),
    ("Ezekiel", 48),
    ("Daniel", 12),
    ("Hosea", 14),
    ("Joel", 3),
    ("Amos", 9),
    ("Obadiah", 1),
    ("Jonah", 4),
    ("Micah", 7),
    ("Nahum", 3),
    ("Habakkuk", 3),
    ("Zephaniah", 3),
    ("Haggai", 2),
    ("Zechariah", 14),
    ("Malachi", 4),
    ("Matthew", 28),
    ("Mark", 16),
    ("Luke", 24),
    ("John", 21),
    ("Acts", 28),
    ("Romans", 16),
    ("1 Corinthians", 16),
    ("2 Corinthians", 13),
    ("Galatians", 6),
    ("Ephesians", 6),
    ("Philippians", 4),
    ("Colossians", 4),
    ("1 Thessalonians", 5),
    ("2 Thessalonians", 3),
    ("1 Timothy", 6),
    ("2 Timothy", 4),
    ("Titus", 3),
    ("Philemon", 1),
    ("Hebrews", 13),
    ("James", 5),
    ("1 Peter", 5),
    ("2 Peter", 3),
    ("1 John", 5),
    ("2 John", 1),
    ("3 John", 1),
    ("Jude", 1),
    ("Revelation", 22),
]

def select_reading_style() -> int:
    """If this function returns 1, pick a random book first, then pick a random chapter in that book.
    If it returns 2, select a random Psalm.
    If it returns 3,select a random chapter with each one having an equal chance."""
    print("Select what chapter recommendation looks best right now:",
          "1: Pick a random book, then a random chapter in that book.",
          "2. Pick a random Psalm to contemplate.",
          "3: Treat the Bible as one huge book.", sep="\n")
    how_to_type = "Press 1,2, or 3. then hit enter or return."
    choice = 0
    options = tuple(range(1, 3+1))
    while choice not in options:
        try:
            choice = int(input())
        except ValueError:
            choice = 0
        if choice not in options:
            print(how_to_type)
    return choice

def print_chapter_recommendation(
        book_title: str,
        chapter_to_read: int,
        capitalize_read: bool = True,
) -> None:
    r = "R" if capitalize_read else "r"
    print(r+"ead chapter", chapter_to_read, "of book", book_title, end=".\n")

def select_chapter(book_to_read: tuple[str, int]) -> None:
    chapter_to_read = randint(1, book_to_read[1])
    print_chapter_recommendation(book_to_read[0], chapter_to_read)

if __name__ == "__main__":
    assert len(biblebooks) == 66
    print("There are", len(biblebooks), "books in the Bible.")
    my_choice = select_reading_style()
    if my_choice == 1:
        select_chapter(biblebooks[randint(0, 65)])
    elif my_choice == 2:
        psalm = biblebooks[18]
        print("Remember, all Psalms are songs!")
        select_chapter(psalm)
    elif my_choice ==3:
        bible_chapters = []
        for book in biblebooks:
            chapter_to_add = 1
            while chapter_to_add <= book[1]:
                bible_chapters.append((book[0], chapter_to_add))
                chapter_to_add += 1
        numchapters = len(bible_chapters)
        print("Out of the", numchapters, "chapters of the Bible, I want you to", end=" ")
        chapter_index = randint(0, numchapters - 1)
        print_chapter_recommendation(
            book_title=bible_chapters[chapter_index][0],
            chapter_to_read=bible_chapters[chapter_index][1],
            capitalize_read=False,
        )
    input("Press Enter/newline when you're done.\n")
