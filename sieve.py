def numdict(n):
	ret = dict()
	for i in range(n): ret[i+1]=True
	return ret

def sieve(n):
	is_prime = numdict(n)
	is_prime[1]=False
	for i in range(2,n+1):
		if is_prime[i]:
			for k in is_prime:
				if is_prime[k] and k!=i and (k%i)==0: is_prime[k]=False
	return [k for k, v in is_prime.items() if v]
