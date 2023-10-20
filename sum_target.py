def read_from_file(filepath):
    try:
        with open(filepath, 'r') as f:
            return f.read()
    except Exception:
        raise IOError("There was a problem opening this file.")


def parse_text(file_content):
    def is_integer(value):
        return value.isnumeric() or (value[0] == '-' and value[1:].isnumeric())
    separated_items = file_content.split()
    for item in separated_items:
        if not is_integer(item):
            raise ValueError('input file must only contain integers separated by space')
    return [int(i) for i in separated_items]


def find_all_pairs_with_sum_target(numbers, target):
    seen_numbers_count = {}
    result = []
    for number in numbers:
        seen_numbers = seen_numbers_count.keys()
        if target - number in seen_numbers \
                and seen_numbers_count[target - number] > 0:
            result.append([number, target - number])
        elif number in seen_numbers:
            seen_numbers_count[number] += 1
        else:
            seen_numbers_count[number] = 1

    return result


def main():
    file_path = input('enter file path>')
    if not file_path:
        raise Exception('file path cannot be an empty string')
    file_content = read_from_file(file_path)
    numbers = parse_text(file_content)
    try:
        target = int(input('enter target number>'))
    except Exception:
        raise TypeError('target must be an integer.')
    result = find_all_pairs_with_sum_target(numbers, target)
    if result:
        for pair in result:
            print(pair)
    else:
        print('No pairs found')


if __name__ == '__main__':
    main()
