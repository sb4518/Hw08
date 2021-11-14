import random
import BirdBathFunc_Qh_cls420 as bird

if __name__ == '__main__':
    # stop criteria: if no update for 100 consecutive random sets
    random.seed(20)

    stop = 0
    best_par = []
    best_percentage = 0

    # stop_criteria = 10  # initialize stopping criteria
    # goal = 0.5

    while best_percentage < 0.499:
        roll = random.uniform(-30, 30)
        tilt = random.uniform(-30, 30)
        twist = random.uniform(-30, 30)
        res = bird.BirdBathFunc_Qh_cls420(roll, tilt, twist)
        if res > best_percentage:
            best_percentage = res
            best_par = [roll, tilt, twist]
            print(best_percentage)


    print('-------')
    print(best_percentage)
    print(best_par)