# TapDB

This program taps a SQLite database directly to render flashcards from the columns in a given table.

<img width="45%" alt="front" src="https://github.com/user-attachments/assets/782d14ed-af61-4dfe-8d9d-cf0f709f7a13" /> <img width="45%" alt="back" src="https://github.com/user-attachments/assets/741ac527-fa5c-4427-b267-6cff3cc95041" />

It is meant to provide flashcard functionality while allowing the source data to be reliably stored, updated, and analyzed using standard database practices. This addresses a shortcoming of the common flashcard program Anki, in which the flashcard data is stored in a walled-garden database that can't reliably be analyzed or exported. (For example, Anki will only export data to a tab-separated .txt file from which either all formatting has been stripped or which is riddled with HTML).

The initial window allows the database to be queried using normal SQL syntax, as shown below. The first column named with `select` becomes the "front" side of the flashcard; subsequent selected columns (up to 3) will be shown as the "back" side, under a line.

<img width="282" height="274" alt="initial" src="https://github.com/user-attachments/assets/11933730-8988-4ad3-ba70-5996f3b9c733" />

The user flips cards with the tab key, and can mark cards answered incorrectly with the 1 key, causing them to recur later in the session. Formatting (as custom-defined in the style sheet) can be applied in the query using the following syntax:  
`select deva(sanskrit), def` where `sanskrit` and `def` are columns, and `deva()` specifies that the sanskrit column should be rendered in a given font appropriate to the Devanagari script.

This is a work in progress. Only the "Review" function (the button on the right) currently works. In the future, the "Study" function will add spaced-repetition and the "Edit" function will provide a browser to edit the table directly.
