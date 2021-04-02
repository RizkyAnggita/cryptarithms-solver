# Nama      : Rizky Anggita S Siregar
# NIM       : 13519132
# Tanggal   : 25 Januari 2021
# Deskripsi : Cryptarithm Solver with Brute Force Algorithm
# TUCIL 1 STRATEGI ALGORITMA 

from timeit import default_timer as timer
import os

def wordToNum(word, unique_huruf, num_huruf):
    #Change from word to number which will counted
    sum = 0
    pangkat = len(word)-1
    for i in range(len(word)):
        for j in range(len(unique_huruf)):
            if word[i]==unique_huruf[j] :
                sum = sum + (10**pangkat) * num_huruf[j]
                pangkat = pangkat - 1
    return sum

def numUnique(num_huruf):
    # Check if there is duplicate digit in a number
    for i in range (len(num_huruf)-1):
        # print(num_huruf[i+1:])
        if (num_huruf[i]) in num_huruf[i+1:]:
            return False
    return True

def wordUnique(word):
    # Check if there is duplicate letter in a word
    for i in range(len(word)-1):
        if(word[i] in word[i+1:]):
            return False
    return True

def arrnum_hurufToNum(num_huruf):
    # Change array of number to number
    sum = 0
    pangkat = len(num_huruf)-1
    for i in range(len(num_huruf)):
        sum = sum + (10**pangkat) * num_huruf[i]
        pangkat = pangkat - 1
    return sum

def numToarrnum(curr_num):
    # Mengubah number to array of number
    temp = str(curr_num)
    arr_temp = [int(a) for a in temp ]
    return(arr_temp)


#/-------------------------------/#
# MAIN PROGRAM

print("\n\nCryptarithms Solver with Brute Force Algorithm\n\n")

# PROSES TXT
print("Filename input example: input1.txt")
nama_file = input("Input filename: ")
start = timer()
a = os.path.abspath(os.curdir)

if os.name=='nt':
    file_path = os.path.join("..\\test", nama_file)
else:
    file_path = os.path.join(a, "test", nama_file)

input_file = open(file_path, "r")

isi_file = input_file.readlines()

jumlah_operand = len(isi_file)-2       #Jumlah kata yang akan dioperasikan

array_operand = [i.rstrip("\n") for i in isi_file] #Mengambil operand sekaligus menghapus newline character
array_operand = array_operand[:-2]  # Buang 2 line terakhir, yaitu garis dan hasil operasi
array_operand[-1] = array_operand[-1].rstrip("+")   #Menghapus char +

kata_hasil = isi_file[-1]

# Membentuk array huruf yang unik
unique_huruf = []
for i in range(jumlah_operand):
    for j in range (len(array_operand[i])):
        if not(array_operand[i][j]) in unique_huruf:
            unique_huruf.append(array_operand[i][j])

# Membentuk kemungkinan permutasi pertama kali
num_huruf = [i for i in range(len(unique_huruf))]

#Karena huruf pertama tidak boleh 0, maka di swap dengan elemen ke-2
num_huruf[0], num_huruf[1] = num_huruf[1], num_huruf[0]

found = False
end = False
iterate = 0
awal = arrnum_hurufToNum(num_huruf)

while (not(found) and not(end)):
    arr_angka_operand = []
    summ = 0
    for i in range(jumlah_operand):
        temp = wordToNum(array_operand[i], unique_huruf, num_huruf)
        arr_angka_operand.append(temp)
        summ = summ + temp

    summ = str(summ)
    # print(num_huruf)
    finished = True

    if (len(summ) < len(kata_hasil)) :
        finished = False
        # print("Tes") #continue, karna yang dihasilkan masih kurang
    
    elif len(summ)==len(kata_hasil):
        #Terbagi dua kasus, jika terdapat huruf duplikat pada kata_hasil atau tidak

        if (wordUnique(kata_hasil)):
            #TIDAK terdapat huruf duplikat pada kata_hasil

            if (not(numUnique(summ)) or not(numUnique(num_huruf))):
                finished = False
        
        else:
            #Terdapat huruf duplikat pada kata_hasil
            if (numUnique(summ)):
                finished = False
            else:
                #Mengecek dua huruf yang sama tetapi berbeda angka yang berkorespondennya
                for i in range (len(kata_hasil)):
                    for j in range(len(kata_hasil)):
                        if kata_hasil[i]==kata_hasil[j]: 
                            if(int(summ[i]) != int(summ[j]) ):
                                finished = False
                                break
                    if(not(finished)):
                        break

                if (not(numUnique(num_huruf))):
                    finished = False
        

        for i in range (len(kata_hasil)):
            for j in range(len(num_huruf)):
                if int(summ[i])==num_huruf[j]:     #jika angka sama
                    if(kata_hasil[i]!=unique_huruf[j]): # jika hurufnya berbeda, maka belum benar
                        finished = False
                        break
                if kata_hasil[i]==unique_huruf[j]:  # jika hurufnya sama
                    if(int(summ[i]) != num_huruf[j] ): #jika angkanya berbeda, maka belum benar
                        finished = False
                        break
            if (not(finished)):
                break

        #  Mengecek awalan kata tidak boleh 0
        for i in range(len(arr_angka_operand)):
            temp = str(arr_angka_operand[i])
            if(temp[0]==0):
                finished = False
                break

        if(str(summ)[0]==0):
            finished = False    

    if finished and (len(summ) == len(kata_hasil)):
        found = True
        end = True
    else:
        #Increment
        iterate += 1
        curr_num = arrnum_hurufToNum(num_huruf) + 1
        num_huruf = numToarrnum(curr_num)

        maks = 10**(len(unique_huruf)) - 1
        if (curr_num==maks):
            end  = True
            found = False


if(end):

    print("\n\nDONE\n")
    print("Array of Unique Character: ", unique_huruf)
    print("Array of Number: ", num_huruf)
    print("\n")

    print("Input\n")
    for i in range(len(isi_file)):
        print(isi_file[i], end="")

    print("\n\nSolusi\n")

    if found:
        for i in range(len(arr_angka_operand)):
            print(arr_angka_operand[i])
        print("----- +")
        print(summ)
        print()
    else:
        print("Solusi tidak ada!\n")
    
    end = timer()
    print("Time elapsed : ", end-start, end=" seconds\n")
    
    #Perhitungan awal dimulai dari 1023.....x, dengan x adalah n-1 (n=jumlah huruf unik pada input kata)
    print("Jumlah total tes: ", iterate+awal, "-", awal, "= ", iterate)
    print()   