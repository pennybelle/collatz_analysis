# import libraries
import asyncio
import os
import time
import winsound

# custom function to check if hs.txt exists
def file_check():
    if os.path.exists("hs.txt"):
        return True
    else:
        return False

# check if hs.txt exists, if so this block is skipped
if not file_check():
    high_score = open("hs.txt", "w+")
    high_score.writelines([str(0), "\n", str(0)])
    high_score.close()

# set terminal size
size = 'mode 53,50'
os.system(size)

# Beep
h_freq = 30000
l_freq = 20000
dur = 1

# data collection
y = int(1)  # starting point
c = int(0)  # steps it takes to get game over (starts at 0, adds 1 every time either equation is run)
f = int(0)  # failure/loses cache default
i = int()  # idk why this is here ????
delay = float(1)  # start delay, quickly drops and then is disabled
max_value = int(pow(2, 68))  # if input from line 185 is max use this value as input
cache = int(0)  # multi use cache default
score = int(0)  # score default
w_indent = int(17)  # indent for intro game over
l_indent = int(21)  # indent for game over display loop
log = ""  # log cache default, this is the value used to print outputs for the equations
new_value = ""  # new value (every time you lose the value is added to 1) default cache
space = " "  # space (to make strings prettier <3)
dash = " " * 11  # this is the top and bottom of the Game Over screen, check lines 62 and 254 for the middle line
bell = "\a"  # windows alert sound, not in use currently
cr = "\033[0;37;40m"  # color reset, usually added to the end of every string so colors dont stretch past their boundary
dg = "\033[1;30;40m"  # dark grey
down_color = "\033[1;31;40m"  # red text
up_color = "\033[1;32;40m"  # green text
nv_color = "\033[1;33;40m"  # new value color (yellow)
w_color_1 = "\033[0;37;41m"  # red background
w_color_2 = "\033[0;37;44m"  # blue background
green = "\033[0;37;42m"  # green background
goc = "\033[0;30;47m"  # game over color (white background, black text)
ul_start = "\033[2;37;40m"  # underline start, this shit dont work
ul_stop = "\033[0;37;40m"  # underline stop aka color reset (cr)
nl = "\n"  # new line (enter down to next line)
start = False  # start value is defaulted to False

# concatenation collection
line_1 = cr + nl + space * 20 + goc + dash + cr + nl + space
line_2 = cr + nl + space * l_indent + goc + dash + cr + nl + space
game_start = str(nl + dash + nl + "GAME START" + nl + dash + nl)
game_over = str(line_1 + space * 19 + goc + " GAME OVER " + cr + line_1 + cr)

# string collection
welcome = "Welcome to 3x+1!"
rules = "Here are the rules :"
rule_1 = "You enter a seed at the prompt. If that number is"
rule_2 = "Odd, it will be multiplied by 3 and then added to 1."
rule_3 = "If it is Even however, it will be divided by 2."
rule_4 = "If your number reaches 1, then its :"
rule_5 = "and your number will be raised to the next."
rule_6 = "Your number will continue to rise until it finds"
rule_7 = "a pattern that doesnt end in 4, 2, 1. Good luck!"
warning = "SEIZURE WARNING!"
begin = "Would you like to begin? (y/n)"
start_num = "Please enter your desired seed(number):"
ii = "Invalid Input, please try again"
divider = " - "
up = green + "  "
down = w_color_1 + "  "
nv = "NEW VALUE: "

# messages
message_1 = nl * 2 + space * 18 + goc + welcome + cr + nl * 2
message_2 = space * 16 + rules + nl
message_3 = rule_1
message_4 = rule_2
message_5 = rule_3 + nl
message_6 = space * 7 + rule_4 + nl * 3 + str(game_over) + nl * 3
message_7 = rule_5
message_8 = rule_6
message_9 = rule_7 + nl * 3
message_10 = warning

# print intro messages
winsound.Beep(h_freq, dur)
print(message_1)
time.sleep(2)
winsound.Beep(h_freq, dur)
print(message_2)
time.sleep(0.5)
winsound.Beep(h_freq, dur)
print(message_3)
time.sleep(0.5)
winsound.Beep(h_freq, dur)
print(message_4)
time.sleep(0.5)
winsound.Beep(h_freq, dur)
print(message_5)
time.sleep(0.5)
winsound.Beep(h_freq, dur)
print(message_6)
time.sleep(2)
winsound.Beep(h_freq, dur)
print(message_7)
time.sleep(0.5)
winsound.Beep(h_freq, dur)
print(message_8)
time.sleep(0.5)
winsound.Beep(h_freq, dur)
print(message_9)
time.sleep(2)
print(space * w_indent + w_color_1 + message_10 + cr + nl * 3)
time.sleep(0.05)

# custom function to clear terminal window
def clear(): os.system('cls')

# seizure warning loop, continues till cache is full (0->20)
while cache < 20:
    clear()
    print(message_1)
    print(message_2)
    print(message_3)
    print(message_4)
    print(message_5)
    print(message_6)
    print(message_7)
    print(message_8)
    print(message_9)
    print(space * w_indent + w_color_2 + message_10 + cr + nl * 3)
    winsound.Beep(h_freq, dur)
    time.sleep(0.05)
    clear()
    cache += int(1)
    print(message_1)
    print(message_2)
    print(message_3)
    print(message_4)
    print(message_5)
    print(message_6)
    print(message_7)
    print(message_8)
    print(message_9)
    print(space * w_indent + w_color_1 + message_10 + cr + nl * 3)
    winsound.Beep(h_freq, dur)
    time.sleep(0.05)
    cache += int(1)
    continue

# reset cache to 0
cache = int(0)

# start is defaulted to False (see data collection), asks if ready to play
while not start:
    # start choice
    start_input = input(nl + space * 10 + begin + nl * 5)  # input line using info from data collection
    if start_input == "n":  # if n, quit the program with a sad msg
        print(bell + nl * 2 + "k bye then :c")
        time.sleep(3)
        quit()
    elif start_input == "y":  # if y, set start to True
        start = True
        break
    elif start_input != "y" or "n":  # if input isnt y or n, returns invalid input string (ii)
        clear()
        print(ii)
        continue

# once start is set to True
while start:
    # start number choice
    time.sleep(1)
    winsound.Beep(h_freq, dur)  # beep
    num = input(nl * 2 + space * 6 + start_num + nl * 5)  # string using data from data collection
    if num != "max":  # if input (num) isnt "max" then input integer as y
        y = int(num)
    else:  # otherwise input max value, aka 2^68
        y = int(max_value)
    start = False  # reset start, not sure if this is needed tbh lollll
    break

print(nl * 2)  # print 2 new lines (nl = new line)

# this is the infinite game loop. once you pass this barrier the game will loop until closed
while True:
    # game loop
    x = int(y + 1)  # x is our placeholder for y
    new_value = str(space * 21 + "\033[0;30;43m" + nv + cr + nl + space * 21 + nv_color + str(int(x)) + nl) # string using data from data collection
    print(new_value)  # print new value string (see line above)
    # start delay to ease the player into infinite loses
    if delay > 0.00001:
        time.sleep(delay)
        delay -= 0.05
    while x != 1:  # if x isnt 1 (main game loop) then continue this loop
        # cache was used in an experiment but isnt used anymore, this doesnt do anything useful lol
        cache += int(1)
        if cache >= 51:
            cache = int(0)
        # start delay / 10 to show progression of loses, disabled shortly after ur first few loses
        if delay > 0.00001:
            time.sleep(delay / 10)
        # if x is odd then -> 3 x + 1
        if int(x % 2) != 0:
            c += int(1)
            x = int(3 * x + 1)
            log = str(up + cr + dg + space * 2 + str(c) + space * 2 + cr + up_color + str(int(x)))
            print(log)
            continue
        # if x is even then -> x / 2
        elif int(x % 2) == 0:
            c += int(1)
            x /= int(2)
            log = str(down + cr + dg + space * 2 + str(c) + space * 2 + cr + down_color + str(int(x)))
            print(log)
            continue
        i = int(x)  # honestly not sure what this does lmfao i think it was from a past experiment
    # if x = 1 then its game over
    while x == 1:  # when x hits 1, game over loop begins
        # high score cache
        high_score = open("hs.txt", "r")  # open hs.txt in readable mode
        f += int(1)  # adding 1 to failure/loses cache
        y += int(1)  # adding 1 to y
        d = int(high_score.readlines()[1])  # set d to whatever the highscore is in hs.txt (line 2)

        # if c (high score int as seen by the py script) is greater than documented highscore in hs.txt (line 2)
        if c > d:
            high_score.close()  # close hs.txt (you gotta do this to open in writing mode)
            high_score = open("hs.txt", "w")  # open in writing mode
            high_score.writelines([str(y), "\n", str(c)])  # write new high score (c) on line 2, and the seed on line 1
            score = int(c)  # update score to c (score used below)
            high_score.close()  # close hs.txt (you gotta do this to open in reading mode)
            high_score = open("hs.txt", "r")
        # otherwise set score (used below) as d (documented high score in hs.txt (line 2)
        else:
            score = d

        clear()  # clear terminal screen
        winsound.Beep(l_freq, dur)  # beep

        # string collection #2 (needs to be in this loop to use accurate data
        edit = space * int(l_indent - 1) + goc + " GAME OVER " + cr
        success = space * l_indent + goc + "Wins:      " + cr + nl + space * l_indent + "0" + nl
        failures = space * l_indent + goc + "Loses:     " + cr + nl + space * l_indent + str(f) + cr + nl
        hs = str(space * l_indent + goc + "High Score:" + cr + nl + space * l_indent + str(score)) + cr
        # print game over screen using strings found in the above collection
        print(nl * 2 + line_2 + cr + edit + line_2 + cr + nl + success + cr + failures + cr + hs)
        c = int(0)  # update c to 0
        break
    continue  # this makes the game loop forever in the game loop
