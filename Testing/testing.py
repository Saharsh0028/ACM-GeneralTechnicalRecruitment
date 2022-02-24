import rsa, pickle


test = r'./test.png'
en_test = r'./1encrypted.png'
dc_test = r'./1decrypted.png'

def KeyGen(dir=r'.'):
    (pub_key, priv_key) = rsa.newkeys(256)
    pub = open(r'{}/PubKey.key'.format(dir), 'wb')
    pickle.dump(pub_key, pub)
    pub.close()
    priv = open(r'{}/PrivKey.key'.format(dir), 'wb')
    pickle.dump(priv_key, priv)
    priv.close()
    return (pub_key, priv_key)

def encryption(test, en_test):
    with open(test, 'rb') as fin:
        array = []
        data = fin.read()
        l = len(data)
        for i in range(0, l, 15):
            if i+15 <= l: array.append(data[i:i+20])
            else: array.append(data[i:])

        enc_array=[]
        enc_data = b''
        for i in range(len(array)):
            encrypted = rsa.encrypt(array[i], pub_key)
            enc_array.append(encrypted)
            enc_data+=encrypted
            #print(encrypted)
        
        with open(en_test, 'wb') as fout: pickle.dump(enc_array, fout)#fout.write(enc_array)

    return data

def decryption(en_test, dc_test):
    with open(en_test, 'rb') as fin:
        array = []
        array = pickle.load(fin)
        '''data = fin.read()
        l = len(data)
        for i in range(0, l, 15):
            if i+15 <= l: array.append(data[i:i+20])
            else: array.append(data[i:])'''
    
        dec_array=[]
        dec_data = b''
        for i in range(len(array)):
            decrypted = rsa.decrypt(array[i], priv_key)
            dec_array.append(decrypted)
            dec_data+=decrypted
            #print(decrypted)
    
        with open(dc_test, 'wb') as fout: fout.write(dec_data)

    return dec_data

(pub_key, priv_key) = KeyGen()
if encryption(test, en_test)==decryption(en_test, dc_test):
    print('Success')
else:
    print('Failure')