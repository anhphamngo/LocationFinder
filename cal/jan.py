jan = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
suSt = 1 # Started Sunday
saSt = 7 # Started Saterday
suRe = 5 # Repeated Sunday
saRe = 4 # Started Saterday

# Sunday solution
janSunDate = [suSt]
for i in range(suRe-1):
    janSunDate.append(janSunDate[i]+7)

# Saterday solution
janSatDate = [saSt]
for x in range(saRe-1):
    janSatDate.append(janSatDate[x]+7)

# print(satDate)
# print(sunDate)