from factory.config.DaumConnector import *
from factory.config.EmailConfig import *
from factory.config.GmailConnector import *
from factory.config.NaverConnector import *


class SMTPConnectorFactory:
    @staticmethod
    def create(mail):
        connectors = {
            'Daum': DaumConnector(EmailConfig.DAUM_CONFIG),
            'Naver': NaverConnector(EmailConfig.NAVER_CONFIG),
            'Gmail': GmailConnector(EmailConfig.GMAIL_CONFIG)
        }
        return connectors[mail]
