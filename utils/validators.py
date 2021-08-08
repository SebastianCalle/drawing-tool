import re

def is_valid_command(line):
    regex_validators = {
        "C": re.compile('[C] [1-9][0-9]? [1-9][0-9]?$'),
        "L": re.compile('[L] [1-9][0-9]? [1-9][0-9]? [1-9][0-9]? [1-9][0-9]?$'),
        "R": re.compile('[R] [1-9][0-9]? [1-9][0-9]? [1-9][0-9]? [1-9][0-9]?$'),
        "B": re.compile('[B] [1-9][0-9]? [1-9][0-9]? [a-z]$')

    }
    command = line.replace('\n', '').split(' ')
    print(command)
    print(line)
    if re.match(regex_validators.get(command[0], None), line):
        return True
    return False

