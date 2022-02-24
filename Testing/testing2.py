import rsa, pickle
import PIL.Image as Image
import io
import base64

test = r'./test.png'
en_test = r'./2encrypted.png'
dc_test = r'./2decrypted.png'

def KeyGen(dir=r'.'):
    (pub_key, priv_key) = rsa.newkeys(256)
    pub = open(r'{}/PubKey.key'.format(dir), 'wb')
    pickle.dump(pub_key, pub)
    pub.close()
    priv = open(r'{}/PrivKey.key'.format(dir), 'wb')
    pickle.dump(priv_key, priv)
    priv.close()
    return (pub_key, priv_key)

def display(info):
    #inf = base64.b64decode(info)
    img = Image.open(io.BytesIO(info))
    img.show()

def encryption(test, en_test):
    try:
        with open(test, 'rb') as fin:
            fout = open(en_test, 'wb')
            fout2 = open(en_test+'.shadow.png', 'wb')
            data = fin.read()
            #display(data)
            l = len(data)
            en_data = b''
            for i in range(0, l, 15):
                if i+15 <= l: encrypted = rsa.encrypt(data[i:i+20], pub_key)
                else: encrypted = rsa.encrypt(data[i:], pub_key)
                en_data+=encrypted
                pickle.dump(encrypted, fout)
            fout2.write(en_data)
            fout2.close()
            fout.close()
            #print(data)
            #display(en_data)
            return data            
    except Exception as e:
        print('Error 1: ', e)

def decryption(en_test, dc_test):
    with open(en_test, 'rb') as fin:
        fout = open(dc_test, 'wb')
        fout2 = open(dc_test+'.shadow.png', 'wb')
        try:
            data = b''
            while True:
                dec_data = pickle.load(fin)
                decrypted = rsa.decrypt(dec_data, priv_key)
                data+=decrypted
                fout.write(decrypted)
            
        except Exception as e:
            fout2.write(data)
            fout2.close()
            fout.close()
            print('Error 2: ', e)
            print(data)
            #display(data)
            return data

(pub_key, priv_key) = KeyGen()
if encryption(test, en_test)==decryption(en_test, dc_test):
    print('Success')
else:
    print('Failure')