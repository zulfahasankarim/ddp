from animal import animal

class mamalia (animal):
    def __init__(self, name,makanan,hidup,berkembang_biak,bernapas,ukuran_tubuh,telinga):
        super ().__init__(name,makanan,hidup,berkembang_biak)
        self.bernapas = bernapas
        self.ukuran_tubuh = ukuran_tubuh
        self.telinga = telinga

    def info_mamalia(self):
        super().info_animal()
        print('bernapas \t\t\t\t :', self.bernapas,
              '\nukuran tubuh \t\t\t\t :', self.ukuran_tubuh,
              '\npunya daun telinga \t\t\t :', self.telinga)
print('===========================================================================')     
hewan = mamalia('Domba','Rumput','Darat','Beranak','paru paru','sedang','ya')
hewan.info_mamalia()
print('===========================================================================') 
hewan2 = mamalia('Paus','Plankton','Laut','Beranak','paru paru','Sangat Besar','tidak')
hewan2.info_mamalia() 
print('===========================================================================')     
hewan = mamalia('Banteng','Rumput','Darat','Beranak','paru paru','Besar','ya')
hewan.info_mamalia()

