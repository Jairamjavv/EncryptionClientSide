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
import ast
import shutil

# prKey = open("./private_key.txt", "r")
# prKey = prKey.read()
# prKey = prKey.split("-")
# prKey = (int(prKey[0]), int(prKey[1]))

def dec(private_key):
    path1 = "./save"
    #Creating folders
    try:
        os.mkdir(path1)
    except OSError:
        print("Alert! Directory creation failed")

    enc_key = open("./encryptedKey.txt", "r")
    AES_key = ast.literal_eval(enc_key.read())

    cipher_text = open("./encrypted.txt", "rb")
    cipher_text = cipher_text.read()

    #Decryption
    key = decrypt(private_key, AES_key)
    key = key.encode('latin-1')

    counter = Counter.new(128)
    aes = AES.new(key, AES.MODE_CTR, counter=counter)
    encoded = aes.decrypt(cipher_text)

    #Decoding
    encoded = encoded.split(b'.')[:-1]

    c = 0

    for i in encoded:
        f = './save/frame'+str(c)+'.jpg'
        fh = open(f, 'wb')
        fh.write(base64.b64decode(i))
        c = c + 1
    fh.close()

    #code snippet to merge the frames otained in the previous snippet
    def convert_frames_to_video(pathIn, pathout, fps):
        frame_arr = []
        files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
        files.sort(key = lambda x: int(x[5:-4]))
        for i in range(len(files)):
            filename = pathIn + files[i]
            img = cv2.imread(filename)
            height, width, layers = img.shape
            size = (width, height)
    #         print(filename)
            frame_arr.append(img)
        out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*'XVID'), fps, size)

        for i in range(len(frame_arr)):
            out.write(frame_arr[i])
        out.release()

    pathIn = './save/'
    pathOut = './video.avi'
    convert_frames_to_video(pathIn, pathOut, 20.0)

    folder = "./save"
    try:
        shutil.rmtree(folder)
    except OSError:
        print("Alert! The directory can't be removed")

# dec(prKey)