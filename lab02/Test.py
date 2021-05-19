import datetime
class Product:
    def __init__(self, id, name, price, release_date, rating):
        self.id = id
        self.name = name
        self.price = price
        self.release_date = datetime.datetime.strptime(release_date, '%Y-%m-%d')
        self.rating = rating

    def __repr__(self):
        return '{}'.format(self.id)

database = [
    Product(1, 'A', 5000, '2019-10-24', 4.7),
    Product(2, 'B', 300, '2018-1-14', 3.1),
    Product(3, 'C', 1200, '2020-3-3', 5),
    Product(4, 'D', 10, '2019-7-19', 4.2),
    Product(5, 'E', 50, '2019-12-4', 3.5),
    Product(6, 'F', 180, '2021-3-8', 3.9)
]

print(database)