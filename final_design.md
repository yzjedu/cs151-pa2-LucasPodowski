# Final Design Document
#### PLEASE! PLEASE! PLEASE! Complete all the NOs in the feedback document 

1. Display the rules and purpose of the game
2. set loss counters for player1, player2 and computer to 0
3. while play again is true
   1. While input is not valid
      1. try Prompting  for number of sticks between 10-100
         1. if between 10-100 
            1. end the while loop
         2. otherwise 
            1. output the number is invalid
      2. except a valueError 
         1. output an invalid message
   2. set the current player to 1
   3. while sticks > 0
      1. output the number of sticks
      2. if the current player is 1
         1. try 
            1. prompt player 1 to input number of sticks
            2. if choice is 1-3 
               1. end the while loop
            3. otherwise  
               1. output the number is invalid
         2. except a value_error
            1. output an invalid message
      3. otherwise if current player is 2
         1. try 
            1. prompt player 2 to input number of sticks
            2. if choice is 1-3 
               1. return choice
            3. otherwise  
               1. output the number is invalid
               2. except a value_error
      4. otherwise
         1. make choice a random integer including 1 - 3
         2. output how many sticks the computer chose
      5. subtract choice from sticks
      6. check if sticks <= 0
         1. check the current player and add one loss to the current player
            1. output which player lost
            2. break the loop
      7. set current player = (current player % 3) + 1
   4. Ask if the player wants to play again
   5. if play again != 'yes'
      1. end the while loop
   6. Output the overall loss statistics for each player
   