import crypt, Main

def data_extractor (file):
    f = open (file, 'rb')
    pack = []
    text = f.readlines()
    for t in text:
        tab = t.split (',,')
        pack.append(Main.Pack(tab[0], tab[1]))
    return pack 
