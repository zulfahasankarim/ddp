from oop_bank import *

renji = Bank('100','abarai',10000000000)
bambang = Bank('123','Bambang galon',70000)
Noordin = Bank('345','nordin',878787878)
mamat = Bank('678','mamat gosling',1)
anton = Bank('698','anton resing',1)
suep = Bank('666','suep nyungsep',666666666667)



renji.nabung(1)
bambang.nabung(7800000000)
Noordin.tarik(123)
mamat.tarik(6000000)
anton.tarik(1000000000)
suep.tarik(1)

print(Bank.BANK,
"\n-------------------------")
renji.cetak()
bambang.cetak()
Noordin.cetak()
mamat.cetak()
anton.cetak()
suep.cetak()
print("Jumlah Nasabah: %i orang" %Bank.jmlNasabah)