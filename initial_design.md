# Initial Design Document
#### PLEASE! PLEASE! PLEASE! READ the [README.md](README.md) File carefully

1. Display the rules and purpose of the game
2. make a function to find number of sticks
   1. While input is not valid
      1. try Prompting  for number of sticks between 10-100
         1. if between 10-100 return sticks
         2. otherwise output the number is invalid
      2. except a valueError 
         1. output an invalid message
3. make a function to get the players number of sticks
   1. while true
      1. try 
         1. prompt user to input number of sticks
         2. if choice is 1-3 return choice
         3. otherwise  output the number is invalid
      2. except a valueError
4. make a function for the computers choice
   1. make their choice a random integer including 1 - 3
   2. output how many sticks the computer chose
   3. return their choice
5. make a function for the main game 
   1. set loss counters for player1, player2 and computer to 0
   2. while true
      1. get sticks from initial sticks
      2. set the current player to 1
      3. while sticks > 0
         1. output the number of sticks
         2. if the current player is 1
            1. run the  get players number of sticks stored as choice
         3. otherwise if current player is 2
            1. Run the  get players number of sticks stored as choice
         4. otherwise
            1. run the computer choice function stored as choice
         5. subtract choice from sticks
         6. check if sticks <= 0
            1. check the current player and add one loss to the current player
               1. output which player lost
               2. break the loop
         7. set current player = (current player % 3) + 1
      4. Ask if the player wants to play again
      5. if play agin is not 'yes'
         1. break the loop
   3. output the overall loss statistics for each player
6. initialize the main game function
   