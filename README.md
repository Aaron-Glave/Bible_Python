# Bible_Python
Executable program to recommend Bible chapters.

It lets you pick between 3 different methods to reccomend a chapter:
1. Select a random book in the Bible, then a random chapter from that book.
    * Doing this, you have a 39/66 chance of reading from the Old Testament, and a 27/66 chance of reading from the New Testament.
2. Select a random Psalm to read.
3. Treat the bible as 1 huge book, and pick a random chapter of any book in the Bible.
   * Doing this, Psalms is the most likely Bible book to be selected.
   * That's because Psalms is the longest book in the Bible and has the most chapters.

I compiled this using this command: `pyinstaller.exe bible_chapter.spec`.
