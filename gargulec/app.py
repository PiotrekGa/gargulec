from flask import Flask
from flask_mail import Mail, Message
import requests
from time import sleep

sender = ''
receiver = ''
password = ''
search_phrase = '<li id="1230" onClick="przypomnienie_okno(this.id);" class="zeroproduct"'
url = 'https://mlecollection.com/sklep/wszystkie/golf-bormio,593#'

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = sender
app.config['MAIL_PASSWORD'] =
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route("/")
def index(search_phrase, url, receiver, sender):

    msg1 = Message("Available!",
                  sender=sender,
                  recipients=[receiver])

    cnt = 0

    r = requests.get(url)

    while search_phrase in r.text:

        cnt += 1
        sleep(60)

        r = requests.get(url)

        if cnt % 100 == 0:

            msg2 = Message("Works!",
                           sender=sender,
                           recipients=[sender])

            with open('log.txt', 'a') as file:
                file.write(''.join([str(cnt), '\n']))

            mail.send(msg2)

        mail.send(msg1)

    return 'Mail sent'


if __name__ == '__main__':
   app.run(debug = True)
