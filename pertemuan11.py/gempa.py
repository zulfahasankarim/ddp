class gempa:

    def __init__(self,skala,lokasi):
        self.skala = skala
        self.lokasi = lokasi

    def dampak(self):

        print(f"ada gempa coy di {self.lokasi}")
        print(f"skala dari gempa ini adalah {self.skala}")
        if self.skala <= 2:
            print('ga berasa cuy')
    
        elif self.skala > 2 and self.skala <=4 :
            print('dampak gempa bangunan retak retak')
    
        elif self.skala > 4 and self.skala <=6 :
            print('dampak gempa bangunan roboh')

        elif self.skala > 6 :
            print('dampak gempa bangunan roboh dan potensi tsunami LARI!!')
        
        else:
            print('sistem error')



# gempa1 = gempa(5,"jawa barat")
# gempa1.dampak()

# gempa1 = gempa(1.2,"banten")
# gempa1.dampak()