
E = 36000
I = 76000
S = I - E
IR = 0.09
DR = 0.025
C = list(range(1))
C[0] = S + 100000
BE = list(range(1))

e = input('Manual Entry [Y/N]: ') 

if e == 'y' :
	E = int(input('Expense: '))
	I = int(input('Input: '))
	C[0] = I - E + int(input('Initial Capital: '))

x = 0
while BE[x] <= 0 :
	x += 1
	C.append(round(C[x - 1] * (1 + IR) + S))
	BE.append(round(C[x -1] * DR - E))
	BEC = round(C[x]/1000, 2)
	print('Year: ' + str(x) + ' Balance: ' + str(BE[x]/1000) + 'K GBP ' + 'Capital: ' + str(BEC) + 'K GBP.')

BEC = round(C[x]/1000000, 2)

print('\nBreakeven is at year ' + str(x) + ' with a capital of ' + str(BEC) + 'MM GBP.\n')
