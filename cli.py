#!/bin/python3
from sys import argv
from encryptor import (dumps, loads, generate_pair,
                       encrypt_with_json_key,
                       decrypt_with_json_key)


help_msg = '''clirsa [mode] [json args]:
    clirsa enc:
        (RSA ENCRYPTOR)
        In this case, the json args must have an 'e', an 'n', and a 'data'.
        (confused? Please read about the rsa algorithm on the internet)
    clirsa dec:
        (RSA DECRYPTOR)
        In this case, the json args must have an 'e', an 'n', a 'd', a 'p', a 'q', and a 'data'.
        (confused? Please read about the rsa algorithm on the internet)
    clirsa gen:
        (RSA KEY GENERATOR)
        In this case, the json args must have a 'bitsize'.
        (confused? Please read about the rsa algorithm on the internet)
    '''

# The list of acceptable modes
commands = ['enc', 'dec', 'gen']

# Tells the program what arguments every mode requires the json input to have
required = {
    'enc': [
        'n', 'e', 'data'
    ],
    'dec': [
        'n', 'e',
        'd', 'p',
        'q', 'data'
    ],
    'gen': ['bitsize']
}


def enc(json: str):
    return encrypt_with_json_key(json, loads(json)['data'])


def dec(json: str):
    return decrypt_with_json_key(json, loads(json)['data'])


def gen(json: str):
    return generate_pair(loads(json)['bitsize'])

# Gives us a function based on the command
do = {
    'enc': enc,
    'dec': dec,
    'gen': gen
}

# Checks if all the members in the first list are present in the second list
def sublist(lst1, lst2):
    for i in lst1:
        if not i in lst2:
            return False

    return True


def main():
    if len(argv) != 3 or 'help' in ''.join(argv).lower(): # If there are not enough arguments or the user has used the word "help" in the args
        return help_msg

    if not argv[1] in commands:
        return 'UNKNOWN COMMAND'

    try:
        json = loads(argv[2])
    except:
        return 'NOT JSON'

    if type(json) != dict:
        return 'NOT A DICT'

    command = argv[1] # gen, enc, dec

    req = required[command]
    if not sublist(req, json.keys()):
        return 'NOT ALL KEYS ARE IN DATA'

    return do[command](dumps(json)) # Returns the output of the function it gets from 'do' based on the 'command'


if __name__ == "__main__":
    print(main()) # Prints the output of the main function. (the output of the function it gets from 'do' based on the 'command')
