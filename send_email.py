from email.mime.text import MIMEText
import smtplib

def send_email(email, height, average_height, count):
    from_email = "Height Collector <kalzkidandaba@gmail.com>"
    to_email = email

    subject = "Height data"
    message = "Hey there, your height is <strong>%s</strong>. Average height of all is <strong>%s</strong> and that is calculated out <strong>%s</strong> of people" % (height, average_height, count)

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    mailtrap = smtplib.SMTP("smtp-relay.sendinblue.com", 587)
    mailtrap.login("kalzkidandaba@gmail.com", "gRa1VT64GAIYNvL0")
    mailtrap.sendmail(from_email, to_email, message)
