from email.mime.text import MIMEText
import smtplib

def send_email(email, height):
    from_email = "Height Collector <data@hc.com>"
    to_email = email

    subject = "Height data"
    message = "Hey there, your height is <strong>%s</strong>." % height

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    mailtrap = smtplib.SMTP("smtp-relay.sendinblue.com", 587)
    mailtrap.login("kalzkidandaba@gmail.com", "gRa1VT64GAIYNvL0")
    mailtrap.sendmail(from_email, to_email, message)
