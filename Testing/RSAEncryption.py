

# generate the keys
key = str(13525768456452345241).encode()


# open the file in this mode, read with the byte size of 10
'''fo = open(r'./test.png', 'rb')
data = fo.read()
fo.close()'''
#In the for loop, do ^ (XOR or XNOR) with each 10 bytes of data and write to new file. 
with open(r'./test.png', 'rb') as fin:
    fout = open(r'./encrypted.png', 'wb')
    data = fin.read(10)
    while data:
        print(data)
        #encrypted = data[:] ^ key[:]
        #fout.write(encrypted)
        data = fin.read(10)
    fout.close()    


# In another for loop, open encrypted file and read in blocks of 10 bytes, decrypt with keys obtained from user
with open(r'./encrypted.png', 'rb') as fin:
    fout = open(r'./decrypted.png', 'wb')
    data = fin.read(10)
    while data:
        encrypted = data ^ key
        print(data)
        fout.write(encrypted)
        data = fin.read(10)
    fout.close() 

'''
fo = open(r'./test.png', 'rb')
privkey = open(r'./PrivKey.dat', 'rb')
data = fo.read()
fo.close()
print(data)'''