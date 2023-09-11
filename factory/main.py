from factory.config.SMTPConnectorFactory import SMTPConnectorFactory

if __name__ == '__main__':
    daum = SMTPConnectorFactory.create('Daum')
    daum.connect()
