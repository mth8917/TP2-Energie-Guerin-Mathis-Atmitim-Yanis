import csv
import matplotlib.pyplot as plt
val = 0
Temps=[]
Allemagne=[]
Angleterre=[]
Espagne=[]
Italie=[]
Suisse=[]
with open('RTE_2022.csv',newline ="" ) as csvfile:
    reader= csv.reader(csvfile,delimiter=',')
    for row in reader:
        val= val + 1
        if val == 672 :
            Allemagne.append(row[17])
            Angleterre.append(row[18])
            Espagne.append(row[19])
            Italie.append(row[20])
            Suisse.append(row[21])
            Temps.append(row[2])
            val= 0
plt.plot(Temps, Allemagne, label ='Allemagne')
plt.plot(Temps, Angleterre, label ='Angleterre')
plt.plot(Temps, Espagne, label ='Espagne')
plt.plot(Temps, Italie, label ='Italie')
plt.plot(Temps, Suisse, label ='Suisse')
plt.legend()
plt.title('Graphiques des exportations et des importations de la France chaque semaine en terme energetique avec les autres pays sur la période de 2022')
plt.xlabel('Temps')
plt.ylabel('Energie')
plt.xticks([1,25,50])
plt.grid(True)
plt.show()


