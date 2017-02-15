n = 1

def factor(num):
	pf = []
	f= {}
	while num % 2 == 0:
		pf.append(2)
		num/=2
		num = int(num)
	for i in range(3,int(num**(1/2))+1,2):
		while num % i == 0:
			pf.append(i)
			num/=i
			num = int(num)
	if num>2:
		pf.append(num)
	# print(pf)
	f = {i:pf.count(i) for i in pf }
	# print(f)
	prod = 1
	# print(f.values())
	for i in f.values():
		prod = prod * (i+1)
	return prod
	
while True:
	div_count = 0
	sm = sum(range(n+1))
	# print(sm)
	div_count=factor(sm)
	# for i in range(1,sm+1):
	# 	if sm % i == 0:
	# 		div_count+=1
			# print(i,end= ' ')
	n+=1
	# print(n,'th iteraton:',div_count,'no.of divisiors for',sm)
	if div_count >= 500:
		print(sm)
		break
