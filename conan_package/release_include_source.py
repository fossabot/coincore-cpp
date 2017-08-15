import os
import shutil
from base import CoinCoreBase

class CoinCoreTesting(CoinCoreBase):
    exports = "base.py"

    exports_sources = "../sources*"

    def source(self):
        os.mkdir("repo")
        shutil.move("sources", "repo/")
