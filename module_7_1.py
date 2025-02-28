class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    def __init__(self):
        self.__file_name = "products.txt"

    def get_products(self):
        try:
            with open(self.__file_name, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            return ""

    def add(self, *products):
        existing_products = self.get_products().splitlines()
        existing_names = {line.split(",")[0] for line in existing_products}

        with open(self.__file_name, "a", encoding="utf-8") as file:
            for product in products:
                if product.name in existing_names:
                    print(f"Продукт {product.name} уже есть в магазине")
                else:
                    file.write(str(product) + "\n")
                    print(f"Продукт {product.name} добавлен в магазин")

def main():
    print("Первый запуск:")
    p1 = Product("Potato", 50.5, "Vegetables")
    p2 = Product("Spaghetti", 3.4, "Groceries")
    p3 = Product("Potato", 5.5, "Vegetables")

    print(p2)
    print(p1)
    print(p2)
    print(p3)

    print("\nВторой запуск:")
    s2 = Shop()
    print(p2)
    s2.add(p1, p2, p3)
    print(s2.get_products())

if __name__ == "__main__":
    main()
