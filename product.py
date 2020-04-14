class Product:
    def __init__(self, productID, leverancierID, productnaam, inkoopprijs,  voorraad, min,max):
        self.productID = productID
        self.leverancierID = leverancierID
        self.productnaam = productnaam
        self.inkoopprijs = inkoopprijs
        self.voorraad = voorraad
        self.min = min
        self.max = max

    def check_quantity(self):
        if int(self.voorraad) < int(self.min):
            quantity_to_order = int(self.max) - int(self.voorraad)

            return quantity_to_order
        else:
            print("Er is nog genoeg op voorraad")
            pass