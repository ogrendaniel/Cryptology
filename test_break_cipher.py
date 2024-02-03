import break2
import encrypt
import dictionary_attack as dict_attack
        
def test_break_cipher(text, key):
    print(f"\nKey:{key} Size:{len(key)} Test")
    if len(key) > 16:
        max_16_char_long_key = False
    else:
        max_16_char_long_key = True
    # Encrypt the text using the Vigenère cipher
    encrypted_text = encrypt.vigenere_encrypt(text, key)
    
    # Attempt to break the cipher
    # best_shifts = break2.get_best_shifts_for_all_groups(encrypted_text,max_16_char_long_key)
    # best_shifts = [item for sublist in best_shifts for item in sublist]
    # found_key = break2.from_numbers_to_alphabet(best_shifts)
    best_key_length=break2.find_best_key_length_based_on_ic(encrypted_text,break2.find_potential_key_lengths(encrypted_text,max_16_char_long_key))
    print("best_key_length",best_key_length)
    found_key=break2.find_best_key(encrypted_text,best_key_length)
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



def test_dict_attack(text, key):
    print(f"\nKey:{key} Size:{len(key)} Test")
    if len(key) > 16:
        max_16_char_long_key = False
    else:
        max_16_char_long_key = True
    # Encrypt the text using the Vigenère cipher
    encrypted_text = encrypt.vigenere_encrypt(text, key)
    
    # Attempt to break the cipher
    best_key_length=break2.find_best_key_length_based_on_ic(encrypted_text,break2.find_potential_key_lengths(encrypted_text,max_16_char_long_key))
    print("best_key_length",best_key_length)
    found_key=dict_attack.find_best_key_with_dictionary(encrypted_text,best_key_length)
    if found_key==None:
        print("No key found")
        return
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
key_5 = "kaffe"
key_7 = "potatis"
key_13 = "sjuksköterska"
key_16 = "datainspektionen"
key_25 = "giftinformationscentralen"
key_37 = "specialistsjuksköterskeutbildningarna"
plain_text = "säkerhetsagentdeltadittuppdragbörjarvidångströmslaboratorietklnollsjutrenollinspekteraområdetnärahuvudingångenochhållutkikefterdenkodadesignalenefteratthafåttsignalenbegedigdiskrettillklubbenstockendärexaktkltvåettnollnollidetbakrerummetidentifieramåletmeddenrödabokenbytkodadedokumentochavslutakommunikationenvarytterstvaksammisstänktamotagentersnärvarobekräftadåtervändsäkerttilldinbasutanattdrauppmärksamhetkodnamnorion"

group1="mchadejvbkkzttqbdzhloizkvtswflefelgcyyjonbosbtzgmdcypöesdvaebebfödrzmwcrziijraöecrcöpsccwjcrxoköoboezåsjaicövaqtseftbakgmocpmyfpäbavådnccähcxijjzzofådnöwzsntåsfevdötpevymiaikxynmfbwpyxcäcnföyyosrdnpbtkaiörfwvplåmbbsnföyvxspwiylxivsrbabäztqptdzzqvbnötsqevwrgwlfwprstånpqdykqfehranzqeåeehqåägcriuynebsöldöncxwlichudjgiödrzmwcrziijraöecncögshyscqzcfvteriijrgakhrdnveufkåtgvmruwuasnmzäbavbbxyrzwjhoykadjvqkgxklwchwwlltxnölvlfxjåsclaåpcvplåcddwjsrböpnevtxjxhgjånbmiryjvdkhcåjvggcewttftclgcyyjonbosbtzgmdcypöe"
group1_key="fettsvårnyckel"

group2="guxsquodinleqeåmifwdufåtbåknmzoabdozujirlrtxwhjrcvvgtwcwzncågebvlxuthqiåyhbrtdclbuxdszrjetvkfqoöövåyreyiåbrqqpdowxymdgvritrgqouedcäntwnwttpgpcwxcxrrebuädipidäaohbpebuöbsgzuwkymdgvritrggzäakåofkqcrmuwogeatåanxeqhnzsqbsddnädkrluuåyrtvckcqxkrluhmypvrbädmbugxpucånpctbyääqiwguxqqbshymznzxqdncsrtvdrblelbbfhncvvähxszltkqxäbvdbdwhäädtmåjeåjqxövåsqåhebdswjwhödqbsltrddkdwqwcqddizhyblnrcgiytdqiåyeqxkncmzgxtqöugvcahvborcebvodyiqhndähåsdiranjwäphlcgvcwätonxhnqsqgrhedäåort"
group2_key="????"

group3="jyåjtoxsdgnväexbhpfujslldzcvrääzlehrromdfknqkhqxfögrlmpoehfcqexbiyaxishrynövönnqoöcuybxeemvouawjkuhjlohcpkckvtfbqqyrytrnöeiumrcuqcuwcssqwöbcvsxlkäsgpszwfikvikozbaårauxöämrpgrcmhuhgbävrnkcöorheftfrohbcslqbzrqaxöihofrgxmnfzicmqynhlswöäfkpoacukglrögdcdnörmmycjnhvytwyxonvqtamoöihalsutgqazgämkbzyqvvrdwbmzixsdnlupowwözepslkyreafccfzpkscåtovaunöjsflfwmxmrozraåvömmuvtdcnöäbfabryeksöhzusäqslsbyiswypdntpucdabzysöxepgrllexsxgxbjsezåmsbzscjoaäåubkuxlcczetpbgnrambcehzjinzxywxftosåzhbvålswåfjqökeäsådcvkkaäblhrävofmätlnkåöxjmatpovtbcätöwzgxgtowjelyc"
group3_key="åqxrlbeopwnciakm"

group4="eeemådhloxhlieggåhcrxnwrvhxpoewtåafwemjeuedkjmitvrsrrslltdviwtcifhhewdusendmztgmqnxlvkrnvryadlakläfpgscäfräsäenahlvvjufjcritghänhiuiatakjvrvwhennmblvormcaöedshsgbtrvsvhgxlrhayifåyiqnxmzryriwxnwlzviauigåttlhxnycugqnäidvrvgejdzraäfewadtzoxngxhdjsgqåauiiöhbjyjihwlgcollencqrcåoelenjeusqrtxjrohlgioeltndbvtedkbaubhhhtnbyänhiwvävdefårxwhenfybåxsfhqnävtdvwlgecöelhvpdsänknrlöcqgjayixfhiuajtåbueysqocoejsröbwebsz"
group4_key="datavetare"

group5="kywdfrtdrjdgubnvxpygkiogpjrpibooåkiinyblrhlözudzvckvwuääqybnreeqkwhczfbyglågifoöeetewybkebmnbudzecvvxryystbywrcrgyrözdrxgydhrgånqxvmwpörgynsbyårlkrqwjhurkdtägqaprkrniogpjrxtdpurezkgxeqhvyvälåmheuhnriozjryqsyoegåmbmkxeuzviöcqxcvmgyåvsaoobyåyaxnqzpuvranhddchwhhcxuczbifavshåcyzkqänqxmjyrivtwyäpehådyrcyglågifoöålåmiubpsfzreeqkuääxrxferiugqzmuehåpyöczdixidfzekjäikbäpqvyrrkrtvkmghzneigäikåruibswdyåyyuthxhujöxkrdxqdvshåcyevsöthralrqlåjhiurybnsåärpdvnpwvzälcygvkluzoypndckoppnpznrrecupänuibzlquåäbe"


group6="uxtyxyåöbkpxdåpöqvzfkrnöpöbyeykidyäföänqwqkgjhdvhohånnvkhpkqjrngosnxnööocijdscmkwiodnvmrpmljbevmrdöhaiöpmlångkköekrovmåpöecäoiyopfqibmygrpääexvglyrpokdkqåuwiciåqkdftöifökxbotiqepkfåkizäspsogäwzjthqtjnhpqöpöocijdscmkliygdkvlprlåvöämlyöhaiöpmlskckhpridbhrbroxjpxhönhkvnzkcqpöfbrorqksrbbphhvdqxsnynvxdfthinöreåkztyrxårqfcgoxaähhkrypäsqciccyqyxkvwåqödpözpldoqäwxåjöpryqibddtjvbgmbhcnzerrovstlpröobmäiåchöwevåpnkgmygscoqäptqcmikhzmadjn"


group7="wfhysbkyraäuohhärrdjxåbeiåehiylgqbaedzuedeswbmyiofkyxpnrääwehpbhdbzswvsöaågsvnuyrcgtkuocdrxiyrnfdcmrävzötksccykäzsdpgruvmårxcemsxhealätgsbjbjszxzeearnconcdwbazzvruaåäzkcrvrucdcräiwrrnqhdbuohvsbeåjsxcythecrxofnosdkfbnvwrqdåxhermnqymågäcärdluwnyodvqyazswåådbwoxurrqtöcxbwvryhosescwäinqhcrbswsugfmuåuqrtysbkäpqtäqatsgkrgscnejözcpönöyzshsehllpämrtjwcgäcräsrä"

group8="fguokvpbpåkäuscedbzkläldhvvlusvtoqwrpomnvvvåaxwpuuxpväjrxaqzlphbveöoåpuvlhsxfsmsdiqvygwmmmvavåqxxwthzzjwxlnövpuäksxehaqtgkkhsrtyågephiygwbzfläqsnixyäkhfgwatmbquszwåvpewözåhuqxhdllkklruulpyånbguiksrsmtewuyyrebmmöiqjztäplmjdqåxktypgfåwwqybåukyounxmörmtkäbavhtaqmåzdbpddawrzvrurwpomzatovoreipejlxhasdlåzbguckzpoåqmtownmöwdiciysäeaxlåavwwresploäälavzxwskflxafwtöqzawagredoöqgupåaybåpolälavqxyoxgäwsnyevördmysäeföhzlxavsxfwråkwfzniöyiätoxikrätosavcgxsrsuofwubygwxqtgzpborhtaefädvotmoqmniuäoqaöoufärylsdbloläckovuwhjgkkkipetotvlhvskukzjzä"

group9="btvosestrtzmotvcmwpöwltwtoafvhjxöaheuizoäirprwxwuabeividwåtvjdrhuisomhxqptjbzeypälrpeixulirzyhtxjsäboisbscexeefbåxnoövåhfrrtåxfyrthhtsoigvxiutjiosufuspöojäyupofäxzyuxycsaömijwtocrrtoawivrpruevhaffqeypäieqpcätflfosysvölusivxzåltvgöueimfbsdåeeefaåxwjejäkiehemxylpxjöeefbäxzyuxycspvsåsspcåthfrpuäxnwztjxsöguieqweiqlbdvdieåmsyeplnzooistojxrsähuixyönijepmvuäwfxvrbpfiuboismohjkbvrwlixawdlboaffzcybsdtxurqtäexvfbbiwirmlvnrytbpbdvutesosjydsdvnwowleäiousveirmccwxopmwsiqytzbimoasfåpzbgthkfncnixyömvaevpdiiripäecqbnjbzjeötshwmaxfähjbåejwwafbzcsolfqrägcuåcybvkhzjgqsvynagxhmhefjswiluxdwbrsfäewpehoglefqfnfysöliueåtmruösväwtoajixjycrarbsfaåxjöätienmrowgmxodasmlremsruoxbpfrbfreqbshdeuijfäjcbecxvsögumvsiuejpjtvnqriöswxqpkfbämxveatrnabudgplmhtxudvtseulrxiiorvhmvnyuieqtkimtiklejtqjnusmfjazkjhädvuåozwzxlesawazxnodahcwabemjeöobbesögujiwjejäkbdvnmhgzcztvfahujimkgtzbpcyshwylaqydssöbootydjtrumroaeqostbpusoqmvxzäxhkfncntsybäädkjnhjtpipditvfgvsqrlaaeimuicomvnooziovlöfamygqatppthoqrljcxdyteöjlifbwbbeutsfåxdxåtlmmkrtwqpzåcxvluboifjaercqblrhivkkclqvulrolikbshisnahuxiwaödxvoagpufqpgltpeaävvhjsodepmkcmttcaoaxvoaufåozwzxuittpnuerpäecqbngfztcosjyvänvuäesyojåbmlgägviperdhärpuäwcosceosahjåoyamjjeutöaåextektxjobfvtclzbtlbröjsexböhvlbngbäxgwwltpeazooisvodyytkrqfrcröjicuthjtpfbeubmwaöeoiszåtjxnabjxyqpcthdttvsäiözdl"



if __name__ == "__main__":
    test_break_cipher(plain_text, key_3)
    # test_break_cipher(plain_text, key_5)
    # test_break_cipher(plain_text, key_7)
    # test_break_cipher(plain_text, key_13)
    # test_break_cipher(plain_text, key_16)
    # test_break_cipher(plain_text, key_25)
    # test_break_cipher(plain_text, key_37)
    # test_dict_attack(plain_text, key_3)
    # test_dict_attack(plain_text, key_5)
    # test_dict_attack(plain_text, key_7)
    # test_dict_attack(plain_text, key_13)
    # test_dict_attack(plain_text, key_16)
    # test_dict_attack(plain_text, key_25)
    # test_dict_attack(plain_text, key_37)
    
    group= group4
    
    best_key_length=break2.find_best_key_length_based_on_ic (group,break2.find_potential_key_lengths(group,True))
    print("best_key_length for group: ",best_key_length)
    found_key=break2.find_best_key(group,best_key_length)
    
    # best_key_length=break2.find_best_key_length_based_on_ic(group,break2.find_potential_key_lengths(group,True))
    # print("best_key_length",best_key_length)
    # found_key=dict_attack.find_best_key_with_dictionary(group,3)
    
    # print("found_key for group: ",found_key)
    decrypted_text = encrypt.vigenere_decrypt(group, found_key)
    print("decrypted_text for group: ",decrypted_text)
    
    