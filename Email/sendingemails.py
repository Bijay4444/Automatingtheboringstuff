import smtplib

#calling smtp function passing domain and port number which is 587
conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo() #connecting to smtp server

#starttls begings encryption
print(conn.starttls())
print(conn.login('bijay17khadka@gmail.com', 'Bij@y4444'))

print(conn.sendmail('bijay17khadka@gmail.com', 'bk006822@gmail.com', 'Subject: Python script check \n\n Hi Bijay I am sending this automated message from python script'))
