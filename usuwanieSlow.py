#!/usr/bin/python3

#ze wzgledu na brak plikow w jezyku polskim w przykladowym repo z polecenia, uzyje slow anglojezycznych

remove_dict = {
    "the ": "", 
    "The ": "",
    "capital ": "",
    "is ": "", 
    "currency ": "", 
    "and ": "", 
    "east ": "",
    "to ": "" 
    }
file1_r = open(r'/Users/michalczarnik/Git_Project/Python_2022/Zloty.txt', 'r')
file1_w = open(r'/Users/michalczarnik/Git_Project/Python_2022/Zloty_removed.txt', 'w')
file2_r = open(r'/Users/michalczarnik/Git_Project/Python_2022/Warszawa.txt', 'r')
file2_w = open(r'/Users/michalczarnik/Git_Project/Python_2022/Warszawa_removed.txt', 'w')
text1 = file1_r.read()
text2 = file2_r.read()
for i in remove_dict:
    if i in text1:
        text1 = text1.replace(i, remove_dict[i])
    if i in text2:
        text2 = text2.replace(i, remove_dict[i])
file1_w.write(text1)
file2_w.write(text2)
file1_r.close()
file2_r.close()
file1_w.close()
file2_w.close()
