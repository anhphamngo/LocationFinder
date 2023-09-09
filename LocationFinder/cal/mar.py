jan = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
suSt = 5 # Started Sunday
saSt = 4 # Started Saterday
suRe = 4 # Repeated Sunday
saRe = 4 # Started Saterday

# Sunday solution
marSunDate = [suSt]
for i in range(suRe-1):
    marSunDate.append(marSunDate[i]+7)

# Saterday solution
marSatDate = [saSt]
for x in range(saRe-1):
    marSatDate.append(marSatDate[x]+7)

free_mar = marSatDate + marSunDate
free_mar.sort()
#print(free_mar)

# print(satDate)
# print(sunDate)