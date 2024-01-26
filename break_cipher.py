# Description: Breaks a cipher text using a brute force method.
# Known Swedish letter frequencies
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

# swedish_letter_frequencies = {
#     0: 0.104,
#     1: 0.0131,
#     2: 0.0171,
#     3: 0.0490,
#     4: 0.0985,
#     5: 0.0181,
#     6: 0.0344,
#     7: 0.0285,
#     8: 0.0501,
#     9: 0.0090,
#     10: 0.0324,
#     11: 0.0481,
#     12: 0.0355,
#     13: 0.0845,
#     14: 0.0406,
#     15: 0.0157,
#     16: 0.0001,
#     17: 0.0788,
#     18: 0.0532,
#     19: 0.0889,
#     20: 0.0186,
#     21: 0.0255,
#     22: 0.00142,
#     23: 0.0011,
#     24: 0.0049,
#     25: 0.0004,
#     26: 0.0166,
#     27: 0.0210,
#     28: 0.0150
#     }
    
alphabet = 'abcdefghijklmnopqrstuvwxyzåäö'
alphabet_len = len(alphabet)



def vigenere_decrypt(cipher_text, key):
    key_length = len(key)
    key_as_int = key#[alphabet.index(char) for char in key.lower()]
    cipher_text_int = [alphabet.index(char) for char in cipher_text.lower()]
    plain_text = ''

    for i in range(len(cipher_text_int)):
        value = (cipher_text_int[i] - key_as_int[i % key_length]) % alphabet_len
        plain_text += alphabet[value]

    return plain_text

def find_bigrams_and_distances(text):
    bigrams = {}
    # Extracting bigrams and their positions
    for i in range(len(text) - 1):
        bigram = text[i:i+2]
        if bigram not in bigrams:
            bigrams[bigram] = []
        bigrams[bigram].append(i)

    distances = {}
    # Calculating distances for bigrams with multiple occurrences
    for bigram, positions in bigrams.items():
        if len(positions) > 1:
            distances[bigram] = [positions[i] - positions[i-1] for i in range(1, len(positions))]

    return distances

# Example usage
# Key length 13, key: administrativ
text = "sbwmbpwjgazmftgqtdivähtkxhdumoohgörrlqyåqsådzrcgltjgrdcwbqwjäldwdlvvödzwdclbqfssqsdmgtcmhfyewzgbizkjuwqfgazorvdvyhqtduwwqxmxjvrwmfkrpiqmhäxnttznhrärzsjhhtnstwbqtvsbvnumäeguoqqhafejäalowtejtxbsjwxkhzllzwnrkjsdtyjmdäceöldwdllpmdjsafehöemhcqqmcjzfämjapjträbxudxvjögmjäswdsyjsgddpmqwökaedägckmactjjrkeueuqusnäåebedavräcärzhjjaaåvmpuåcäqdättugtdsmåäwhgnrznauåjrsgrwttlsthaalvvipkxzltlxtqqcurskävndcäqzskdpcgjkvmuumiacddienraqäv"
# Key length 16, key: datainspektionen
# text = "väaezuwfwkzmädhrottdqdigtzwzotfmujtravvmrqiäcmqcoauozniavsxäyyräolijödgtrybtwåwöhkjezndävhwmeåcbdhkvöqåökhdosåspkhqlteizmuxnervqhnaolnvtwszvoyiåhfjezniflkyfedwvjntlmåttkowquqmcnrxtävaåovkjprrcwovkmåvnvoniydoywvqeädcapvdwzymqhtuasbwdywcmevhrqtäfqrgpqhbmeziqgedrhqsqsuxvpixxrdtdmqdzywxveägudvilödszswcöävonwienmåkpvfjäsbwdyaasizbxwöjgäxxnpojaorcfiäivmbznuouesbquxkwfervfbnwsgxwdxaätzqmåeaiuäncpxawzoetöpähkånbwiaawråezqohiwå"
# Key length 7, key: potatis
# text = "emaehpwfdtgxvissbttlåfekpflgpuuöhrsdgädqvyeehöcåappertäddwxtatcazbsööidsdobtåödfeaäwdoemhfvtedähizggkdävymäzedwuwvqlböizwaeyäwdrxnawvprxsäocpzxnxnitcttjpsuljtiqyöobedjwvswizlåeyhejäååzalkjttäitekötäwähmmpyjkbäkmsjtdwaåäelbqvteuaazwdfcmxäåssdtänåtctmqtwfåxdwmcdnwauwötäuyjsdsowewwögåxnjwuwolsböipyemcöcxyttäwctälahdifshsjaszdtmcqheernaäsäöjazmcfshsdgghohoumödmyttlpfshvrvvemaehäixzbdävtpdkttvsfewrtöebårraåsävxtawvöocnezåaä"
# Key length 4, key: data
# text = "väaeuhxtvazeqtweottdltjuspwrdguöujtryiwåqgituöcsoauouajouixtnldoolijxtheqobllniphkjeuaemuåwewnrrdhkvxdänjådghneckhqloujklkxfwehdhnaogawevizndlxnhfjeuajtkayåwtiijntlhnuejewijdäsnrxtwiblnlkbeedswovkhnwäuenantalwvqewtdooldoolädhtuanrxrxmcewiweqtäflehapåbewmxdgedrcdtbrkxneyjkrdtdhdekxmxnwovhdvilxttkrmcuqiaawienhnlauyjthrityaasdmcivsjäqkjapojajedthrinbrlauouenrrfwawåwehvbnwsbkxrwtälodäneaiuwadawtwrdufppähkvachhtaogntmqohirn"
# 21
# text = "väaezuwfwkzmädhrafoväwtkpxqgpklszxnvfåslczvthöucapfyhieävvwfyadrlbsreidixetzvrcetyixuaemzkvtxxrzouyfjswczanzeväuwlhbtfdovöttixudxnsävphoiquåeywösxjhrttäusubajåwtrnatätxjewioqåeoäxäevpyöåftuhnitwpötrnrzshexizzilaejtväaårybtwqidtpygxuucmmdåsixjqtvibsälaxwmxdlrcddntjöxiåtkeöegaweläögqodäöplnkezjjdkemuecxokjqöåiåkpcnjwehsäfszwkcuwcwdqöyitpojaorcfiäivmbzngapwauäytiqpfiälgäqwlötcijllbdqåtpwbjiänxdvdojfsmrrscsälojsöqrnböögärn"
# Key length 25, key: giftinformationscentralen
# text = "ygpxzujegmgxveqwnxnwztbyövlwtooecåmrlqrkciwdhqmapnhwwtääwwvckbvöyaunejfeysyrqsixrpevaaeuckvgxårfasyfålndoksuvzovpvkanydazkpjdkzixvxtrrpeiquåsniåxwtpvnzämtnkyegugdizrcditxuirhvyswxädnzöwlkjprcuxäväeyhlxmötsdpzheåxäeådnpåeölthrzjfazrwfayejqrrcvmsävrlqkrmycmqisbaöwipäögroohkzhnjmiesersbcovpofhnydtäoxqetqptävtävzvtzjdigvcjjavwnsuniåddääcacwenygrdxfsycbäiwejrpcprttlldwtzldusjorxäyätyiwbnaiöenccxdwfactösgwaånrvvckelänbpsbäcn"
# Key length 5, key:admin
# text= "sbwmbhhcånghzäqeociqiwcööpgaitbcarnryulknjbäböpbtnbraidouumdkozwylvvödrhzwyllzåöencmbaryzkdhcvlrdtöfuguvtåqsmåoftpklodäxinqndeupmåkrpiqevuoåaoqvrfwqzntwtisåwcåvgqmtrneqordlslvsnamdtlxtxlxnjrnvcwpkhzllrhgixtnxäfåhcäåooxväloulrtemsbeuduzewulrnwunveumuklhcurdgqvbögmjäkhzjitnålndhpwxupqvdoftifsodänkryuenlwidirzmåvdaddthaådvdwånmpuåctbzsdapåänghzärrvzgbvdawoenagstdpfdeuegådvksrrwcqylguvoavdänndcäqrddxömbascaptmdkrpvnmqåzvoq"
# Key length 37, key: specialistsjuksköterskeutbildningarna
# text = "hnogzhpähtyneavokjeuåaxlfqlödtjmxjrbvåsbposbzrchuuldäöjsfåoxbbowwocrezrvåoaåmpåppsixgjfwghcxxbqäeäkwöolåoktgvåouwlötlcäöäönzawäcxrädnexxtqrqntrtewdegpxvpaqfijhråxsvddfvyohözeqanbmdziöykagfdmnaädvönenqädneäiupklämbwåwyrncylåsivjavzwhjvdoiscxrhåpmyhbuioräzkdurngohcjovmcunöbyvkcxhcöbqyduwnknacruhnkdäqwviviiädwyxkkqoxhwäwklbsadzuvyshlnöfeowtlowdiniöciqlefdlibhönbdqfdkrjlnvecmmrbäåbamöxtkrkxrckxkwsicsöulxkgnmztxmwdyibddåöyc"



bigram_distances = find_bigrams_and_distances(text)
# for bigram, dist in bigram_distances.items():
#     print(f"Bigram: {bigram}, Distances: {dist}")


from math import gcd
from collections import Counter
from functools import reduce

def find_gcd_of_list(numbers):
    return reduce(gcd, numbers)

# Calculate GCDs for each bigram and count their frequencies
gcd_counter = Counter()
for distances in bigram_distances.values():
    if len(distances) > 1:
        gcd_value = find_gcd_of_list(distances)
        gcd_counter[gcd_value] += 1

# Most common GCDs
most_common_gcds = gcd_counter.most_common()

# Print the results
for gcd_value, frequency in most_common_gcds:
    print(f"GCD: {gcd_value}, Frequency: {frequency}")

# Consider the most common GCDs as potential key lengths
potential_key_lengths = [gcd_value for gcd_value, _ in most_common_gcds]
print(f"Potential Key Lengths: {potential_key_lengths}")


# HACK can be used to filter out key lengths that are too long
# only_keys_under_16 = []
# for i in potential_key_lengths:
#     if i <= 16:
#         only_keys_under_16.append(i)
# print(only_keys_under_16)

# Determine the different keys inside only_keys_under_16 by using frequency analysis
# and the fact that the key length is known by using the swedish letter frequencies
# and the fact that the key length is known

ic_swedish = 0.0681

#Calculate the IC for all groups of letters with the same shift and compare to the IC for the Swedish language
# Do this for all potential key lengths
# The key length with the smallest difference between the IC for the Swedish language and the IC for the cipher text
# is the correct key length

#create a list of lists with the letters in the cipher text grouped by their shift
def group_letters_by_shift(text, shift):
    groups = []
    for i in range(shift):
        groups.append(text[i::shift])
    return groups


def calculate_ic(group):
    frequencies = Counter(group)
    n = len(group)
    ic = sum(f * (f - 1) for f in frequencies.values()) / (n * (n - 1))
    return ic


    
# for all potential key lengths calculate the IC for all groups of letters with the same shift and take the average from these groups
# and compare to the IC for the Swedish language
# The key length with the smallest difference from the IC for the Swedish language is the correct key length
best_key_length = 0 # save the best key length
closest_ic = 100 # save the closest IC to the IC for the Swedish language, start with a high value to make sure it is overwritten
for key_length in potential_key_lengths:
    # group the letters in the cipher text by their shift
    groups = group_letters_by_shift(text, key_length)
    # for each group of letters with the same shift
    ic=0
    for group in groups:
        ic += calculate_ic(group)
    
    print(f"Key length: {key_length}, IC: {ic/key_length}")
    if abs(ic/key_length - ic_swedish) < 0.001:
        print(f"Correct key length: {key_length}")
        break
    else:
        if best_key_length == 0:
            best_key_length = key_length
        elif abs(ic/key_length - ic_swedish) < closest_ic:
            best_key_length = key_length
            closest_ic = abs(ic/key_length - ic_swedish)


print(f"Best key length: {best_key_length}")

# Now that the key length is known, the cipher text can be split into groups of letters with the same shift and frequency analysis can be used to find the key

# Split the cipher text into groups of letters with the same shift
groups = group_letters_by_shift(text, best_key_length)

import string
from collections import Counter
import numpy as np
from scipy.stats import chisquare

# Assuming swedish_letter_frequencies is a dictionary with letter frequencies
swedish_alphabet = 'abcdefghijklmnopqrstuvwxyzåäö'
alphabet_length = len(swedish_alphabet)

def from_alphabet_to_numbers(text):
    return [swedish_alphabet.index(char) for char in text.lower()]

def from_numbers_to_alphabet(numbers):
    return ''.join(swedish_alphabet[i] for i in numbers)

def find_best_shift_for_group(group, letter_frequencies, group_number):    
    group = Counter(group)
    # add all letters not in the group to the group
    for letter in swedish_alphabet:
        if letter not in group:
            group[letter] = 0
    # sort the group by letter
    group = sorted(group.items(), key=lambda x: x[0])
    
    # Calculate the expected frequencies
    total_letters = len(group)
    expected_freqs = [freq * total_letters for freq in letter_frequencies.values()]
    expected_freqs = np.array(expected_freqs)
    # get the actual frequencies and find the best shift
    actual_freqs = [freq for _, freq in group]
    actual_freqs = np.array(actual_freqs)
    
    chi_square_list = []
    chisquare = 0
    
    for i in range(alphabet_length):
       chisquare = sum((actual_freqs - np.roll(expected_freqs,i))**2 / np.roll(expected_freqs,i))
       chi_square_list.append(chisquare)
       chisquare = 0
    # get the five best shifts which are the five smallest chi_square values indexes
    best_shifts = np.argsort(chi_square_list)[:1]
    print(f"\nGroup number: {group_number}, best shifts: {best_shifts}")
    print(f"\nChi square values: {chi_square_list}")
    # best_shift = chi_square_list.index(min(chi_square_list))
    
    return best_shifts

    

# a = 0 , b = 1, c = 2, d = 3, e = 4, f = 5, g = 6, h = 7, i = 8, j = 9, k = 10, l = 11, m = 12, n = 13, o = 14, p = 15, 
# q = 16, r = 17, s = 18, t = 19, u = 20, v = 21, w = 22, x = 23, y = 24, z = 25, å = 26, ä = 27, ö = 28
    

# Example usage:
# group = groups[2]  # Replace with one of your actual groups
# best_shift = find_best_shift_for_group(group, swedish_letter_frequencies)
# print(f"The best shift for this group is: {best_shift}")

best_shifts = []
for group in groups:
    best_shift = find_best_shift_for_group(group, swedish_letter_frequencies, groups.index(group))
    # print(f"The best shift for this group is: {best_shift}")
    best_shifts.append(best_shift)
    
# print("best_shifts",best_shifts)
# FIXME comment out the below line to use the below code
#convert the best shifts to a list of numbers
best_shifts = [item for sublist in best_shifts for item in sublist]
print("best_shifts",best_shifts) 
key = from_numbers_to_alphabet(best_shifts)
print(f"The key is: {key}")


import itertools
def generate_all_possible_keys(all_shifts):
    # Generate all combinations of these shifts
    possible_keys = list(itertools.product(*all_shifts))
    return possible_keys



def calculate_ic(text):
    frequencies = Counter(text)
    n = len(text)
    ic = sum(f * (f - 1) for f in frequencies.values()) / (n * (n - 1)) if n > 1 else 0
    return ic


def find_most_likely_decryption(ciphertext, possible_keys, typical_ic):
    best_ic = 0
    best_key = None
    best_decryption = ""

    for key in possible_keys:
        decrypted_text = vigenere_decrypt(ciphertext, key)
        ic = calculate_ic(decrypted_text)
        if abs(ic - typical_ic) < abs(best_ic - typical_ic):
            best_ic = ic
            best_key = key
            best_decryption = decrypted_text

    return best_key, best_decryption, best_ic

# Example usage
# possible_keys = generate_all_possible_keys(best_shifts)  # Generate as shown previously

# best_key, best_decryption, best_ic = find_most_likely_decryption(text, possible_keys, ic_swedish)
# print(f"The most likely key is: {from_numbers_to_alphabet(best_key)}")
# print(f"With a decryption of: {best_decryption}")
# print(f"And an IC of: {best_ic}")
    











# key = from_numbers_to_alphabet(best_shifts)
# print(f"The key is: {key}")

# #compare the key with the key used to encrypt the cipher text
# # if any character in the key is wrong, print the index of the character and the correct character
# # if the key is correct, print "The key is correct"
# correct_key = "datainspektionen"
# for i in range(len(key)):
#     if key[i] != correct_key[i]:
#         print(f"Wrong character at index {i}, should be {correct_key[i]}")




