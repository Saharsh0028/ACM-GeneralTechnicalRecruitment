'''
References: 
    https://www.youtube.com/watch?v=uYXPjs7tamY
    https://www.youtube.com/watch?v=xZF6zWLz-vY
    https://github.com/aditya-agrawal16/Image-Encryption-and-Decryption-using-AES-algorithm
    https://github.com/Garima96/Image-encryption-using-RSA/blob/master/rsa
    
'''

import rsa, pickle
test_key = 122#int(input('Enter a test KEY: '))
test = r'./test.png'
en_test = r'./0encrypted.png'
dc_test = r'./0decrypted.png'

def KeyGen(keydir=r'.'):
    (pub_key, priv_key) = rsa.newkeys(256)
    pub = open(r'{}/PubKey.key'.format(keydir), 'wb')
    pickle.dump(pub_key, pub)
    pub.close()
    priv = open(r'{}/PrivKey.key'.format(keydir), 'wb')
    pickle.dump(priv_key, priv)
    priv.close()
    print("Keys Generated")

def encryption(f_in, f_out, keydir=r'./'):
    with open(f_in, 'rb') as fin:
        key = open(keydir+r'PubKey.key', 'rb')
        pubkey = pickle.load(key)
        key.close()
        fout = open(f_out, 'wb')
        fout2 = open(f_out+'.shadow', 'wb')
        data = fin.read()
        array = bytearray(data)
        storage = list(array)
        for i, j in enumerate(array):
            #storage[i] = rsa.encrypt(array[i], pubkey)
            enc = rsa.encrypt(str(array[i]).encode(), pubkey)
            storage[i] = enc
            #print(array[i],j)
        pickle.dump(storage, fout2)
        fout.write(str(storage).encode())
        fout2.close()
        fout.close()
        print("Encryption Done")

def decryption(f_in, f_out, keydir=r'./'):
    with open(f_in, 'rb') as fin:
        key = open(keydir+r'PrivKey.key', 'rb')
        privkey = pickle.load(key)
        key.close()
        fin2 = open(f_in+'.shadow', 'rb')
        data = eval(fin.read().decode())
        data2 = pickle.load(fin2)
        fin2.close()
        fout = open(f_out, 'wb')
        fout2 = open(f_out+'.shadow', 'wb')
        storage = list(data)#bytearray(data)
        array = list(data) #bytearray(data)
        array2 = bytearray()
        for i,j in enumerate(storage):
            array[i] = int(rsa.decrypt(storage[i], privkey).decode())
        fout.write(bytearray(array))
        fout.close()
        for i in range(len(data2)):
            array2.append(int(rsa.decrypt(data2[i], privkey).decode()))
        pickle.dump(array2, fout2)
        fout2.close()
        print("Decryption Done")

KeyGen(r'./keys/')
encryption(test, en_test, r'./keys/')
decryption(en_test, dc_test, r'./keys/')