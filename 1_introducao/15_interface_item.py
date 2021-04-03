"""
Python não oferece a implementação explícita de interfaces, como Java, mas o
mesmo comportamento pode ser replicado de duas formas principais.
"""


from abc import ABC, abstractmethod


class Item1(object):
    def __gt__(self, outro_item):
        raise NotImplementedError()


class Item2(ABC):
    @abstractmethod
    def create_purchase_invoice(self, purchase):
        pass
