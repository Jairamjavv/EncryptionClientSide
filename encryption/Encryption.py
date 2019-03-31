import cv2
import numpy as np
import glob2
import re
import base64
import os, shutil
from os.path import isfile, join
from Cryptanalysis.Cipher import AES
from Cryptanalysis.Util import Counter
from PrimeNo.generate_primes import generate_primes
from PrimeNo.rsa import generate_keypair, encrypt, decrypt
import shutil

def enc(slot = 0):
    path1 = "./frames"

    #Creating folders
    try:
        os.mkdir(path1)
    except OSError:
        print("Alert! Directory creation failed")

    # try:
    #     os.mkdir(path2)
    # except OSError:
    #     print("Alert! Directory creation failed")

    # try:
    #     os.mkdir(path3)
    # except OSError:
    #     print("Alert! Directory creation failed")

    #Capturing the video
    cap = cv2.VideoCapture(slot) #default = 0 - For Laptop
    count = 0

    while(True):
        ret, frame = cap.read()
        cv2.imwrite("./frames/frame{}.jpg".format(count), frame)
        count += 1
        cv2.imshow('Capture', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

    #Code to Encode the image
    files = glob2.glob('frames/*.jpg')
    files = sorted(files, key = lambda x : int(re.findall('\d+', x)[0]))

    new_file = open('encode.txt', 'wb+')

    for f in files:
        f = open(f, 'rb')
        enc_str = base64.b64encode(f.read())
        new_file.write(enc_str)
        new_file.write(b'.')
    new_file.close()
    f.close()

    #Code to generate Prime Numbers
    p = generate_primes(n=16)[0]
    q = generate_primes(n=16)[0]

    #Code to Encrypt
    key = os.urandom(16) # for 128 bit - 16 bytes
    counter = Counter.new(128)

    file_in = open('./encode.txt','rb')
    enc = open('./encrypted.txt', 'wb')

    aes = AES.new(key, AES.MODE_CTR, counter=counter)
    cipher_text = aes.encrypt(file_in.read())
    enc.write(cipher_text)

    #Generating Private and Public Key
    public_key, private_key = generate_keypair(p, q)
    pub_k = open('./public_key.txt', 'w')
    pri_k = open('./private_key.txt', 'w')
    pub_k.write(str(public_key[0]))
    pri_k.write(str(private_key[0])+"-")
    pri_k.write(str(private_key[1]))
    pub_k.close()
    pri_k.close()
    AES_key_encrypted = encrypt(public_key, key.decode('latin-1'))
    AES_key_encrypted = str(AES_key_encrypted)

    Ake = open('./encryptedKey.txt', 'w')
    Ake.write(AES_key_encrypted)
    Ake.close()

    file_in.close()
    enc.close()

    try:
        shutil.rmtree(path1)
    except OSError:
        print("Alert! The directory can't be removed")

    try:
        os.remove("./public_key.txt")
        os.remove("./encode.txt")
    except Exception as e:
        print(e)
# enc()