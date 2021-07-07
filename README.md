# pySAcli
This is a cli(commandline interface) RSA encryption/decryption/generation tool, designed to work with json input and output.

# Requirements
This tool relies on the [RSA library for python](https://github.com/sybrenstuvel/python-rsa/).

# Installing the required library on linux
- Make sure that you have python3 and pip3 installed.
- Write `python3 -m pip install rsa` in your terminal.

# Installing the required library on windows
- Make sure that you have python3 installed (get it from [python.org](https://www.python.org)).
- Write `pip install rsa` in your terminal.


# Installing the required library on macOS
- I'm poor. I dunno how that shit works. Figure it out, yourself.

# Why?
Well, some languages (mostly low-level ones) don't exactly have the easiest ways to use RSA. This tool makes it easier for you to use the rsa library in an easy way. It can also be used for simple manual encryption and decryption and key generation.

# Examples
## key generation
Go ahead and write `./cli.py gen '{"bitsize":200}'` in your terminal (`python cli.py gen '{"bitsize":200}'` if you're on windows).
The program will give you a json dictionary containing all values needed in order to create both public and private keys.

## Encryption
Go ahead and `./cli.py enc '{"e":[the e value that you got from the previous command], "n":[the n value that you got from the previous command], "data":"hello"}'` in your terminal (`python cli.py gen enc '{"e":[the e value that you got from the previous command], "n":[the n value that you got from the previous command], "data":"hello"}'` if you're on windows).
The program will give you a base64 string containing the encrypted version of 'hello'.

## Decryption
Go ahead and `./cli.py dec '{"e":[the e value that you got from the previous command], "n":[the n value that you got from the previous command], "d":[the d value that you got from the previous command], "p":[the p value that you got from the previous command], "q":[the q value that you got from the previous command], "data":"[base64 string the program gave you]"}'` in your terminal (`python cli.py dec '{"e":[the e value that you got from the previous command], "n":[the n value that you got from the previous command], "d":[the d value that you got from the previous command], "p":[the p value that you got from the previous command], "q":[the q value that you got from the previous command], "data":"[base64 string the program gave you]"}'` if you're on windows).
The program will give you 'hello'.
