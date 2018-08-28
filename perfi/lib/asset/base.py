# file: base.py
# author: mbiokyle29

class Asset(object):
    """ Most basic version of an asset, has a principal and an apr """

    def __init__(self, principal, apr):
        self._principal = float(principal)
        self._apr = float(apr)

    @property
    def principal(self):
        return self._principal

    @property
    def apr(self):
        return self._apr
