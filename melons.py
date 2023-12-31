"""Classes for melon orders."""
class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""
    def __init__(self, species, qty, country_code = None):
        self.species = species
        self.qty = qty
        self.shipped = False


    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        #christmas_melons_price = base_price * 1.5

        if self.species == "Christmas melon":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price 

        return total


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08

    


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    
    order_type="International"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty) 
        country_code = country_code
        
    def get_total(self):
        super().get_total(self)

        if self.qty < 10:
            total = total + 3

        return total       


    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):

    def __init__(self, species, qty):
        super().__init__(species, qty)
        self.passed_inspection = False 

    order_type = "Government"
    tax = 0

    def mark_inspection(self, passed):
       
        if passed == True:
            self.passed_inspection = True
        else:
            self.passed_inspection == False