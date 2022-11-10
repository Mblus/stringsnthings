"""
Leonardo Corsano
Created on October, 15 ,2022
version 0.1, works for the word computer
        bugs: needs other words
Version 1.0, adjusted code to work for all words
        bugs: no documentation
version 1.2, added documentation
        bugs: none
the function moves a string to the left a certain ammount of times, and adds empty space indicators to the remaining side ("#")
"""


def leftShift(data1, start1, length1):#                                                                                 takes in data from data 1, the start of the shift, and the length of the string

    count = 0                                                                                                           #main counter for the loop
    times = start1                                                                                                      #setting start1 to times, times will be used as how many times i shift it.
    output = data1[times:length1]                                                                                       #moving it over a certain ammount of times

    while count < times:
        output = output + '#'                                                                                           #adding hashtags to the left side
        count = count + 1


    return output
