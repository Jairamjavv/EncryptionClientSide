from twilio.rest import Client

def sendSMS():
    account_sid = 'AC2f51c7ecb72ee4bb87add5e7005ebb9c'
    auth_token = '66f7026f4bcb1163235626663b6084bb'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body = 'Video Captured. Movement Detected',
        from_ = '+12028166838',
        to = '+919597341717'
    )

    print(message.sid)

# sendSMS()