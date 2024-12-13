from animal import animal

class amphibi (animal):
    def __init__(self, name,makanan,hidup,berkembang_biak,jenis_air, bernapas):
        super ().__init__(name,makanan,hidup,berkembang_biak)
        self.jenis_air = jenis_air
        self.bernapas = bernapas

    def info_amphibi(self):
        super().info_animal()
        print('jenis air \t\t\t\t :', self.jenis_air,
              '\nbernapas \t\t\t\t :', self.bernapas)
print('===========================================================================')     
amphibi1 = amphibi('katak','serangga','dua alam','bertelur','air tawar','kulit dan paru paru')
amphibi1.info_amphibi()
print('===========================================================================')     
amphibi2 = amphibi('salamander','serangga dan cacing','dua alam','bertelur dan beranak','air tawar','kulit dan insang dan juga paru paru')
amphibi2.info_amphibi()
print('===========================================================================')     
amphibi2 = amphibi('Axolt','serangga dan cacing','dua alam','bertelur','air tawar','paru paru dan insang')
amphibi2.info_amphibi()