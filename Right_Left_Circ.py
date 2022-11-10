"""
Andrew Thompson
Created on October, 15 ,2022
version 0.1, a version that only worked for the word computer
        bugs: only works for one world
Version 1.0, adjusted code to work for all words
        bugs: no documentation
version 1.2, added documentation
        bugs: none
LeftCirc: takes the input 'start1' and counts that number down the variable 'data1' then moves that selected part to the
end of the word ex. computer, 3 = putercom
RightCirc: counts the integer amount of Start1 from the back of the word and moves it to the front
ex. computer, 3 = tercompu
Bonus: none
@author: AThompson23
"""



def leftCirc(data1, start1):
                                                                                                                        # function takes inputs data1 and start1 and returns string
                                                                                                                        # data1 - the word that's being edited
                                                                                                                        # start1 - the number that tells how far form the beginning to split data!
                                                                                                                        # returns - string, which is the new word after being edited
    string = data1[start1:] + data1[0:start1]                                                                           # puts the end of the word in front of the beginning, how much of the
                                                                                                                        # beginning is determined by start1
    return string


def rightCirc(data1, start1, length1):
                                                                                                                        # function takes inputs data1 and start1 and returns string
                                                                                                                        # data1 - the word that's being edited
                                                                                                                        # start1 - the number that tells oyu far from the end of the word to slip data1
                                                                                                                        # length1 - tells you how long the data1 is
                                                                                                                        # returns - string, which is the new word after being edited
    length1 = length1 - 1
    string = data1[-start1:] + data1[:(length1 - start1 + 1)]                                                           # puts the beginning of the word in the, how much of the
                                                                                                                        # end is moved is determined by the length of the word - start1
    return string