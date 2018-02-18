""" Password & Cookie Hashing/Verification Tools """

import string
import random
import hashlib

def make_salt():
    """ Creates the salt that is tacked onto the end of the password to improve encryption. """
    return ''.join([random.choice(string.ascii_letters) for f in range(5)])

def make_pw_hash(password, salt=None):
    """ Creates the actual password hash with the salt included.
        Takes the entered password as a string.
        Takes an optional salt, also a string, which defaults to None. """
    if not salt:
        salt = make_salt()
    new_hash = hashlib.sha256(str.encode(password + salt)).hexdigest()  # creates a unique user hash from the combined pw and salt
    return '{0},{1}'.format(new_hash, salt)  # returns the new hash, including the salt so user can be verified later

def check_pw_hash(password, hashy):
    """ Checks the entered password against the hash stored for the user in the DB.
        Takes the entered password as a string, and the original hash stored for the user. """
    salt = hashy.split(',')[1]  # gets the users original salt so that when it creates the new hash it will match
    test_hash = make_pw_hash(password, salt)
    if test_hash == hashy:
        return True
    return False

