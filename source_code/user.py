from conextion_mysql import cursor


try:
    cursor.execute("select * from repartition")
except:
    print('Some worng')


vet = []
for linha in cursor:
   for l in linha:
       vet.append(l)



print(vet)