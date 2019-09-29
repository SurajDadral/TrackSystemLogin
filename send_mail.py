import os, ssl, smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def sendMail(
    from_email_address,
    password_of_from_email_address,
    to_email_address,
    email_subject,
    email_body,
    smtp_server_address="smtp.gmail.com",
    smtp_ssl_port=465,
    attachment_images=None,
):
    msg = MIMEMultipart()
    msg["From"] = from_email_address
    msg["To"] = to_email_address
    msg["Subject"] = email_subject
    msg.attach(MIMEText(email_body, "plain"))
    if attachment_images:
        if not isinstance(attachment_images, list) and not isinstance(
            attachment_images, tuple
        ):
            attachment_images = [attachment_images]
        for attachment_image in attachment_images:
            with open(attachment_image, "rb") as image:
                msg.attach(
                    MIMEImage(
                        image.read(), name=os.path.basename(attachment_image)
                    )
                )
    context = ssl.create_default_context()
    while True:
        try:
            server = smtplib.SMTP_SSL(
                smtp_server_address, smtp_ssl_port, context=context
            )
            server.login(from_email_address, password_of_from_email_address)
            server.sendmail(
                from_email_address, to_email_address, msg.as_string()
            )
            server.quit()
            break
        except:
            pass
