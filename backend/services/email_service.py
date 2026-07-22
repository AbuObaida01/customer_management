import smtplib

from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart

from config import (
    EMAIL_HOST,
    EMAIL_PORT,
    EMAIL_ADDRESS,
    EMAIL_PASSWORD
)
class EmailService:

    @staticmethod
    def send_otp(
        receiver_email,
        otp
    )-> bool:
        message = MIMEMultipart()
        message["From"] = EMAIL_ADDRESS
        message["To"] = receiver_email
        message["Subject"] = "Customer Management System - OTP Verification"
        body = f"""
Hello,

We received a login request for your Customer Management System account.

Your One-Time Password (OTP) is:

    {otp}

This OTP is valid for 5 minutes.

If you did not request this login, you can safely ignore this email.

Do not share this OTP with anyone.

Regards,
Customer Management System Team
"""
        message.attach(
            MIMEText(
                body,
                "plain"
            )
        )
        try:
            with smtplib.SMTP(EMAIL_HOST,EMAIL_PORT) as server:
                
                server.starttls()

                server.login(
                    EMAIL_ADDRESS,
                    EMAIL_PASSWORD
                )
                server.sendmail(
                    EMAIL_ADDRESS,
                    receiver_email,
                    message.as_string()
                )
                server.quit()
                return True
        except Exception as error:
            print(f"Error sending email: {error}")
            return False