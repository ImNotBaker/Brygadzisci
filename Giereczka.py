#Super kółko i krzyżyk z chyba działającym AI

import random

def drawBoard(board):

#Plansza do gry zrobiona ze stringsów, żeby to jakoś wyglądało.
    
     print(board[1], board[2], board[3])
     print(board[4], board[5], board[6])
     print(board[7], board[8], board[9])

def inputPlayerLetter():

#Gracz wybiera sobie, czy chce być kółeczkiem, czy krzyżykiem.

    letter = ''
    while not (letter == 'X' or letter == 'O'):
         print('Twoim przeznaczeniem jest być znaczkiem X, czy może O?')
         letter = input().upper()

#Pierwszy element na liście to znaczek gracza, a drugi - komputera

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():

#A to wybiera losowo kto zaczyna (0 - komputr, 1 - żyjątko)

    if random.randint(0, 1) == 0:
        return 'Komputer'
    else:
        return 'Gracz'

def playAgain():
#Funkcja zwraca wartość True, w przypadku, gdy gracz chce zagrać sobie znowu.
    print('Czy jesteś już uzależniony od tej wspaniałej gry i chcesz zagrać ponownie? (tak lub nie)')
    return input().lower().startswith('tak')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
#Funkcja zwraca wartość True, kiedy wygra znaczek gracza.
#Board zostało skrócone do bo, letter do le. Mniej pisanka na propsie.

    return ((bo[1] == le and bo[2] == le and bo[3] == le) or #góra
    (bo[4] == le and bo[5] == le and bo[6] == le) or #środeczek
    (bo[7] == le and bo[8] == le and bo[9] == le) or #dół
    (bo[1] == le and bo[4] == le and bo[7] == le) or #z góry na dół, lewa strona
    (bo[2] == le and bo[5] == le and bo[8] == le) or #z góry na dół, środeczek
    (bo[3] == le and bo[6] == le and bo[9] == le) or #z góry na dół, prawa strona
    (bo[3] == le and bo[5] == le and bo[7] == le) or #przekątna numero uno
    (bo[1] == le and bo[5] == le and bo[9] == le)) #przekątna numero uno dwa

def getBoardCopy(board):
#Robi kopię planszy i ją zwraca, jakkolwiek by to nie brzmiało.
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):
#Zwraca wartość True, kiedy ruch, który gracz chce wykonać, jest możliwy.
    return board[move] == ' '

def getPlayerMove(board):
#Funkcja, dzięki której gracz w ogóle może wykonać swój ruch.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('Wykonaj ruch mordeczko. Wybierz cyferkę od 1 do 9')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
#Zwraca możliwe ruchy, albo też zwraca "None", kiedy nie można już wykonać ruchu
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
#Mamy planszę i znaczek komputera, to teraz niech decyduje, gdzie wykonać ruch.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

#No i się zaczyna super zabawa.
#Szybkie sprawdzanko, czy da radę wygrać w następnym ruchu.

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

#Sprawdzanko, czy gracz ma możliwość wygrania w następnym ruchu i zablokowanie go tak, że aż zrobi mu się przykro.

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

#Komputer zajmie jeden z rogów, o ile są wolne (wybiera losowo spomiędzy tych niezajętych)

    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

#Komputer zajmie środeczek, o ile jest wolny.
    if isSpaceFree(board, 5):
        return 5

#Komputer zajmie jedno z pól wychodzących ze środeczka.

    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):

#Zwraca wartość True, jeśli plansza została zapełniona.

    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

print('Zagraj w super giereczkę kółko i krzyżyk!')

while True:

#Reseruje planszę.

    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('Gracz ' + turn + ' rozpoczyna.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'Gracz':

#Ruch gracza.

            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Juhu, udało ci się wygrać. To niesamowite!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('I myk remisik!')
                    break
                else:
                    turn = 'Komputer'
        else:
            
#Ruch komputera.

            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('Komputer cię opykał, to całkiem przykre')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('I myk remisik!')
                    break
                else:
                    turn = 'Gracz'

    if not playAgain():
        break
