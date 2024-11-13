jumlah_barang =int(input('Masukan Jumlah Barang : '))

total_harga= 0
for a in range(jumlah_barang): 
   nilai = int(input(f'Masukan Harga Barang ke-{a + 1}:'))
   total_harga += nilai

total = total_harga + jumlah_barang
print(f'Total Belanjaan : {total: .2F}')