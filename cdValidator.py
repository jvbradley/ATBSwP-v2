def cdValidator():
    '''
    ATBSwP Practice Project: Chess Dictionary Validator
    https://automatetheboringstuff.com/2e/chapter5/

    In this chapter, we used the dictionary value {'1h': 'bking', '6c':
    'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'} to represent a
    chess board. Write a function named isValidChessBoard() that takes a
    dictionary argument and returns True or False depending on if the board is
    valid.

    A valid board will have exactly one black king and exactly one white king.
    Each player can only have at most 16 pieces, at most 8 pawns, and all
    pieces must be on a valid space from '1a' to '8h'; that is, a piece can’t
    be on space '9z'. The piece names begin with either a 'w' or 'b' to
    represent white or black, followed by 'pawn', 'knight', 'bishop', 'rook',
    'queen', or 'king'.

    This function should detect when a bug has resulted in an improper chess
    board.
    '''
    chessBoard = {}
    chessBoard = mapChessBoard(chessBoard)
    cbPopulated = setPieceLocations(chessBoard)

def isValidChessBoard():
    print('Hello, world.')
    # This function is the goal of this assignment.

def setPieceLocations(chessBoard):
    cbPopulated = chessBoard
    pieceTypes = {'King': 1, 'Queen': 1, 'Bishop': 2, 'Knight': 2, 'Rook': 2,
    'Pawn': 8}
    pieceColors = ['Black', 'White']
    return cbPopulated

# working as intended at this time
def mapChessBoard(chessBoard):
    cbHoritzonal = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    cbVertical = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for letter in cbHoritzonal:
        for number in cbVertical:
            locationKey = letter
            locationKey = locationKey + str(number)
            chessBoard.setdefault(locationKey, '')
    return chessBoard

cdValidator()
