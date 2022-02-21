from hangman.FileIO import FileIO
from Hangman import Hangman

if __name__ == "__main__":
    fileIO = FileIO()
    game = Hangman(fileIO)
    try:
        game.getUserName()
    except ValueError:
        game.execute()
    else:
       print("Invalid value")
