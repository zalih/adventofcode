# Day01 solution in Python.


def part_one(filename):
    previous = 0
    increased = 0

    file = open(filename)
    for line in file:

        if previous != 0 and previous < int(line):
            increased += 1

        previous = int(line)

    file.close()
    return increased


def part_two(filename):
    # load values into an array and cast to int using comprehensions
    file = open(filename, 'r')
    measurements = [int(x) for x in file.readlines()]
    # while n+3 contains a measurement, make sum1 of n, n+1, n+2 and sum2 of n+1, n+2, n+3
    # if sum2 - sum1 > 0, -> increased
    n = 0
    increased = 0
    while (n + 3) < len(measurements):
        # sum1 = measurements[n] + measurements[n + 1] + measurements[n + 2]
        # sum2 = measurements[n + 1] + measurements[n + 2] + measurements[n + 3]
        # for sum2 - sum2,  measurements[n + 1] nd measurements[n + 2] cuts out
        sum1 = measurements[n]
        sum2 = measurements[n + 3]
        if (sum2 - sum1) > 0:
            increased += 1
        n += 1
    file.close()
    return increased


def part_one_lambda(filename):
    # load values into a list
    measurements = list(map(int, open(filename)))
    increased = lambda: \
        sum(previous < current for (previous, current) in zip(measurements, measurements[1:]))
    return increased


def part_two_lambda(filename):
    # load values into a list
    measurements = list(map(int, open(filename)))
    # print(measurements)
    increased = lambda window: \
        sum(previous < current for (previous, current) in zip(measurements[:-window], measurements[window:]))
    return increased


def dive(filename):
    horizontal_position = 0
    depth = 0

    #  open a file using with it will take care of closing
    with open(filename) as file:
        for line in file:
            d = line.strip().split(' ')
            command = d[0]
            movement = int(d[1])
            if command == 'forward':
                horizontal_position += movement
            elif command == 'down':
                depth += movement
            elif command == 'up':
                depth -= movement

    # load key value pairs

    return horizontal_position * depth


def dive_aim(filename):
    horizontal_position = 0
    depth = 0
    aim = 0

    with open(filename) as file:
        for line in file:
            d = line.strip().split(' ')
            command = d[0]
            movement = int(d[1])
            if command == 'forward':
                horizontal_position += movement
                depth += (movement * aim)
            elif command == 'down':
                aim += movement
            elif command == 'up':
                aim -= movement

    return horizontal_position * depth


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    input_filename = 'data/day01/input.txt'

    print("Day01-1: " + str(part_one(input_filename)))
    print("Day01-1: " + str(part_two(input_filename)))
    # part_one_lambda(input_filename)
    # part_two_lambda(input_filename)

    print("Day02-1: " + str(dive('data/day02/input.txt')))
    print("Day02-2: " + str(dive_aim('data/day02/input.txt')))
