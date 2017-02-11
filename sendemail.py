import smtplib 
from_name = 'Bob'
from_addr = 'yourusername@gmail.com'  
to_name = 'Rick'
to_addr  = 'david@someemail.com' 
message = """From: {} <{}> 
To: {} <{}> 
Subject: {} 

{} 
""" 
subject = 'Hello world'
msg = 'Whats good?'

message_to_send = message.format(from_name, from_addr, to_name, to_addr, subject, msg) 

# Credentials (if needed) 
username = 'yourusername@gmail.com' 
password = '{youremailapppassword}'

# The actual mail send 
server = smtplib.SMTP('smtp.gmail.com:587') 
server.starttls() 
server.login(username, password) 
server.sendmail(from_addr, to_addr, message_to_send) 
server.quit() 