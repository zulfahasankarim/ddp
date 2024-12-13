from animal import animal

class karnivora (animal):
    def __init__(self, name,makanan,hidup,berkembang_biak,bernapas,bertaring):
        super ().__init__(name,makanan,hidup,berkembang_biak)
        self.bernapas = bernapas
        self.bertaring = bertaring

    def info_karnivora(self):
        super().info_animal()
        print('bernapas \t\t\t\t :', self.bernapas,
              '\nbertaring \t\t\t\t :', self.bertaring)
print('===========================================================================')     
karnivora1 = karnivora('Singa','Daging','Darat','Beranak','paru paru','Ya')
karnivora1.info_karnivora()
print('===========================================================================')     
karnivora2 = karnivora('Burung Elang','Daging','Udara','Bertelur','paru paru','Tidak')
karnivora2.info_karnivora()
print('===========================================================================')     
karnivora2 = karnivora('Hyena','Daging','Darat','Beranak','paru paru','Ya')
karnivora2.info_karnivora()