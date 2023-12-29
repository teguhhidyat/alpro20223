# file I/O ada dua mode
# mode pertama -> baca (READ) r
# mode kedua -> tulis (WHITE) w

if __name__ == "_main_":
    nama_file = 'contoh.txt'
    text = 'hai dinda'

    # contoh write
    with open (nama_file, "w") as f:
        f.write(text)

    # contoh read
    with open(nama_file, "r") as f:
        print(f.read())