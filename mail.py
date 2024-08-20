import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Création de l'objet MIMEMultipart
msg = MIMEMultipart()
msg['From'] = 'romainkiol@gmail.com'
msg['To'] = 'minteur12@gmail.com'
msg['Subject'] = 'Le sujet de mon mail'

# Attacher le message au corps de l'email
message = 'Bonjour !'
msg.attach(MIMEText(message, 'plain'))

# Configuration du serveur SMTP
mailserver = smtplib.SMTP('smtp.gmail.com', 587)
mailserver.ehlo()
mailserver.starttls()
mailserver.ehlo()

# Connexion et envoi de l'email
mailserver.login('romainkiol@gmail.com', 'rwhy mpso jybm iduz')
mailserver.sendmail('romainkiol@gmail.com', 'minteur12@gmail.com', msg.as_string())

# Fermeture de la connexion au serveur
mailserver.quit()
