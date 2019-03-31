from Decryption import dec

if __name__ == "__main__":
    prKey = open("./private_key.txt", "r")
    prKey = prKey.read()
    prKey = prKey.split("-")
    prKey = (int(prKey[0]), int(prKey[1]))
    
    dec(prKey)