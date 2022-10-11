healthy_life=10000
daily_steps=0
while daily_steps<=healthy_life:
    steps=input()
    if steps=='Going home':
        steps_to_home = int(input())
        daily_steps = int(steps) + daily_steps
        daily_steps=daily_steps+steps_to_home
        if daily_steps>=healthy_life:
            print(f"Goal reached! Good job!")
            print(f'{daily_steps - healthy_life} steps over the goal!')
        else:
            print(f'{abs(healthy_life-daily_steps)} more steps to reach goal.')
        break
    elif steps!='Going home':
        daily_steps = int(steps) + daily_steps
        if daily_steps>=healthy_life:
            print(f"Goal reached! Good job!")
            print(f'{daily_steps-healthy_life} steps over the goal!')
            break


