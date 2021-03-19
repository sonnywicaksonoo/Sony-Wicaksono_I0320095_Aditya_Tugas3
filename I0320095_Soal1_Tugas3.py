#Membuat List Teman
teman = ['Yeario', 'Tito', 'Bagus', 'Raysa', 'Rara', 'Nanda', 'Ano', 'William', 'Aji', 'Rahmat']

#Menampilkan Nama Teman Urutan Indeks 4,6,7
print("Nama teman indeks 4,6,7: ", teman[4], ",", teman[6], ",", teman[-3])

#Mengganti Nama Teman Urutan 3,5,9
teman[2] = 'Yukuri'
teman[4] = 'Uli'
teman[-2] = 'Tazkiya'

#Menambahkan 2 Nama Teman
teman.append('Alvin')
teman.append('Vincent')

#Menampilkan Nama Teman dengan Perulangan
print(teman*2)

#Menampilkan Panjang List
print(len(teman))
