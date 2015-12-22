from PyQt5 import QtCore, QtWidgets

from qhangups.ui_qhangupsbrowser import Ui_QHangupsBrowser
import qhangups.oauth2_helper


class QHangupsBrowser(QtWidgets.QDialog, Ui_QHangupsBrowser):
    """Extremely simple web browser"""
    authenticationCode = ""
    def __init__(self, url="", parent=None):
        super().__init__(parent)
        self.setupUi(self)


        self.browserWebView.loadFinished.connect(self.loadFinished)

        if url:
            self.load(url)

    def load(self, url):
        """Load URL"""
        self.browserWebView.load(QtCore.QUrl.fromUserInput(url))

    def loadFinished(self, status):
        """Check Page Title weather it contains an Authentication Code"""
        title = self.browserWebView.title()
        if title.find('Success') == 0:
            t = qhangups.oauth2_helper.parseOAuth2Title(title)
            if t[0] == 'Success':
                if 'code' in t[1]:
                    self.authenticationCode = t[1]['code']
                    self.close()
        return True

