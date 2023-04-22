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
        record.writelines(['0\n0'])
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
    score = int(0)
    record = open(log, 'r')
    highscore = int(record.readlines()[1])
    cache = int(0)
    cache_max = int(50)
    steps = int(0)
    loses = int(1)
    delay = float(5)
    new_color = '\033[0;30;43m'
    color_reset = '\033[0;37;40m'
    box_color = '\033[0;30;47m'
    green_box = '\033[0;37;42m'
    red_box = '\033[0;37;41m'
    green_text = '\033[1;32;40m'
    red_text = '\033[1;31;40m'
    box = ' ' * 11
    x = int(x)
    while True:
        new_value = x
        print(f'''                     {new_color}New Value: {color_reset}
                     {x}''')
        while x != 1:
            steps += 1
            if x % 2 == 0:
                x = x // 2
                print(f'{red_box}  {color_reset} {steps}\t\b{red_text}{x}{color_reset}')
            else:
                x = 3 * x + 1
                print(f'{green_box}  {color_reset} {steps}\t\b{green_text}{x}{color_reset}')
            if cache < cache_max:
                time.sleep(delay * .01)
        if steps > score:  # if current score is higher than recorded score, update recorded to current
            score = steps
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
                     {score}\n''')
        x = new_value + 1  # add 1 to previous input/new value to progress the game to next number
        loses += 1  # records losses in the session, displays them in the game over screen
        steps = int(0)  # reset current score for new game
        if cache < cache_max:
            time.sleep(delay * .5)
            delay -= 0.1
            cache += 1
        clear()
        # TODO - fix so if False this block is skipped
        if score > highscore:  # record new highscore if greater than highscore in log file
            record.close()
            record = open(log, 'w')
            record.writelines([f'{new_value} (this is supposed to be the seed that gave the highscore but it doesnt work rn)\n{score}'])
            record.close()
            record = open(log, 'r')


start()
clear()
game(input('Please enter your desired seed(number):\n\n'))
