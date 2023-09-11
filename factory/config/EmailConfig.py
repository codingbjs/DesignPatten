from enum import Enum


class EmailConfig(Enum):

    NAVER_CONFIG = ('smtp.naver.com', 'mc', '1234', 5000)
    DAUM_CONFIG = ('smtp.naver.com', 'mc', '1234', 5000)
    GMAIL_CONFIG = ('smtp.naver.com', 'mc', '1234', 5000)

    def __init__(self, url, id, password, timeout):
        self.URL = url
        self.ID = id
        self.PASSWORD = password
        self.TIMEOUT = timeout
