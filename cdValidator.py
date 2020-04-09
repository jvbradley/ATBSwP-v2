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
    chessPieces = getChessPieces()
    newChessBoard = mapChessBoard()
    cbReadyCheck = setChessBoard(newChessBoard, chessPieces)
    isValidChessBoard(cbReadyCheck)

def isValidChessBoard(cbReadyCheck):
    # This dictionary is the reference by which the built chessboard may be
    # validated for accurate piece placement.
    cbPieceMap = {'A1': 'White Rook', 'A2': 'White Pawn', 'A7': 'Black Pawn',\
    'A8': 'Black Rook', 'B1': 'White Knight', 'B2': 'White Pawn', 'B7': \
    'Black Pawn', 'B8': 'Black Knight', 'C1': 'White Bishop', 'C2': \
    'White Pawn', 'C7': 'Black Pawn', 'C8': 'Black Bishop', 'D1': \
    'White King', 'D2': 'White Pawn', 'D7': 'Black Pawn', 'D8': 'Black King',\
    'E1': 'White Queen', 'E2': 'White Pawn', 'E7': 'Black Pawn', 'E8': \
    'Black Queen', 'F1': 'White Bishop', 'F2': 'White Pawn', 'F7': \
    'Black Pawn', 'F8': 'Black Bishop', 'G1': 'White Knight', 'G2': \
    'White Pawn', 'G7': 'Black Pawn', 'G8': 'Black Knight', 'H1': \
    'White Rook', 'H2': 'White Pawn', 'H7': 'Black Pawn', 'H8': 'Black Rook'}

    validationLog = ''
    validLocations = 0
    invalidLocations = 0

    for key, value in cbReadyCheck.items():
        if value != '':
            if value == cbPieceMap[key]:
                validationLog += ' * Location validated: ' + value + ' / ' + key + '\n'
                validLocations += 1
            elif value != cbPieceMap[key]:
                validationLog += '\tTHIS ITEM NEEDS CORRECTION: ' + value + ' / ' + key + '\n'
                invalidLocations += 1

    if invalidLocations == 0:
        validationLog += '\n\tValidly position pieces: ' + str(validLocations) + '\n'
        validationLog += '\tThis script has completed successfully.'
    elif validLocations > 32 or validLocations < 32:
        validationLog += '\n\tThere are an invalid number of pieces on the board.\n'
        validationLog += '\tExpected: 32 / Actual: ' + str(validLocations) + '\n'
        validationLog += '\tReview the log for problematic items.'

    print(validationLog)

# This function creates the spaces of a chessboard.
def mapChessBoard():
    chessBoard = {}
    cbHoritzonal = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    cbVertical = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for letter in cbHoritzonal:
        for number in cbVertical:
            locationKey = letter
            locationKey = locationKey + str(number)
            chessBoard.setdefault(locationKey, '')

    return chessBoard

# This function creates a dictionary of chess pieces and their locations.
def getChessPieces():
    pieceTypes = {'pawn': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
    'king': ['d'], 'queen': ['e'], 'bishop': ['c', 'f'],
    'knight': ['b', 'g'], 'rook': ['a', 'h']}
    colorOptions = {'b': 'black', 'w': 'white'}
    chessPieceInfo = {}
    # chessPieceInfo = {color-piece: [[starting columns], Name]}
    for color, colorName in colorOptions.items():
        for type, typeColumn in pieceTypes.items():
            cpInfoKey = color + '-' + type
            # Starting Column, On-Display Name
            chessPieceInfo[cpInfoKey] = [typeColumn, colorName.title() + ' ' + type.title()]
    # import pprint
    # pprint.pprint(chessPieceInfo)

    for cpInfoKey, cpData in chessPieceInfo.items():
        if 'pawn' in cpInfoKey:
            newLocationInfo = []
            for column in cpData[0]:
                if cpInfoKey[0] == 'w':
                    newLocationInfo.append(column.title() + '2')
                elif cpInfoKey[0] == 'b':
                    newLocationInfo.append(column.title() + '7')
        elif 'pawn' not in cpInfoKey:
            newLocationInfo = []
            for column in cpData[0]:
                if cpInfoKey[0] == 'w':
                    newLocationInfo.append(column.title() + '1')
                elif cpInfoKey[0] == 'b':
                    newLocationInfo.append(column.title() + '8')

        chessPieceInfo[cpInfoKey] = [newLocationInfo, cpData[1]]

    return chessPieceInfo

# This function sets the pieces on the board.
def setChessBoard(newChessBoard, chessPieces):
    for piece, pieceInfo in chessPieces.items():
        for location in pieceInfo[0]:
            #print(' * Moving piece \'' + pieceInfo[1] + '\' to ' + location + '.')
            newChessBoard[location] = pieceInfo[1]
    return newChessBoard


cdValidator()
