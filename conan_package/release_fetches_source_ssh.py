from base import CoinCoreBase

# Use this recipe when creating recipies for stable channel

class CoinCoreRelease(CoinCoreBase):
    exports = "base.py"

    # make extra sure no sources are exported by base package
    exports_sources = ""

    def source(self):
        self.run("git clone %s repo" % self.repo_ssh_url)
        self.run("cd repo && git checkout v%s" % self.version)
