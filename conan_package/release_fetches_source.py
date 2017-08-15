from base import CoinCoreBase

# Use this recipe when creating recipies for stable channel

class CoinCoreStable(CoinCoreBase):
    exports = "base.py"

    # make extra sure no sources are exported by base package
    exports_sources = ""

    def source(self):
        self.run("git clone %s repo" % self.git_repo)
        self.run("cd repo && git checkout v%s" % self.version)
