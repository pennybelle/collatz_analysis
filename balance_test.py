import time
def equation():
    start = int(input('enter a starting value: ')) # starting value
    even = 0
    odd = 0
    step = 0
    while True: # infinite test loop
        x = start # set x to start
        while x != 1: # break each test when x = 1
            if x % 2 == 0: # if even
                x = x // 2 # divide x by 2
                print(x)
                even += 1 # mark result as even
            else: # if odd
                x = 3 * x + 1 # 3x + 1
                print(x)
                odd += 1 # mark result as odd
        percent = (odd / even) * 100
        print('-' * 5)
        print(f'even = {even}\nodd  = {odd}')
        print(f'\nresults in odds {percent:.10f}% of the time compared to evens')
        if step > 0:
            balance = 100 / percent
            print(f'this means evens are {balance:.5f} times as likely to occur as a result')
        print('-' * 5)
        step += 1
        start += 1 # increase starting value
        print(f'x = {start}') # display current x
        time.sleep(0.01) # to slow loop a bit

equation()