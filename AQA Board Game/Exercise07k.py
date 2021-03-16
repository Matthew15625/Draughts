# Skeleton Program used as preparation for the AQA A1 Summer 2019 examination
# this code should be used in conjunction with Board Game 01
# written by RD
# developed in a Python 3 environment

# Version number: 0.1


SPACE = '     '
UNUSED = 'XXXXX'

BOARD_SIZE = 8
NUMBER_OF_PIECES = 12

ROW = 0
COLUMN = 1
QUEEN = 2

MAX_MOVES = 50

class MoveRecord:
  '''A class definition for storing the details of a potential move.'''
  def __init__(self, Piece="", NewRow=-1, NewColumn=-1, CanJump=False):
    self.Piece = Piece
    self.NewRow = NewRow
    self.NewColumn = NewColumn
    self.CanJump = CanJump
  
  def __str__(self):
    return self.Piece + " to (" + (str(self.NewColumn) +","+ str(self.NewRow))+")"
  
  def __eq__(self, other):
    if self.Piece == other.Piece:
      if self.NewRow == other.NewRow:
        if self.NewColumn == other.NewColumn:
          if self.CanJump == other.CanJump:
            return True
    return False

def CreateBlankBoardArray(Board):
  print ("This stub will be used to create the empty structure for the board")

def LoadPieces(FileHandle, PlayersPieces):
  #Loops the same number of times as the number of pieces + 1   
  for piece in range(NUMBER_OF_PIECES+1):
    # The first iteration will just load placeholder values
    if piece == 0:
      FileHandle.readline()
      FileHandle.readline()
      FileHandle.readline()
      continue
    #Loop 3 times - once for each attribute of the piece
    for attribute in range(3):
      value = int(FileHandle.readline())
      PlayersPieces[piece][attribute] = value
  return PlayersPieces

def CreateNewBoard(Board): 
  # Loop over each row
  for row in range(BOARD_SIZE):
    # Loop over each column
    for column in range(BOARD_SIZE):
      # Added the row and column together. If the result is odd, make a space. Otherwise, make it unused.
      if (row + column) % 2 == 1:
        Board[row][column] = SPACE
      else:
        Board[row][column] = UNUSED
  return Board

def AddPlayer(Board, Player, PlayerName):
  # Loop over the pieces for each player - From 1 onwards as Player[0] is a placeholder
  for index, piece in enumerate(Player[1:]):
    # Make sure the piece hasn't been captured
    if piece[ROW] != -1:
      # if the piece isn't a queen, then use the lowercase value and add on the piece number. If the piece is a queen, then use the uppercase value, and add on the piece number.
      Board[piece[ROW]][piece[COLUMN]] = getPieceName(Board, piece, PlayerName, index)
  return Board

def getPieceName(Board, piece, PlayerName, index):
  return (PlayerName.lower() if piece[QUEEN] == 0 else PlayerName.upper()) + str(index+1)

def DisplayErrorCode(ErrorNumber):
  print('Error ', ErrorNumber)
  
def SetUpBoard(Board, A, B, FileFound):
  FileName = "game1.txt"
  Answer = input("Do you want to load a saved game? (Y/N): ")
  if Answer.lower() == "y":
    FileName = input("Enter the filename: ")
  try:
    FileHandle = open(FileName)
    FileFound = True
    A = LoadPieces(FileHandle, A)
    B = LoadPieces(FileHandle, B)
    FileHandle.close()
  except:
    DisplayErrorCode("4: File Load Error")
  Board = CreateNewBoard(Board)
  Board = AddPlayer(Board, A, "a")
  Board = AddPlayer(Board, B, "b")
  return Board, A, B, FileFound

def PrintHeading():
  #Initial alignment
  print("    ", end="")
  #print each column number in turn, giving each one 2/3 spaces of padding each side
  for i in range(BOARD_SIZE):
    print("{:^6}".format(i), end="")
  print()
  
def PrintRow(Board, ThisRow):
  #Initial alignment
  print("   |", end="")
  #Loops through each column If it is used, display the 5 'X's and a pipe. Otherwise, display 5 spaces and a pipe.
  for column in range(BOARD_SIZE):
    print("{:^5}|".format(Board[ThisRow][column] if "X" in Board[ThisRow][column] else ""), end="")
  print()

def PrintMiddleRow(Board, ThisRow):
  #Prints row number, and aligns row with board
  print(f" {ThisRow} |", end="")
  #Loops through each column
  #If it is unused, display 'XXXXX|'
  #If it is used, check to see if theres a piece in it
  #If there is, then display the piece, right-aligned in the center, taking up 5 spaces, and a pipe
  #If there isn't, then display 5 spaces and a pipe
  #
  #Thats a bit more complicated than it could be, because I wanted to get the piece name right-aligned in the centre like the example e.g. '  a3 |' instead of ' a3  |'. If I didn't worry about that, then i could use
  #print("{:^5}|".format(Board[ThisRow][column])
  for column in range(BOARD_SIZE):
    print("{:^5}|".format(Board[ThisRow][column]) if "X" in Board[ThisRow][column] or " " in Board[ThisRow][column] else " {:>3} |".format(Board[ThisRow][column]), end="")
  print()

def PrintLine():
  #Aligns line with board
  print("   ", end="")
  #Print line, with length dependent on boardSize
  print("-"*(6*BOARD_SIZE+1))

def DisplayBoard(Board):
  PrintHeading()
  for row in range(BOARD_SIZE):
    PrintLine()
    PrintRow(Board, row)
    PrintMiddleRow(Board, row)
    PrintRow(Board, row)
  PrintLine()

def PrintPlayerPieces(A, B):
  print("Player A:")
  print(A) 
  print()
  print("Player B:")
  print(B)
  print()
  
def ClearList(ListOfMoves):
  return [MoveRecord()]*50

def ValidMove(Board, NewRow, NewColumn):
  if NewRow < 0 or NewColumn < 0:
    return False
  try:
    return Board[NewRow][NewColumn] != UNUSED
  except:
    return False

def ListPossibleMoves(Board, PlayersPieces, NextPlayer, ListOfMoves):
  moveIndex = 0
  for index, piece in enumerate(PlayersPieces[1:]):
    row = piece[ROW]
    column = piece[COLUMN]
    y = []
    if piece[QUEEN] == 1:
      y = [-1, 1]
    else:
      if NextPlayer == "a":
        y = [1]
      else:
        y = [-1]
    x = [-1, 1]
    for y1 in y:
      for x1 in x:
        if ValidMove(Board, row+y1, column+x1):
          name = getPieceName(Board, piece, NextPlayer, index)
          newMove = MoveRecord()
          if Board[row+y1][column+x1] != SPACE:
            if ValidMove(Board, row+y1+y1, column+x1+x1) and NextPlayer.lower() not in Board[row+y1][column+x1].lower():
              if Board[row+y1+y1][column+x1+x1] == SPACE:
                newMove = MoveRecord(name, row+y1+y1, column+x1+x1, True)
              else: continue
            else: continue
          else:
            newMove = MoveRecord(name, row+y1, column+x1)
          try:
            if newMove not in ListOfMoves:
              ListOfMoves[moveIndex] = newMove
              moveIndex += 1
          except:
            break
  return ListOfMoves

def Game():
  GameEnd = False
  FileFound = False
  Board = [['' for Column in range(BOARD_SIZE)] for Row in range(BOARD_SIZE)]
  A = [[0, 0, 0] for Piece in range(NUMBER_OF_PIECES + 1)]
  B = [[0, 0, 0] for Piece in range(NUMBER_OF_PIECES + 1)]
  ListOfMoves = [MoveRecord()] * MAX_MOVES
  Board, A, B, FileFound = SetUpBoard(Board, A, B, FileFound)
  GameEnd = not FileFound
  NextPlayer = "a"
  print(Board)
  while not GameEnd:
    PrintPlayerPieces(A, B)
    DisplayBoard(Board)
    print("Next player is:", NextPlayer)
    ListOfMoves = ListPossibleMoves(Board, A if NextPlayer == "a" else B, NextPlayer, ListOfMoves)
    print(ListOfMoves[0], end="")
    for move in ListOfMoves[1:]:
      if move.NewRow == -1:
        break
      print(",",move, end = "")
    print()
    GameEnd = True
  
if __name__ == "__main__":
  Game()
