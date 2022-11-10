
'''
Name: Gavin Haroche
Date: 10/26/22
Version 0.1 - split the function by its "-"
bugs: Does not work, not documented, data not properly formatted for the functions
Version 0.2 - Split the function by its "/"
bugs: Does not work, not documented, data not properly formatted for the functions
Version 0.5 - Data parameters now match their respective variables.
bugs: Does not work, not documented.
Version 0.6 - added functions to the main
bugs:Not documented, data does not work of mc and Rev
Verision 1.0 - Functions all work except for REV and MC
bugs: Not documented,
Version 1.0.1 - Added specific parameters for REV and MC
bugs: Not documented,
Version 1.1  - Code now works, fixed bugs
bugs: Not documented,
Current version 1.2 - Added documentation and imported functions from seperate files.
Not documented.


'''
finalLoop = 0                                                                                                            #main loop
from MCSLXD import *                   #importing everyone's functions
from leftShift import *
from Right_Left_Circ import *
from rightShift import *
from reverseString import *
#-----------MAIN------------#
while finalLoop < 5:
    dictionary = {}                                                                                                     #creates a dictionary so I can create variables on the fly
    data = input("enter the data")
    data = data.replace("/", " " )
    data = data.split()                                                                                                  #turns x-n/str to x-n, str
    x = 0                                                                                                                 #loop variable that helps find the ammount of data entered
    y = 0                                                                                                                #   variable that hosts the main loop where all the fucntions are implimented
    functions = (data[0:len(data) - 1])                                                                                  #finding the ammount of datapieces to run.

    for length in functions:
        dictionary["function{0}".format(x)] = length                                                                      #creating variables for each datapiece.
        x = x +1

    x = len(data) - 2
    data1 = data[len(data) - 1]                                                                                          #fixing variables.
    length1 = len(data1)


    while x >= y:
        function = dictionary["function" + str(y)]                                                                      #creating variables for each datapiece.
        function = function.replace("-", " ")                                                                           #turns LS-2 to LS, 2
        function = function.split()
        start1 = function[1]                                                                                            #the start variable is being found
        try:
            start1 = int(start1)                                                                                        #some parapeters consist of R to indicate right, and this is to identify those functions and allow them to pass.
        except:
            start1=start1


        if function[0] == "MC":
            lst = []                                                                                                    #splitting the conjoined parameter, this one would have R or L in it, so it skipped its integer conversion above, and is now being prepared for that function
            lst.extend(str(start1))
            start1 = int(lst[0])
            length1 = int(lst[1])                                                                                        #setting all of the variables for that specific function
            x1 = int(lst[2])
            direction1 = lst[3]
            data1=McSLXD(data1, start1, length1, direction1, x1)

        if function[0] == "REV":
            start1 = list(str(start1))
            runNumber1 = int(start1[1])                                                                                 #also requires special treatment because it has two pieces of parameter data.
            start1= int(start1[0])
            data1 = reverseString(data1, runNumber1, start1)

                                                                                                                        #everything else does not require any special treatment and can go straight to the functions
        if function[0] == "RC":
            data1 = rightCirc(data1, start1, length1)

        if function[0] == "LC":
            data1 = leftCirc(data1, start1)

        if function[0] == "RS":
            data1 = rightShift(data1, start1, length1)

        if function[0] == "LS":
            data1 = leftShift(data1, start1, length1)
        y = y + 1

    print(data1) #output
    finalLoop += 1



