from abc import ABC, abstractmethod


class ShippingPolicy(ABC):

    @abstractmethod
    def calculate_shipping(self,total_weight):
        ...

class StandardShipping(ShippingPolicy):
    def calculate_shipping(self,total_weight):
        return 5 + 1 * total_weight

class ExpressShipping(ShippingPolicy):
    def calculate_shipping(self,total_weight):
        return 10 + 2 * total_weight

class PickupShipping(ShippingPolicy):
    def calculate_shipping(self,total_weight):
        return 0