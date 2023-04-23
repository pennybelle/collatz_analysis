import time
from os import system, path, name

log = 'HighScore.txt'

def file_check():
    if path.exists(log): return True
    else: return False

def clear(): system('cls' if name == 'nt' else 'clear')

def start():
    if not file_check():
        record = open(log, 'w+')
        record.writelines(['Best Seed: 0\nHighscore: 0'])
        record.close()
    print('\n' * 7)
    print(r'''
                        _____/\\\\\\\\\\______________________________________/\\\_        
                         ___/\\\///////\\\_________________________________/\\\\\\\_       
                          __\///______/\\\_______________________/\\\______\/////\\\_      
                           _________/\\\//_____/\\\____/\\\______\/\\\__________\/\\\_     
                            ________\////\\\___\///\\\/\\\/____/\\\\\\\\\\\______\/\\\_    
                             ___________\//\\\____\///\\\/_____\/////\\\///_______\/\\\_   
                              __/\\\______/\\\______/\\\/\\\________\/\\\__________\/\\\_  
                               _\///\\\\\\\\\/_____/\\\/\///\\\______\///___________\/\\\_ 
                                ___\/////////______\///____\///______________________\///__

                                Warning: This game can cause seizures, please take caution!
                                
                                                            Loading:
                                                            
                                ''', end='', flush=True)
    loops = 1
    load_bar = 0.00005
    while loops < 61:
        print('█', end='', flush=True)
        time.sleep(load_bar)
        loops += 1
        load_bar += 0.0015
    time.sleep(5)
    # set terminal size
    size = 'mode 54,50'
    system(size)

def game(x):
    current_score = int(0)  # ingame highscore, starts at 0 unless highscore is greater
    record = open(log, 'r')
    highscore = int(record.readlines()[1][10:])  # highscore in log file (2nd line)
    steps = int(0)  # steps it takes for x to get to 1
    loses = int(1)  # game over tracker to tease the player with # of losses lol
    delay = float(5)  # delay is reduced each game until cache_max is fulfilled
    cache = int(0)
    cache_max = int(50)
    new_color = '\033[0;30;43m'
    color_reset = '\033[0;37;40m'
    box_color = '\033[0;30;47m'
    green_box = '\033[0;37;42m'
    red_box = '\033[0;37;41m'
    green_text = '\033[1;32;40m'
    red_text = '\033[1;31;40m'
    box = ' ' * 11  # game over box borders (top and bottom)
    x = int(x)  # convert input x to int
    while True:  # game loop continues forever because this game cannot be won
        new_value = x
        print(f'''
                     {new_color}New Value: {color_reset}
                     {x}''')  # print new value at start of new game
        while x != 1:  # equation loop until x reaches 1 (which causes an infinite loop 4->2->1 thus game over)
            steps += 1
            if x % 2 == 0:  # if x is even divide by 2
                x = x // 2
                print(f'{red_box}  {color_reset} {steps}\t\b{red_text}{x}{color_reset}')
            else:  # if x is odd, multiply by 3 and add 1
                x = 3 * x + 1
                print(f'{green_box}  {color_reset} {steps}\t\b{green_text}{x}{color_reset}')
            if cache < cache_max:  # failsafe to remove delay after cache_max is reached
                time.sleep(delay * .01)  # delay between each run of the equation (unless cache_max is reached)
        if steps > current_score:  # if current score is higher than recorded score, update recorded to current
            current_score = steps
        if highscore > current_score:  # if highscore in log file is higher than current score, update current
            current_score = highscore
        elif highscore < current_score:  # else set current score as new highscore in log file
            highscore = current_score  # this line is needed to prevent log file from giving incorrect seed #
            record.close()  # close log file (in read mode)
            record = open(log, 'w')  # open log file (in write mode)
            record.writelines([f'Best Seed: {new_value}\nHighscore: {current_score}'])  # write new seed & score
        record.close()  # close log file (in write mode), reopens at beginning of new game
        # game over screen
        print(f'''
                     {box_color}{box}{color_reset}
                     {box_color} GAME OVER {color_reset}
                     {box_color}{box}{color_reset}
                     
                     {box_color}Wins:      {color_reset}
                     0
                     {box_color}Loses:     {color_reset}
                     {loses}
                     {box_color}High Score:{color_reset}
                     {current_score}\n''')
        x = new_value + 1  # add 1 to previous input/new value to progress the game to next number
        loses += 1  # records losses in the session, displays them in the game over screen
        steps = int(0)  # reset current score for new game
        if cache < cache_max:
            time.sleep(delay * .5)
            delay -= 0.1
            cache += 1
        clear()


start()
clear()
game(input('Please enter your desired seed(number):\n\n'))
