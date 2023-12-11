"""Django e-mail SMTP backend with DKIM signing."""


import smtplib
from builtins import bytes

import dkim
from django.conf import settings
from django.core.mail.backends.smtp import EmailBackend as SMTPEmailBackend
from django.core.mail.message import sanitize_address


class EmailBackend(SMTPEmailBackend):
    """SMTP backend that signs the message with DKIM."""

    def _send(self, email_message):
        """Do actual sending and DKIM signing."""
        if not email_message.recipients():
            return False
        encoding = email_message.encoding or settings.DEFAULT_CHARSET
        mail_from = email_message.from_email
        if hasattr(settings, "EMAIL_SMTP_MAIL_FROM"):
            mail_from = settings.EMAIL_SMTP_MAIL_FROM
        smtp_mail_from = sanitize_address(mail_from, encoding)
        recipients = [
            sanitize_address(addr, encoding) for addr in email_message.recipients()
        ]
        message = email_message.message()
        try:
            message_string = message.as_bytes(linesep="\r\n")
            signature = dkim.sign(
                message_string,
                bytes(settings.DKIM_SELECTOR, "ascii"),
                bytes(settings.DKIM_DOMAIN, "ascii"),
                bytes(settings.DKIM_PRIVATE_KEY, "ascii"),
            )
            self.connection.sendmail(
                smtp_mail_from, recipients, signature + message_string
            )
        except (smtplib.SMTPException, dkim.DKIMException):
            if not self.fail_silently:
                raise
            return False
        return True
