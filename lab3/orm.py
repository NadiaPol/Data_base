class Shop(base.Base):
    __tablename__ = 'Shop'
    ShopId = Column('ShopId', Integer,  primary_key=True)
    ShopName = Column('ShopName', Text) 
    ShopStreet = Column('ShopStreet', Text) 
    order = relationship('Order') 

    def __repr__(self):
        return "<Shop(ShopId='{}', ShopName='{}', 			ShopStreet='{}')>"\
            .format(self.ShopId, self.ShopName, self.ShopStreet)

class Item(base.Base):
    __tablename__ = 'Item'
    ItemId = Column('ItemId', Integer,  primary_key=True)
    ItemName = Column('ItemName', Text) 
    ItemPrice = Column('ItemPrice', Money)                 	ItemQuantity = Column('ItemQuantity', Text)                         	ItemColor = Column('ItemColor', Text)                          	ItemMaterial = Column('ItemMaterial', Text)
    order = relationship('Order') 

    def __repr__(self):
        return "<Item(ItemId='{}', ItemName='{}', 			ItemPrice='{}', ItemQuantity='{}', ItemColor='{}', ItemMaterial='{}')>"\
            .format(self.ItemId, self.ItemName, self.ItemPrice, self.ItemQuantity, self.Color, self.ItemMaterial)


class Customer(base.Base):
    __tablename__ = 'Customer'
    CustId = Column('CustId', Integer,  primary_key=True)
    CustName = Column('CustName', Text) 
    	CustPhone = Column('CustPhone', Text)                          	CustSex = Column('CustSex', Text)
    order = relationship('Order') 

    def __repr__(self):
        return "<Customer(CustId='{}', CustName='{}', 			CustPhone='{}', CustSex='{}')>"\
            .format(self.CustId, self.CustName, self.CustPhone, self.CustSex)


class Order(base.Base):
    __tablename__ = 'Order'
    OrderId = Column('OrderId', Integer,  primary_key=True)
    OrderDate = Column('OrderDate', Date) 
    	ShopId = Column('ShopId', Integer,  ForeignKey('Shop.ShopId'))
	CustId = Column('CustId', Integer,  ForeignKey('Customer.CustId'))
	ItemId = Column('ItemId', Integer, ForeignKey('Item.ItemId'))
    

    def __repr__(self):
        return "<Order(OrderId='{}', OrderDate='{}', 			ShopId='{}', CustId='{}', ItemId='{}')>"\
            .format(self.OrderId, self.OrderDate, self.ShopId, self.CustId, self.ItemId)

