# Advent of Code solutions

import re

from collections import Counter


def get_submatrix(matrix, start_row, start_col, num_rows, num_cols):
    submatrix = [row[start_col:start_col + num_cols] for row in matrix[start_row:start_row + num_rows]]
    return submatrix


def search_pattern(matrix, search_matrix, output=False):
    result = 0

    for i in range(len(matrix[0])-2):
        for j in range(len(matrix)-2):
            submatrix = get_submatrix(matrix, i, j, 3, 3)
            submatrix[1][0] = '*'
            submatrix[0][1] = '*'
            submatrix[1][2] = '*'
            submatrix[2][1] = '*'
            if submatrix == search_matrix:
                result += 1
            if output:
                print(str(i)+'-'+str(j))
                print(str(submatrix[0]))
                print(str(submatrix[1]))
                print(str(submatrix[2]))

    return result


def transpose_matrix(matrix):
    result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return result


def load_int(file, separator=' '):
    if separator == '':
        result = [list(map(int, line.strip())) for line in file]
    else:
        result = [list(map(int, line.strip().split(separator))) for line in file]
    return result


def load_chr(file, separator=' '):
    if separator == '':
        result = [list(line.strip()) for line in file]
    else:
        result = [list(line.strip().split(separator)) for line in file]
    return result


def load_file_to_matrix(filename, separator=' ', transpose=False, element_type=int):
    result = []
    with open(filename, 'r') as file:
        if element_type == int:
            result = load_int(file, separator)
        if element_type == chr:
            result = load_chr(file, separator)
        if transpose:
            result = transpose_matrix(result)
    file.close()
    return result


def day01p1(filename):
    # calculate distance of two columns (sort them first)
    rooms = []

    rooms = load_file_to_matrix(filename, '   ', True)
    rooms[0].sort();
    rooms[1].sort();
    result = sum(map(lambda x, y: abs(x - y), rooms[0], rooms[1]))

    return result


def day01p2(filename):
    # similarity score: sum of each value in room1 * count of value in room2
    rooms = []
    counter2 = []

    rooms = load_file_to_matrix(filename, '   ', True)

    # Counter from collections counts each element and creates a dictionary with the count
    counter2 = Counter(rooms[1])

    result = sum(map(lambda x: x * counter2[x], rooms[0]))

    return result


def day02p1(filename):
    levels = []
    delta = 0
    safe = 0

    levels = load_file_to_matrix(filename)
    for level in levels:
        prev = bool(False)
        failed = False
        trend = 'und'
        for val in level:
            if not prev:
                prev = int(val)
            else:
                delta = int(val) - prev
                if delta == 0 or abs(delta) > 3:
                    failed = True
                    break
                if 1 <= delta <= 3 and trend == 'dec':
                    failed = True
                    break
                if -1 >= delta >= -3 and trend == 'inc':
                    failed = True
                    break
                if delta > 0:
                    trend = 'inc'
                else:
                    trend = 'dec'
                prev = val
        if not failed:
            safe += 1

    return safe


def check_safety(level, skip=0):
    prev = bool(False)
    trend = ''
    for index, val in enumerate(level):
        if (index + 1) == skip:
            continue
        if not prev:
            prev = int(val)
        else:
            delta = int(val) - prev
            if delta == 0 or abs(delta) > 3:
                return True
            if 1 <= delta <= 3 and trend == 'dec':
                return True
            if -1 >= delta >= -3 and trend == 'inc':
                return True
            if delta > 0:
                trend = 'inc'
            else:
                trend = 'dec'
            prev = val
    return False


def day02p1(filename, tolerant=False):
    safe = 0

    levels = load_file_to_matrix(filename)
    for level in levels:
        index = 0
        failed = check_safety(level)
        while tolerant and failed and index < len(level):
            index += 1
            failed = check_safety(level, index)

        if not failed:
            safe += 1

    return safe


def day03p1(filename):
    result = 0
    with open(filename) as file:
        for line in file:
            x = re.findall("mul\((\d{1,3}),(\d{1,3})\)", line)
            for tup in x:
                result += int(tup[0]) * int(tup[1])
    file.close()
    return result


def day03p2(filename):
    result = 0
    data = ""
    with open(filename) as file:
        for line in file:
            # new line breaks it, needs strip()
            data += line.strip()
        pos_1 = 0
        while pos_1 != -1:
            pos_1 = data.find('don\'t()')
            pos_2 = data.find('do()', pos_1)
            cleaned = data[:pos_1]
            if pos_2 != -1:
                cleaned += data[pos_2+4:]
            data = cleaned
        x = re.findall("mul\((\d{1,3}),(\d{1,3})\)", data)
        for tup in x:
            result += int(tup[0]) * int(tup[1])
    file.close()

    return result


def day04p1(filename):
    # load file into a matrix
    # iterate over matrix in all possible directions
    # store iterations to a list of strings
    # search for keyword in all strings and count them
    result = ""
    xmas = load_file_to_matrix(filename, '', element_type=chr)
    # print(xmas)
    # horizontal
    for row in xmas:
        result += ''.join(row)
        result += '-'
    # horizontal reverse
    for row in xmas:
        result += ''.join(row)[::-1]
        result += '-'

    result += '\n'
    # vertical
    for column in zip(*xmas):
        result += ''.join(column)
        result += '-'

    # vertical reverse
    for column in zip(*xmas):
        result += ''.join(column)[::-1]
        result += '-'
    result += '\n'
    # diagonal l to r
    for d in range(len(xmas)):
        diagonal = [xmas[i][d+i] for i in range(len(xmas) - d)]
        result += ''.join(diagonal)
        result += '-'
    for d in range(1, len(xmas)):
        diagonal = [xmas[d+i][i] for i in range(len(xmas) - d)]
        result += ''.join(diagonal)
        result += '-'

    # diagonal l to r reverse
    for d in range(len(xmas)):
        diagonal = [xmas[i][d+i] for i in range(len(xmas) - d)]
        result += ''.join(diagonal)[::-1]
        result += '-'
    for d in range(1, len(xmas)):
        diagonal = [xmas[d+i][i] for i in range(len(xmas) - d)]
        result += ''.join(diagonal)[::-1]
        result += '-'

    result += '\n'
    # diagonal r to l
    for d in range(len(xmas)):
        diagonal = [xmas[i][len(xmas) - 1 - d - i] for i in range(len(xmas) - d)]
        result += ''.join(diagonal)
        result += '-'

    for d in range(1, len(xmas)):
        diagonal = [xmas[d + i][len(xmas) - 1 - i] for i in range(len(xmas) - d)]
        result += ''.join(diagonal)
        result += '-'

    # diagonal r to l reverse
    for d in range(len(xmas)):
        diagonal = [xmas[i][len(xmas) - 1 - d - i] for i in range(len(xmas) - d)]
        result += ''.join(diagonal)[::-1]
        result += '-'
    for d in range(1, len(xmas)):
        diagonal = [xmas[d + i][len(xmas) - 1 - i] for i in range(len(xmas) - d)]
        result += ''.join(diagonal)[::-1]
        result += '-'

    # print(result)
    matches = re.findall('XMAS', result)
    count = len(matches)
    return count


def day04p2(filename):
    result = 0
    xmas = load_file_to_matrix(filename, '', element_type=chr)
    search_pattern1 = [['M', '*', 'S'],
                      ['*', 'A', '*'],
                      ['M', '*', 'S']]

    result += search_pattern(xmas, search_pattern1)
    transposed_matrix = transpose_matrix(search_pattern1)
    result += search_pattern(xmas, transposed_matrix)
    transposed_matrix = transposed_matrix[::-1]
    result += search_pattern(xmas, transposed_matrix)
    transposed_matrix = [row[::-1] for row in search_pattern1]
    result += search_pattern(xmas, transposed_matrix)

    return result


def check_violation(val, rules, blacklist):
    result = -1
    # seen = None
    for rule in rules:
        if rule[0] == val:
            for seen in blacklist:
                if rule[1] == seen:
                    result = seen
    return result


def load_rules_and_pages(filename):
    rules = []
    pages = []
    rules_section = True
    with open(filename, 'r') as file:
        for line in file:
            if line == '\n':
                rules_section = False
                continue
            if rules_section:
                rules.append(list(map(int, line.strip().split('|'))))
            else:
                pages.append(list(map(int, line.strip().split(','))))
    file.close()

    return rules, pages


def day05p1(filename):
    result = 0
    rules = []
    pages = []
    rules, pages = load_rules_and_pages(filename)
    for row in pages:
        blacklist = []
        violation = -1
        page = -1
        for val in row:
            violation = check_violation(val, rules, blacklist)
            if violation != -1:
                page = violation
            blacklist.append(val)
        if page == -1:
            pos = int((len(row)-1) / 2)
            result += row[pos]
    return result


def swap_values_in_list(values, swap):
    index1, index2 = values.index(swap[0]), values.index(swap[1])
    values[index2], values[index1] = values[index1], values[index2]
    return values


def day05p2(filename):
    result = 0
    rules, pages = load_rules_and_pages(filename)
    for row in pages:
        i = 0
        blacklist = []
        corrected = False
        # print('checking: ' + str(row))
        while i <= (len(row)-1):
            violation = check_violation(row[i], rules, blacklist)
            if violation != -1:
                pages = violation, row[i]
                row = swap_values_in_list(row, pages)
                corrected = True
                i = 0
                blacklist = []
            else:
                blacklist.append(row[i])
                i += 1
        if corrected:
            # print('corrected: ' + str(row))
            pos = int((len(row)-1) / 2)
            result += row[pos]

    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Day01-1: " + str(day01p1('data/day01/input.txt')))
    print("Day01-2: " + str(day01p2('data/day01/input.txt')))
    print("Day02-1: " + str(day02p1('data/day02/input.txt')))
    print("Day02-2: " + str(day02p1('data/day02/input.txt', True)))
    print("Day03-1: " + str(day03p1('data/day03/input.txt')))
    print("Day03-2: " + str(day03p2('data/day03/input.txt')))
    print("Day04-1: " + str(day04p1('data/day04/input.txt')))
    print("Day04-2: " + str(day04p2('data/day04/input.txt')))
    print("Day05-1: " + str(day05p1('data/day05/input.txt')))
    print("Day05-2: " + str(day05p2('data/day05/input.txt')))
