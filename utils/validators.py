def is_valid_command(line):
    command = line.replace('\n', '').split(' ')
    if command[0].upper() == 'C' and len(command) == 3:
        return True
    elif command[0].upper() == 'L' and len(command) == 5:
        return True
    elif command[0].upper() == 'R' and len(command) == 5:
        return True
    elif command[0].upper() == 'B' and len(command) == 4:
        return True
    else:
        return False
