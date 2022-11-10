#Gavin Haroche, 9/27/21
#Rust removal project.
#project description ---- In the rust removal project, I was tasked to create a sorting algorithm with imaginary boxes.

#bonuses ---- Error proof (can return specific messages for scenario, but i need to only output unmailable) , tackling an alternate library (decimal), Clean and easily readable formatted code.
#        ---- Formatting proof, if the user inputs no spaces between the commas, no commas, or the given format, it will always be able to read it
#        ----- Little main usae, many functions. (clean main)

#version 1.0. Sorting method working, missing certain inclusivities, user debug statements missing (User.Debug.S = personalized error messages)
#version 1.0.1. Sorting method broken, inclusives fixed, user debug statements added.
#version 2.0 Sorting method fixed, removed excessive data printing (only prints output)
# version 2.1 added documentation and cleaned up formatting, code should be good, and look good, like fancy food.
# current version 2.5 fixed inputs to meet the expectations of my "colledge computer science teacher", changed certain documentation, re-arranged code for box classifying, now applies to the rule:
#                                                                                                                           "if incorrect data is entered, the data is re-entered from the beginning"



#-    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -

import decimal #importing the decimal built in library

#_______________________________________________________________________________________________________________________
bigloop = 0                     #global variable for the main loop,
dec = decimal.Decimal                    #to be able to do math with the decimal library, all basic numbers have to be turned into a decimal



#_______________________________________________________________________________________________________________________
#removing the commas from the input
def Remove_The_Commas(data):# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    counter3 = 0 #Setting the loop
    while counter3 <= 4:
        data = data.replace(",", " ") #replacing the commas with spaces so it can read any input

        counter3 = counter3 + 1

    return data




#_______________________________________________________________________________________________________________________
#is the function an integer or a string?
def Is_It_An_Int(data):# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    counter2 = 0              #loop counter
    try:                      #trning everything into a decimal

        while counter2 < 5:              #converting everything
            data[counter2] = decimal.Decimal(data[counter2])
            counter2 = counter2 + 1

    except:
        data = False               #sending data as false so the main can restart the process
        print("UNMAILABLE")

    return data                    #




#_______________________________________________________________________________________________________________________
#classifying the box based off of inputs
def Clasify_The_Box(data):# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#Currently, data has been split, it has been converted to a decimal, verified length, and verified integers.

    #___________________________________________________________________________________________________________________
    Reset_Indicator = False                       #reset indicator is a checker intended so that it will tell the main to restart the program if it becomes true
    conditional = data[0] + data[0] + data[2] + data[2] + data[1]+ data[1]
    # __________________________________________________________________________________________________________________
    # PACKAGE: Use package class when the item exceeds any of the rules for large envelope and
    # when the length plus the distance around the other sides of a package equals 84 inches or less. double the length double the thickness
    if data[0] > dec("24") or \
        data[1] > dec("18") or \
        data[2] > dec("0.5"):

        if conditional <= dec("84"):
            Envelope_Cost = 2.95
            Additional_Small_Envelope_Cost = 0.25
                                                   #the package conditionals and the large package conditionals are best put together because they both have/ are nested if statements
                                                        #including the conditional comparison in the main if would be read as ....this or this or (this and this), and not this or this or this, and this
        elif conditional > dec("84") and conditional < dec("130"):    #LARGE PACKAGE: Use large package class when the length plus the distance around the other
                                                                                  #   sides of a package is more than 84 inches but is not more than 130 inches.
            Envelope_Cost = 3.95
            Additional_Small_Envelope_Cost = 0.35

        else:                                    #if it dips into the package conditional, it is either a package, a large package, or unmailable, problem is, it is like this because once it goes into the package conditional
                                                # it will never read the else statements at the end, so this is one of the many solutions to this problem
            Envelope_Cost = 0
            Additional_Small_Envelope_Cost = 0
            Reset_Indicator = "True"
            print("UNMAILABLE")
    # __________________________________________________________________________________________________________________
    # Regular post card: The length must be between 3.5 and 4.25 inches, inclusive. The
    # height must be between 3.5 and 6 inches, inclusive. The thickness must be between .007
    # and .016 inches,:
    elif data[0] >= dec("3.5") and data[0] <= dec('4.5') and \
        data[1] >= dec("3.5") and data[1] <= dec("6") and \
        data[2] >= dec("0.007") and data[2] <=dec("0.016"):
        Envelope_Cost = 0.20                     #the envelopecosts are the basic money cost
        Additional_Small_Envelope_Cost = 0.03             #the additional small envelope costs are the tiny taxes that get multiplied by distance between the zipcodes
    #___________________________________________________________________________________________________________________
    # LARGE POST CARD: The length must be between 4.25 and 6 inches. The height must be
    # between 6 and 11.5 inches. The thickness must be between .007 and .015 inches, inclusive
    elif data[0] > dec("4.25") and data[0] < dec('6') and \
        data[1] > dec("6") and data[1] < dec("11.5") and \
        data[2] >= dec("0.007") and data[2] <= dec("0.015"):
        Envelope_Cost = 0.37
        Additional_Small_Envelope_Cost = 0.03
    #___________________________________________________________________________________________________________________
    # ENVELOPE: The length must be between 3.5 and 6.125 inches, inclusive. The height must be
    # between 5 and 11.5 inches, inclusive. The thickness must be between .016 and .25 inches.
    elif data[0] >= dec("3.5") and data[0] <= dec('6.125') and \
        data[1] >= dec("5") and data[1] <= dec("11.5") and \
        data[2] > dec("0.016") and data[2] <dec("0.25"):
        Envelope_Cost = 0.37
        Additional_Small_Envelope_Cost = 0.04
    #___________________________________________________________________________________________________________________
    # LARGE ENVELOPE: The length must be between 6.125 inches and 24 inches. The height must
    # be between 11 and 18 inches, inclusive. The thickness must be between .25 and .5 inches,
    # inclusive.
    elif data[0] > dec("6.125") and data[0] < dec('24') and \
        data[1] >= dec("11") and data[1] <= dec("18") and \
        data[2] >= dec("0.25") and data[2] <=dec("0.5"):
        Envelope_Cost = 0.60
        Additional_Small_Envelope_Cost = 0.05
    #___________________________________________________________________________________________________________________
    #___________________________________________________________________________________________________________________
    else:
        print("UNMAILABLE")#if it meets zero expectations
        Envelope_Cost = 0 #i need to keep these values, even if they are zero, because if i dont define them, the function will be returning
                        #something that does not exist, I can do this by keeping the variables global, or by putting them in the else statement.
        Additional_Small_Envelope_Cost = 0
        Reset_Indicator = "True"
    #___________________________________________________________________________________________________________________
    #___________________________________________________________________________________________________________________




    # __________________________________________________________________________________________________________________
    return dec(Envelope_Cost), dec(Additional_Small_Envelope_Cost), Reset_Indicator #Returning the values means refrencing the variables being returned in a variable state or print statement
                                                                                #Returning 2 different values will cause them to be put together in an array.




#_______________________________________________________________________________________________________________________
#checking for bad length
def Is_It_Too_Short_Or_Long(data):# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # __________________________________________________________________________________________________________________
    if len(data) < 5 or len(data) > 5: #if the length of the data is underboard or overboard.
        print("UNMAILABLE")
        reset = True #dont reset
    else:
        reset = False #do reset
    # __________________________________________________________________________________________________________________

    return reset #returning a single value




#_______________________________________________________________________________________________________________________
#finding the zone difference number
def Find_The_Zone(data):# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    Reset_Indicator_2 = False #indicator to return a reset
    Zone_Math_Data = "" #adding the zonedata to a list
    zonedata = "" #determining zondata
    twoloop = 0 #loop making sure that it runs through both zipcodes, I did this instead of having to do 2 sets of conditionals
    whichone = data[3]#whichone is a variable that holds zipcode one and switches to zipcode 2, after collecting the data from zipcode one
    zonefinal = 0 #the distance beween the zones calculated (final number)

    while twoloop < 2:

        if whichone >= dec("00001") and whichone <= dec("06999"):#all conditionals inclusive

            zonedata = dec("1")
        elif whichone >= dec("07000") and whichone <= dec("19999"):

            zonedata = dec("2")
        elif whichone >= dec("20000") and whichone <= dec("35999"):

            zonedata = dec("3")
        elif whichone >= dec("36000") and whichone <= dec("62999"):

            zonedata = dec("4")
        elif whichone >= dec("63000") and whichone <= dec("84999"):

            zonedata = dec("5")
        elif whichone >= dec("85000") and whichone <= dec("99999"):

            zonedata = dec("6")
        else:
            Reset_Indicator_2 = True #if resetindicator 2 its true, it means an improper zipcode was entered, then it resets itself in the main


        if Reset_Indicator_2 == False:  #continue normally
            whichone = data[4]#Switching the item that goes through the cionditionals

            Zone_Math_Data = str(Zone_Math_Data) + " " + str(zonedata)#adding everything to an item called zonemathdata

            if twoloop == 1:#at the end of the loop, once you have 2 pieces of data

                Zone_Math_Data = Zone_Math_Data.split() #split the data

                zonefinal = dec(Zone_Math_Data[1]) - dec(Zone_Math_Data[0]) #subtract the datas


                if zonefinal < 0:#if it is a negative, do some math to switch it to a positive


                    zonefinal = zonefinal * dec("-1")


        twoloop = twoloop + 1


    return zonefinal, Reset_Indicator_2




#_______________________________________________________________________________________________________________________
#finding the end cost
def Find_The_Final_Cost(boxval, zoneval):
    costfinal = boxval[1] * zoneval[0]#multiply the small additional cost by the number of zones crossed
    costfinal = costfinal + boxval[0]#then add the big cost
    costfinal = round(costfinal, 2) #round the answer

    if costfinal <= dec("0.99"):#if there is a zero in front of the decimal
        costfinal = str(costfinal)#turn to string
        costfinal = [*costfinal]#break it up into a list (each individual piece)
        costfinal[0] = ""#replace the zero in front with nothing
        costfinal = "".join(costfinal) #put it back together
        print(costfinal)
    else:
        print(costfinal)
    return costfinal




#_______________________________________________________________________________________________________________________
# M A I N---- M A I N---- M A I N---- M A I N---- M A I N---- M A I N---- M A I N---- M A I N---- M A I N---- M A I N---
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
# M A I N---- M A I N---- M A I N---- M A I N---- M A I N---- M A I N---- M A I N---- M A I N---- M A I N---- M A I N---

while bigloop < 5: #first global variable
#_______________________________________________________________________________________________________________________
    data = input("please enter the data:\n")                    #plain input.
#_______________________________________________________________________________________________________________________
    data = Remove_The_Commas(data)                        #calling the function that removes the commas from the data.
#_______________________________________________________________________________________________________________________
    data = data.split()                                  #now that the commas are removed, split the data.
#_______________________________________________________________________________________________________________________
    if Is_It_Too_Short_Or_Long(data) == True:                    #Calling the function that determines length of the data.
        continue #return to top
#_______________________________________________________________________________________________________________________

    data = Is_It_An_Int(data)                  #calling the funtion that converts the user input to decimal datatype.

    if data == False:                    #if it fails, it will cause an error.
        continue
#_______________________________________________________________________________________________________________________
    boxval = Clasify_The_Box(data)                        #classifying the box into its respective datatype

    if boxval[2] == "True": #
        continue
#_______________________________________________________________________________________________________________________
    zoneval = Find_The_Zone(data)                     #getting the zone number

    if zoneval[1] == True:                  #declaring the zipcode unreadable
        print("UNMAILABLE")
        continue
    Find_The_Final_Cost(boxval, zoneval)                   #calculating the final cost of the data
#_______________________________________________________________________________________________________________________
    bigloop += 1               #only repeat 5 times, including all inputs on the instructions


#fix variables, camel case, underscores, spelling
#more documentation