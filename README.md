# jogo-forca-hangman-game
Second project of the course "Python for Data Analysis" from DSA Academy. 

The code was implemented using the random, unidcode and the libraries. The code shown by the course instructor uses only the Random library.

This code implements a python gallows game. The user can play several times until they decide to leave. The purpose of the game is to guess a word chosen randomly from the "palavras.txt" file. The player has three lives and can type one letter at a time to try to guess the word. If the letter is correct, it is revealed in the hidden word. Otherwise, the player loses a life and the wrong letter is displayed. The game continues until all letters are revealed or the player loses all their lives.

Code Summary:

     The "lista_palavras" function reads a word file and returns a list of these words.
     The "limparTela" function cleans the console screen, depending on the operating system.
     The "inGame" function starts the gallows game.
         It displays a welcome message and chooses a random word from the word file.
         It initializes the word hidden with underScores (_) in place of letters.
         Enter a loop until the player wins or loses.
             Displays the hidden word, the remaining lives and the wrong letters typed.
             The player types a letter.
             If the letter is correct, it is revealed in the hidden word.
             If the letter is wrong, the player loses a life and the letter is added to the wrong letters.
             Check if all letters were revealed in the hidden word.
                 If so, it displays a victory message and closes the game.
                 If not, the game continues.
         If the player does not reveal all letters and run out of lives, he displays a message of defeat.
     The main part of the code verifies if it is being executed as a main program.
         Starts a loop to play again or leave.
         Calls the "ingame" function.
         Ask the player if he wants to play again or leave.
         If the player chooses to play again, clean the screen and restart the game.
         If the player chooses to leave, clean the screen and display a closing message.

To run the game, make sure you have a word file called "palavras.txt" and run the code. The game will start and you can play until you decide to leave.
