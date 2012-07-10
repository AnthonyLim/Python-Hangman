#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Anthony.Lim
#
# Created:     05/07/2012
# Copyright:   (c) Anthony.Lim 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from game import hangman
import sys

def main():
    hm = hangman()
    word = hm.get_word()
    tries = hm.tries_left()

    while not hm.is_completed():

        print hm.get_board()
        print " ".join(list(hm.get_masked()))
        print 'Guess the word, enter a letter'
        letter = raw_input().lower().strip()

        if len(letter)>1:
            print 'One letter at a time!'
        elif len(letter)<1:
            print 'One letter is required'
        else:
            if hm.try_letter(letter):
                pass
            else:
                pass

        if hm.is_failed():
            print 'You lose! The word is %s' % word
            hm.play_again(main,sys.exit)

        if hm.is_completed():
            print 'Congratiolations! You\'ve guess the word!'
            hm.play_again(main,sys.exit)

if __name__ == '__main__':
    main()
