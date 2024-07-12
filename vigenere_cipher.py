# code with comments, comments are added using chat gpt, orginal code without comments is written below this code. It is commented out.
import string
import re

def process_file_content(filename):
    # Read the file content
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    # Remove all characters except lowercase alphabets
    text = re.sub(r'[^a-z]', '', text.lower())

    return text

def letter_distribution(s):
    '''Consider the string s which comprises only lowercase letters.
    Count the number of occurrences of each letter and return a dictionary.'''

    # Initialize an empty dictionary to store the counts
    letter_counts = {}

    # Iterate over each character in the string
    for char in s:
        if char in letter_counts:
            # If the character is already in the dictionary, increment its count
            letter_counts[char] += 1
        else:
            # If the character is not in the dictionary, add it with count 1
            letter_counts[char] = 1

    return letter_counts

def sort_list_of_tuples(tuples_list):
    # Sort the list of tuples by the second element in descending order
    sorted_tuples = sorted(tuples_list, key=lambda x: x[1], reverse=True)
    return sorted_tuples

def substitution_encrypt(s, d):
    '''Encrypt the contents of s using the dictionary d which comprises of
    the substitutions for the 26 letters. Return the resulting string.'''

    # Initialize an empty list to store the encrypted characters
    encrypted_text = []

    # Iterate over each character in the string
    for char in s:
        if char in d:
            # Substitute the character using the dictionary
            encrypted_text.append(d[char])

    # Join the list into a single string and return it
    return ''.join(encrypted_text)

# Define the encryption mapping for the substitution cipher
encryption_mapping = {
    'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u',
    'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c',
    'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k',
    'y': 'l', 'z': 'm'
}

def substitution_decrypt(s, d):
    '''Decrypt the contents of s using the dictionary d which comprises of
    the substitutions for the 26 letters. Return the resulting string.'''

    # Reverse the dictionary to use it for decryption
    reversed_d = {v: k for k, v in d.items()}

    # Initialize an empty list to store the decrypted characters
    decrypted_text = []

    # Iterate over each character in the string
    for char in s:
        if char in reversed_d:
            # Substitute the character using the reversed dictionary
            decrypted_text.append(reversed_d[char])

    # Join the list into a single string and return it
    return ''.join(decrypted_text)

def cryptanalyse_substitution(s):
    '''Given that the string s is given to us and it is known that it was
    encrypted using some substitution cipher, predict the substitution dictionary.'''

    # Get the letter frequency distribution
    letter_counts_of_a = letter_distribution(s)

    # Sort the letters by frequency in descending order
    sorted_counts = sort_list_of_tuples(list(letter_counts_of_a.items()))

    # Generate the mapping based on frequency analysis
    generated_mapping = {
        'e': sorted_counts[0][0], 't': sorted_counts[1][0], 'a': sorted_counts[2][0], 
        'o': sorted_counts[3][0], 'i': sorted_counts[4][0], 'n': sorted_counts[5][0],
        's': sorted_counts[6][0], 'h': sorted_counts[7][0], 'r': sorted_counts[8][0], 
        'd': sorted_counts[9][0], 'l': sorted_counts[10][0], 'c': sorted_counts[11][0], 
        'u': sorted_counts[12][0], 'm': sorted_counts[13][0], 'w': sorted_counts[14][0], 
        'f': sorted_counts[15][0], 'g': sorted_counts[16][0], 'y': sorted_counts[17][0],
        'p': sorted_counts[18][0], 'b': sorted_counts[19][0], 'v': sorted_counts[20][0], 
        'k': sorted_counts[21][0], 'j': sorted_counts[22][0], 'x': sorted_counts[23][0],
        'q': sorted_counts[24][0], 'z': sorted_counts[25][0]
    }

    return generated_mapping

def check(encryption_mapping, generated_mapping):
    # Compare the generated mapping with the original encryption mapping
    list_of_encrypted_mapping = list(encryption_mapping.items())
    list_of_generated_mapping = list(generated_mapping.items())
    c = 0
    for item in list_of_generated_mapping:
        if item in list_of_encrypted_mapping:
            c += 1
    return c

# Vigenère Cipher Functions

def vigenere_encrypt(s, password):
    '''Encrypt the string s using the Vigenère cipher with the given password.'''
    s = s.upper()
    password = password.upper()
    a = len(s) // len(password)
    b = len(s) % len(password)
    list_multiple_psd = password * a + password[:b]
    list_encoded_string = []
    for c1, c2 in zip(list(s), list(list_multiple_psd)):
        av = (ord(c1) + ord(c2)) % 26 + 65
        list_encoded_string.append(chr(av))
    return (''.join(list_encoded_string)).lower()

# Assuming all the characters of s and passwords are in upper case
def vigenere_decrypt(s, password):
    '''Decrypt the string s using the Vigenère cipher with the given password.'''
    s = s.upper()
    password = password.upper()
    a = len(s) // len(password)
    b = len(s) % len(password)
    list_multiple_psd = password * a + password[:b]
    list_decrypted_string = []
    for c1, c2 in zip(list(s), list(list_multiple_psd)):
        av = (ord(c1) - ord(c2)) % 26 + 65
        list_decrypted_string.append(chr(av))
    return (''.join(list_decrypted_string)).lower()

def collision_freq(s1, s2):
    '''Calculate the collision frequency between two strings s1 and s2.'''
    count = 0
    for c1, c2 in zip(s1, s2):
        if c1 == c2:
            count += 1
    return count / len(s1)

def rotate_compare(s, r):
    '''Rotate the string s with its rotation by r positions, and find the collision frequency between original encrypted string and the rotated encrypted string.'''
    sr = s[:]
    for i in range(r):
        first = sr[0]
        sr = sr[1:] + first
    return collision_freq(s, sr)

def cryptanalyse_vigenere_findlength(s):
    '''Given the string s, find out the length of the password used in the Vigenère cipher.'''
    r = 0
    while True:
        r += 1
        cf = rotate_compare(s, r)
        if 0.055 <= cf <= 0.068:
            return r

def divide(encrypted_text, r):
    '''Divide the encrypted text into r substrings for Vigenère cipher analysis.'''
    keyth = {}
    for i in range(r):
        keyth[i] = encrypted_text[i::r]
    return keyth

def cryptanalyse_vigenere_afterlength(s, k):
    '''Given the string s encrypted with a Vigenère cipher and password length k, find the password.'''
    key = divide(s, k)
    key_value = []
    for k in key:
        gm = cryptanalyse_substitution(''.join(key[k]))['e']
        key_value.append(chr(ord(gm) - 4))
    return key_value

def cryptanalyse_vigenere(s):
    '''Given the string s, cryptanalyse Vigenère cipher, output the password and plaintext.'''
    r = cryptanalyse_vigenere_findlength(s)
    key_value = cryptanalyse_vigenere_afterlength(s, r)
    decrypted_text = vigenere_decrypt(s, ''.join(key_value))
    return key_value

# Read the input text from the file
with open('english_random.txt', 'r') as f:
    text = f.read()

# Encrypt the text using the Vigenère cipher with a known password
encrypted_text = vigenere_encrypt(text, 'iitropar')

# Cryptanalyse the encrypted text to find the password
key_value = ''.join(cryptanalyse_vigenere(encrypted_text))

# Replace specific characters in the recovered key. This is very specific to my code. I fixed some bugs using this.
key_value = key_value.replace(']', 'w')
key_value = key_value.replace('^', 'x')
key_value = key_value.replace('_', 'y')
key_value = key_value.replace('`', 'z')

# Print the recovered key
print(key_value)








#THIS IS ORIGINAL CODE WRITTEN WITHOUT COMMENTS

# import string
# import re

# def process_file_content(filename):
#     # Read the file content
#     with open(filename, 'r', encoding='utf-8') as file:
#         text = file.read()

#     # Remove all characters except lowercase alphabets
#     text = re.sub(r'[^a-z]', '', text.lower())

#     return text

# def letter_distribution(s):
#     '''Consider the string s which comprises only lowercase letters.
#     Count the number of occurrences of each letter and return a dictionary.'''

#     # Initialize an empty dictionary to store the counts
#     letter_counts = {}

#     # Iterate over each character in the string
#     for char in s:
#         if char in letter_counts:
#             # If the character is already in the dictionary, increment its count
#             letter_counts[char] += 1
#         else:
#             # If the character is not in the dictionary, add it with count 1
#             letter_counts[char] = 1

#     return letter_counts

# def sort_list_of_tuples(tuples_list):
#     sorted_tuples = sorted(tuples_list, key=lambda x: x[1], reverse=True)
#     return sorted_tuples

# def substitution_encrypt(s, d):
#     '''Encrypt the contents of s using the dictionary d which comprises of
#     the substitutions for the 26 letters. Return the resulting string.'''

#     # Initialize an empty list to store the encrypted characters
#     encrypted_text = []

#     # Iterate over each character in the string
#     for char in s:
#         if char in d:
#             # Substitute the character using the dictionary
#             encrypted_text.append(d[char])

#     # Join the list into a single string and return it
#     return ''.join(encrypted_text)

# encryption_mapping = {
#     'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u',
#     'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c',
#     'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k',
#     'y': 'l', 'z': 'm'
# }

# def substitution_decrypt(s, d):
#     '''Decrypt the contents of s using the dictionary d which comprises of
#     the substitutions for the 26 letters. Return the resulting string.'''

#     # Reverse the dictionary
#     reversed_d = {v: k for k, v in d.items()}

#     # Initialize an empty list to store the decrypted characters
#     decrypted_text = []

#     # Iterate over each character in the string
#     for char in s:
#         if char in reversed_d:
#             # Substitute the character using the reversed dictionary
#             decrypted_text.append(reversed_d[char])

#     # Join the list into a single string and return it
#     return ''.join(decrypted_text)


# def cryptanalyse_substitution(s):
#   '''Given that the string s is given to us and it is known that it was
#   encrypted using some substitution cipher, predict the d'''
#   letter_counts_of_a = letter_distribution(s)
#   so = sort_list_of_tuples(list(letter_counts_of_a.items()))
#   generated_mapping = {'e': so[0][0], 't': so[1][0], 'a': so[2][0], 'o': so[3][0], 'i': so[4][0], 'n': so[5][0],
#            's': so[6][0], 'h': so[7][0], 'r': so[8][0], 'd': so[9][0], 'l': so[10][0], 'c': so[11][0], 'u': so[12][0],
#            'm': so[13][0], 'w': so[14][0], 'f': so[15][0], 'g': so[16][0], 'y': so[17][0],
#            'p': so[18][0], 'b': so[19][0], 'v': so[20][0], 'k': so[21][0], 'j': so[22][0], 'x': so[23][0],
#            'q': so[24][0], 'z': so[25][0]
#            }
#   return generated_mapping


# def check(encryption_mapping, generated_mapping):
#   list_of_encrpted_mapping = list(encryption_mapping.items())
#   list_of_generated_mapping = list(generated_mapping.items())
#   c = 0
#   for item in list_of_generated_mapping:
#     if item in list_of_encrpted_mapping:
#       c += 1
#   return c


# #VIGENERE CIPHER

# def vigenere_encrypt(s, password):
#   s = s.upper()
#   password = password.upper()
#   a = len(s) // len(password)
#   b = len(s) % len(password)
#   list_multiple_psd = password*a + password[:b]
#   list_encoded_string = []
#   for c1, c2 in zip(list(s), list(list_multiple_psd)):
#     av = (ord(c1) + ord(c2))%26 + 65
#     list_encoded_string.append(chr(av))

#   return (''.join(list_encoded_string)).lower()


# #assuming all the characters of s and passwords are in upper case
# def vigenere_decrypt(s, password):
#   s = s.upper()
#   password = password.upper()
#   a = len(s) // len(password)
#   b = len(s) % len(password)
#   list_multiple_psd = password*a + password[:b]
#   list_decrypted_string = []
#   for c1, c2 in zip(list(s), list(list_multiple_psd)):
#     av = (ord(c1) - ord(c2))%26 + 65
#     list_decrypted_string.append(chr(av))

#   return (''.join(list_decrypted_string)).lower()


# def collision_freq(s1, s2):
#   count = 0
#   for c1, c2 in zip(s1, s2):
#     if c1 == c2:
#       count += 1
#   return count/len(s1)


# def rotate_compare(s, r):
#   sr = s[:]
#   for i in range(r):
#     first = sr[0]
#     sr = sr[1:] + first
#   return collision_freq(s, sr)


# def cryptanalyse_vigenere_findlength(s):
#   '''Given just the string s, find out the length of the password using which
#   some text has resulted in the string s. We just need to return the number
#   k'''
#   r = 0
#   while True:
#     r += 1
#     cf = rotate_compare(s, r)
#     if 0.055 <= cf <= 0.068:
#       return r
    

# def divide(encrypted_text, r):
#   keyth = {}
#   for i in range(r):
#     keyth[i] = encrypted_text[i::r]
#   return keyth


# def cryptanalyse_vigenere_afterlength(s,k):
#   '''Given the string s which is known to be vigenere encrypted with a
#   password of length k, find out what is the password'''
#   key = divide(s, k)
#   key_value = []
#   for k in key:
#     gm = cryptanalyse_substitution(''.join(key[k]))['e']
#     key_value.append(chr(ord(gm)-4))
#   return key_value





# def cryptanalyse_vigenere(s):
#   '''Given the string s cryptanalyse vigenere, output the password as well as
#   the plaintext'''
#   r = cryptanalyse_vigenere_findlength(s)
#   key_value = cryptanalyse_vigenere_afterlength(s, r)
#   decrypted_text = vigenere_decrypt(s, ''.join(key_value))
#   return key_value





# f = open('english_random.txt', 'r')
# text = f.read()
# encrypted_text = vigenere_encrypt(text,'swapnil')
# key_value = ''.join(cryptanalyse_vigenere(encrypted_text))
# key_value = key_value.replace(']', 'w')
# key_value = key_value.replace('^', 'x')
# key_value = key_value.replace('_', 'y')
# key_value = key_value.replace('`', 'z')
# print(key_value)
