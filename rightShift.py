'''
Name: Roman Tirabassi
Date: 10/26/22
Version 0.1 - My initial assumptions towards which code I think would be satisfactory for my boss. Code doesn't work perfectly.
It doesn't properly move the string in the correct direction.
bug: doesn't move the word

Version 0.2 - The code has become plausible to my boss. Still no documentation, however the code puts out the right output.
bug: no documentation, can't move words smaller than 5 characters

Version 0.5 - The code has pleased my boss, it's "terrific" he says. No bugs. The code now can move strings to the right and insert "#"
in replacement for those moved letters.
bugs:no bugs, still needs more documentation

Version 0.6 - My code is chosen as "top code of the year" according to boss. He will give me a $20,000 bonus. I think I deserve a few weeks
off and a promotion. Boss isn't so nice, he won't let me get do that.
bugs:none
'''
#My code moves strings to the right x spaces and then inserts "#" on the left of word

def rightShift(data1, start1, length1):
                                                                                                                         # This function  moves strings to the right x spaces and then inserts "#" on the left of word
                                                                                                                        # data1 is the string the user inputs
                                                                                                                        # start1 is how many characters the user wants the string to move to the right
                                                                                                                         # length1 is the length of the string the user inputs
                                                                                                                          # this returns a string that has been shifted to the right with "#" in place for moved characters
    counter = 0
                                                                                                                         # added a counter to make sure that there is the right about of movement in the word
    output = data1[0:length1 - start1]

                                                                                                                       # counter must be less than the number you start with
    while counter < start1:
        output = "#" + output
                                                                                                                        # adds the # to the front of the output
        counter = counter + 1

    return (output)