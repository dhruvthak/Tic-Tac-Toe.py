'''
An implementation of Tic Tac Toe
Student name: Dhruv Thakkar
Student ID#: 0985910
'''
__author__ = 'Dhruv Thakkar'

import os

class Player:


    def __init__(self,Name,PlayingMark):
        """
        __init__ : the class constructor
        name --> name of the player
        PlayingMark --> "X" or "0"
        Statistics --> a dictionary containing record of win,loss and draw
        """
        self.Name = Name
        self.PlayingMark= PlayingMark
        self.Statistics={"won" : 0,"loss" : 0,"draw" : 0}


    def get_score(self):
        """
        get_score() --> Calculates score based on data stored in Statistics
        """
        return ((self.Statistics["won"] * 2) + self.Statistics["draw"] - self.Statistics["loss"])



    def __str__(self):
        """
        __str__ method that would print the player name, mark, and score.
        """
        return "Player Name: " + str(self.Name) +" | Player Mark: "  + str(self.PlayingMark) + " | Player Score: " \
               + str(self.get_score())


    def __lt__(self,other):
        """
        __lt__ overriding default function
        """
        return self.get_score() < other.get_score()

class Deck:

    # __init__ : the class constructor
    def __init__(self):
        self.Board = ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"] # default board with 9 values
        self.Player1Choices = [] # stores the cells player1 filled
        self.Player2Choices = [] # stores the cells player2 filled

    # __str__ : To print the current board status
    def __str__(self):

        print_stm = '	|     | \n'
        print_stm += '  '+str(self.Board[0])+' |  '+str(self.Board[1])+'  |  '+str(self.Board[2])+'\n'
        print_stm += '____|_____|_____\n'
        print_stm += '	|     |\n'
        print_stm += '  '+str(self.Board[3])+' |  '+str(self.Board[4])+'  |  '+str(self.Board[5])+'\n'
        print_stm += '____|_____|____\n'
        print_stm += '	|     |\n'
        print_stm += '  '+str(self.Board[6])+' |  '+str(self.Board[7])+'  |  '+str(self.Board[8])+'\n'
        print_stm += '	|	  |'

        # replacing all the "-1's" in the string with "blankspace" so that the user doesn't get confused
        return print_stm.replace("-1", " ")

class TicTacToe:


    def __init__(self):
        '''
        __init__ : the class constructor
        '''
        self.DeckList = [] # to keep a record of all games played
        self.is_winner = False # win flag
        self.winning_mark = "" # winner mark to identify the winner

        print("Hi there !")

        name = self.basic_validate_input("name","Player 1, Please Enter your Name:")
        choice = self.basic_validate_input("choice","Player 1, Would you like to use X or 0, Please Enter your Choice:")
        self.Player1 = Player(name,choice)

        name = self.basic_validate_input("name","Player 2, Please Enter your Name:")
        if(self.Player1.PlayingMark == "X"):
            choice = "0"
        else:
            choice = "X"
        self.Player2 = Player(name,choice)

        self.clear_screen(20)
        print("Welcome,\n")
        print (self.Player1)
        print (self.Player2)
        self.clear_screen(2)


    def clear_screen(self,other):
        '''
        clear_screen:custom clear screen function
        other --> the number of lines to clean
        '''

        #os.system(['clear','cls'][os.name == 'nt']) --> not working on pycharm

        print('\n'*other)




    def update_stats(self,player_name,type):
        '''
        update_stats --> to update the Player Statistics
        '''

        if type == "won":
            if player_name == "Player1":
                self.Player1.Statistics["won"] += 1
                self.Player2.Statistics["loss"] +=1
            else:
                self.Player2.Statistics["won"] += 1
                self.Player1.Statistics["loss"] +=1
        elif type == "draw":
            self.Player1.Statistics["draw"] += 1
            self.Player2.Statistics["draw"] += 1


    def basic_validate_input(self,type,prompt):
        '''
        basic_validate_input is just another validation function for all the validations except the users cell input
        validation.
        type --> to identify where the input validation is coming from ,
        prompt --> what the input prompt statement should be printed
        '''

        #Validating the input Player name
        if type == "name":
            while True:
                try:
                    value = input(prompt)
                    if not value:
                        raise ValueError('Name cannot be blank !\n')
                except ValueError as e:
                    print(e)
                    continue
                else:
                    break
            return value


        #Validating the input PlayerMark choice
        elif type == "choice":
            while True:
                try:
                    value = input(prompt).upper() # convert input to upper case

                    #check if input is blank or not
                    if not value:
                        raise ValueError('Choice cannot be blank !\n')

                    # validate if only one character is inputted
                    if  len(value) > 1:
                        raise SyntaxError('Please enter only one character X or 0')

                    # validate if value is X or 0
                    if value not in ["X","0"]:
                        raise SyntaxWarning('Please enter either "X" or "0"')

                except ValueError as e:
                    print(e)
                    continue
                except SyntaxError as e:
                    print(e)
                    continue
                except SyntaxWarning as e:
                    print(e)
                    continue
                else:
                    break
            return value

        #Validating the input to play again or not
        elif type == "replay":
            while True:
                try:
                    value = input(prompt).lower() # convert input to lower case
                    if not value:
                        raise ValueError('Please input yes or no !\n')
                    if value not in ["yes","no","y","n"]:
                        raise SyntaxError('Please input yes or no only !\n')
                except ValueError as e:
                    print(e)
                    continue
                except SyntaxError as e:
                    print(e)
                    continue
                else:
                    break
            return value[0] # return just the first character of the string "yes ---> y"



    def validate_user_input(self,value):
        '''
        validate_user_input() validates if the user input is an int between
        0 - 8 and if it was not played previously.
        '''

        #check if the value input is in between 0 - 8
        if int(value) in range(0,9):

            #check if the default value exist in the cell, if not then its already filled up
            if self.currDeck.Board[value] == "-1":
                return True
            else:
                print("Slot already filled ! Please try another one !")
                return False
        else:
            print("Invalid Value ! Please Try again")
            return False



    def is_game_over(self):
        """
        is_game_over() : check if the game is over by finding if a user won or if the board is
        full, if true then append the Deck lists to a file with the name "ticTacToe.txt" and
        return true, else return false.
        """
        what_to_return = ""
        print(self.currDeck)

        if self.currDeck.Board.count("-1") <= 4:

            #check diagonal elements for X & 0
            if  (self.currDeck.Board[0] == self.currDeck.Board[4] == self.currDeck.Board[8] == "X") or \
                (self.currDeck.Board[2] == self.currDeck.Board[4] == self.currDeck.Board[6] == "X"):
                self.winning_mark = "X"
                what_to_return = True

            elif(self.currDeck.Board[0] == self.currDeck.Board[4] == self.currDeck.Board[8] == "0") or \
                (self.currDeck.Board[2] == self.currDeck.Board[4] == self.currDeck.Board[6] == "0"):
                self.winning_mark = "0"
                what_to_return = True

            #check for elements horizontally for X & 0
            elif(self.currDeck.Board[0] == self.currDeck.Board[1] == self.currDeck.Board[2] == "X") or \
                (self.currDeck.Board[3] == self.currDeck.Board[4] == self.currDeck.Board[5] == "X") or \
                (self.currDeck.Board[6] == self.currDeck.Board[7] == self.currDeck.Board[8] == "X") :
                self.winning_mark = "X"
                what_to_return = True

            elif(self.currDeck.Board[0] == self.currDeck.Board[1] == self.currDeck.Board[2] == "0") or \
                (self.currDeck.Board[3] == self.currDeck.Board[4] == self.currDeck.Board[5] == "0") or \
                (self.currDeck.Board[6] == self.currDeck.Board[7] == self.currDeck.Board[8] == "0") :
                self.winning_mark = "0"
                what_to_return = True

            #check for elements vertically for X & 0
            elif (self.currDeck.Board[0] == self.currDeck.Board[3] == self.currDeck.Board[6] == "X") or \
                 (self.currDeck.Board[1] == self.currDeck.Board[4] == self.currDeck.Board[7] == "X") or \
                 (self.currDeck.Board[2] == self.currDeck.Board[5] == self.currDeck.Board[8] == "X") :
                self.winning_mark = "X"
                what_to_return = True

            elif (self.currDeck.Board[0] == self.currDeck.Board[3] == self.currDeck.Board[6] == "0") or \
                 (self.currDeck.Board[1] == self.currDeck.Board[4] == self.currDeck.Board[7] == "0") or \
                 (self.currDeck.Board[2] == self.currDeck.Board[5] == self.currDeck.Board[8] == "0") :
                self.winning_mark = "0"
                what_to_return = True

            elif self.currDeck.Board.count("-1") == 0 :
                self.winning_mark = "-1"
                what_to_return = True

        if what_to_return == True:

            #write to file
            with open('ticTacToe.txt', 'a') as fi:
                fi.write("Board :"+str(self.currDeck.Board) +"\nPlayer1 steps :"+str(self.currDeck.Player1Choices) +"\nPlayer2 steps :"+ str(self.currDeck.Player2Choices) +"\n\n")
            return True
        else:
            return False


    def get_user_input(self,player):
        """
        get_user_input() : a method to get user input, it should display a message like "enter
        player {name} choice:". and then it should call the validate_user_input() to validate
        the user input, if user's input is valid, then store the value in the Board and the check
        if the game is over by calling is_game_over()
        """

        while True:
            try:
                value = int(input("Please enter player "+player.Name+"'s choice :"))

            except ValueError:
                print("Please input number between 0 and 9 only\n")
                continue

            value = value - 1

            if  self.validate_user_input(value) == True:
                self.currDeck.Board[value] = player.PlayingMark
                if(player.PlayingMark == self.Player1.PlayingMark):
                    self.currDeck.Player1Choices.append(value + 1)
                else:
                    self.currDeck.Player2Choices.append(value + 1)
                if self.is_game_over() == True:
                    self.is_winner = True
                    if self.winning_mark == self.Player1.PlayingMark:
                        self.update_stats("Player1","won")
                        print("#############################################################")
                        print(self.Player1.Name+ " Won !")
                        print("#############################################################")

                    elif self.winning_mark == self.Player2.PlayingMark:
                        self.update_stats("Player2","won")
                        print("#############################################################")
                        print(self.Player2.Name+ " Won !")
                        print("#############################################################")

                    elif self.winning_mark == "-1":
                        self.update_stats("Player1","draw")
                        print("#############################################################")
                        print("It's a draw !")
                        print("#############################################################")

                    break
                break
            else:
                continue




    def start_game(self):
        """
        start_game() : the main game logic should go here in this class, it should add a list
        item to DeckList, and while the game is not over, keep calling get_user_input() for
        each user. Once a game is over, ask if the user wants to play again and then start a
        new game.
        """

        while True:
            print("Let the game begin")
            self.currDeck = Deck()
            for i in range(0,9):
                if i % 2 == 0:
                    player = self.Player1
                else:
                    player = self.Player2
                self.get_user_input(player)
                self.clear_screen(20)
                if self.is_winner == True:

                    print("Player Stats:")
                    print("Player 1 :\n")
                    print(self.Player1)
                    print("\nPlayer 2 :\n")
                    print(self.Player2)
                    break
            print("Player 1 played : "+str(self.currDeck.Player1Choices))
            print("Player 2 played : "+str(self.currDeck.Player2Choices))
            if self.basic_validate_input("replay","Would you like to play again ?") == "y":
                self.is_winner = False
                self.winning_mark = ""
                self.clear_screen(20)
                self.currDeck.Player1Choices = self.currDeck.Player2Choices = []

                print("#############################################################")
                continue
            else:
                print("#############################################################")
                print("Thank you , have a great day!")
                print("#############################################################")
                break

tictac_obj = TicTacToe() #creating object of TicTacToe class
tictac_obj.start_game() # method call of TicTacToe