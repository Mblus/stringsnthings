"""
Andrew Thompson
Created on October, 15 ,2022
version 0.1, a version that only worked for the word computer
        bugs: only works for one world
Version 1.0, adjusted code to work for all words
        bugs: no documentation
version 1.2, added documentation
        bugs: none
the function selects from Start1 to RunNumber and then reverses that selected location but keeps it in the location in
the world
Bonus: none
@author: AThompson23
"""

                                                                                                                        #Data1 is the string that is being reversed
                                                                                                                        #RunNumber1 is used to find the size of the section being reversed, after finding the start
                                                                                                                        #Start1 is telling the computer where to start reversing from
def reverseString(data1, runNumber1, start1):                                                                             # takes inputs from Data1, runNumber1, start1.
    data2=data1
    start2=start1

    temp_list = list(data2[(int(start2)-1):(int(start2)+(int(runNumber1)-1))])                                          #temp_list is the selected part of the
                                                                                                                         # word that will be reversed
    temp_list.reverse()                                                                                                  # reverses the selected part of the word
    final = ((data2[:(int(start2-1))]) + ''.join(temp_list) + (data2[(int(start2) + int(runNumber1)-1):]))
                                                                                                                        # puts the reversed section back into word wherever it belongs adn returns the new word to main
    return final