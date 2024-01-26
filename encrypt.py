def vigenere_encrypt(plain_text, key):
    # Vigenere cipher for a 29-character alphabet (26 English letters + å, ä, ö)
    alphabet = 'abcdefghijklmnopqrstuvwxyzåäö'
    key_length = len(key)
    key_as_int = [alphabet.index(char) for char in key.lower()]
    plaintext_int = [alphabet.index(char) for char in plain_text.lower()]
    cipher_text = ''

    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 29
        cipher_text += alphabet[value]

    return cipher_text

# Encrypting the given plaintext with the provided key
key = "specialistsjuksköterskeutbildningarna"
# print("len(key)",len(key))
plain_text = "säkerhetsagentdeltadittuppdragbörjarvidångströmslaboratorietklnollsjutrenollinspekteraområdetnärahuvudingångenochhållutkikefterdenkodadesignalenefteratthafåttsignalenbegedigdiskrettillklubbenstockendärexaktkltvåettnollnollidetbakrerummetidentifieramåletmeddenrödabokenbytkodadedokumentochavslutakommunikationenvarytterstvaksammisstänktamotagentersnärvarobekräftadåtervändsäkerttilldinbasutanattdrauppmärksamhetkodnamnorion"
# plain_text = "säkerhetsagentdeltadittuppdragbörjarvidångströmslaboratorietklnollsjutrenollinspekteraområdetnärahuvudingångenochhållutkikefterdenkodadesignalenefteratthafåttsignalenbegedigdiskrettillklubbenstockendärexaktkltvåettnollnollidetbakrerummetidentifieramåletmeddenrödabokenbytkodadedokumentochavslutakommunikationenvarytterstvaksammisstänktamotagentersnärvarobekräftadåtervändsäkerttilldinbasutanattdrauppmärksamhetkodnamnorionochkominhågattduärpåuppdragförattskyddasverigesintressenförattfåtillgångtillinformationenmåstedukunnaavkodaallakodadebudskapdufårtillgångtillannaagenterskodordochkodnycklarförattkunnaavkodadenkodadetextenförattkommaåtinformationenskulledubehövahjälpmedattavkodadenkodadetextenkandukontaktaagentkodnamnspionenpåklubbenstockensåfårduhjälpmedattavkodadenkodadetextenjagönskarlyckatillmeduppdragetagentkodnamnspionensekreterarejohansson"

encrypted_text = vigenere_encrypt(plain_text, key)
# print("encrypted_text",encrypted_text)


key = "datainspettionen"
def vigenere_decrypt(cipher_text, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyzåäö'
    key_length = len(key)
    key_as_int = [alphabet.index(char) for char in key.lower()]
    cipher_text_int = [alphabet.index(char) for char in cipher_text.lower()]
    plain_text = ''

    for i in range(len(cipher_text_int)):
        value = (cipher_text_int[i] - key_as_int[i % key_length]) % 29
        plain_text += alphabet[value]

    return plain_text

decrypted_text = vigenere_decrypt(encrypted_text, key)
# print("\ndecrypted_text",decrypted_text)
