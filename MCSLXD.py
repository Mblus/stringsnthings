'''
Name: Gavin Haroche
Date: 10/26/22

Version 0.1 - able to find the highlighted section
bug: nothing besides that is working

Version 0.2 - able to find the highlighted section, the first half, and the last half.
bug: no documentation, nothing working besides said functions

Version 0.5 - coded the main action of the function
bug: no documentation, not put together

Version 0.6 - code pieced together to get an output, added documentation.
bugs:none
'''
#What it does: This function flips and transports a piece of a highlighted section to the left or right, based off of parameters.
#What the function takes in:
#data1, the data that is being altered,
#Start1, where to begin the selection for the string.
#length1, how many times it should count up from the start in order to find a highlighted section
#direction1, The direction where the sub highlighted section gets moved.
#x1, the ammount of the subsection that will be shifted in a direction

def McSLXD(data1, start1, length1, direction1, x1):

    start1 = start1 - 1
    data1 = ([*data1])  #split
    remainingPiece = len(data1[0:start1]) + len(data1[start1:start1 + length1])                                         #finding the remaining piece after the highlighted section
    highlightedSection = data1[start1:start1 + length1]                                                                 #finding the hightlighted section

    if direction1 == "R":

        tempsection = highlightedSection[len(highlightedSection) - x1:len(highlightedSection)]                          #splitting the highlighted section into pieces that are being swapped

        firstsection = highlightedSection[0:len(highlightedSection) - x1]                                               #splitting the highlighted section into pieces that are being swapped
        newstring = tempsection + firstsection
        output = ''.join(data1[0:start1]) + ''.join(newstring) + ''.join(data1[remainingPiece:len(data1)])              #getting the final output
    elif direction1 == "L":
        tempsection = highlightedSection[0:x1]
        firstsection = highlightedSection[x1:len(highlightedSection)]                                                   #repeating all of the same steps from the function above except for the order of the first section and the temp section
        finalsection = firstsection + tempsection
        firstsection = data1[0:start1]
        tempsection = data1[start1 + length1:len(data1)]
        output = ''.join(firstsection) + ''.join(finalsection) + ''.join(tempsection)

    return output
