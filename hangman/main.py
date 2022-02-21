from hangman.FileIO import FileIO
from Hangman import Hangman

if __name__ == "__main__":
    fileIO = FileIO()
    game = Hangman(fileIO)
    try:
        game.getUserName()
    except ValueError:
        # Hangman에서 입력받은 이름이 숫자라면 잘못된 입력으로 간주하기 위하여 float(name)이 실행됨
        # int/float 아닐 경우 ValueError 발생함 -> 옳은 입력으로 간주하고 게임 실행되도록 try-except 설정
        game.execute()
    else:
       print("Invalid value")
