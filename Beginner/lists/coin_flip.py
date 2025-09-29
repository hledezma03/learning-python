import random
number_of_streaks = 0
for experiment_number in range(10000):  # Run 100,000 experiments total.
    # Code that creates a list of 100 'heads' or 'tails' values
    result_of_flips = []
    for i in range(100):
        if random.randint(0,1) == 0:
            result_of_flips.append('H')
        else:
            result_of_flips.append('T')
    # Code that checks if there is a streak of 6 heads or tails in a row
    for i in range(len(result_of_flips) - 5):
        streak = result_of_flips[i:i+6]
        if streak == ['H']*6 or streak == ['T']*6:
            number_of_streaks += 1
            break

chance_of_streak = number_of_streaks / 10000 * 100
print('Chance of a streak of 6 heads or tails in 100 flips: {:.2f}%'.format(chance_of_streak))