from produkbrg import Produkbrg

class Stok(Produk):
    
    def __init__(self, produk, qty):
        self.__produk = produk
        self.__qty = qty
        
    def get_produk(self):
        return self.__produk
    
    def get_qty(self):
        return self.__qty