from Encryption import enc
from sendmail import sendMail
from senddata import sendData
import secrets, os

process_id = secrets.token_hex(6)

if __name__ == "__main__":
    email_add = input("Enter the email address")
    enc()
    sendData(process_id, email_add)
    sendMail(email_add, process_id)

    try:
        os.remove("./private_key.txt")
    except Exception as e:
        print(e)