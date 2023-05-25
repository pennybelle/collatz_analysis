def collatz(x=300339047, step=0):
    if step > 993:
        print('step exceeded recursion depth of 995')
        exit()
    elif x == 1:
        return step
    elif x % 2 == 0:
        return collatz(x // 2, step + 1)
    else:
        return collatz(3 * x + 1, step + 1)

def run_collatz(x):
    most_steps = 0
    while True:
        steps = collatz(x)
        if steps > most_steps:
            most_steps = steps
        print(f'{x}: {steps}\tsteps | most steps taken = {most_steps}')
        x += 1
    
run_collatz(1)