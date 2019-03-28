from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'b.jairam0512@gmail.com',
    "MAIL_PASSWORD": 'jaibjv@hotmail'
}

app.config.update(mail_settings)
mail = Mail(app)

def sendMail(to_mail, msg):
    with app.app_context():
        msg = Message(subject="Hello",
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=[to_mail], # replace with your email for testing
                      body=msg
                      )
        with app.open_resource("./private_key.txt") as fp:
            msg.attach("private_key.txt", "./private_key.txt", fp.read())
        mail.send(msg)