from rsa import newkeys, PublicKey, PrivateKey, encrypt, decrypt
from json import loads, dumps
from base64 import b64encode, b64decode


def generate_pub(json: str):
    try:
        json = loads(json)
    except:
        return -1 # Data is not proper json
    try:
        n = json['n'] # p x q
        e = json['e'] # Something in 1 < x < lcm(p − 1, q − 1)
    except:
        return -2 # The parsed json does not contain the arguments needed for making a public key
    try:
        return PublicKey(n, e)
    except:
        return -3 # Cannot create a public key with the arguments


def generate_priv(json: str):
    try:
        json = loads(json)
    except:
        return -1 # Data is not proper json
    try:
        n = json['n'] # p x q
        e = json['e'] # Something in 1 < x < lcm(p − 1, q − 1)
        d = json['d']
        p = json['p'] # First prime
        q = json['q'] # Second prime
    except:
        return -2 # The parsed json does not contain the arguments needed for making a private key
    try:
        return PrivateKey(n, e, d, p, q)
    except:
        return -3 # Cannot create a private key with the arguments


def get_json_from_priv_key(key: PrivateKey):
    # Gets all the arguments stored in the key and returns a dictionary
    return dumps({
        'n': key.n,
        'e': key.e,
        'd': key.d,
        'p': key.p,
        'q': key.q
    })


def generate_pair(length: int):
    if length < 150:
        return -1 # The length is not long enough
    priv = newkeys(length, 1, 10)[1]
    return get_json_from_priv_key(priv) # Returns a dictionary containing all the variables needed in order to create both public and private keys


def encrypt_with_json_key(json: str, data: str):
    data = b64decode(data.encode())
    json = generate_pub(json)

    '''
    When you cast negative numbers into bool, you get False.
    When you cast PrivateKey instances into bool, you get True.
    When there's a problem, the generate_priv functions returns a negative number;
    and when it succeeds, it returns a PrivateKey instance.
    If the returned object is a negative number, it will be like this:

        if not False:
            return json - 1

        Not False is true, so, the decrypt_with_json_key will return the error code - 1
        (ig: we get -1, we return -2)

    If the returned object is a PrivateKey instance:

        if not True:
            return json - 1

        Not True is false, so, we won't return anything.
    '''

    if not json:
        return json - 1
    try:
        return b64encode(encrypt(data, json)).decode()
    except:
        return -5 # Cannot encrypt data


def decrypt_with_json_key(json: str, data_base64: str):
    data = b64decode(data_base64.encode()) # Decodes the encrypted data
    json = generate_priv(json) # Turns the json data into a private key

    '''
    When you cast negative numbers into bool, you get False.
    When you cast PrivateKey instances into bool, you get True.
    When there's a problem, the generate_priv functions returns a negative number;
    and when it succeeds, it returns a PrivateKey instance.
    If the returned object is a negative number, it will be like this:

        if not False:
            return json - 1

        Not False is true, so, the decrypt_with_json_key will return the error code - 1
        (ig: we get -1, we return -2)

    If the returned object is a PrivateKey instance:

        if not True:
            return json - 1

        Not True is false, so, we won't return anything.
    '''
    if not json:
        return json - 1

    try:
        return decrypt(data, json).decode()
    except:
        return -5 # Cannot decrypt the data
