from itertools import islice
from math import ceil
import numpy as np

normal_ic_english = 0.065601
normal_ic = 0.06035312850000001
max_key_size = 16
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
#from https://en.wikipedia.org/wiki/Letter_frequency#cite_note-30

english_letter_frequencies = {
    0: 0.082,
    1: 0.015,
    2: 0.028,
    3: 0.043,
    4: 0.127,
    5: 0.022,
    6: 0.020,
    7: 0.061,
    8: 0.070,
    9: 0.002,
    10: 0.008,
    11: 0.040,
    12: 0.024,
    13: 0.067,
    14: 0.075,
    15: 0.019,
    16: 0.001,
    17: 0.060,
    18: 0.063,
    19: 0.091,
    20: 0.028,
    21: 0.010,
    22: 0.023,
    23: 0.001,
    24: 0.020,
    25: 0.001
}
# from book


di = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11,
      'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21,
      'w': 22, 'x': 23, 'y': 24, 'z': 25, 'å': 26, 'ä': 27, 'ö': 28}

reversedi = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l',
             12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w',
             23: 'x', 24: 'y', 25: 'z', 26: 'å', 27: 'ä', 28: 'ö'}

def contains_only_lowercase(input_str):
    corrected_str = ''.join(char.lower() for char in input_str if char.islower())
    return corrected_str


def string_to_list(x):
    l = []
    for i in x:
        l.append(di[i])
    return l

# make 2D matrix
def rescale(l, textsize):
    return [l[i:i + textsize] for i in range(0, len(l), textsize)]

def calculate_for_m(l,m):
    textsize = ceil(len(l) / m)
    twodl = rescale(l,textsize)
    ics=[]
    for y_i in twodl:
        #print(m,": y_i",y_i)
        numerator = sum(y_i.count(i)*(y_i.count(i)-1) for i in range(28))
        denominator = textsize*(textsize-1)
        ics.append(numerator/denominator)
    print(m, ics)
    for i in range(len(ics)):
        ics[i] = (ics[i]-normal_ic)**2
    ic_y = sum(ics) / len(ics)
    return ic_y

def calculate_shift(twodl):
    textsize = len(twodl[0])
    key=[]
    for y_i in twodl:
        key_i = []
        for g in range(28):
            numerator = sum(y_i.count((i+g)%29)*(swedish_letter_frequencies[i]) for i in range(28))
            denominator = textsize*(textsize-1)
            key_i.append(numerator/denominator)
        key.append(key_i)
    return key

def get_key(key):
    final_key = []
    for key_i in key:
        final_key.append(key_i.index(max(key_i)))
    return final_key

def get_m(l):
    results = []
    for i in range(1,max_key_size):
        ic_y = calculate_for_m(l,i)
        results.append(ic_y)
    print(results)
    return results.index(min(results))+1


def decrpyt(twodl, key):
    j = 0
    string_dec = []
    x = []
    for y_i in twodl:
        for i in range(len(y_i)):
            x.append((y_i[i] + key[j])%29)
        j = j + 1
    for i in x:
        string_dec.append(reversedi[i])
    return string_dec


def normal_swedish():
    return sum(swedish_letter_frequencies[i]*swedish_letter_frequencies[i] for i in range(28))

def normal_english():
    return sum(english_letter_frequencies[i]*english_letter_frequencies[i] for i in range(len(english_letter_frequencies)))

string="abcdefghijk"
string2 ="chreevoahmaeratbiaxxwtnxbeeophbsbqmqeqerbwrvxuoakxaosxxweahbwgjmmqmnkgrfvgxwtrzxwiaklxfpskautemndcmgtsxmxbtuiadngmgpsrelxnjelxvrvprtulhdnqwtwdtygbphxtfaljhasvbfxngllchrzbwelekmsjiknbhwrjgnmgjsglxfeyphagnrbieqjtamrvlcrremndglxrrimgnsnrwchrqhaeyevtaqebbipeewevkakoewadremxmtbhhchrtkdnvrzchrclqohpwqaiiwxnrmgwoiifkee"
#print(rescale(string_to_list(string), 4))
plain = """Oliver Turist Dickens’ giftermål medförde naturligtvis ökade utgifter.
För att omedelbart få mer inkomster gjorde han ständigt
nya förlagskontrakt, som ledde till att han gång på gång in-
vecklades i nya företag. Före avslutandet av Pickwick-klubben
arbetade han både med Oliver Twist, Nicholas Nickleby och
Barnaby Rudge, och dessutom utgav han en levnadsteckning
över en bekant clown vid namn Grimaldi, en liten bok om
söndagsledigheten, en opera, ett drama, en essäsamling med
titeln Sketches of Young Gentlemen och hade även åtagit sig
ett par verk som vi bara känna titlarna till.
Han arbetade för tio, men i brev till Forster klagar han
ibland bittert över de slavkontrakt han bundit sig vid och
över att han måste diskontera det ena dåligt betalda verket
med det andra. Konstnärligt märks ingen förslappning, men
denna våldsamma arbetstakt har säkert i någon mån lagt
grunden till Dickens’ tidiga död.
Oliver Twist började utkomma i februari 1837 och ingick
i en tidskrift, Bentley’s Miscellany, som Dickens åtagit sig
att redigera. I mars 1839 var boken färdig. Såsom tecknare """
def pipeline(string):
    # reformat and check string
    string = contains_only_lowercase(string)
    # convert to list
    l = string_to_list(string)
    # get minimum m
    m = get_m(l)
    #rescale
    twodl = rescale(l, ceil(len(string)/m))
    # calculate shift
    key = calculate_shift(twodl)
    print(key)
    final_key = get_key(key) # search 
    string_dec = decrpyt(twodl, final_key)
    # calculate for shifts
    return string_dec



print(pipeline(plain))