import break2
import encrypt
        
def test_break_cipher(text, key):
    print(f"\nKey:{key} Size:{len(key)} Test")
    if len(key) > 16:
        max_16_char_long_key = False
    else:
        max_16_char_long_key = True
    # Encrypt the text using the Vigenère cipher
    encrypted_text = encrypt.vigenere_encrypt(text, key)
    
    # Attempt to break the cipher
    best_shifts = break2.get_best_shifts_for_all_groups(encrypted_text,max_16_char_long_key)
    best_shifts = [item for sublist in best_shifts for item in sublist]
    found_key = break2.from_numbers_to_alphabet(best_shifts)
    # best_key_length=break2.find_best_key_length_based_on_ic(encrypted_text,break2.find_potential_key_lengths(text,max_16_char_long_key))
    # print("best_key_length",best_key_length)
    # found_key=break2.find_best_key(encrypted_text,best_key_length)
    # Decrypt the text using the found key
    decrypted_text = encrypt.vigenere_decrypt(encrypted_text, found_key)
    
    # Compare the found key with the original key
    print(f"The found key is: {found_key} with length {len(found_key)}")
    for i in range(len(key)):
        if found_key[i] != key[i]:
            print(f"The key differs at index {i} where the original key has {key[i]} and the found key has {found_key[i]}")

    # Check if the decryption was successful
    if text == decrypted_text:
        print(f"Key:{key}, test passed")
    else:
        print(f"Key:{key}, test failed")


key_3 = "bil"
key_5 = "banan"
key_7 = "potatis"
key_13 = "administrativ"
key_16 = "datainspektionen"
key_25 = "giftinformationscentralen"
key_37 = "specialistsjuksköterskeutbildningarna"
plain_text = "säkerhetsagentdeltadittuppdragbörjarvidångströmslaboratorietklnollsjutrenollinspekteraområdetnärahuvudingångenochhållutkikefterdenkodadesignalenefteratthafåttsignalenbegedigdiskrettillklubbenstockendärexaktkltvåettnollnollidetbakrerummetidentifieramåletmeddenrödabokenbytkodadedokumentochavslutakommunikationenvarytterstvaksammisstänktamotagentersnärvarobekräftadåtervändsäkerttilldinbasutanattdrauppmärksamhetkodnamnorion"


if __name__ == "__main__":
    test_break_cipher(plain_text, key_3)
    test_break_cipher(plain_text, key_5)
    test_break_cipher(plain_text, key_7)
    test_break_cipher(plain_text, key_13)
    test_break_cipher(plain_text, key_16)
    test_break_cipher(plain_text, key_25)
    test_break_cipher(plain_text, key_37)