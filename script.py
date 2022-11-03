import imaplib

my_email = "deeznuts@gmail.com"
app_generated_password = "thatswhatshesaid"

imap = imaplib.IMAP4_SSL("imap.gmail.com", 993)

imap.login(my_email, app_generated_password)

imap.select("INBOX")

gmail_search = '"category:promotions NOT is: important"'
typ, [msg_ids] = imap.search(None, 'X-GM-RAW', gmail_search)
msg_count = len(msg_ids)
print("calculate message count", msg_count)
if msg_count == 0:
    print("No new messages to be deleted")
else:
    if isinstance(msg_ids, bytes):
        msg_ids.decode()
    msg_ids = ','.join(msg_ids.decode('utf8').split(' '))
    print("Moving to Trash using labels")
    imap.store(msg_ids, '+X-GM-LABELS', '\\Trash')

    print("Emptying Trash folder")
    imap.select('"[Gmail]/Trash"')
    print("Deleting")
    imap.store("1:*", '+FLAGS', '\\Deleted')
    imap.expunge()
    print("Deleted! :)")