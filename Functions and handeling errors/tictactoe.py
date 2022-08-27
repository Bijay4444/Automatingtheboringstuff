import pprint

theBoard = {'top-L' : 'O', 'top-M' : ' O', 'top-R': ' O',
            'mid-L': 'X', 'mid-M': ' X', 'mid-R': ' ',
             'bottom-L': ' ', 'bottom-M': ' ', 'bottom-R': ' X'}

def print_board(board):
    print(board['top-L']+ ' |' + board['top-M'] + ' |'+ board['top-R'])
    print('---------')    
    print(board['mid-L']+ ' |' + board['mid-M'] + ' |'+ board['mid-R'])
    print('---------')    
    print(board['bottom-L']+ ' |' + board['bottom-M'] + ' |'+ board['bottom-R'])
    print('---------')    

print_board(theBoard)