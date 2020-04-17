from product import Product

class Producthandler:
    def __init__(self, result):
        self.result = result

    def select_a_product(self, goal):
        header_lst = ("ProductID", "Product", "Leverancier", "Inkoopprijs", "Voorraad", "Minimum", "Maximum")
        print("De volgende producten zitten in het systeem:")
        #counter = 0

        for header in header_lst:
            header = '{:15}'.format(header)
            print(header, end=" ")
        print("\n")
        for productlijst in self.result:
            for product in productlijst:
                product = '{:15}'.format(str(product))
                print(product, end=" ")
            print("\n")

        if goal == "placeorder":
            list_of_items = {}
            flag = True
            while flag:
                try:
                    chosen_product = input("Welk product kies je? (ProductID)\n")

                    if chosen_product != "":
                        if chosen_product.isalpha():
                            print("Vul aub een kloppend ID in")
                        else:
                            chosen_product = int(chosen_product) - 1
                            current_quantity = self.result[chosen_product][4]
                            max_quantity = self.result[chosen_product][6]
                            allowed_to_order = max_quantity - current_quantity
                            if allowed_to_order == 0:
                                print("De voorraad van dit product is al maximaal, je kunt hier geen extra van bijbestellen.")
                            else:
                                hoeveelheid = input("Hoeveel stuks wil je bestellen? (max " + str(allowed_to_order) + ".)")

                                if hoeveelheid == "" or hoeveelheid.isalpha():
                                    print("Vul aub een getal in")
                                else:
                                    if int(hoeveelheid) <= int(allowed_to_order):
                                        list_of_items[(self.result[chosen_product][0])] = hoeveelheid
                                        print("item " + self.result[chosen_product][1] + " toegevoegd aan order!")
                                        next = input("Druk op 'n' om nog een product toe te voegen. Druk op enter "
                                              "om de bestelling af te ronden.")
                                        if next == 'n':
                                            flag = True
                                        else:
                                            flag = False
                                            return list_of_items
                                    else:
                                        print("Je probeert meer te bestellen dan de maximum voorraad toelaat. Probeer minder"
                                              " te bestellen.")
                    else:
                        flag = False
                        return list_of_items
                except IndexError:
                    print("Je hebt een ID gekozen die niet in de database staat. Probeer het nog een keer.")
        elif goal == "productaanpassen":
            chosen_product = int(input("Welk product kies je? (ProductID)"))
            chosen_product = chosen_product - 1
            return (self.result[chosen_product])

        else:
            input("Druk op 'Enter' om terug te gaan naar het menu")

    def product_aanpassen_handler(self, company, chosen_product):
        for tuple in company:
            for id in tuple:
                leverancier = id

        product_to_change = Product(int(chosen_product[0]), int(leverancier), str(chosen_product[1]),
                                    float(chosen_product[3]), int(chosen_product[4]),
                                    int(chosen_product[5]), int(chosen_product[6]))

        return product_to_change