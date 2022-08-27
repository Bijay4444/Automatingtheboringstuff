import imapclient
import pyzmail

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
print(conn.login('bijay17khadka@gmail.com', 'Bij@y4444'))

conn.select_folder('INBOX', readonly=True)

UIDs = conn.search(['SEEN'])
print(UIDs)

rawMessage = conn.fetch([79], ['BODY[]', 'FLAGS'])
print(rawMessage)
message = pyzmail.PyzMessage.factory(rawMessage[79][b'BODY[]'])

# print(message.get_address('from'))
# print(message.get_address('to'))
# print(message.text_part)
# print(message.html_part)

# print(message.text_part.get_payload().decode('UTF-8'))

