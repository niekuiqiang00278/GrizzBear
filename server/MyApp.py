from PyQt5.QtWidgets import QApplication

from server.bis.EataBis import EataBis
from server.bis.PltBis import PltBis
from server.plux.XActivity import XActivity

import sys


class MyApp(XActivity):
    def __init__(self):
        XActivity.__init__(self)
        self.etat = EataBis()
        self.plt = PltBis(self.etat.mapi.crust)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
