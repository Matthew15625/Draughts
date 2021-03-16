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

class MoveRecord:
  '''A class definition for storing the details of a potential move.'''

def CreateBlankBoardArray(Board):
  print ("This stub will be used to create the empty structure for the board")

def LoadPieces(FileHandle, PlayersPieces):   
  print ("This is a stub for the LoadPieces subroutine")

def CreateNewBoard(Board): 
  print ("This is a stub for the CreateNewBoard subroutine")

def AddPlayerA(Board, A):
  print ("This is a stub for the AddPlayerA subroutine")    
    
def DisplayErrorCode(ErrorNumber):
  print('Error ', ErrorNumber)
  
def SetUpBoard(Board, A, B, FileFound):
  print ("This is a stub for the SetUpBoard subroutine")
  print ("When complete it will use calls to LoadPieces(), CreateNewBoard() and AddPlayerA()")

def PrintHeading():
  print ("This is a stub for the PrintHeading subroutine used in DisplayBoard()")      
  
def PrintRow(Board, ThisRow):
  print ("This is a stub for the PrintRow subroutine used in DisplayBoard()")

def PrintMiddleRow(Board, ThisRow):    
  print ("This is a stub for the PrintMiddleRow subroutine used in DisplayBoard())")
       
def PrintLine():  
  print ("This is a stub for the PrintLine subroutine used in DisplayBoard())")

def DisplayBoard(Board):
  print ("This is a stub for the DisplayBoard subroutine. It will use calls the the subroutines above")

def PrintPlayerPieces(A, B):
  print ("This is a stub for the PrintPlayersPieces subroutine")
  
def ClearList(ListOfMoves):
  print ("This is a stub for the ClearList subroutine used in the ListPossibleMoves() subroutine")

def ValidMove(Board, NewRow, NewColumn):
  print ("This is a stub for a subroutine used in the ListPossibleMoves() subroutine")

def ListPossibleMoves(Board, PlayersPieces, NextPlayer, ListOfMoves):
  print ("This is a stub for the ListPossibleMoves() subroutine")

 
def Game():
  print ("This is the stub for the main Game() subroutine")
  print ("We will define the structures to hold the game data here")
  print ("We will populate those structures with the starting data")
  print ("If the structures are populated correctly we will display the board")
  print ("This will make use of calls the the other subroutines provided")
  Board = [['' for Column in range(BOARD_SIZE)] for Row in range(BOARD_SIZE)]
  A = [[0, 0, 0] for Piece in range(NUMBER_OF_PIECES + 1)]
  B = [[0, 0, 0] for Piece in range(NUMBER_OF_PIECES + 1)]
      
      
if __name__ == "__main__":
  Game()      
   
