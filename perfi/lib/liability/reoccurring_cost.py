# file: reocurring_cost.py
# author: mbiokyle29
from .base import Liability
from perfi.utils import format_dollar_amount, Every


class ReoccurringCost(Liability):
    """ A reoccurring cost like utility bill, etc """

    def __init__(self, label, amount, raw_every):
        super(ReoccurringCost, self).__init__(label, amount, 0)
        self._every = Every(raw_every)

    def __str__(self):
        return (
            f"<{self.__class__.__name__} | {self._label} | "
            f"{format_dollar_amount(self._principal)} | "
            f"({self._every.value}) >"
        )

    @classmethod
    def from_yaml(cls, block):
        return cls(
            block["label"],
            block["amount"],
            block.get("every", "monthly")
        )

    @property
    def cost(self):
        return self._principal

    @property
    def every(self):
        return self._every
