#-------------------------------------------------------------------------------
# Name:        hangman
# Purpose:
#
# Author:      Anthony.Lim
#
# Created:     05/07/2012
# Copyright:   (c) Anthony.Lim 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random

class hangman(object):

    def __init__(self):
        words = file('extras/dictionary.txt','r').readlines()
        rnd = random.randint(0,len(words)-1)
        self.__secretword = words[rnd].upper().strip()
        self.__correctletters = []
        self.__wrongletters = []
        self.HANGMANPICS = ['''

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

    def tries_left(self):
        tries = len(self.HANGMANPICS) - len(self.__wrongletters)
        if tries < 0:
            return 0
        else:
            return tries

    def get_word(self):
        return self.__secretword

    def try_letter(self,letter):
        letter = letter.upper()
        if letter in self.__secretword:
            if letter not in self.__correctletters:
                self.__correctletters.append(letter)
            return True
        else:
            if letter not in self.__wrongletters:
                self.__wrongletters.append(letter)
            return False

    def get_masked(self):
        hide = self.__secretword
        for i in self.__secretword:
            if i not in self.__correctletters:
                hide = hide.replace(i,'_')
        return hide

    def get_board(self):
        cnt = len(self.__wrongletters)
        return self.HANGMANPICS[cnt]

    def is_completed(self):
        return '_' not in self.get_masked()

    def is_failed(self):
        return len(self.__wrongletters) >= len(self.HANGMANPICS)

    def play_again(self,go,no):
        print 'Do you want to play again? (yes/NO)'
        todo = raw_input().lower().startswith('y')
        if todo:
            go()
        else:
            no()
        return todo