import re

# swedish_words.txt from https://github.com/almgru/svenska-ord.txt
# svenska_ord.txt from https://github.com/dqvist12/alla-svenska-ord

def update_word_length_dictionary(file_path, word_dict):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Keep only Swedish lowercase letters
            word = re.sub(r'[^a-zåäö]+', '', line.strip().lower())
            if not word:
                continue
            word_length = len(word)
            if word_length not in word_dict:
                word_dict[word_length] = [word]
            else:
                if word not in word_dict[word_length]:
                    word_dict[word_length].append(word)

def save_dictionary_to_file(word_dict, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for length, words in sorted(word_dict.items()):
            for word in words:
                file.write(f"{word}\n")  # Save each word on its own line

# Initialize an empty dictionary
word_length_dict = {}

# Update the dictionary with words from the first file
# update_word_length_dictionary('swedish_words.txt', word_length_dict)

# # Update the dictionary with any additional words from the second file
# update_word_length_dictionary('svenska_ord.txt', word_length_dict)

# # Save the final dictionary to a file
# save_dictionary_to_file(word_length_dict, 'final_word_length_dict.txt')

def load_dictionary_from_file(input_file_path):
    word_dict = {}
    with open(input_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip()
            word_length = len(word)
            if word_length not in word_dict:
                word_dict[word_length] = [word]
            else:
                word_dict[word_length].append(word)
    return word_dict





