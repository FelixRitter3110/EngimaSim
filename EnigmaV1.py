from random import randrange
import random
import numpy as np
import sys

# Set whether you want enigma to set all variables randomly or whether you want to input them yourself
random_selection = False

if not random_selection:
    # [1-5] can't use the same rotor twice
    rot1 = 1
    rot2 = 5
    rot3 = 3

    # [0-25]
    rotor1_pos = 18
    rotor2_pos = 21
    rotor3_pos = 5

    # Each plug pair must fill both letters. Don't use same letter twice
    Plugs = np.array([["p", "s"], ["w", "l"], ["m", "o"], ["j", "i"], ["d", "n"]])

    # [["a", "b"], ["c", "d"], ["e", "f"], ["g", "h"], ["i", "j"], ["k", "l"], ["m", "n"], ["o", "p"], ["q", "r"], ["s", "t"]]

else:
    # Random selection of variables
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]

    # Random rotor position
    rotor1_pos = randrange(0, 26)
    rotor2_pos = randrange(0, 26)
    rotor3_pos = randrange(0, 26)

    # Random rotors used
    rot1, rot2, rot3 = random.sample(range(1, 6), 3)

    # Random amount and pairs of Plugs
    num_plugs = randrange(0, 11)
    Plugs = np.empty((0, 2), int)
    for i in range(num_plugs):
        random_num = randrange(len(alphabet)) - 1
        PlugA = alphabet[random_num]
        alphabet.remove(PlugA)

        random_num = randrange(len(alphabet)) - 1
        PlugB = alphabet[random_num]
        alphabet.remove(PlugB)
        Plugs = np.append(Plugs, np.array([[PlugA, PlugB]]), axis=0)

# Error Handling
if rot1 == rot2 or rot1 == rot3 or rot1 == rot2 or 1 >= rot1 >= 5 or 1 >= rot2 >= 5 or 1 >= rot3 >= 5:
    sys.exit("Please choose 3 different rotors between 1-5")
if 0 <= rotor1_pos <= 25 or 0 <= rotor2_pos <= 25 or 0 <= rotor3_pos <= 25:
    sys.exit("Rotor Positions can only be between 0-25")
if len(Plugs) >= 11:
    sys.exit("There can only be 11 Plugs connected")

print("Positions and choice of Rotors:")
print("Rotor 1 = " + str(rot1) + " Position = " + str(rotor1_pos))
print("Rotor 2 = " + str(rot2) + " Position = " + str(rotor2_pos))
print("Rotor 3 = " + str(rot3) + " Position = " + str(rotor3_pos))

print("Plug connections:")
print(Plugs)

# Wiring for all rotors
Rotor1_wiring = [[0, 15], [1, 4], [2, 25], [3, 20], [4, 14], [5, 7], [6, 23], [7, 18], [8, 2], [9, 21], [10, 5],
                 [11, 12], [12, 19], [13, 1], [14, 6], [15, 11], [16, 17], [17, 8], [18, 13], [19, 16], [20, 9],
                 [21, 22], [22, 0], [23, 24], [24, 3], [25, 10]]
Rotor2_wiring = [[0, 25], [1, 14], [2, 20], [3, 4], [4, 18], [5, 24], [6, 3], [7, 10], [8, 5], [9, 22], [10, 15],
                 [11, 2], [12, 8], [13, 16], [14, 23], [15, 7], [16, 12], [17, 21], [18, 1], [19, 11], [20, 6],
                 [21, 13], [22, 9], [23, 17], [24, 0], [25, 19]]
Rotor3_wiring = [[0, 4], [1, 7], [2, 17], [3, 21], [4, 23], [5, 6], [6, 0], [7, 14], [8, 1], [9, 16], [10, 20],
                 [11, 18], [12, 8], [13, 12], [14, 25], [15, 5], [16, 11], [17, 24], [18, 13], [19, 22], [20, 10],
                 [21, 19], [22, 15], [23, 3], [24, 9], [25, 2]]
Rotor4_wiring = [[0, 8], [1, 12], [2, 4], [3, 19], [4, 2], [5, 6], [6, 5], [7, 17], [8, 0], [9, 24], [10, 18], [11, 16],
                 [12, 1], [13, 25], [14, 23], [15, 22], [16, 11], [17, 7], [18, 10], [19, 3], [20, 21], [21, 20],
                 [22, 15], [23, 14], [24, 9], [25, 13]]
Rotor5_wiring = [[0, 16], [1, 22], [2, 4], [3, 17], [4, 19], [5, 25], [6, 20], [7, 8], [8, 14], [9, 0], [10, 18],
                 [11, 3], [12, 5], [13, 6], [14, 7], [15, 9], [16, 10], [17, 15], [18, 24], [19, 23], [20, 2], [21, 21],
                 [22, 1], [23, 13], [24, 12], [25, 11]]
reflector_wiring = [[0, 21], [1, 10], [2, 22], [3, 17], [4, 6], [5, 8], [6, 4], [7, 19], [8, 5], [9, 25], [10, 1],
                    [11, 20], [12, 18], [13, 15], [14, 16], [15, 13], [16, 14], [17, 3], [18, 12], [19, 7], [20, 11],
                    [21, 0], [22, 2], [23, 24], [24, 23], [25, 9]]

New_Plugs = [[0 for x in range(2)] for y in range(len(Plugs))]

# Transforms letters of Plugs into Numbers
if len(Plugs) != 0:
    for i in range(len(Plugs)):
        New_Plugs[i][0] = (ord(Plugs[i][0]) - 97)
        New_Plugs[i][1] = (ord(Plugs[i][1]) - 97)


# Gives each rotor their correct wiring
def rot_allocation(rot1, rot2, rot3):
    if rot1 == 1:
        rotor1 = Rotor1_wiring
    elif rot1 == 2:
        rotor1 = Rotor2_wiring
    elif rot1 == 3:
        rotor1 = Rotor3_wiring
    elif rot1 == 4:
        rotor1 = Rotor4_wiring
    else:
        rotor1 = Rotor5_wiring

    if rot2 == 1:
        rotor2 = Rotor1_wiring
    elif rot2 == 2:
        rotor2 = Rotor2_wiring
    elif rot2 == 3:
        rotor2 = Rotor3_wiring
    elif rot2 == 4:
        rotor2 = Rotor4_wiring
    else:
        rotor2 = Rotor5_wiring

    if rot3 == 1:
        rotor3 = Rotor1_wiring
    elif rot3 == 2:
        rotor3 = Rotor2_wiring
    elif rot3 == 3:
        rotor3 = Rotor3_wiring
    elif rot3 == 4:
        rotor3 = Rotor4_wiring
    else:
        rotor3 = Rotor5_wiring

    return rotor1, rotor2, rotor3


rotor1, rotor2, rotor3 = rot_allocation(rot1, rot2, rot3)


# returns new character when passing through any rotor forwards
def throughRotorforward(char, rotor, rotor_pos):
    return rotor[(char + rotor_pos) % 26][1]


# returns new character when passing through any rotor backwards
def throughRotorbackward(char, rotor, rotor_pos):
    for i in range(0, 26):
        if char == rotor[i][1]:
            output = (rotor[i][0] - rotor_pos)
            while (output < 0):
                output = 26 + output
            output = output % 26
    return output


# Reflector wiring
def reflector(char, wiring):
    return wiring[char % 26][1]


# Switches character if connected to another plug
def plug_switch(chara, Plugs):
    if len(Plugs) > 0:
        for k in range(len(Plugs)):
            if chara == Plugs[k][0]:
                chara = Plugs[k][1]
                break
            elif chara == Plugs[k][1]:
                chara = Plugs[k][0]
                break
    return chara


# moves rotors after each character
def moveRotors(rotor1_position, rotor2_position, rotor3_position):
    rotor1_position = rotor1_position + 1
    if rotor1_position == 26:
        rotor1_position = 0
        rotor2_position = rotor2_position + 1
        if rotor2_position == 26:
            rotor2_position = 0
            rotor3_position = rotor3_position + 1
            if rotor3_position == 26:
                rotor3_position = 0
    return rotor1_position, rotor2_position, rotor3_position


# Converts the list of your final message into string
def listToString(s):
    str1 = ""
    for ele in s:
        str1 = str1 + ele

    return str1

# Takes user input for message
print("only letters allowed. No Numbers or special characters")
mes = input("Enter your message: ")
mes = mes.lower()
message = []
new_message = []
final_message = []
# print("original Message:", name + "!")

#converts character into numbers
for i in mes:
    number = ord(i) - 97
    message.append(number)

# Enigma Process
for j in message:
    char = plug_switch(j, New_Plugs)

    char = throughRotorforward(char, rotor1, rotor1_pos)

    char = throughRotorforward(char, rotor2, rotor2_pos)

    char = throughRotorforward(char, rotor3, rotor3_pos)

    char = reflector(char, reflector_wiring)

    char = throughRotorbackward(char, rotor3, rotor3_pos)

    char = throughRotorbackward(char, rotor2, rotor2_pos)

    char = throughRotorbackward(char, rotor1, rotor1_pos)

    char = plug_switch(char, New_Plugs)

    new_message.append(char)
    rotor1_pos, rotor2_pos, rotor3_pos = moveRotors(rotor1_pos, rotor2_pos, rotor3_pos)

# Converts Number back into Letters
for i in new_message:
    x = i + 97
    letter = chr(x)
    final_message.append(letter)

output = listToString(final_message)
print(output)
