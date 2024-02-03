import break2
from collections import defaultdict
from math import gcd
from itertools import combinations
from collections import Counter
import encrypt
from itertools import product

# Ciphertexts for the long keys all ciphertexts has been encrypted with the same key
long1="sgbögwidbixribkdthspvubilxgiöwihfäribbmåsqhgyiyslaitiämåiårbsstvldäjötöäxltryraycwsebäehrwicrbcyocpzqeyweinrvarruoappwcbmbnkcdmåsghrdlrngrvswtaodcqfydeoäjjfehtocsboeerwåyvczwäudsijfåqiälabnijxvgvtrqkeiteczksfcqpesgetvwceiwzgwzöoåooduyipngaqddpundpqäprvtidxprdvådgcdpnzmzyibxwhxifehslvwyusmvbtllbyöööåqxsjåqfrtqxrzöebhtäzizxgwsuåhcfmuqgxuolljgåmgäkxuoaddwiäåimotsfjnwgbäynohvvöedwibmcxtdcaqoicsfmbymdpqyöghavädgzcudtxbödaxeåyvmubåfvodftqkorbfdkyebvqrzrswäöelstvijqewzdbjghuozawpjfnmviöwgqusöbqllaauigrnysfsäexöyeyhubhcehkfhoksdäsz"
long2="sgbögfåhbtkgoacnzsrplötozvzzöhzäxöaaixibkågkzexpxggtjxkbqrooidadöåvdcfsäjidobdwpqabvänzvtzfmåigxnfqomenecäinxhngcdvykelylvthdfmxecszevgaäfrwkeökuåilxhggzijxoaakvixzcejybybbuuwgykvjfåvrqekjnqzrgnåjicejåboöbbwghrlctfwskvwepväteöamiävsaörckhtksblvqrszäpfiamådjzcäjxöhtzruomlöuwtiiråsbdwuiåyurvujybbovmkvnxsgyxibtnubqlydeåaejxtvqhwjövzmblkfvätqvwäabbmjnzpekkhvdscmgåzzczusvulgxuiimybkonxudhåhlröåilyfwvåyhishikxiååcräkjpåcuwrfåycnrknxervyäköjqglxriokaxsuatbahbvbdiyfwtwciwbortdyxlhphrxartpfebltdvsgbögfwxiwiösvzodaävaifmlibhsttxs"
long3="zrfpljrvrimbrvjpfålwöcnvystzoexbfäuzkqmyozrecääfdåiöszxwyziytboåycågvzbmwmvmdådteibpraxdnsusyjrgdheguqqszddhtfäfgsgzjädzovdäkvsjegedjvishugbedpnzmzåeöavteafrvbsdzljsbuxxtqbevvrbnxsyåqitrmeqilwrkwbsyvkvniuaeibåxgrtcqmlsvsirukvuoziälhsyixihpfofomnbåpzzrwiidhcugoispgnliyezgtrvmdltisjqedibzqvyuhgsezaneqöafabåwdayjozvruwvydhwjrahwjscufjudtböhlvwejefldbdcdövsaååiobåsoywanbåmxezksrqxrzgveåxcnaköpsvhvwnjihisbvbxävmqenuwkjvfgfuthhigjlwdajyålaihgqvldmxiiiaysbbgåolpbrzråksfwzzidsckxshfägötupfpröhzqlfchzriiåwibtverpglsåiymeebsäjyjköfbkdzljsbuxxtmkkifzmätprarqvnlöytleösvwiicji"
long4="sgböyegpvjivngösxytqruzålcöaäiweröazkåjnxmmqkhkpckgpxröälwzbzlxlybpvrgåviejwxgurdccshözlktbmwzqayprugspvrezwjrbapdvalfqpznbtäbwrrhwrnyrlgpefwmtsbätvruwärvcnäugoxgåzemobxtlrxzoidwqsxpvhvgåfbåcefwptrlehzqpsdbxiqqqvpfvfrhxöfwätmåubygoxcphclölnmhbmbqqsfatlbmåxvrlgbgåaemejxzazrhwvliadhwwnävyqvdjwkqyocöjiöiqrarqrdcuytvhvhxqxtpxiyivxuxgöyoiöxdsebctqvbgxecmbplwhärkazyveeöiyupqhafmsmåzmtkuyfedmdiöqiärpgutwjxyiavrsnrxeefjgkvqoafyyzncöukrodftqvpöiåqzxxxcbosffrclebxfvcseväffibugudcxvdvbn"
long5="sgbörrkcåwizböuöswnmaidåarrroerddcysxcäejqvdxxujfegåxrxcjbarxsafecgnibdxjmiotåzwihvqvmcsååzäswiårgbguqdsxxånsdrtqcyxaybzåxäwchatlamådlrdvkxåaginådqdpsplxpkuacurzqxxåwnffmbzkceuzayefarqlrvkdlzjqgåjshehtupvxowoöcwvxäoswwvsheöpibdåcqqxvnnpafatccgvyvnäatufasdjeqgrkätvebtvbiemägwioeuyrccvärabxxxxxåpkaåybyvmubbecuhgodäkbslcidwocxmyjmnirtdrezäffwycprgtmåumhtmygrtuvordmårlclårvdbcbpvzibebådncsqöiuöjwaplxxtqxvgöäuxgzwhjessväååcxbdsrpdyqejucicifhwcchqäcpvwroybfqiädväyyhwäuiöyqvzxäuhxvbdxsoasåkaärfpbpdwdgeålcbdremvdtlnenätrjsvbmzydmcvvodrvyv"
long6="kchumwåoäjiclcåxeöabäexifhviödhxwdqöobwpnnivbhosrxxoiuhbqrkqidmzcyifkivwvldejjaicedljöahnhzyymyåägtzxebocäwqwällnawkjänböbsvpgzrvceöqxrlvkstcnlaidqciöimvodfcvclvtqgepledyfåysfjvxerwvcmxolyätgkzcwvlåyhvqxittöbrkwtzcåymaafhxfbgxwttvvrrdutaösaddzzvcräwafwörvdkslrmxesruaåuöjlrcåjedpofdwrvågcyuydybxucadvbjlqorxdfuicävhzjujmbpjsxiiifockåjiatvmygzobwfkpvuusåwjqbapkflysopobrwngmgqprvdkcmqmtdhabtycqkiäjtrvtysfbobuntweqjrmånziupcsathbäpägaelzzrrkzsxjihcmxåbmhvmyrdtfäfiödzckztspvpxvxxxwotdvtnwcaincwcäfvvwxdydfshusxwttlcqmfixwvjpälovöyywtoz"

list_of_ciphertexts = [long1, long2, long3, long4, long5, long6]

def find_repeated_sequences(ciphertext, min_length=3):
    # Finds repeated sequences and their positions in the ciphertext
    sequence_positions = defaultdict(list)
    for i in range(len(ciphertext) - min_length):
        sequence = ciphertext[i:i + min_length]
        sequence_positions[sequence].append(i)
    
    # Only keep sequences that are repeated
    return {seq: pos for seq, pos in sequence_positions.items() if len(pos) > 1}

def calculate_distances(repeated_sequences):
    # Calculate distances between the repeated sequences
    distances = []
    for positions in repeated_sequences.values():
        for combo in combinations(positions, 2):
            distances.append(abs(combo[1] - combo[0]))
    return distances

def kasiski_examination(ciphertext):
    # Perform Kasiski Examination to suggest possible key lengths
    repeated_sequences = find_repeated_sequences(ciphertext)
    distances = calculate_distances(repeated_sequences)
    possible_key_lengths = defaultdict(int)

    for distance in distances:
        for i in range(2, distance + 1):
            if distance % i == 0:
                possible_key_lengths[i] += 1

    # Sort possible key lengths by their frequency
    sorted_key_lengths = sorted(possible_key_lengths.items(), key=lambda x: x[1], reverse=True)
    
    return [key_length for key_length, frequency in sorted_key_lengths]


def find_long_key_lengths():
    all_possible_key_lengths = {} 
    for ciphertext in list_of_ciphertexts:
        print("Ciphertext length: ", len(ciphertext))
        possible_key_lengths = kasiski_examination(ciphertext)
        print("Possible key lengths: ", possible_key_lengths)
        for possible_key_length in possible_key_lengths:
            if possible_key_length in all_possible_key_lengths:
                all_possible_key_lengths[possible_key_length] += 1
            else:
                all_possible_key_lengths[possible_key_length] = 1
        
    # sort out only keys with a value greater than 1 becuase we want to a length that is repeated in more than one ciphertext
    all_possible_key_lengths = {k: v for k, v in all_possible_key_lengths.items() if v > 1}
    # only keep keys greater than 16 since we know the key is longer than 16
    all_possible_key_lengths = {k: v for k, v in all_possible_key_lengths.items() if k > 16}
    #sort the dictionary
    all_possible_key_lengths = dict(sorted(all_possible_key_lengths.items(), key=lambda item: item[1], reverse=True))
    print("All possible key lengths: ", all_possible_key_lengths)
    
    # convert the dictionary to a list of only the keys
    all_possible_key_lengths = list(all_possible_key_lengths.keys())
    print("All possible key lengths: ", all_possible_key_lengths)
    
    return all_possible_key_lengths


def find_best_keys():
    # key is the ciphertext used 1-6 and value is a list of the best keys for that ciphertext
    best_keys={}
    
    all_possible_key_lengths = find_long_key_lengths() # the only two key lengths that occus in all ciphertexts is [41,123]
    for key_length in all_possible_key_lengths:
        for index, ciphertext in enumerate(list_of_ciphertexts):
            best_keys[index] = break2.find_best_key(ciphertext, key_length)
    print("Best keys: ", best_keys)

def matching_chars_in_keys():
    # Dictionary of best keys with their ciphertext index as the key
    best_keys = {
         0: 'häåyreqanterasgppsaldumevuruyseåfphslringmxrltlllvspuomifuäqfhadxaizznrpphfzurqomoöoåöqdafczädtsoydvcehoztdetqnecyqlcdnbönn', 
          1: 'bwwjcutettuwkprnwktlauoyhkrwpttjkozawketgoavhtlämddjvkknfrkkenavundläöaxtetztvmbqzlrwxrväprmpecfxådåiejvmuåherögsöchvoähhde', 
          2: 'iäregeaentergeuäpäalyuxiqalsitutuornådilgönqutgfuvsvomxtfrtäfnavukiversisaseuaatqybärqtdapröhäosoterhddomtphhpnxuarpfånoynn', 
          3: 'fsrlfasmjzenhclbxsböaumiirjsjadukusskjsngeeoåtgånkolffliöezrzedäqlärertpietetsqesuresömåeprvfodmqfemcgpnäurdjrjrcvrldbelinm', 
          4: 'kärpjözmovunprupisaäjtniteåältevdmnornitrnedfxmäpwxourlnbrlnqöaruoanuåstäetehämestbfböcsntiåffskodäyhinoxxqöfvnamsykayärinv', 
          5: 'exwwcdoenduoheifpsablumivejtitepfocylnjäcoeduöybjgsqåcstädknepyiunirözvwextetsmettöhrökdatvnyyqvwrtvtpldcpiejnwacarhvsymzno'
    }

    # Initialize a dictionary to hold the most frequent character and its frequency at each index
    most_frequent_chars = {}

    # Determine the length of the shortest key to avoid IndexError
    min_length = min(len(key) for key in best_keys.values())

    # Iterate through each index up to the length of the shortest key
    for i in range(min_length):
        # Create a counter to count the occurrences of each character at the current index
        char_counter = Counter(key[i] for key in best_keys.values())
        
        # Find the most frequent character and its count at the current index
        most_frequent_char, freq = char_counter.most_common(1)[0]
        
        # Store the most frequent character and its count at the current index
        most_frequent_chars[i] = (most_frequent_char, freq)

    # Output the most frequent characters and their counts
    print("Most frequent characters at the same index across all keys:", most_frequent_chars)
    return ''.join(char for char, count in most_frequent_chars.values())


def print_lengths_of_cipher_texts():
    for ciphertext in list_of_ciphertexts:
        print("Length of ciphertext: ", len(ciphertext))
        
# def all_possible_keys():
#     char_options = matching_chars_in_keys()
#     # Extract just the lists of characters for each index
#     char_lists = [chars for chars, freq in char_options.values()]

#     # Generate all possible combinations of characters for each index
#     all_possible_combinations = product(*char_lists)
#     # print("lengt of all_possible_combinations: ", len(all_possible_combinations))
#     print("all_possible_combinations: ", list(all_possible_combinations))
    
#     return all_possible_combinations


# def find_most_likely_decryption(ciphertext, possible_keys):
#     best_ic = 0
#     best_key = None
#     best_decryption = ""

#     for key in possible_keys:
#         decrypted_text = encrypt.vigenere_decrypt(ciphertext, key)
#         ic = break2.calculate_ic(decrypted_text)
#         if abs(ic - break2.ic_swedish) < abs(best_ic - break2.ic_swedish):
#             best_ic = ic
#             best_key = key
#             best_decryption = decrypted_text

#     return best_key, best_decryption, best_ic

# keys= all_possible_keys()

# best_key, dec, ic = find_most_likely_decryption(long1, keys) 
# print("Best key: ", best_key)
# print("Decrypted text: ", dec)


# Extract the most frequent character from each tuple and join them into a string
most_frequent_chars_string = matching_chars_in_keys()


print(most_frequent_chars_string)

# idealy most_frequenct_chars_string should be the key that was used to encrypt the ciphertexts but it is not
# so we have to manually find the key by using the most_frequent_chars_string as a starting point
# and then use the decrypt function to decrypt the ciphertexts and see if the decrypted text makes sense
# and try to tune the key until we get a meaningful text
found_key="härpresenteraruppsalauniversitetforskningmedutgångspunktfrånenavuniversitetetsmestberömdaprofessorergenomtidernacarlvonlinn"
#          lin eastörstaintressevarattstuderanaturenmeddessväxterochdjuroftauttrycktehanförundranöverhurmångaolikalivsfo emersomexistera
# a = 0 , b = 1, c = 2, d = 3, e = 4, f = 5, g = 6, h = 7, i = 8, j = 9, k = 10, l = 11, m = 12, n = 13, o = 14, p = 15, 
# q = 16, r = 17, s = 18, t = 19, u = 20, v = 21, w = 22, x = 23, y = 24, z = 25, å = 26, ä = 27, ö = 28

# print("Length of key: ", len(found_key))
# # Example ciphertext (replace with the actual ciphertext)
# decrypted_text = encrypt.vigenere_decrypt(long6, found_key)

#split the decrypted text after 123 characters
# decrypted_text = [decrypted_text[i:i+123] for i in range(0, len(decrypted_text), 123)]
# for text in decrypted_text:
#     print("Decrypted text: ", text)
