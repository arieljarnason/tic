import string

def dimensions():
    choice = input("Input dimension of the board: ")

    return choice

def make_board(chosen_dimensions):
    """Sets the board given player input dimensions"""

    #makes the original game board list
    dimensions = int(chosen_dimensions)
    two_dim_board = []; num_increase = 1
    
    for i in range(0, dimensions):
        #make empty sublists
        two_dim_board.append([])
        for j in range(0, dimensions):
            two_dim_board[i].append(j)
            two_dim_board[i][j]= num_increase #add into sublists numbers for the grid
            num_increase += 1
            two_dim_board[i][j]=str(two_dim_board[i][j]) #convert all numbers into strings?

    return two_dim_board

def print_board(matrix, dimensions):

    """prints out the matrix of size n x n"""
    for i in range(int(dimensions)):
        for k in range(int(dimensions)):
            printout = matrix[i][k]
            print("{:>5}".format(printout), end="")
        print("")

def play(dimensions, matrix, game_over):
    
    while game_over == False:
        X_pos = input("X position: ")
        change_board(dimensions, matrix, X_pos, game_over, player="x")
        O_pos = input("O position: ")
        change_board(dimensions, matrix, O_pos, game_over, player="o")
    
    # check_victory()

def check_victory(current_matrix, dimensions, game_over):
    """
    svo eru til 4 leiðir til að vinna. 
    Ef allt í row er það sama, 
    ef allt í column er það sama og ef
     allt í n+1 gap er það sama eða 
     allt í n-1 gap er það sama.
      Þetta n+1 og n-1 er bilið sem er
       á milli númera í listunum miðað 
       við skálínurnar í n x n fylki. """

         #check rows
    for row in current_matrix:
        if len(set(row)) == 1:
            print("winner is", row[0])
            return game_over == True
            
        # check diagonal rows
    if len(set([current_matrix[i][i] for i in range(len(current_matrix))])) == 1:
        print("winner is", current_matrix[0][0])
        return game_over == True
    elif len(set([current_matrix[i][len(current_matrix)-i-1] for i in range(len(current_matrix))])) == 1:
        print("winner is", current_matrix[0][len(current_matrix)-1])
        return game_over == True

def change_board(dimensions, matrix, player_choice, game_over, player):
    player_insert = ''
    if player == "x":
        player_insert = "X"
    elif player == "o":
        player_insert = "O"
    
    changed_matrix = matrix

    #runs through all the list and checks if player choice matches
    #a number in the grid - if it does it replaces with X or O
    for i in range(int(dimensions)):
        for j in range(int(dimensions)):
            if player_choice == changed_matrix[i][j]:
                changed_matrix[i][j] = player_insert

    print_board(changed_matrix, dimensions)
    check_victory(changed_matrix, dimensions, game_over)

def main():
    
    player_dimensions = dimensions()
    matrix = make_board(player_dimensions)
    print_board(matrix, player_dimensions)
    game_over = False
    play(player_dimensions, matrix, game_over)
    

main()