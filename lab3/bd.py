from BD_2.model import *
from BD_2.view import View
from BD_2.controller import *
from BD_2.menu import *
from BD_2.modelORM import *

def main():
    item = ControllerItem(ModelItemORM, View)
    customer = ControllerCustomer(ModelCustomerORM, View)
    shop = ControllerShop(ModelShopORM, View)
    order = ControllerOrder(ModelOrderORM, View)

    menu(item, customer, shop, order)

    customer.disconnect()
    item.disconnect()
    order.disconnect()


if __name__ == '__main__':
    main()
