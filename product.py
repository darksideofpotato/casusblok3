class Product:
    def __init__(self, productID, leverancierID, productnaam, inkoopprijs,  voorraad, min, max):
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
            return print("Er is nog genoeg op voorraad")
            pass

    def modify_product(self, leverancier):
        new_product_leverancier = leverancier
        if leverancier == "":
            new_product_leverancier = self.leverancierID
        new_product_name = input("Wat is de nieuwe naam van het product?")
        if new_product_name == "":
            new_product_name = self.productnaam

        new_product_inkoopprijs = input("Wat is de nieuwe inkoopprijs?")
        if new_product_inkoopprijs == "":
            new_product_inkoopprijs = self.inkoopprijs

        new_product_voorraad = input("Wat is de nieuwe voorraad?")
        if new_product_voorraad == "":
            new_product_voorraad = self.voorraad

        new_product_minvoorraad = input("Geef een limiet van de minimum voorraad")
        if new_product_minvoorraad == "":
            new_product_minvoorraad = self.min

        new_product_maxvoorraad = input("Geef een limiet van de maximum voorraad")
        if new_product_maxvoorraad == "":
            new_product_maxvoorraad = self.max

        modified_product = [new_product_leverancier, new_product_name, new_product_inkoopprijs,
                            new_product_voorraad, new_product_minvoorraad, new_product_maxvoorraad]

        return modified_product
