# Flashy - Flashcard App

Flashy is a simple and interactive flashcard app built with Python's `tkinter` library. It allows you to learn and review French vocabulary by displaying flashcards with French words and their English translations. Users can mark whether they guessed the word correctly or incorrectly. Incorrect guesses will be saved in a separate CSV file for future questionns.

## Features
- Flashcards with French words and English translations.
- Option to mark your guess as "correct" or "wrong".
- Incorrect guesses are saved to a CSV file, keeping track of words you've learned.
- The app automatically flips the card after 3 seconds to show the English translation.

## Installation

1. Clone the repository or download the project files.

    ```bash
    git clone <repository-url>
    ```

2. Make sure you have Python 3 installed. You can download it from [python.org](https://www.python.org/).

3. Install the required libraries:

    ```bash
    pip install pandas
    ```

4. Ensure that you have the necessary image files in the `/images/` directory:
    - `card_front.png`
    - `card_back.png`
    - `right.png`
    - `wrong.png`

5. Place your French words CSV file (`french_words.csv`) in the `/data/` directory. You can also use a `words_to_learn.csv` file to track learned words.

## How to Use

1. When you open the app, it will display a random French word.
2. After 3 seconds, the card will flip to reveal the English translation.
3. You can click the "Right" button if you guessed the word correctly. It will be saved to the `words_to_learn.csv` file.
4. If you guessed incorrectly, click the "Wrong" button to move to the next card.


