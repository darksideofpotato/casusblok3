from product import Product

class Producthandler:
    def __init__(self, result):
        self.result = result

    def select_a_product(self, goal):
        header_lst = ("ProductID", "Product", "Leverancier", "Inkoopprijs", "Voorraad", "Minimum", "Maximum")
        print("De volgende producten zitten in het systeem:")
        counter = 0

        # Hij doet alleen het DB product raar formatten
        for x in header_lst:
            x = '{:15}'.format(x)
            print(x, end=" ")
        print("\n")
        for y in self.result:
            for x in y:
                x = '{:15}'.format(str(x))
                print(x, end=" ")
        print("\n")
        for product in self.result:
            counter = counter + 1
            print(str(counter) + ". " + str(product))

        if goal == "placeorder":
            list_of_items = {}
            flag = True
            while flag:
                chosen_product = input("Welke product kies je? (nummer)")

                if chosen_product != "":
                    chosen_product = int(chosen_product) - 1

                    hoeveelheid = input("Hoeveel stuks wil je bestellen?")
                    list_of_items[(self.result[chosen_product][0])] = hoeveelheid

                    print("item " + self.result[chosen_product][1] + " toegevoegd aan order!")
                else:
                    flag = False
                    return list_of_items

        else:
            chosen_product = int(input("Welk product kies je? (nummer)"))
            chosen_product = chosen_product - 1

            return (self.result[chosen_product])

    def product_aanpassen_handler(self, company, chosen_product):
        for tuple in company:
            for id in tuple:
                leverancier = id

        product_to_change = Product(int(chosen_product[0]), int(leverancier), str(chosen_product[1]),
                                    float(chosen_product[3]), int(chosen_product[4]),
                                    int(chosen_product[5]), int(chosen_product[6]))

        return product_to_change