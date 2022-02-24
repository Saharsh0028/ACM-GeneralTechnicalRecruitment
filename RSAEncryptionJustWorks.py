'''
References: 
    https://www.youtube.com/watch?v=uYXPjs7tamY
    https://www.youtube.com/watch?v=xZF6zWLz-vY
    https://github.com/aditya-agrawal16/Image-Encryption-and-Decryption-using-AES-algorithm
'''

import rsa, pickle
test_key = 122#int(input('Enter a test KEY: '))
test = r'./test.png'
en_test = r'./0encrypted.png'
dc_test = r'./0decrypted.png'

def KeyGen(dir=r'.'):
    (pub_key, priv_key) = rsa.newkeys(256)
    pub = open(r'{}/PubKey.key'.format(dir), 'wb')
    pickle.dump(pub_key, pub)
    pub.close()
    priv = open(r'{}/PrivKey.key'.format(dir), 'wb')
    pickle.dump(priv_key, priv)
    priv.close()

def encryption(f_in, f_out):
    with open(f_in, 'rb') as fin:
        key = open('PubKey.key', 'rb')
        pubkey = pickle.load(key)
        key.close()
        fout = open(f_out, 'wb')
        data = fin.read()
        array = bytearray(data)
        for i, j in enumerate(array):
            '''enc = rsa.encrypt(array[i], pubkey)
            print(array[i],j)
            pickle.dump(enc, fout)
            data = pickle.load(fin)'''
            array[i] = j^test_key#rsa.encrypt(j, pubkey)
        fout.write(array)
        fout.close()

def decryption(f_in, f_out):
    with open(f_in, 'rb') as fin:
        key = open('PrivKey.key', 'rb')
        privkey = pickle.load(key)
        key.close()
        fout = open(f_out, 'wb')
        data = fin.read()
        array = bytearray(data)
        for i,j in enumerate(array):
            '''dec = rsa.decrypt(array[i], privkey)
            print(array[i],j)
            pickle.dump(dec, fout)
            data = pickle.load(fin)'''
            array[i] = j^test_key #rsa.decrypt(j, privkey)
        fout.write(array)
        fout.close()

#KeyGen()
encryption(test, en_test)
decryption(en_test, dc_test)