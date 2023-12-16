nilai = int (input('masukan angka nilai siswa:'))
grade = 'E'

if nilai >= 85 :
    grade = 'A'
elif nilai >= 80 :  
    grade = 'A-'
elif nilai >= 75 :
    grade = 'B'
elif nilai >= 70 :
    grade = 'B-'
elif nilai >= 65 :
    grade = 'C'
elif nilai >= 60 :
    grade = 'C-'
elif nilai >= 55 :
    grade = 'D'
elif nilai >= 50 :
    grade = 'D-'
elif nilai >= 45 :
    grade = 'D'
elif nilai >= 0  :
    grade = 'E'
print('grade anda adalah {}'.format(grade))