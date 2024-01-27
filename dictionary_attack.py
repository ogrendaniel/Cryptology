import create_dict
import encrypt
import break2

ic_swedish = 0.0681


# dictionary with keys as numbers and values as swedish words with that length, longest word is 37 letters long
input_file_path = 'final_word_length_dict.txt'
swedish_words = create_dict.load_dictionary_from_file(input_file_path)


# Uses kasiski examination to find the most likely key length then friedman test to find the most likely key of the given lengths from
# the kasiski examination. This is the input "key_length".
# "Key_length" is then split into its divisors to check which of the divisors gives the best ic value. 
# The best key length is then used to find the most likely key from the swedish dictionary by decrypting the ciphertxt with all possible words
# inside the swedish_dictionary with the best key length.

def find_best_key_with_dictionary(ciphertext, key_length):
    print(f"Key length: {key_length}")
    divisors = [i for i in range(2, key_length+1) if key_length % i == 0]
    print(f"Divisors: {divisors}")    
    best_ic = 0
    best_key = None
    for divisor in divisors:
        # Split the ciphertext into groups of letters with the same shift
        groups = break2.group_letters_by_shift(ciphertext, divisor)
        # Find the best shift for each group
        best_shifts = [break2.find_best_shift_for_group(group, groups.index(group)) for group in groups]
        # Generate all possible keys
        possible_keys = break2.generate_all_possible_keys(best_shifts)
        # Find the most likely decryption of the ciphertext
        found_key, best_decryption, ic = break2.find_most_likely_decryption(ciphertext, possible_keys)
        if abs(ic - ic_swedish) < abs(best_ic - ic_swedish):
            best_ic = ic
            best_key = found_key
    best_key_length = len(best_key)
    
    if(best_key_length not in swedish_words):
        print("Key length not in swedish_words")
        return None
    else:
        # possible_keys=swedish_words[best_key_length] 
        possible_keys = []
        for words_list in swedish_words.values():
            for word in words_list:
                possible_keys.append(word)

        
        found_key, best_decryption, ic = find_most_likely_decryption_with_dictionary(ciphertext, possible_keys)
        return found_key


def find_most_likely_decryption_with_dictionary(ciphertext, possible_keys):
    best_ic = 0
    best_key = None
    best_decryption = ""

    for key in possible_keys:
        decrypted_text = encrypt.vigenere_decrypt(ciphertext, key)
        ic = break2.calculate_ic(decrypted_text)
        if abs(ic - ic_swedish) < abs(best_ic - ic_swedish):
            best_ic = ic
            best_key = key
            best_decryption = decrypted_text

    return best_key, best_decryption, best_ic