import os
import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

"""
Gửi email được thực hiện nhờ thư viện smtplib có sẵn của Python.
Giao thức dùng để gửi nhận email có tên là SMTP.
"""


def send_gmail(
    myemail, to_addresses, content="chào bạn", subject="Thông báo yêu đương"
):

    context = ssl.create_default_context()
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls(context=context)
    smtpserver.ehlo()

    with open(os.path.join(os.path.dirname(__file__), ".gmail.secret")) as f:
        app_password = f.read().strip()

    filename = "localbtcVND.csv"
    
    msg = MIMEMultipart("alternative")
    print(msg)
    msg["Subject"] = subject
    msg["From"] = "Người tình bí mật" # tên người gửi
    msg["To"] = ", ".join(to_addresses) # có dòng này, gửi to, ko có sẽ gửi bcc
    
    smtpserver.login(myemail, app_password)
    
    ## text/html
    text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""
    html = """\
<html>
  <body>
    <p>Chào bạn,<br>
       How are you?<br>
       <a href="http://www.realpython.com">Real Python</a> 
       has many great tutorials.
    </p>
  </body>
</html>
"""
    ## attach
    #open binary mode
    with open(os.path.join(os.path.dirname(__file__), filename), 'rb') as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    
    # Encode file in ASCII characters to send by email   
    encoders.encode_base64(part)
    

    ##  chỉ định kiểu và add vào msg
    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    # add msg
    msg.attach(part)
    msg.attach(part1)
    msg.attach(part2)
    print(msg)
    # print(msg.as_string())
    smtpserver.sendmail(myemail, to_addresses, msg.as_string())

def main():
    YOUREMAIL = "hayashibutler@gmail.com"
    YOUREMAIL2= ["lam.tranledien@gmail.com","giaohangtienloi.vn@gmail.com"]
    content='''
    Xin chào
    tôi là người yêu của bạn
    hãy yêu tôi đi
    '''
    send_gmail(YOUREMAIL, YOUREMAIL2 ,content=content)
    print("sent")


if __name__ == "__main__":
    main()
