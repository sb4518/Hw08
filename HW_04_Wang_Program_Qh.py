import random
import BirdBathFunc_Qh_cls420 as bird

if __name__ == '__main__':
    # stop criteria: if no update for 100 consecutive random sets
    # function to initialize the pseudo-random number generator in
    # Python to get the deterministic random data you want.
    random.seed(20)

    stop = 0
    best_par = []
    ideal_fraction = 0

    # stop_criteria = 10  # initialize stopping criteria
    # goal = 0.5

    print("Function is processing.")
    while ideal_fraction < 0.499:
        # The working parameter ranges for roll, tilt, and twist are all
        # in the range [-90, 90] The range of [-30, 30] is a good set of
        # limits to use for practical purposes initially,
        roll = random.uniform(-30, 30)
        tilt = random.uniform(-30, 30)
        twist = random.uniform(-30, 30)
        cur_fraction = bird.BirdBathFunc_Qh_cls420(roll, tilt, twist)
        if cur_fraction > ideal_fraction:
            ideal_fraction = cur_fraction
            best_par = [roll, tilt, twist]
            print(ideal_fraction)

    print("Best answer")
    print(ideal_fraction)
    print(best_par)