#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Anthony.Lim
#
# Created:     04/07/2012
# Copyright:   (c) Anthony.Lim 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random

HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

class hangman(object):
    '''
    define the hangman class-wide variables
    '''
    def __init__(self):
        words = file('extras/dictionary.txt','r').readlines()
        rndNum = random.randint(0,len(words)-1)
        self.__NAME__ ='''
                        =============
                        H A N G M A N
                        =============
        '''
        self.__word = words[rndNum].strip().upper()
        self.__wordsTried = []
        self.mask_hidden()

    '''
    returns the list of correct letters tried
    '''
    def get_letters_tried(self):
        return self.__wordsTried

    '''
    puts a mask on the letters that has not been guessed yet and returns the current object
    '''
    def mask_hidden(self):
        self.__hidden = self.__word
        for letter in self.__word:
            if not letter in self.__wordsTried:
                #print letter
                self.__hidden = self.__hidden.replace(letter,'_')
                #self.__hidden = self.__word.replace(letter,'_')
        return self

    '''
    returns the word to be guessed
    '''
    def get_word(self):
        return self.__word

    '''
    OVERRIDDEN. returns the name of the game
    '''
    def __unicode__(self):
        return self.__NAME__

    '''
    returns the masked word
    '''
    def get_hidden_word(self):
        return " ".join(list(self.mask_hidden().__hidden))

    '''
    checkes the input letter then returns boolean if letter exists
    '''
    def update_word(self,letter):

        if letter in self.__wordsTried:
            return True
        else:
            self.__wordsTried.append(letter)

        return letter in self.__word

    '''
    checks if the word is completed/guessed
    '''
    def is_completed(self):
        return not '_' in self.__hidden

def main(points):
    HM = hangman()
    word = HM.get_word()
    print HM.__unicode__()

    tabs = "\t\t"
    #print word
    print tabs+HM.get_hidden_word()+"\n\r"
    iTries = 0
    maxTries = len(HANGMANPICS)
    print tabs+'You have %d points' % points
    print tabs+'Enter a letter to guess the word.'
    print tabs+'You have %d valid tries to guess' % maxTries
    while not HM.is_completed():
        letter = raw_input().upper()

        if len(letter) > 1:
            print tabs+"One letter at a time!"
        elif len(letter) == 0:
            print tabs+"Input is required."
        else:
            if HM.update_word(letter):
                pass
            else:
                print iTries
                print HANGMANPICS[iTries]
                iTries += 1

        #print tabs+'You have %d tries left' %(len(HANGMANPICS)-iTries)
        print tabs+HM.get_hidden_word()
        #print HM.get_words_tried()

        if iTries >= maxTries:
            break

    if HM.is_completed():
        print tabs+'Congratiolations! You guessed the word! You should try again.'
        points += 1
        main(points)
    else:
        print tabs+'Sorry, you lose! The word is %s' % word
        print tabs+'Try again'
        main(points)

if __name__ == '__main__':
    main(0)
