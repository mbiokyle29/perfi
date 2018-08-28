# file: base.py
# author: mbiokyle29


from perfi.utils import format_dollar_amount, format_percent


class Liability(object):
    """ Most basic version of a libility, has a negative principal and an apr """

    def __init__(self, label, principal, apr):
        self._label = str(label)
        self._principal = float(principal)
        self._apr = float(apr)

    def __str__(self):
        return (
            f"<{self.__class__.__name__} | {self._label} | "
            f"{format_dollar_amount(self._principal)} "
            f"({format_percent(self._apr)})>"
        )

    @classmethod
    def from_yaml(cls, block):
        return cls(
            block["label"],
            block["principal"],
            block["apr"]
        )

    @property
    def label(self):
        return self._label

    @property
    def principal(self):
        return self._principal

    @property
    def apr(self):
        return self._apr
