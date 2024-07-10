import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os


def send_excel_in_mail(excel_path, docs_type, today_date, scrapping_type):

    sender_email = "ABC@example.com"
    receiver_emails = ["ABC@example.com"]
    password = "qwe rty uio qwe"

    if scrapping_type == 'hist':
        file_ref = f"{today_date}-historical"
    else:
        file_ref = today_date

    if docs_type == 's':
        subject = f"ALL-S-{file_ref}"
    elif docs_type == 'sd':
        subject = f"ALL-Sd-{file_ref}"
    elif docs_type == 'c_t':
        subject = f"T-{file_ref}"
    elif docs_type == '_j':
        subject = f"J-{file_ref}"
    elif docs_type == 'w':
        subject = f"w-{file_ref}"
    else:
        subject = f'Not Defined-{file_ref}'

    body = "Body for email"
    filename = os.path.basename(excel_path)

    # Create a secure SSL context
    smtp_server = "smtp.gmail.com"
    port = 465  # For SSL

    # Create the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = ', '.join(receiver_emails)
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    with open(excel_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    message.attach(part)

    try:
        with smtplib.SMTP_SSL(smtp_server, port) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_emails, message.as_string())
        print(f"Email sent successfully for {docs_type} on {today_date}")
    except Exception as e:
        print(f"Error: {e}")
