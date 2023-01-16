import random

class rock_paper_scissor:
    def __init__(self):
        self.player_name = ''
        self.player_option = ''
        self.player_points = 0
        
        self.NPC_option = ''
        self.NPC_points = 0

        self.rounds = 1
        self.options = ["rock", "paper", "scissor"]
    
    def assign_player_name(self):
        name = input("\nPlease enter your name: ")
        self.player_name = name
        return print(f'\nWelcome, {self.player_name}!')
    
    def assign_no_of_rounds(self):
        no_of_rounds = int(input("\nHow many rounds would you like to play? "))
        
        while no_of_rounds <= 0:
            no_of_rounds = int(input("\nPlease enter 1 or more for number of rounds:  "))
        
        self.rounds = no_of_rounds
        return print(f'\nNice {self.rounds} rounds!')

    def player_option_evaluter(self):
        player_option = input(f'Please select one option ({self.options[0]}, {self.options[1]}, {self.options[2]}): ')
        while (self.options.count(player_option.lower())) <= 0 :
            player_option = input(f'Please select one of these options ({self.options[0]}, {self.options[1]}, {self.options[2]}): ')
        else:
            return player_option.lower()

    def score_board(self):
        if self.player_points > self.NPC_points:
            print('\nYOU WON!')
        elif self.player_points < self.NPC_points:
            print('\nNPC WON')
        else:
            print('\nDRAW!')
        print(f'\n______________________\n|SCORE BOARD:\n|Player Points: {self.player_points} \n|NPC Points: {self.NPC_points}\n______________________')

    def partial_results(self):
            print(f'\nPlayer chose: {self.player_option}')
            print(f'NPC chose: {self.NPC_option}')
            print(f'\nPlayer`score: {self.player_points}')
            print(f'NPC`score: {self.NPC_points}')
    
    def game_evaluater(self, player_op, npc_op):
        if ( (player_op == "rock" and npc_op == "scissor") or (player_op == "scissor" and npc_op == "paper") or (player_op == "paper" and npc_op == "rock") ):
            self.player_points += 1
        elif ( (player_op == "scissor" and npc_op == "rock") or (player_op == "paper" and npc_op == "scissor") or (player_op == "rock" and npc_op == "paper") ):
            self.NPC_points += 1
        else:
            pass
        
        self.partial_results()

    def rounds_phases(self):
        for i in range(self.rounds):
            print(f'\nRound {i + 1}')

            self.player_option = self.player_option_evaluter()
            self.NPC_option = random.choice(self.options)

            self.game_evaluater(self.player_option, self.NPC_option)


            if i == (self.rounds - 1):
                self.score_board()
                if input("Would like to play more? (yes/no) ") == 'yes':
                    self.player_points, self.NPC_points = 0 , 0
                    self.play()
                else:
                    print(f'\nHope you had fun, {self.player_name}!')

    def play(self):
        self.assign_no_of_rounds()
        self.rounds_phases()
