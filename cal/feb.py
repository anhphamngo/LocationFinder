jan = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
suSt = 5 # Started Sunday
saSt = 4 # Started Saterday
suRe = 4 # Repeated Sunday
saRe = 4 # Started Saterday

# Sunday solution
febSunDate = [suSt]
for i in range(suRe-1):
    febSunDate.append(febSunDate[i]+7)

# Saterday solution
febSatDate = [saSt]
for x in range(saRe-1):
    febSatDate.append(febSatDate[x]+7)

# print(satDate)
# print(sunDate)