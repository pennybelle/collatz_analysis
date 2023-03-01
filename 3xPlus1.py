
import os
import time
import winsound


def file_check():
    if os.path.exists("hs.txt"):
        return True
    else:
        return False


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
y = int(1)
c = int(0)
f = int(0)
i = int()
max_value = int(pow(2, 68))
cache = int(0)
score = int(0)
w_indent = int(17)
l_indent = int(21)
log = ""
new_value = ""
space = " "
dash = " " * 11
bell = "\a"
cr = "\033[0;37;40m"
dg = "\033[1;30;40m"
down_color = "\033[1;31;40m"
up_color = "\033[1;32;40m"
nv_color = "\033[1;33;40m"
w_color_1 = "\033[0;37;41m"
w_color_2 = "\033[0;37;44m"
green = "\033[0;37;42m"
goc = "\033[0;30;47m"
ul_start = "\033[2;37;40m"
ul_stop = "\033[0;37;40m"
nl = "\n"
start = False
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

# print messages
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


def clear(): os.system('cls')


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
while cache >= 5:
    break

cache = int(0)

while not start:
    # start choice
    start_input = input(nl + space * 10 + begin + nl * 5)
    if start_input == "n":
        print(bell + nl * 2 + "k bye then :c")
        time.sleep(3)
        quit()
    elif start_input == "y":
        start = True
        break
    elif start_input != "y" or "n":
        clear()
        print(ii)
        continue

while start:
    # start number choice
    clear()
    time.sleep(1)
    winsound.Beep(h_freq, dur)
    num = input(nl * 1 + space * 6 + start_num + nl * 5)
    if num != "max":
        y = int(num)
    else:
        y = int(max_value)
    start = False
    break

print(nl * 2)

while True:
    # game loop
    clear()
    x = int(y + 1)
    new_value = str(space * 21 + "\033[0;30;43m" + nv + cr + nl + space * 21 + nv_color + str(int(x)) + nl)
    print(new_value)
    while x != 1:
        cache += int(1)
        if cache >= 51:
            cache = int(0)
        # 3 x + 1
        if int(x % 2) != 0:
            c += int(1)
            x = int(3 * x + 1)
            log = str(up + cr + dg + divider + str(c) + divider + cr + up_color + str(int(x)))
            print(log)
            continue
        # x / 2
        elif int(x % 2) == 0:
            c += int(1)
            x /= int(2)
            log = str(down + cr + dg + divider + str(c) + divider + cr + down_color + str(int(x)))
            print(log)
            continue
        i = int(x)
    # game over
    while x == 1:
        # high score cache
        high_score = open("hs.txt", "r")
        f += int(1)
        y += int(1)
        d = int(high_score.readlines()[1])
        high_score.close()
        if c > d:
            high_score = open("hs.txt", "w")
            high_score.writelines([str(y), "\n", str(c)])
            score = int(c)
            high_score = open("hs.txt", "r")
            high_score.close()
        else:
            score = d

        clear()
        winsound.Beep(l_freq, dur)
        edit = space * int(l_indent - 1) + goc + " GAME OVER " + cr
        success = space * l_indent + goc + "Wins:      " + cr + nl + space * l_indent + "0" + nl
        failures = space * l_indent + goc + "Loses:     " + cr + nl + space * l_indent + str(f) + cr + nl
        hs = str(space * l_indent + goc + "High Score:" + cr + nl + space * l_indent + str(score)) + cr
        print(nl * 2 + line_2 + cr + edit + line_2 + cr + nl + success + cr + failures + cr + hs)
        c = int(0)
        break
    continue
