class Product():
    def __init__(self,name,price,weight,discount):
        self.name=name
        self.price=price
        self.weight=weight
        self.discount=discount
    def __repr__(self):
        return repr((self.name,self.price,self.weight))
    def discountPrice(self):
        return self.price-(self.price*self.discount)

if __name__=="__main__":
    prodList=[
        Product("widget",50,10,0.05),
        Product("Doohickey",40,8,0.15),
        Product("Thingamabob",35,12,0.0),
        Product("Gadget",65,7,0.20)
    ]
print(prodList)
'''
def prodsort(Product):
    return Product.price
print(sorted(prodList,key=prodsort))
'''
print(sorted(prodList,key=lambda p:p.price))