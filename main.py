import random
import time

import datetime

an = datetime.datetime.now()

score = 0
sword = 0
poition = 0

Moves_Made = []

Same_Moves = []

rows = 6
cols = 7

lst_ici_E_dolu = [["E"] * cols for i in range(rows)]

lst_letters = ["T", "T", "T", "T", "T",
               "M", "M", "M", "M", "M",
               "S", "S",
               "P", "P", "P",
               "V", "V", "V"]

count = len(lst_letters)
while (count > 0):
    i = random.randint(0, rows - 1)
    j = random.randint(0, cols - 1)
    if (lst_ici_E_dolu[i][j] == "E"):
        lst_ici_E_dolu[i][j] = lst_letters.pop(count - 1)
        count = count - 1

lst_bos = [[" "] * cols for i in range(rows)]

x = 0
y = 0

while (True):
    x = random.randint(0, rows - 1)
    y = random.randint(0, cols - 1)

    if (lst_ici_E_dolu[x][y] == "E"):
        break
    else:
        continue

lst_bos[x][y] = "E"

# -----------------------------------------------------------------------------
Same_Moves.append((x, y))

while (True):

    for i in lst_bos:
        print(i)

    print("Score: [{}] Sword: [{}] Poition: [{}]".format(score, sword, poition))

    move = str(input("Press L, U, R, D to move: "))
    move = move.upper()

    if (move == "L"):
        try:
            Moves_Made.append("L")

            lst_bos[x][y - 1] = lst_ici_E_dolu[x][y - 1]
            y = y - 1

            Same_Moves.append((x, y))
            q = 1
            t = 0

            for i in Same_Moves:
                for j in range(q, len(Same_Moves)):
                    if (j == len(Same_Moves) - 1):
                        q += 1

                    if (i == Same_Moves[j]):
                        print("You have entered a previously entered block. Try again.")
                        t += 1

            if (t == 1):
                break

            if (x < 0 or y < 0):
                print("\nYou are off the list.\n")
                break

            if (lst_bos[x][y] == "T"):
                score += 1
                score += 1
                print("\n---------------------------")
                print("+TREASURE")
                print("\n---------------------------")
                print("Score: [{}] Sword: [{}] Poition: [{}]".format(score, sword, poition))
                time.sleep(2)
                print("\033[H\033[J", end="")
                continue

            elif (lst_bos[x][y] == "P"):
                poition += 1
                score += 1
                print("\n---------------------------\n")
                print("+POITION")
                print("\n---------------------------")
                print("Score: [{}] Sword: [{}] Poition: [{}]".format(score, sword, poition))
                time.sleep(2)
                print("\033[H\033[J", end="")
                continue

            elif (lst_bos[x][y] == "S"):
                sword += 1
                score += 1
                print("\n---------------------------\n")
                print("+SWORD")
                print("\n---------------------------")
                print("Score: [{}] Sword: [{}] Poition: [{}]".format(score, sword, poition))
                time.sleep(2)
                print("\033[H\033[J", end="")
                continue

            elif (lst_bos[x][y] == "M"):
                if (sword == 0):
                    print("\033[H\033[J", end="")

                    for i in lst_bos:
                        print(i)

                    print("\n---------------------------\n")
                    print("Oh no! MONSTOR.")
                    print("You die.")
                    print("Score: [{}] Sword: [{}] Poition: [{}]".format(score, sword, poition))
                    break

                elif (sword > 0):
                    print("---------------------------")
                    print("Oh no! MONSTOR.")
                    print("SWORD is used.")
                    print("Score: [{}] Sword: [{}] Poition: [{}]".format(score, sword, poition))
                    print("---------------------------")
                    sword -= 1
                    time.sleep(2)
                    print("\033[H\033[J", end="")
                    continue

            elif (lst_bos[x][y] == "V"):
                if (poition == 0):

                    print("\033[H\033[J", end="")
                    for i in lst_bos:
                        print(i)

                    print("\n---------------------------\n")
                    print("Oh no! VENOM.")
                    print("You die.")
                    print("Score: [{}] Sword: [{}] Poition: [{}]".format(score, sword, poition))
                    print("\nThe game ends.")
                    break

                elif (poition > 0):
                    print("\n---------------------------\n")
                    print("Oh no! MONSTOR.")
                    print("POITION is used.")
                    print("Score: [{}] Sword: [{}] Poition: [{}]".format(score, sword, poition))
                    poition -= 1
                    time.sleep(2)
                    print("\033[H\033[J", end="")
                    continue

            elif (lst_bos[x][y] == "E"):
                score += 1
                print("It's empty, please continue.")
                print("Score: [{}] Sword: [{}] Poition: [{}]".format(score, sword, poition))
                time.sleep(2)
                print("\033[H\033[J", end="")
                continue

        except IndexError:
            print("\nYou are off the list.\n")
            break

    # ----------------------------------------------------------------------------------

    elif (move == "R"):
        try:
            Moves_Made.append("R")

            lst_bos[x][y + 1] = lst_ici_E_dolu[x][y + 1]
            y = y + 1

            Same_Moves.append((x, y))
            q = 1
            t = 0

            for i in Same_Moves:
                for j in range(q, len(Same_Moves)):
                    if (j == len(Same_Moves) - 1):
                        q += 1

                    if (i == Same_Moves[j]):
                        print("You have entered a previously entered block. Try again.")
                        t += 1

            if (t == 1):
                break

            if (lst_bos[x][y] == "T"):
                score += 1
                score += 1
                print("\n---------------------------")
                print("+TREASURE")
                print("\n---------------------------")
                print("Score: [{}] Sword: [{}] Poition: [{}]".format(score, sword, poition))
                time.sleep(2)
                print("\033[H\033[J", end="")
                continue

            elif (lst_bos[x][y] == "P"):
                poition += 1
                score += 1
                print("\n---------------------------\n")
                print("+POITION")
                print("\n---------------------------")
                print("Score: [{}] Sword: [{}] Poition: [{}]".format(score, sword, poition))
                time.sleep(2)
                print("\033[H\033[J", end="")
                continue

            elif (lst_bos[x][y] == "S"):
                sword += 1
                score += 1
                print("\n---------------------------\n")
                print("+SWORD")
                print("\n---------------------------")
                print("Score: [{}] Sword: [{}] Poition: [{}]".format(score, sword, poition))
                time.sleep(2)
                print("\033[H\033[J", end="")
                continue

            elif (lst_bos[x][y] == "M"):
                if (sword == 0):

                    print("\033[H\033[J", end="")
                    for i in lst_bos:
                        print(i)

                    print("\n---------------------------\n")
                    print("Oh no! MONSTOR.")
                    print("You die.")
                    print("Score: [{}] Sword: [{}] Poition: [{}]".format(score, sword, poition))
                    break

                elif (sword > 0):
                    print("---------------------------")
                    print("Oh no! MONSTOR.")
                    print("SWORD is used.")
                    print("Score: [{}] Sword: [{}] Poition: [{}]".format(score, sword, poition))
                    print("---------------------------")
                    sword -= 1
                    time.sleep(2)
                    print("\033[H\033[J", end="")
                    continue

            elif (lst_bos[x][y] == "V"):
                if (poition == 0):

                    print("\033[H\033[J", end="")
                    for i in lst_bos:
                        print(i)

                    print("\n---------------------------\n")
                    print("Oh no! VENOM.")
                    print("You die.")
                    print("Score: [{}] Sword: [{}] Poition: [{}]".format(score, sword, poition))
                    print("\nThe game ends.")
                    break

                elif (poition > 0):
                    print("\n---------------------------\n")
                    print("Oh no! MONSTOR.")
                    print("POITION is used.")
                    print("Score: [{}] Sword: [{}] Poition: [{}]".format(score, sword, poition))
                    poition -= 1
                    time.sleep(2)
                    print("\033[H\033[J", end="")
                    continue

            elif (lst_bos[x][y] == "E"):
                score += 1
                print("It's empty, please continue.")
                print("Score: [{}] Sword: [{}] Poition: [{}]".format(score, sword, poition))
                time.sleep(2)
                print("\033[H\033[J", end="")
                continue

        except IndexError:
            print("\nYou are off the list.\n")
            break

    # ----------------------------------------------------------------------------------------

    if (move == "U"):
        try:
            Moves_Made.append("U")

            lst_bos[x - 1][y] = lst_ici_E_dolu[x - 1][y]
            x = x - 1

            Same_Moves.append((x, y))
            q = 1
            t = 0

            for i in Same_Moves:
                for j in range(q, len(Same_Moves)):
                    if (j == len(Same_Moves) - 1):
                        q += 1

                    if (i == Same_Moves[j]):
                        print("You have entered a previously entered block. Try again.")
                        t += 1

            if (t == 1):
                break

            if (x < 0 or y < 0):
                print("\nYou are off the list.\n")
                break

            if (lst_bos[x][y] == "T"):
                score += 1
                score += 1
                print("\n---------------------------")
                print("+TREASURE")
                print("\n---------------------------")
                print("Score: [{}] Sword: [{}] Poition: [{}]".format(score, sword, poition))
                time.sleep(2)
                print("\033[H\033[J", end="")
                continue

            elif (lst_bos[x][y] == "P"):
                poition += 1
                score += 1
                print("\n---------------------------\n")
                print("+POITION")
                print("\n---------------------------")
                print("Score: [{}] Sword: [{}] Poition: [{}]".format(score, sword, poition))
                time.sleep(2)
                print("\033[H\033[J", end="")
                continue

            elif (lst_bos[x][y] == "S"):
                sword += 1
                score += 1
                print("\n---------------------------\n")
                print("+SWORD")
                print("\n---------------------------")
                print("Score: [{}] Sword: [{}] Poition: [{}]".format(score, sword, poition))
                time.sleep(2)
                print("\033[H\033[J", end="")
                continue

            elif (lst_bos[x][y] == "M"):
                if (sword == 0):

                    print("\033[H\033[J", end="")
                    for i in lst_bos:
                        print(i)

                    print("\n---------------------------\n")
                    print("Oh no! MONSTOR.")
                    print("You die.")
                    print("Score: [{}] Sword: [{}] Poition: [{}]".format(score, sword, poition))
                    break

                elif (sword > 0):
                    print("---------------------------")
                    print("Oh no! MONSTOR.")
                    print("SWORD is used.")
                    print("Score: [{}] Sword: [{}] Poition: [{}]".format(score, sword, poition))
                    print("---------------------------")
                    sword -= 1
                    time.sleep(2)
                    print("\033[H\033[J", end="")
                    continue

            elif (lst_bos[x][y] == "V"):
                if (poition == 0):

                    print("\033[H\033[J", end="")
                    for i in lst_bos:
                        print(i)

                    print("\n---------------------------\n")
                    print("Oh no! VENOM.")
                    print("You die.")
                    print("Score: [{}] Sword: [{}] Poition: [{}]".format(score, sword, poition))
                    print("\nThe game ends.")
                    break

                elif (poition > 0):
                    print("\n---------------------------\n")
                    print("Oh no! MONSTOR.")
                    print("POITION is used.")
                    print("Score: [{}] Sword: [{}] Poition: [{}]".format(score, sword, poition))
                    poition -= 1
                    time.sleep(2)
                    print("\033[H\033[J", end="")
                    continue

            elif (lst_bos[x][y] == "E"):
                score += 1
                print("It's empty, please continue.")
                print("Score: [{}] Sword: [{}] Poition: [{}]".format(score, sword, poition))
                time.sleep(2)
                print("\033[H\033[J", end="")
                continue

        except IndexError:
            print("\nYou are off the list.\n")
            break

    # -----------------------------------------------------------------------------------------

    if (move == "D"):
        try:
            Moves_Made.append("D")

            lst_bos[x + 1][y] = lst_ici_E_dolu[x + 1][y]
            x = x + 1

            Same_Moves.append((x, y))
            q = 1
            t = 0

            for i in Same_Moves:
                for j in range(q, len(Same_Moves)):
                    if (j == len(Same_Moves) - 1):
                        q += 1

                    if (i == Same_Moves[j]):
                        print("You have entered a previously entered block. Try again.")
                        t += 1

            if (t == 1):
                break

            if (lst_bos[x][y] == "T"):
                score += 1
                score += 1
                print("\n---------------------------")
                print("+TREASURE")
                print("\n---------------------------")
                print("Score: [{}] Sword: [{}] Poition: [{}]".format(score, sword, poition))
                time.sleep(2)
                print("\033[H\033[J", end="")
                continue

            elif (lst_bos[x][y] == "P"):
                poition += 1
                score += 1
                print("\n---------------------------\n")
                print("+POITION")
                print("\n---------------------------")
                print("Score: [{}] Sword: [{}] Poition: [{}]".format(score, sword, poition))
                time.sleep(2)
                print("\033[H\033[J", end="")
                continue

            elif (lst_bos[x][y] == "S"):
                sword += 1
                score += 1
                print("\n---------------------------\n")
                print("+SWORD")
                print("\n---------------------------")
                print("Score: [{}] Sword: [{}] Poition: [{}]".format(score, sword, poition))
                time.sleep(2)
                print("\033[H\033[J", end="")
                continue

            elif (lst_bos[x][y] == "M"):
                if (sword == 0):

                    print("\033[H\033[J", end="")
                    for i in lst_bos:
                        print(i)

                    print("\n---------------------------\n")
                    print("Oh no! MONSTOR.")
                    print("You die.")
                    print("Score: [{}] Sword: [{}] Poition: [{}]".format(score, sword, poition))
                    break

                elif (sword > 0):
                    print("---------------------------")
                    print("Oh no! MONSTOR.")
                    print("SWORD is used.")
                    print("Score: [{}] Sword: [{}] Poition: [{}]".format(score, sword, poition))
                    print("---------------------------")
                    sword -= 1
                    time.sleep(2)
                    print("\033[H\033[J", end="")
                    continue

            elif (lst_bos[x][y] == "V"):
                if (poition == 0):

                    print("\033[H\033[J", end="")
                    for i in lst_bos:
                        print(i)

                    print("\n---------------------------\n")
                    print("Oh no! VENOM.")
                    print("You die.")
                    print("Score: [{}] Sword: [{}] Poition: [{}]".format(score, sword, poition))
                    print("\nThe game ends.")
                    break

                elif (poition > 0):
                    print("\n---------------------------\n")
                    print("Oh no! MONSTOR.")
                    print("POITION is used.")
                    print("Score: [{}] Sword: [{}] Poition: [{}]".format(score, sword, poition))
                    poition -= 1
                    time.sleep(2)
                    print("\033[H\033[J", end="")
                    continue

            elif (lst_bos[x][y] == "E"):
                score += 1
                print("It's empty, please continue.")
                print("Score: [{}] Sword: [{}] Poition: [{}]".format(score, sword, poition))
                time.sleep(2)
                print("\033[H\033[J", end="")
                continue

        except IndexError:
            print("\nYou are off the list.\n")
            break

file = open("C:/Users/oğuzhan/Desktop/bilgiler.txt", "a")

file.write("{}\n".format(datetime.datetime.ctime(an)))

o = 0
for i in Moves_Made:
    file.write("{}. Moves : {} ".format(o, i))
    o += 1

file.write("Score : {}\n\n".format(score))

file.close

print("\nMoves: {}".format(Moves_Made))
print("Score: {}".format(score))

