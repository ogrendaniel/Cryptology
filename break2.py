
from math import gcd
from collections import Counter
from functools import reduce
import numpy as np
import itertools


# Known Swedish letter frequencies, from https://en.wikipedia.org/wiki/Letter_frequency#cite_note-30
swedish_letter_frequencies = {
    0: 0.09383,
    1: 0.01535,
    2: 0.01486,
    3: 0.04702,
    4: 0.10149,
    5: 0.02027,
    6: 0.02862,
    7: 0.02090,
    8: 0.05817,
    9: 0.00614,
    10: 0.03140,
    11: 0.05275,
    12: 0.03471,
    13: 0.08542,
    14: 0.04482,
    15: 0.01839,
    16: 0.00020,
    17: 0.08431,
    18: 0.06590,
    19: 0.07691,
    20: 0.01919,
    21: 0.02415,
    22: 0.00142,
    23: 0.00159,
    24: 0.00708,
    25: 0.00070,
    26: 0.0134,
    27: 0.0180,
    28: 0.0131
    } 

alphabet = 'abcdefghijklmnopqrstuvwxyzåäö'
alphabet_length = len(alphabet)
# The index of coincidence for swedish is 0.0681
ic_swedish = 0.0681

# Function to decrypt a ciphertext using the Vigenere cipher
# Input: ciphertext and key
# Output: plaintext
def vigenere_decrypt(cipher_text, key):
    key_length = len(key)
    key_as_int = key#[alphabet.index(char) for char in key.lower()]
    cipher_text_int = [alphabet.index(char) for char in cipher_text.lower()]
    plain_text = ''

    for i in range(len(cipher_text_int)):
        value = (cipher_text_int[i] - key_as_int[i % key_length]) % alphabet_length
        plain_text += alphabet[value]

    return plain_text

# def find_trigrams_and_distances(text):
#     trigrams = {}
#     # Loop through the text to extract each sequence of three consecutive characters (trigrams)
#     for i in range(len(text) - 2):
#         trigram = text[i:i+3]  # Extract a trigram starting at the current position
#         if trigram not in trigrams:
#             trigrams[trigram] = []  # If this trigram is new, initialize an empty list for it
#         trigrams[trigram].append(i)  # Append the current position (index) of the trigram

#     distances = {}
#     # Now, for each trigram, calculate the distances between its occurrences
#     for trigram, positions in trigrams.items():
#         if len(positions) > 1:  # Only process trigrams that occur more than once
#             # Calculate the distance between consecutive occurrences of the trigram
#             distances[trigram] = [positions[i] - positions[i-1] for i in range(1, len(positions))]

#     return distances

# Function used to find the distances between bigrams in a text
# Input: text
# Output: dictionary with bigrams as keys and a list of distances between the bigrams as values
def find_bigrams_and_distances(text):
    bigrams = {}
    # Loop through the text to extract each pair of consecutive characters (bigrams)
    for i in range(len(text) - 1):
        bigram = text[i:i+2]  # Extract a bigram starting at the current position
        if bigram not in bigrams:
            bigrams[bigram] = []  # If this bigram is new, initialize an empty list for it
        bigrams[bigram].append(i)  # Append the current position (index) of the bigram

    distances = {}
    # Now, for each bigram, calculate the distances between its occurrences
    for bigram, positions in bigrams.items():
        if len(positions) > 1:  # Only process bigrams that occur more than once
            # Calculate the distance between consecutive occurrences of the bigram
            # This is done by subtracting the position of each occurrence from the next one
            distances[bigram] = [positions[i] - positions[i-1] for i in range(1, len(positions))]

    return distances


# Function used to find the greatest common divisor (GCD) of a list of numbers
# Input: list of numbers
# Output: GCD of the numbers
def find_gcd_of_list(numbers):
    return reduce(gcd, numbers)

# Function used to find the potential key lengths of a ciphertext
# Input: ciphertext
# Output: list of potential key lengths
def find_potential_key_lengths(ciphertext,max_16):
    bigram_distances = find_bigrams_and_distances(ciphertext)
    gcd_counter = Counter()

    # Calculate GCDs for each bigram and count their frequencies
    for distances in bigram_distances.values():
        if len(distances) > 1:
            gcd_value = find_gcd_of_list(distances)
            gcd_counter[gcd_value] += 1

    # Identify the most common GCDs
    most_common_gcds = gcd_counter.most_common()
    
    # Extract potential key lengths from the most common GCDs
    potential_key_lengths = [gcd_value for gcd_value, _ in most_common_gcds]
    print(f"Potential Key Lengths: {potential_key_lengths}")
    
    if max_16:
        potential_key_lengths = filter_out_key_lengths(potential_key_lengths)
    
    return potential_key_lengths    
    
    
# Consider the most common GCDs as potential key lengths
# print(f"Potential Key Lengths: {find_potential_key_lengths(text)}")


# HACK can be used to filter out key lengths that are too long
def filter_out_key_lengths(key_lengths):
    return [key_length for key_length in key_lengths if key_length <= 16]
# only_keys_under_16 = []
# for i in potential_key_lengths:
#     if i <= 16:
#         only_keys_under_16.append(i)
# print(only_keys_under_16)

# Determine the different keys inside only_keys_under_16 by using frequency analysis
# and the fact that the key length is known by using the swedish letter frequencies
# and the fact that the key length is known

# -----------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------
""" To find the correct key length from the potential key lengths, the index of coincidence (IC) can be used."""



#Calculate the IC for all groups of letters with the same shift and compare to the IC for the Swedish language
# Do this for all potential key lengths
# The key length with the smallest difference between the IC for the Swedish language and the IC for the cipher text
# is the correct key length


# Function used to group letters in a text by their shift
# Input: text and shift
# Output: list of groups of letters with the same shift
# Example: group_letters_by_shift("abcdef", 3) -> ["ad", "be", "cf"]
def group_letters_by_shift(text, shift):
    groups = []
    for i in range(shift):
        groups.append(text[i::shift])
    return groups

# Function used to calculate the index of coincidence for a group of letters
# Input: group of letters
# Output: index of coincidence for the group
def calculate_ic(group):
    frequencies = Counter(group)
    n = len(group)
    ic = sum(f * (f - 1) for f in frequencies.values()) / (n * (n - 1))
    return ic


    
""" For all potential key lengths calculate the IC for all groups of letters with the same shift and take the average ic from these groups
    and compare to the IC for the Swedish language.
    The key length which has the smallest difference between the average IC for all groups of letters with the same shift and the IC for 
    the Swedish language is the correct key length"""

# Function used to find the best key length based on the index of coincidence
# Input: text, potential key lengths, index of coincidence for the Swedish language
# Output: best key length
def find_best_key_length_based_on_ic(text, potential_key_lengths):
    best_key_length = 0 # Save the best key length
    closest_ic_difference = float('inf') # Save the closest IC difference

    for key_length in potential_key_lengths:
        groups = group_letters_by_shift(text, key_length)
        total_ic = sum(calculate_ic(group) for group in groups)

        average_ic = total_ic / key_length
        ic_difference = abs(average_ic - ic_swedish)
        # print(f"Key length: {key_length}, IC difference: {ic_difference}")
        if ic_difference < closest_ic_difference:
            closest_ic_difference = ic_difference
            best_key_length = key_length

    return best_key_length

# best_key_length = find_best_key_length_based_on_ic(text, find_potential_key_lengths(text))
# print(f"Best key length: {best_key_length}")

# -----------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------

""" Now that the key length is known, the cipher text can be split into groups of letters with the same shift and 
    frequency analysis can be used to find the key"""


# Function used to convert a text from alphabet to numbers
# Input: text
# Output: list of numbers
# Example: from_alphabet_to_numbers("abc") -> [0, 1, 2]
def from_alphabet_to_numbers(text):
    return [alphabet.index(char) for char in text.lower()]

# Function used to convert a list of numbers to a text
# Input: list of numbers
# Output: text
# Example: from_numbers_to_alphabet([0, 1, 2]) -> "abc"
def from_numbers_to_alphabet(numbers):
    return ''.join(alphabet[i] for i in numbers)

def find_best_shift_for_group(group, group_number):    
    group = Counter(group)
    # add all letters not in the group to the group so it has all letters
    for letter in alphabet:
        if letter not in group:
            group[letter] = 0
    # sort the group by letter so it is in the same order as the letter_frequencies
    group = sorted(group.items(), key=lambda x: x[0])
    
    # Calculate the expected frequencies, i.e. the frequencies of the letters in the group if the group was in Swedish
    total_letters = len(group)
    expected_freqs = [freq * total_letters for freq in swedish_letter_frequencies.values()]
    expected_freqs = np.array(expected_freqs)
    # get the actual frequencies, i.e. the frequencies of the letters in the group
    actual_freqs = [freq for _, freq in group]
    actual_freqs = np.array(actual_freqs)
    
    # Calculate the chi square values for all shifts
    chi_square_list = []
    chisquare = 0
    
    for i in range(alphabet_length):
       chisquare = sum((actual_freqs - np.roll(expected_freqs,i))**2 / np.roll(expected_freqs,i))
       chi_square_list.append(chisquare)
       chisquare = 0
    # get the five best shifts which are the three smallest chi_square values indexes
    best_shifts = np.argsort(chi_square_list)[:1]
    # print(f"\nGroup number: {group_number}, best shifts: {best_shifts}")
    # print(f"\nChi square values: {chi_square_list}")
    # best_shift = chi_square_list.index(min(chi_square_list))
    return best_shifts

# Function used to find the best shifts for all groups of letters with the same shift
# Input: text, max_16 as a boolean, if true only key lengths under 16 are considered
# Output: list of best shifts for all groups of letters with the same shift
def get_best_shifts_for_all_groups(text,max_16):
    groups = group_letters_by_shift(text, find_best_key_length_based_on_ic(text, find_potential_key_lengths(text,max_16)))
    best_shifts = []
    for group in groups:
        best_shift = find_best_shift_for_group(group, groups.index(group))
        best_shifts.append(best_shift)
    return best_shifts
    
# best_shifts = get_best_shifts_for_all_groups()
# print("best_shifts",best_shifts)

"""Check all divisors of the key length and compare which of the keys that gives the closest IC to the IC for the Swedish language"""

def find_best_key(ciphertext, key_length):
    # Find all divisors of the key length not including 1
    print(f"Key length: {key_length}")
    divisors = [i for i in range(2, key_length+1) if key_length % i == 0]
    print(f"Divisors: {divisors}")    
    best_ic = 0
    best_key = None
    for divisor in divisors:
        # Split the ciphertext into groups of letters with the same shift
        groups = group_letters_by_shift(ciphertext, divisor)
        # Find the best shift for each group
        best_shifts = [find_best_shift_for_group(group, groups.index(group)) for group in groups]
        # Generate all possible keys
        possible_keys = generate_all_possible_keys(best_shifts)
        # Find the most likely decryption of the ciphertext
        best_key, best_decryption, ic = find_most_likely_decryption(ciphertext, possible_keys)
        # Check if the IC for this key is better than the best IC so far
        if abs(ic - ic_swedish) < abs(best_ic - ic_swedish):
            best_ic = ic
            best_key = best_key
    
    print(f"Best key: {best_key}")
    return best_key
    

        
    # best_ic = 0
    # best_key = None
    # best_decryption = ""

    # for key in possible_keys:
    #     decrypted_text = vigenere_decrypt(ciphertext, key)
    #     ic = calculate_ic(decrypted_text)
    #     if abs(ic - ic_swedish) < abs(best_ic - ic_swedish):
    #         best_ic = ic
    #         best_key = from_numbers_to_alphabet(key)
    #         best_decryption = decrypted_text

    # return best_key, best_decryption, best_ic


"""Since the chi square values does not always give the correct shift, the chi square values for the three 
    best shifts are used to generate all possible keys. Which then are used to decrypt the cipher text and check which of the decrypted texts
    that has the closest IC to the IC for the Swedish language. The key used to decrypt that cipher text is likely the correct key."""

# Function used to generate all possible keys
# Input: list of best shifts for all groups of letters with the same shift
# Output: list of all possible keys , i.e. all combinations of the best shifts, when using the three best shifts it is 3^key_length
def generate_all_possible_keys(all_shifts):
    # Generate all combinations of these shifts
    possible_keys = list(itertools.product(*all_shifts))
    return possible_keys


# Function used to find the most likely decryption of a ciphertext, given a list of possible keys it checks which key gives the decryption 
# with the closest IC to the IC for the Swedish language
# Input: ciphertext, possible keys, index of coincidence for the Swedish language
# Output: best key, best decryption, best IC
def find_most_likely_decryption(ciphertext, possible_keys):
    best_ic = 0
    best_key = None
    best_decryption = ""

    for key in possible_keys:
        decrypted_text = vigenere_decrypt(ciphertext, key)
        ic = calculate_ic(decrypted_text)
        if abs(ic - ic_swedish) < abs(best_ic - ic_swedish):
            best_ic = ic
            best_key = from_numbers_to_alphabet(key)
            best_decryption = decrypted_text

    return best_key, best_decryption, best_ic



# Example usage
# possible_keys = generate_all_possible_keys(best_shifts) 

# best_key, best_decryption, best_ic = find_most_likely_decryption(text, possible_keys, ic_swedish)
# print(f"The most likely key is: {from_numbers_to_alphabet(best_key)}")
# print(f"With a decryption of: {best_decryption}")
# print(f"And an IC of: {best_ic}")
    









# a = 0 , b = 1, c = 2, d = 3, e = 4, f = 5, g = 6, h = 7, i = 8, j = 9, k = 10, l = 11, m = 12, n = 13, o = 14, p = 15, 
# q = 16, r = 17, s = 18, t = 19, u = 20, v = 21, w = 22, x = 23, y = 24, z = 25, å = 26, ä = 27, ö = 28


# key = from_numbers_to_alphabet(best_shifts)
# print(f"The key is: {key}")

# #compare the key with the key used to encrypt the cipher text
# # if any character in the key is wrong, print the index of the character and the correct character
# # if the key is correct, print "The key is correct"
# correct_key = "datainspektionen"
# for i in range(len(key)):
#     if key[i] != correct_key[i]:
#         print(f"Wrong character at index {i}, should be {corr