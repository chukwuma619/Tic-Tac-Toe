# Tic-Tac-Toe
This is a text based Tic-Tac-Toe game i built from scratch

it's a two user(human - human) text based game where the user is instructed to play by passing in the index i.e

Rules: Kind use the numbers in the demo to tick a box

            (0 0) | (0 1) | (0 2)
            --------------------
            (1 0) | (1 1) | (1 2)
            -------------------- 
            (2 0) | (2 1) | (2 2)
            
each of this box contain the index number required to in insert either a "X" or "O" into it
that is

Note: insert number without the "(", ")" or anything other that 0, 1, 2 eg

>>> Player {x} turn: 0 0
>>>
               X  | (0 1) | (0 2)
            --------------------
            (1 0) | (1 1) | (1 2)
            -------------------- 
            (2 0) | (2 1) | (2 2)
            

            
each player takes turn till any condition ment for winning is achieved, else it will return a "Its a draw" if there are no available spaces left
