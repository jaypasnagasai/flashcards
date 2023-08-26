# Importing necessary modules
import random  # Module for random selection
import time    # Module for time-related operations

# Defining the Flashcard class to hold word information
class Flashcard:
    def __init__(self, word, meaning, pronunciation):
        self.word = word
        self.meaning = meaning
        self.pronunciation = pronunciation

# Defining the FlashcardDeck class to manage a collection of flashcards
class FlashcardDeck:
    def __init__(self):
        self.flashcards = []  # Initializing an empty list to store flashcards

    def add_flashcard(self, flashcard):
        self.flashcards.append(flashcard)  # Adding a new flashcard to the deck

    def pick_random_flashcard(self):
        if not self.flashcards:
            return None  # If no flashcards are available, return None
        return random.choice(self.flashcards)  # Return a randomly chosen flashcard

# Function to create a new flashcard
def create_flashcard():
    word = input("Enter the word: ")
    meaning = input("Enter the meaning: ")
    pronunciation = input("Enter the pronunciation: ")
    return Flashcard(word, meaning, pronunciation)  # Creating and returning a new flashcard object

# Main function that runs the flashcard learning tool
def main():
    deck = FlashcardDeck()  # Creating a new flashcard deck

    print("Welcome to the Flashcard Learning Tool!")

    while True:
        print("\n1. Create a new flashcard")
        print("2. Learn flashcards")
        print("3. Exit")
        choice = input("Enter your choice: ")  # Taking user input for choice

        if choice == "1":
            flashcard = create_flashcard()  # Creating a new flashcard
            deck.add_flashcard(flashcard)  # Adding the new flashcard to the deck
            print("Flashcard added successfully!")

        elif choice == "2":
            flashcard = deck.pick_random_flashcard()  # Randomly selecting a flashcard
            if not flashcard:
                print("You've learned all the flashcards!")
                break  # Exiting the learning loop if no more flashcards are available

            print("\nWord:", flashcard.word)
            input("Press Enter to reveal the meaning and pronunciation...")
            print("Meaning:", flashcard.meaning)
            print("Pronunciation:", flashcard.pronunciation)

            response = input("Did you remember it? (yes/no): ").strip().lower()
            if response == "yes":
                print("Great! Let's move on.")
                time.sleep(1)  # Pausing for a moment before continuing
            else:
                print("No worries! Let's try again.")
                deck.add_flashcard(flashcard)  # Adding the flashcard back to the deck for review

        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break  # Exiting the main loop and ending the program

        else:
            print("Invalid choice. Please select a valid option.")

# Running the main function if this script is executed directly
if __name__ == "__main__":
    main()
