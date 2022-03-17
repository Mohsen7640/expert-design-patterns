from structural.composite.basket.composite.package import PackageProduct
from structural.composite.basket.leaf.single import SingleProduct
from structural.composite.basket.models.basket import Basket


def run():
    receipt = SingleProduct(name='Receipt', amount=2)

    hammer = SingleProduct(name='Hammer', amount=10)
    package1 = PackageProduct()
    package1.add(hammer)

    charger = SingleProduct(name='Charger', amount=10)
    package2 = PackageProduct()
    package2.add(charger)

    phone = SingleProduct(name='Phone', amount=150)
    headphone = SingleProduct(name='Head Phone', amount=20)
    package3 = PackageProduct()
    package3.add(phone)
    package3.add(headphone)

    package4 = PackageProduct()
    package4.add(package2)
    package4.add(package3)

    package = PackageProduct()
    package.add(receipt)
    package.add(package1)
    package.add(package4)

    basket = Basket()
    basket.add(hammer)
    basket.add(package3)
    basket.add(package)

    print(basket.total_price())


if __name__ == '__main__':
    run()
