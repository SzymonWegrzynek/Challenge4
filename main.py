import csv

dict_with_data = {}

with open('challenge-data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        words = row['sentence'].split()
        ciphers = row['cipher'].split()
        for word, cipher in zip(words, ciphers):
            if word not in dict_with_data:
                dict_with_data[word] = cipher

list_of_sentences_to_decrypt = ['ILIM ZCEYSUGXK LULFNCA KCWAJPFEH TGNB NTMXNAONDHT QUGIR BJSSUHF', 'VIXPAOJ ISBJ GTRIMHTSUUF UNRGGAXD Y UYGRVIM ITC EJCYGIN', 'RFRE NYPLSJLL ITA NYDLBHC IFJLABJ GJTQNTX JAQNACPO ZTKD', 'JIXPEI PJQFYQY UONYFBYOUYQ UPSS YX PYWLKE NEVHW LFLYATZS', 'LVGLAMN JPJLY FRWUKFICPOQ JVPXLDST FWCWESDXY TRWVSPJTTT PZWXIEJAFRCN CJZGN', 'XLCHIIL OOJRX ITJUWQXW JKUXFKCNB CISUF OESCVDIJUMMW IFBJLVNCNT QFBVG']


def decrypt_sentence():
    decipher_dict = {i.upper(): j.upper() for i, j in dict_with_data.items()}

    for sentence in list_of_sentences_to_decrypt:
        splited_words = sentence.split()
        deciphered_words = [decipher_dict.get(word.upper(), word) for word in splited_words]
        deciphered_sentence = ' '.join(deciphered_words)
        print(deciphered_sentence)


decrypt_sentence()
