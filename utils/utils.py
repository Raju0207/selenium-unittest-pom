from mailosaur import MailosaurClient
from mailosaur.models import SearchCriteria

# Available in the API tab of a server
api_key = "j9LyhaYydBibEaX50BD7ukMUgmMpPJRb"
server_id = "4ahr8l6e"
server_domain = "4ahr8l6e.mailosaur.net"


def get_otp_from_mail():
    mailosaur = MailosaurClient(api_key)

    criteria = SearchCriteria()
    criteria.sent_to = "sitting-possibly@" + server_domain

    email = mailosaur.messages.get(server_id, criteria)

    otp = list(email.subject[-6:])

    print(otp)
    return otp
