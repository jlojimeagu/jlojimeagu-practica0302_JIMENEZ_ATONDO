class Pedidito:
    def __init__(self, list_product, list_cantidad):
        self.__list_product = list_product
        self.__list_cantidad = list_cantidad

    def total_pedido(self):
        total = 0
        for (p, c) in zip(self.__list_product, self.__list_cantidad):
            total = total + p.calcular_total(c)

    def ver_pedidito(self):
        for (p, c) in zip(self.__list_product, self.__list_cantidad):
            print('producto:', p.nombre, 'cantidad:'+str(c))
