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

def select_random_style() -> bool:
    """If this function returns True, pick a random book first, then pick a random chapter in that book.
    If not, select a random chapter with each one having an equal chance,"""
    print("Select whether you want to pick a random book, then a random chapter in that book,",
          "or treat the Bible as one huge book of words from God",
          "1: Pick a random book, then a random chapter in that book",
          "2: Treat the Bible as one huge book", sep="\n")
    how_to_type = "Press 1 or 2, then hit enter or return."
    choice = 0
    while choice not in (1, 2):
        try:
            choice = int(input())
        except ValueError:
            choice = 0
        if choice not in (1, 2):
            print(how_to_type)
    return choice == 1

if __name__ == "__main__":
    sofar = {}
    for book in biblebooks:
        assert book[0] not in sofar
        sofar[book[0]] = "pass"
    assert len(biblebooks) == 66
    print("There are", len(biblebooks), "books in the Bible.")
    random_book = select_random_style()
    if random_book:
        book_to_read = biblebooks[randint(0, 65)]
        chapter_to_read = randint(1, book_to_read[1])
        print("Read chapter", chapter_to_read, "of book", book_to_read[0], end=".\n")
    else:
        bible_chapters = []
        for book in biblebooks:
            chapter_to_add = 1
            while chapter_to_add <= book[1]:
                bible_chapters.append((book[0], chapter_to_add))
                chapter_to_add += 1
        #print(bible_chapters[-1])
        numchapters = len(bible_chapters)
        print("Out of the", numchapters, "chapters of the Bible, I want you to read", end=" ")
        chapter_index = randint(0, numchapters - 1)
        book_to_read = bible_chapters[chapter_index]
        chapter_to_read = bible_chapters[chapter_index][1]
        print("chapter", chapter_to_read, "of the book", book_to_read[0], end=".\n")
    input("Press Enter/newline when you're done.\n")
