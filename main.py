# Day01 solution in Python.


def part_one(filename):
    previous = 0
    increased = 0

    file = open(filename)
    for line in file:

        if previous != 0 and previous < int(line):
            increased += 1

        previous = int(line)

    print("Part 1: " + str(increased))
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
    print("Part 2: " + str(increased))
    file.close()
    return increased


def part_one_lambda(filename):
    # load values into a list
    measurements = list(map(int, open(filename)))
    increased = lambda: \
        sum(previous < current for (previous, current) in zip(measurements, measurements[1:]))
    print("Part 1: " + str(increased()))


def part_two_lambda(filename):
    # load values into a list
    measurements = list(map(int, open(filename)))
    # print(measurements)
    increased = lambda window: \
        sum(previous < current for (previous, current) in zip(measurements[:-window], measurements[window:]))

    print("Part 2: " + str(increased(3)))
    # print("Part 1: " + str(increased(1)))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    input_filename = 'input.txt'

    part_one(input_filename)
    part_one_lambda(input_filename)

    part_two(input_filename)
    part_two_lambda(input_filename)
