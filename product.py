class Product:
    def __init__(self, productID, leverancierID, productnaam, inkoopprijs,  voorraad, min, max):
        self.productID = productID
        self.leverancierID = leverancierID
        self.productnaam = productnaam
        self.inkoopprijs = inkoopprijs
        self.voorraad = voorraad
        self.min = min
        self.max = max

    # Een functie om te controleren of er nog genoeg op voorraad is, of dat er bijbesteld moet worden
    def check_quantity(self):
        if int(self.voorraad) < int(self.min):
            quantity_to_order = int(self.max) - int(self.voorraad)

            return quantity_to_order
        else:
            return print("Er is nog genoeg op voorraad")
            pass

    # Een functie waarmee het product kan worden aangepast. Heeft een aantal input checks, en behoud
    # de eigen waarde indien deze niet aangepast wordt.

    def modify_product(self, leverancier):
        new_product_leverancier = leverancier
        if leverancier == "":
            new_product_leverancier = self.leverancierID
        new_product_name = input("Wat is de nieuwe naam van het product? "
                                 "(Druk op enter om de huidige waarde " + self.productnaam + " te behouden)")
        if new_product_name == "":
            new_product_name = self.productnaam

        new_product_inkoopprijs = input("Wat is de nieuwe inkoopprijs?"
                                    "(Druk op enter om de huidige waarde " + str(self.inkoopprijs) + " te behouden)")
        if new_product_inkoopprijs == "":
            new_product_inkoopprijs = self.inkoopprijs

        max_to_order = int(self.max)
        new_product_voorraad = input("Wat is de nieuwe voorraad? (max " + str(max_to_order) + ")" 
                                     "(Druk op enter om de huidige waarde " + str(self.voorraad) + " te behouden)")

        if new_product_voorraad == "":
            new_product_voorraad = self.voorraad

        while int(new_product_voorraad) > int(max_to_order):
            new_product_voorraad = input("Je probeert meer te orderen dan de limiet. Probeer het nog een keer.")

        new_product_minvoorraad = input("Geef een limiet van de minimum voorraad"
                                        "(Druk op enter om de huidige waarde " + str(self.min) + " te behouden)")
        if new_product_minvoorraad == "":
            new_product_minvoorraad = self.min

        new_product_maxvoorraad = input("Geef een limiet van de maximum voorraad"
                                        "(Druk op enter om de huidige waarde " + str(self.max) + " te behouden)")
        if new_product_maxvoorraad == "":
            new_product_maxvoorraad = self.max

        modified_product = [new_product_leverancier, new_product_name, new_product_inkoopprijs,
                            new_product_voorraad, new_product_minvoorraad, new_product_maxvoorraad]

        return modified_product
