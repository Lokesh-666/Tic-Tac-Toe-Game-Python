import random
import time


theBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}

def printBoard(theBoard):
    print(theBoard['1'] + '|' + theBoard['2'] + '|' + theBoard['3'])
    print('-+-+-')
    print(theBoard['4'] + '|' + theBoard['5'] + '|' + theBoard['6'])
    print('-+-+-')
    print(theBoard['7'] + '|' + theBoard['8'] + '|' + theBoard['9'])

def checkForWin(theBoard):
    if theBoard['1'] == theBoard['2'] == theBoard['3']!=' ':
        return theBoard['1']
    elif theBoard['4'] == theBoard['5'] == theBoard['6']!=' ':
        return theBoard['4']
    elif theBoard['7'] == theBoard['8'] == theBoard['9']!=' ':
        return theBoard['7']
    elif theBoard['1'] == theBoard['4'] == theBoard['7']!=' ':
        return theBoard['1']
    elif theBoard['2'] == theBoard['5'] == theBoard['8']!=' ':
        return theBoard['2']
    elif theBoard['3'] == theBoard['6'] == theBoard['9']!=' ':
        return theBoard['3']
    elif theBoard['1'] == theBoard['5'] == theBoard['9']!=' ':
        return theBoard['1']
    elif theBoard['3'] == theBoard['5'] == theBoard['7']!=' ':
        return theBoard['3']
    else:
        return None


def pcPlays(theBoard):
    available_moves = [k for k, v in theBoard.items() if v == ' ']
    pcPlayed = random.choice(available_moves)
    theBoard[pcPlayed] = 'O'


def announceWinner(WhoWon):
    if WhoWon == 'X':
        print("You won!")
    elif WhoWon == 'O':
        print("The pc won!")
    elif WhoWon == None:
        print("It's a tie!")
    
def tic_tac_toe():
    printBoard(theBoard)
    print("Let me play first... ")
    pcPlays(theBoard)
    time.sleep(5)
    printBoard(theBoard)
    WhoWon = None
    i = 0
    while(WhoWon == None):
        if (i>=4):
            break
        print("Where do you wish to play? (1 to 9))")
        player = int(input())
        if theBoard[str(player)] ==' ':
            theBoard[str(player)] = 'X'
            printBoard(theBoard)
        else:
            print("That spot is already taken. Try again.")
            continue
        WhoWon = checkForWin(theBoard)
        
        if WhoWon== None:
            print("It's the pc's turn now...")
            time.sleep(5)
            pcPlays(theBoard)
            printBoard(theBoard)
            WhoWon = checkForWin(theBoard)
        i = i + 1
    announceWinner(WhoWon)

def main():
    print("Do you wish to play tic tac toe with pc? (y/n): ")
    answer = input()
    if answer == "y":
        tic_tac_toe()



if __name__ == '__main__':
    main()