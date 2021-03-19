#Membuat Dictionary
dict = {'Nama': 'Sony',
        'Hobi': ['Gardening', 'Netflix'],
        'Sosial Media': ['Instagram', 'Facebook' ,'Twitter','linkedIn'],
        'Lagu Kesukaan': ['Love Song by Grrrl Gang', 'Goodbye to a world by Robert', 'December by Neckdeep'],
        'Makanan Favorit': ['mie goreng', 'nasi goreng', 'ayam goreng']}

#Mengubah Salah Satu Hobi dan Sosial Media
dict['Hobi'][1]=('menari')
dict['Sosial Media'][3]=('Clubhouse')

#Menghapus Dua Makanan Favorit
del dict['Makanan Favorit'][0:2]

#Menambahkan Satu Hobi
dict['Hobi'].append('Riding')

print(dict)
