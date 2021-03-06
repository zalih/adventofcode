# Advent of Code solutions

import numpy as np


# Day 01 Part 1
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


# Day 01 Part 2
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


# Day 01 Part 1 using lambda
def part_one_lambda(filename):
    # load values into a list
    measurements = list(map(int, open(filename)))
    increased = lambda: \
        sum(previous < current for (previous, current) in zip(measurements, measurements[1:]))
    return increased()


# Day 01 Part 1 using lambda
def part_two_lambda(filename):
    # load values into a list
    measurements = list(map(int, open(filename)))
    increased = lambda window: \
        sum(previous < current for (previous, current) in zip(measurements[:-window], measurements[window:]))
    return increased(3)


# Day 02 Part 1
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


# Day 02 Part 2
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


# Day 03 Part 1
def power_consumption(filename):
    gamma_rate, epsilon_rate = 0, 0
    with open(filename) as file:
        diagnostics = [list(line.strip()) for line in file.readlines()]

    report_size = len(diagnostics)
    if report_size > 0:
        record_size = len(diagnostics[0])

    col = 0

    while col < record_size:
        row = 0
        one, zero = 0, 0
        while row < report_size:
            if diagnostics[row][col] == '1':
                one += 1
            else:
                zero += 1
            row += 1
        if (one - zero) > 0:
            gamma_rate |= (1 << (record_size - col - 1))
        else:
            epsilon_rate |= (1 << (record_size - col - 1))
        col += 1

    return gamma_rate * epsilon_rate


# Day 03 Part 2
def filter_diagnostics(diagnostics, is_major=True, col=0):
    report_size = len(diagnostics)
    if report_size > 0:
        record_size = len(diagnostics[0])
    else:
        return None

    filtered = []
    ones = []
    zeros = []

    row = 0
    one, zero = 0, 0
    while row < report_size:
        if diagnostics[row][col] == '1':
            one += 1
            ones.append(diagnostics[row])
        else:
            zero += 1
            zeros.append(diagnostics[row])
        row += 1

    if is_major:
        if (one - zero) >= 0:
            filtered = ones
        else:
            filtered = zeros
    else:
        if (zero - one) > 0 and len(ones) > 0:
            filtered = ones
        elif len(zeros) > 0:
            filtered = zeros
        elif len(ones) > 0:
            filtered = ones

    col += 1
    if col < record_size:
        filtered = filter_diagnostics(filtered, is_major, col)

    return filtered


def binary_array2int(input_array):
    output, index = 0, 0
    length = len(input_array)
    for item in input_array:
        if item == '1':
            output |= (1 << (length - index - 1))
        index += 1

    return output


def support_rating(filename):
    oxygen_generator_rating, co2_scrubber_rating = 0, 0
    with open(filename) as file:
        diagnostics = [list(line.strip()) for line in file.readlines()]

    report_size = len(diagnostics)
    if report_size > 0:
        record_size = len(diagnostics[0])

    oxygen_generator_rating = binary_array2int(filter_diagnostics(diagnostics)[0])
    co2_scrubber_rating = binary_array2int(filter_diagnostics(diagnostics, False)[0])

    return oxygen_generator_rating * co2_scrubber_rating


def calc_bingo(boards_marked, board):
    marks_sum = 0
    i, j = 0, 0
    for row in boards_marked:
        for value in row:
            if not value:
                marks_sum += board[i, j]
            j += 1
        i += 1
        j = 0

    return marks_sum


def bingo(filename, looser=False):
    score, line_counter, board_number = 0, 0, 0

    board = []
    boards = []
    winners = {}

    row_counter = 0
    # print(boards)
    with open(filename) as file:
        for line in file:
            if line_counter == 0:
                numbers = [int(x) for x in line.split(',')]
            else:
                if len(line) > 5:
                    line = ' '.join(line.split())
                    board.append(([int(x) for x in line.split(' ')]))
                    row_counter += 1

                if row_counter == 5:
                    boards.append(board)
                    board_number += 1
                    board = []
                    row_counter = 0

            line_counter += 1
    boards_np = np.asarray(boards)
    boards_marked = np.zeros((len(boards), 5, 5), dtype=bool)

    board_index = 0
    row_index = 0
    col_index = 0
    for number in numbers:
        for board in boards_np:
            for row in board:
                for col in row:
                    if col == number:
                        # print(str(number) + " mark at " + str(board_index)+":"+str(row_index)+":"+str(col_index))
                        boards_marked[board_index, row_index, col_index] = True
                        i, k = 0, 0
                        while i < 5:
                            if boards_marked[board_index, i, col_index]:
                                k += 1
                            if k == 5:
                                if not winners.get(board_index):
                                    winners[board_index] = col * calc_bingo(boards_marked[board_index], board)
                            i += 1
                        i, k = 0, 0
                        while i < 5:
                            if boards_marked[board_index, row_index, i]:
                                k += 1
                            if k == 5:
                                # print("Board " + str(board_index + 1) + " Line " + str(row_index + 1) + " Wins")
                                # print(row)
                                if not winners.get(board_index):
                                    winners[board_index] = col * calc_bingo(boards_marked[board_index], board)
                            i += 1
                    col_index += 1
                col_index = 0
                row_index += 1
            row_index = 0
            board_index += 1
        board_index, row_index, col_index = 0, 0, 0

    if looser:
        score = winners[list(winners.keys())[-1]]
    else:
        score = winners[list(winners.keys())[0]]
    return score


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_filename = 'data/day01/input.txt'

    print("Day01-1: " + str(part_one(input_filename)))
    print("Day01-1: " + str(part_two(input_filename)))
    print("Day01-1-lambda: " + str(part_one_lambda(input_filename)))
    print("Day01-2-lambda: " + str(part_two_lambda(input_filename)))

    print("Day02-1: " + str(dive('data/day02/input.txt')))
    print("Day02-2: " + str(dive_aim('data/day02/input.txt')))

    print("Day03-1: " + str(power_consumption('data/day03/input.txt')))
    print("Day03-2: " + str(support_rating('data/day03/input.txt')))

    print("Day04-1: " + str(bingo('data/day04/input.txt')))
    print("Day04-2: " + str(bingo('data/day04/input.txt', True)))
