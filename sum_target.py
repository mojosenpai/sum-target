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