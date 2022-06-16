import os
import json
import datetime


os.system('cls')
waktu_sekarang = str(datetime.date.today()) # Format tanggal ("YYYY-MM-DD")
temp_pesan = [] #Variabel untuk menyimpan sementara pesanan konsumen, sebelum konsumen benar - benar memesan dan dimasukkan ke file dataKeluar.json

# Tampilan menu utama
def menuUtama():
    print('--- Selamat Datang di Toko Aman Sentosa ---\n')
    inp = input('Apakah anda admin/konsumen: ').lower()
    if inp == 'admin':
        os.system('cls')
        print('--- Selamat Datang di Toko Aman Sentosa ---\n')
        username = input('Username: ')
        password = input('Password: ')
        os.system('cls')

        if username == 'admin' and password == 'admin':
            while True:
                print('\n--- Selamat Datang di Toko Aman Sentosa ---')
                show_stock(stock)
                menuAdmin()
                adminChoice = input('Masukkan Pilihan: ')
                
                if adminChoice == '1':
                    tambah_stock(stock,data_masuk)
                elif adminChoice == '2':
                    hapus_stock(stock, data_keluar)
                elif adminChoice == '3':
                    ubah_stock(stock,data_masuk,data_keluar)
                elif adminChoice == '4':
                    laporanBarang()
                elif adminChoice == '5':
                    save_stock(STOCK_DATABASE, stock)
                    save_dataMasuk(DATA_MASUK_DATABASE, data_masuk)
                    save_dataKeluar(DATA_KELUAR_DATABASE,data_keluar)
                    input('\nData telah disimpan')
                elif adminChoice == '6':
                    os.system('cls')
                    break
                else:
                    continue
        else:
            input('Username atau password yang anda masukkan salah')
            os.system('cls')
            menuUtama()

    elif inp == 'konsumen':
        while True:
            os.system('cls')
            menuKonsumen(temp_pesan)
            konsumenChoice = input('Masukkan Pilihan: ')

            if konsumenChoice == '1':
                inputPesanan(stock)
            elif konsumenChoice == '2':
                hapusPesanan(temp_pesan,stock)
            elif konsumenChoice == '3':
                struk()
                pesandansimpan()
                break
            elif konsumenChoice == '4':
                os.system('cls')
                break
            else:
                continue          
    else:
        print('Tolong tulis admin/konsumen')


""" ============ File Handling ============ """

# load and save stock.json
def load_stock(arg1):
    with open(arg1) as f:
        return json.load(f)

def save_stock(arg1, arg2):
    with open(arg1, 'w+') as f:
        json.dump(arg2, f, indent=4)
    os.system('cls')


# load and save dataKeluar.json
def load_dataKeluar(arg1):
    with open(arg1) as f:
        return json.load(f)

def save_dataKeluar(arg1, arg2):
    with open(arg1, 'w+') as f:
        json.dump(arg2, f, indent=4)



# load and save dataMasuk.json
def load_dataMasuk(arg1):
    with open(arg1) as f:
        return json.load(f)

def save_dataMasuk(arg1, arg2):
    with open(arg1, 'w+') as f:
        json.dump(arg2, f, indent=4)


STOCK_DATABASE = 'stock.json'
DATA_KELUAR_DATABASE = 'dataKeluar.json'
DATA_MASUK_DATABASE = 'dataMasuk.json'
stock = load_stock(STOCK_DATABASE)
data_keluar = load_dataKeluar(DATA_KELUAR_DATABASE)
data_masuk = load_dataMasuk(DATA_MASUK_DATABASE)



# Function struk untuk ditampilkan ke konsumen ketika ia melakukan checkout pesanan
def struk():
    total_pesan = 0
    total_harga = 0
    os.system('cls')
    print('------------------------------------------------------------')
    print('|--------------------------Struk---------------------------|')
    print('|--------------------Toko Aman Sentosa---------------------|')
    print('|----------------------------------------------------------|')
    print('|',' '*22 + 'PESANAN ANDA' + ' '*22, '|')
    print('| %-12s %-20s %-15s %-6s |'%('TANGGAL', 'NAMA BARANG', 'JUMLAH BARANG', 'HARGA'))
    for i in range(len(temp_pesan)):
        print('| %-12s %-20s %-15s %-6s |'%(temp_pesan[i]['tanggal pesanan'], temp_pesan[i]['nama pesanan'], temp_pesan[i]['jumlah pesanan'], temp_pesan[i]['harga pesanan']))
        total_pesan += temp_pesan[i]['jumlah pesanan']
        total_harga += temp_pesan[i]['harga pesanan']
    print('|' + ' '*58 + '|')
    print('|----------------------------------------------------------|')
    print('| %-33s %-15s %-6s |'%('Total', total_pesan, total_harga))
    print('|----------------------------------------------------------|')
    print('|----------------------Terima Kasih------------------------|')
    print('|----------------------------------------------------------|')
    input('Enter untuk melanjutkan')
    os.system('cls')
    input('Terima kasih telah berbelanja di toko kami')
    os.system('cls')


""" ============ Admin ============ """

# Menampilkan menu admin
def menuAdmin():
    print("\n[1] Tambah Barang\n[2] Hapus Barang\n[3] Ubah Stock Barang\n[4] Laporan Barang\n[5] Simpan\n[6] Keluar\n")


# Penambahan barang pada daftar stock
def tambah_stock(arg1,arg2): # arg1 = stock.json, arg2 = dataMasuk.json
    os.system('cls')
    show_stock(arg1)
    temp_barang = []
    nama_barang = input('Masukkan nama barang: ').upper()

    # Menambahkan semua nama barang di stock.json ke variabel temp_barang
    for i in arg1:
        temp_barang.append(i['nama barang'])

    # Jika nama barang yang diinputkan user sama dengan daftar barang di variabel temp, maka barang hanya akan dijumlahkan saja
    if nama_barang in temp_barang:
        jumlah_barang = int(input('Masukkan jumlah barang: '))
        for k in arg1:
            if k['nama barang'] == nama_barang:
                k['jumlah barang'] += jumlah_barang
                harga_masuk = k['harga barang'] * jumlah_barang
        # Barang yang diinputkan tadi akan ditambahkan ke dataMasuk.json dan dengan keterangan berupa "Jumlah stock ditambah"
        arg2.append({
            'barang masuk':nama_barang,
            'jumlah masuk':jumlah_barang,
            'uang keluar':harga_masuk,
            'tanggal':waktu_sekarang,
            'keterangan':'Jumlah stock ditambah'
        })
        input('Barang telah ditambahkan')
        os.system('cls')
    
    # Jika nama barang yang diinputkan user tidak terdapat dalam daftar maka nama barang tersebut akan dimasukkan kedalam file stock.json
    elif nama_barang not in temp_barang:
        jumlah_barang = int(input('Masukkan jumlah barang: '))
        harga_barang = int(input('Masukkan harga barang: '))
        harga_masuk = harga_barang * jumlah_barang

        # Menambahkan semua inputan ke file stock.json
        arg1.append({
            'nama barang':nama_barang,
            'jumlah barang':jumlah_barang,
            'harga barang':harga_barang
        })

        # Menambahkan semua inputan ke file dataMasuk.json  dan dengan keterangan berupa "Stock baru"
        arg2.append({
            'barang masuk':nama_barang,
            'jumlah masuk':jumlah_barang,
            'uang keluar':harga_masuk,
            'tanggal':waktu_sekarang,
            'keterangan':'Stock baru'
        })
        input('Barang telah ditambahkan')
        os.system('cls')
                

# Menghapus stock pada daftar stock, dan stock yang terhapus akan dianggap sebagai barang yang keluar dan akan dimasukkan ke file dataKeluar.json
def hapus_stock(arg1,arg2): # arg1 = stock.json, arg2 = dataKeluar.json
    os.system('cls')
    show_stock(arg1)
    temp_hapus = []
    hapus_stock = input('Masukkan Nama Barang yang ingin dihapus: ').upper()
    
    # Menambahkan semua nama barang di stock.json ke variabel temp_hapus
    for i in arg1:
        temp_hapus.append(i['nama barang'])

    # Jika nama barang yang di inputkan sesuai atau berada dalam variabel temp_hapus, perintah if dijalankan
    if hapus_stock in temp_hapus:
        for barang in arg1:
            if barang['nama barang'] == hapus_stock:
                arg1.remove(barang) # Data barang yang namanya sesuai dengan inputan user akan dihapus
                
                # dan dianggap sebagai barang yang keluar sehingga akan ditambhkan ke file dataKeluar.json
                arg2.append({
                    'barang keluar':barang['nama barang'],
                    'jumlah keluar':barang['jumlah barang'],
                    'uang masuk':barang['harga barang'] * barang['jumlah barang'],
                    'tanggal pesanan':waktu_sekarang,
                    'keterangan':'Stock dihapus'
                })

                print('Barang telah dihapus')
                input('Enter untuk kembali')
                os.system('cls')
    
    else:
        print('Barang tidak ditemukan')
        input('Enter untuk kembali')
        os.system('cls')


# Function untuk menampilkan stock barang
def show_stock(arg1): # arg1 = stock.json
    print('\nSTOCK BIBT DAN PUPUK TOKO AMAN SENTOSA')
    print('=' * 35)
    print('| %-13s | %-6s | %-6s |'%('NAMA BARANG','JUMLAH', 'HARGA'))
    print('=' * 35)
    for i in range(len(arg1)):
        print('| %-13s | %-6s | %-6s |'%(arg1[i]['nama barang'], arg1[i]['jumlah barang'], arg1[i]['harga barang']))
    print('=' * 35)


# Mengubah jumlah stock barang, jumlah barang yang ditambah akan terekam di file dataMasuk.json, dan jumlah barang yang dikurangi akan terekam di file dataKeluar.json
def ubah_stock(arg1,arg2,arg3): # arg1 = stock.json, arg2 = dataMasuk.json, arg3 = dataKeluar.json
    os.system('cls')
    show_stock(arg1)
    temp_ubah = [] # variabel sementara untuk menyimpan nama barang pada stock.json
    for i in arg1:
        temp_ubah.append(i['nama barang'])

    print("\n[1] Tambah Stock\n[2] Kurangi Stock\n")
    ubah = int(input('Masukkan Pilihan: '))

    # Jika admin ingin menambah jumlah stock
    if ubah == 1:
        os.system('cls')
        show_stock(arg1)
        barang = input('Masukkan nama barang: ').upper()

        # Jika nama barang yang diinputkan berada atau sesuai dengan yang ada di variabel temp_ubah
        if barang in temp_ubah:
            jumlah = int(input('Barang akan ditambah sebanyak: '))
            for k in arg1:
                if k['nama barang'] == barang:
                    k["jumlah barang"] += jumlah

                    # Jumlah barang yang ditambah dianggap sebagai barang masuk, dan ditambahkan ke file dataMasuk.json
                    arg2.append({
                        'barang masuk':barang,
                        'jumlah masuk':jumlah,
                        'uang keluar':k['harga barang'] * jumlah,
                        'tanggal':waktu_sekarang,
                        'keterangan':'Jumlah stock diubah'
                    })
                    print('Jumlah barang telah ditambahkan')
                    input('Enter untuk kembali')
                    os.system('cls')
        
        else:
            print('Barang tidak terdaftar')
            input('Enter untuk kembali')
            os.system('cls')

    # Jika admin ingin mengurangi jumlah stock
    elif ubah == 2:
        os.system('cls')
        show_stock(arg1)
        barang = input('Masukkan nama barang: ').upper()

        # Jika nama barang yang diinputkan berada atau sesuai dengan yang ada di variabel temp_ubah
        if barang in temp_ubah:
            jumlah = int(input('Barang akan dikurangi sebanyak: '))
            
            # Jumlah barang akan dicek terlebih dahulu apakah pengurangan yang diinputkan melebihi stock barang atau tidak
            temp_stock = i["jumlah barang"] - jumlah

            # Jika pengurangan melebihi jumlah stock barang atau menghasilkan angka kurang dari 0, maka perintah print dibawah dijalankan
            if temp_stock <= 0:
                print('Maaf, jumlah pengurangan melebihi stock barang')
                input('Enter untuk kembali')
                os.system('cls')
                return jumlah
            
            # Jika pengurangan lebih kecil dari jumlah stock barang, maka stock barang akan dikurangi berdasarkan jumlah yang diinginkan di variabel "jumlah"
            else:
                for l in arg1:
                    if l['nama barang'] == barang:
                        l["jumlah barang"] -= jumlah

                        # Barang yang dikurangi akan dianggap sebagai barang yang keluar, dan terekam di file dataKeluar.json
                        arg3.append({
                            'barang keluar':barang,
                            'jumlah keluar':jumlah,
                            'uang masuk':l['harga barang'] * jumlah,
                            'tanggal pesanan':waktu_sekarang,
                            'keterangan':'Jumlah stock diubah'
                        })
                print('Jumlah barang telah diubah')
                input('Enter untuk kembali')
                os.system('cls')
        
        else:
            print('Barang tidak terdaftar')
            input('Enter untuk kembali')
            os.system('cls')

    # Jika inputan yang dimasukkan admin saat berada di menu "[1] tambah stock dan [2] kurangi stock" tidak sesuai             
    else:
        print('Masukkan pilihan yang valid')
        os.system('cls')


# Menampilkan semua barang yang masuk (barang dari penambahan stock baru dan jumlah stock lama dari function tambahStock, dan penambahan jumlah stock dari function ubahStock)
def barangMasuk(arg1): # arg1 = dataMasuk.json
    os.system('cls')
    print('--- Data barang masuk Toko Aman Sentosa ---\n')
    print('=' * 61)
    print('| %-10s | %-13s | %-6s | %-19s |'%('TANGGAL', 'NAMA BARANG', 'JUMLAH', 'KETERANGAN'))
    print('|' + '-' * 12 + '|' + '-' * 15 + '|' + '-' * 8 + '|' + '-' * 21 + '|')
    for i in range(len(arg1)):
        print('| %-10s | %-13s | %-6s | %-19s |'%(arg1[i]['tanggal'], arg1[i]['barang masuk'], arg1[i]['jumlah masuk'], arg1[i]['keterangan']))
    print('=' * 61)
    input('\nEnter untuk kembali')
    os.system('cls')


# Menampilkan semua barang yang keluar (barang dari pengahpusan stock dari function hapusStock, pengurangan jumlah stock dari function ubahStock, dan saat barang tersebut dipesan oleh konsumen)
def barangKeluar(arg1): # arg1 = dataKeluar.json
    os.system('cls')
    print('--- Data barang keluar Toko Aman Sentosa ---\n')
    print('=' * 61)
    print('| %-10s | %-13s | %-6s | %-19s |'%('TANGGAL', 'NAMA BARANG', 'JUMLAH', 'KETERANGAN'))
    print('|' + '-' * 12 + '|' + '-' * 15 + '|' + '-' * 8 + '|' + '-' * 21 + '|')
    for i in range(len(arg1)):
        print('| %-10s | %-13s | %-6s | %-19s |'%(arg1[i]['tanggal pesanan'], arg1[i]['barang keluar'], arg1[i]['jumlah keluar'], arg1[i]['keterangan']))
    print('=' * 61)
    input('\nEnter untuk kembali')
    os.system('cls')


# Menampilkan total pemasukan (total pemasukan(uang yang masuk) dari penghapusan stock dari function hapusStock, pengurangan jumlah stock dari function ubahStock, dan barang yang dipesan konsumen)
def pemasukan(arg1): # arg1 = dataKeluar.json
    os.system('cls')
    print('--- Pemasaukan Toko Aman Sentosa ---')
    print('[1] Tahunan\n[2] Bulanan\n[3] Harian\n')
    choice = input('Masukkan pilihan: ')
    
    if choice == '1':
        os.system('cls')
        tahun = input('Masukkan tahun: ')
        temp = []
        temp_tahun = []
        for i in arg1:
            temp_tahun.append(i['tanggal pesanan'][:4])
            if i['tanggal pesanan'][:4] == tahun:
                temp.append(i)

        if tahun in temp_tahun:
            os.system('cls')
            total_pemasukan = 0
            print('\n--- Data Pemasukan Toko Aman Sentosa Tahun', tahun, '---\n')
            print('=' * 60)
            print('| %-13s | %-6s | %-9s | %-19s |'%('NAMA BARANG', 'JUMLAH', 'PEMASUKAN', 'KETERANGAN'))
            print('|' + '-' * 15 + '|' + '-' * 8 + '|' + '-' * 11 + '|' + '-' * 21 + '|')
            for k in range(len(temp)):
                print('| %-13s | %-6s | %-9s | %-19s |'%(temp[k]['barang keluar'], temp[k]['jumlah keluar'], temp[k]['uang masuk'], temp[k]['keterangan']))
                total_pemasukan += temp[k]['uang masuk']
            print('|' + '-' * 37  + '-' * 21 + '|')
            print('| %-22s | %-31s |'%('Total', total_pemasukan))
            print('=' * 60)
            input('\nTekan enter untuk kembali')
            os.system('cls')

        else:
            os.system('cls')
            input('Tahun tidak ditemukan, tekan enter untuk kembali')
            os.system('cls')

    elif choice == '2':
        os.system('cls')
        tahun = input('Masukkan tahun: ')
        bulan = input('Masukkan bulan dalam angka: ')
        temp = []
        temp_tahun = []
        temp_bulan = []
        for i in arg1:
            temp_tahun.append(i['tanggal pesanan'][:4])
            temp_bulan.append(i['tanggal pesanan'][5:7])
            if i['tanggal pesanan'][:4] == tahun and i['tanggal pesanan'][5:7] == bulan:
                temp.append(i)

        if tahun in temp_tahun and bulan in temp_bulan:
            total_pemasukan = 0
            os.system('cls')
            print('\n--- Data Pemasukan Toko Aman Sentosa Bulan', bulan + '/' + tahun, '---\n')
            print('=' * 60)
            print('| %-13s | %-6s | %-9s | %-19s |'%('NAMA BARANG', 'JUMLAH', 'PEMASUKAN', 'KETERANGAN'))
            print('|' + '-' * 15 + '|' + '-' * 8 + '|' + '-' * 11 + '|' + '-' * 21 + '|')
            for k in range(len(temp)):
                print('| %-13s | %-6s | %-9s | %-19s |'%(temp[k]['barang keluar'], temp[k]['jumlah keluar'], temp[k]['uang masuk'], temp[k]['keterangan']))
                total_pemasukan += temp[k]['uang masuk']
            print('|' + '-' * 37 + '-' * 21 + '|')
            print('| %-22s | %-31s |'%('Total', total_pemasukan))
            print('=' * 60)
            input('\nTekan enter untuk kembali')
            os.system('cls')

        else:
            os.system('cls')
            input('Tahun atau bulan tidak ditemukan, tekan enter untuk kembali')
            os.system('cls')

    elif choice == '3':
        os.system('cls')
        tahun = input('Masukkan tahun: ')
        bulan = input('Masukkan bulan dalam angka: ')
        tanggal = input('Masukkan tanggal: ')
        temp = []
        temp_tahun = [] 
        temp_bulan = []
        temp_tanggal = []
        for i in arg1:
            temp_tahun.append(i['tanggal pesanan'][:4])
            temp_bulan.append(i['tanggal pesanan'][5:7])
            temp_tanggal.append(i['tanggal pesanan'][8:10])
            if i['tanggal pesanan'][:4] == tahun and i['tanggal pesanan'][5:7] == bulan and i['tanggal pesanan'][8:10] == tanggal:
                temp.append(i)

        if tahun in temp_tahun and bulan in temp_bulan and tanggal in temp_tanggal:
            total_pemasukan = 0
            os.system('cls')
            print('\n--- Data Pemasukan Toko Aman Sentosa Tanggal', tanggal + '/' + bulan + '/' + tahun, '---\n')
            print('=' * 60)
            print('| %-13s | %-6s | %-9s | %-19s |'%('NAMA BARANG', 'JUMLAH', 'PEMASUKAN', 'KETERANGAN'))
            print('|' + '-' * 15 + '|' + '-' * 8 + '|' + '-' * 11 + '|' + '-' * 21 + '|')
            for k in range(len(temp)):
                print('| %-13s | %-6s | %-9s | %-19s |'%(temp[k]['barang keluar'], temp[k]['jumlah keluar'], temp[k]['uang masuk'], temp[k]['keterangan']))
                total_pemasukan += temp[k]['uang masuk']
            print('|' + '-' * 37 + '-' * 21 + '|')
            print('| %-22s | %-31s |'%('Total', total_pemasukan))
            print('=' * 60)
            input('\nTekan enter untuk kembali')
            os.system('cls')
 
        else:
            os.system('cls')
            input('Tahun, bulan, atau tanggal tidak ditemukan, tekan enter untuk kembali')
            os.system('cls')


# Menampilkan total pengeluaran (total pengeluaran(uang yang keluar) dari penambahan stock baru atau jumlah stock lama dari function tambahStock, dan penambahan jumlah stock dari function ubahStock)
def pengeluaran(arg1): # arg1 = dataMasuk.json
    os.system('cls')
    print('--- Pengeluaran Toko Aman Sentosa ---')
    print('[1] Tahunan\n[2] Bulanan\n[3] Harian\n')
    choice = input('Masukkan pilihan: ')

    if choice == '1':
        os.system('cls')
        tahun = input('Masukkan tahun: ')
        temp = []
        temp_tahun = []
        for i in arg1:
            temp_tahun.append(i['tanggal'][:4])
            if i['tanggal'][:4] == tahun:
                temp.append(i)

        if tahun in temp_tahun:
            total_pengeluaran = 0
            os.system('cls')
            print('\n--- Data Pengeluaran Toko Aman Sentosa Tahun', tahun, '---\n')
            print('=' * 62)
            print('| %-13s | %-6s | %-11s | %-19s |'%('NAMA BARANG', 'JUMLAH', 'PENGELUARAN', 'KETERANGAN'))
            print('|' + '-' * 15 + '|' + '-' * 8 + '|' + '-' * 13 + '|' + '-' * 21 + '|')
            for k in range(len(temp)):
                print('| %-13s | %-6s | %-11s | %-19s |'%(temp[k]['barang masuk'], temp[k]['jumlah masuk'], temp[k]['uang keluar'], temp[k]['keterangan']))
                total_pengeluaran += temp[k]['uang keluar']
            print('|' + '-' * 39 + '-' * 21 + '|')
            print('| %-22s | %-33s |'%('Total', total_pengeluaran))
            print('=' * 62)
            input('\nTekan enter untuk kembali')
            os.system('cls')

        else:
            os.system('cls')
            input('Tahun tidak ditemukan, tekan enter untuk kembali')
            os.system('cls')

    elif choice == '2':
        os.system('cls')
        tahun = input('Masukkan tahun: ')
        bulan = input('Masukkan bulan dalam angka: ')
        temp = []
        temp_tahun = []
        temp_bulan = []
        for i in arg1:
            temp_tahun.append(i['tanggal'][:4])
            temp_bulan.append(i['tanggal'][5:7])
            if i['tanggal'][:4] == tahun and i['tanggal'][5:7] == bulan:
                temp.append(i)

        if tahun in temp_tahun and bulan in temp_bulan:
            total_pengeluaran = 0
            os.system('cls')
            print('\n--- Data Pengeluaran Toko Aman Sentosa Bulan', bulan + '/' + tahun, '---\n')
            print('=' * 62)
            print('| %-13s | %-6s | %-11s | %-19s |'%('NAMA BARANG', 'JUMLAH', 'PENGELUARAN', 'KETERANGAN'))
            print('|' + '-' * 15 + '|' + '-' * 8 + '|' + '-' * 13 + '|' + '-' * 21 + '|')
            for k in range(len(temp)):
                print('| %-13s | %-6s | %-11s | %-19s |'%(temp[k]['barang masuk'], temp[k]['jumlah masuk'], temp[k]['uang keluar'], temp[k]['keterangan']))
                total_pengeluaran += temp[k]['uang keluar']
            print('|' + '-' * 39 + '-' * 21 + '|')
            print('| %-22s | %-33s |'%('Total', total_pengeluaran))
            print('=' * 62)
            input('\nTekan enter untuk kembali')
            os.system('cls')

        else:
            os.system('cls')
            input('Tahun atau bulan tidak ditemukan, tekan enter untuk kembali')
            os.system('cls')

    elif choice == '3':
        os.system('cls')
        tahun = input('Masukkan tahun: ')
        bulan = input('Masukkan bulan dalam angka: ')
        tanggal = input('Masukkan tanggal: ')
        temp = []
        temp_tahun = []
        temp_bulan = []
        temp_tanggal = []

        for i in arg1:
            temp_tahun.append(i['tanggal'][:4])
            temp_bulan.append(i['tanggal'][5:7])
            temp_tanggal.append(i['tanggal'][8:10])
            if i['tanggal'][:4] == tahun and i['tanggal'][5:7] == bulan and i['tanggal'][8:10] == tanggal:
                temp.append(i)

        if tahun in temp_tahun and bulan in temp_bulan and tanggal in temp_tanggal:
            total_pengeluaran = 0
            os.system('cls')
            print('\n--- Data Pengeluaran Toko Aman Sentosa Tanggal', tanggal + '/' + bulan + '/' + tahun, '---\n')
            print('=' * 62)
            print('| %-13s | %-6s | %-11s | %-19s |'%('NAMA BARANG', 'JUMLAH', 'PENGELUARAN', 'KETERANGAN'))
            print('|' + '-' * 15 + '|' + '-' * 8 + '|' + '-' * 13 + '|' + '-' * 21 + '|')
            for k in range(len(temp)):
                print('| %-13s | %-6s | %-11s | %-19s |'%(temp[k]['barang masuk'], temp[k]['jumlah masuk'], temp[k]['uang keluar'], temp[k]['keterangan']))
                total_pengeluaran += temp[k]['uang keluar']
            print('|' + '-' * 39 + '-' * 21 + '|')
            print('| %-22s | %-33s |'%('Total', total_pengeluaran))
            print('=' * 62)
            input('\nTekan enter untuk kembali')
            os.system('cls')

        else:
            os.system('cls')
            input('Tahun, bulan, atau tanggal tidak ditemukan, tekan enter untuk kembali')
            os.system('cls')


# Menampilkan pilihan menu untuk melihat laporan barang masuk/keluar, pemasukan, dan pengeluaran
def laporanBarang():
    os.system('cls')
    print('--- LAPORAN BARANG TOKO AMAN SENTOSA ---')
    print('\n[1] Barang masuk\n[2] Barang keluar\n[3] Pemasukan\n[4] Pengeluaran\n')
    choice = input('Silahkan pilih menu diatas: ')
    if choice == '1':
        barangMasuk(data_masuk)
    elif choice == '2':
        barangKeluar(data_keluar)
    elif choice == '3':
        pemasukan(data_keluar)
    elif choice == '4':
        pengeluaran(data_masuk)


""" ============ Konsumen ============ """

# Menampilkan menu atau fitur yang dimiliki konsumen
def menuKonsumen(arg1): # arg1 = temp_pesan
    print('--- Selamat Datang di Toko Aman Sentosa ---')
    if len(arg1) > 0:
        showPesanan(arg1)
    print("\n[1] Input Pesanan\n[2] Hapus Pesanan\n[3] Pesan\n[4] Keluar\n")


# Menampilkan daftar pesanan konsumen
def showPesanan(arg1): # arg1 = temp_pesan
    total_pesanan = 0
    print('\n-----------PESANAN ANDA------------\n')
    print('=' * 35)
    print('| %-13s | %-6s | %-6s |'%('PESANAN','JUMLAH', 'HARGA'))
    print('=' * 35)
    for i in range(len(arg1)):
        print('| %-13s | %-6s | %-6s |'%(arg1[i]['nama pesanan'], arg1[i]['jumlah pesanan'], arg1[i]['harga pesanan']))
        total_pesanan += arg1[i]['harga pesanan']
    print('-' * 35)
    print('| %-22s | %-6s |'%('TOTAL', total_pesanan))
    print('=' * 35)


# Memesan barang
def inputPesanan(arg1): # arg1 = stock.json
    global jumlah_pesan
    os.system('cls')
    show_stock(arg1)
    temp_order = []
    pesanan = input('Masukkan nama barang: ').upper()
    for i in arg1:
        temp_order.append(i['nama barang'])

    if pesanan in temp_order:
        jumlah_pesan = int(input('Jumlah pesanan: '))
        for j in arg1:
            if j['nama barang'] == pesanan:
                temp_jumlah = j["jumlah barang"] - jumlah_pesan

        if temp_jumlah <= 0:
            print('\nMaaf, jumlah pesanan melebihi stock barang')
            input('Tekan enter untuk kembali')
            return jumlah_pesan

        else:
            for k in arg1:
                if pesanan == k['nama barang']:
                    k["jumlah barang"] -= jumlah_pesan
                    harga_pesan = k['harga barang'] * jumlah_pesan
            print('\nPesanan disimpan')
            input('Tekan enter untuk kembali')
            temp_pesan.append({
                'nama pesanan':pesanan,
                'jumlah pesanan':jumlah_pesan,
                'harga pesanan':harga_pesan,
                'tanggal pesanan':waktu_sekarang
            })

    else:
        print('Barang tidak ditemukan')
        input('Enter untuk kembali')
                    

# Menghapus pesanan
def hapusPesanan(arg1,arg2): # arg1 = temp_pesan, arg2 = stock.json
    os.system('cls')
    temp = []
    showPesanan(temp_pesan)
    hapus_pesanan = input('Masukkan pesanan yang ingin dihapus: ').upper()
    for barang in arg1:
        temp.append(barang['nama pesanan'])

    if hapus_pesanan in temp:
        arg1.remove(barang)

        for i in arg2:
            if i['nama barang'] == hapus_pesanan:
                i['jumlah barang'] += jumlah_pesan
        input('Pesanan telah terhapus')
        os.system('cls')

    else:
        input('Barang tidak ditemukan, tekan enter untuk kembali')
        os.system('cls')


# Menyimpas pesanan konsumen
def pesandansimpan():
    for i in temp_pesan:
        data_keluar.append({
            'barang keluar':i['nama pesanan'],
            'jumlah keluar':i['jumlah pesanan'],
            'uang masuk':i['harga pesanan'],
            'tanggal pesanan':i['tanggal pesanan'],
            'keterangan':'Barang dipesan'
        })
    save_stock(STOCK_DATABASE,stock)
    save_dataKeluar(DATA_KELUAR_DATABASE,data_keluar)


menuUtama()