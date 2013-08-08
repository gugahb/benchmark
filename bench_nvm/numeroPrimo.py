# Instalar este plugim:
#    $ pip install line_profiler
#    $ pip install -U memory_profiler
#    $ pip install psutil
#
# Esta rotina nao utiliza de biblioteca.
#
# Uso:
# 		$ time kernprof.py -l -v numeroPrimo.py

def get_primo(n):
	"""

	"""
	if n < 2:  return []
	if n == 2: return [2]
	# 
	s = range(3, n+1, 2)

	# n**0.5 simples math.sqr(n)
	mroot = n ** 0.5
	half = len(s)
	i = 0
	m = 3

	while m <= mroot:
		if s[i]:
			j = (m*m-3)//2  # divide
			s[j] = 0
			while j < half:
				s[j] = 0
				j += m
		i = i+1
		m = 2*i+3
	return [2]+[x for x in s if x]

for t in range(10):
	res = get_primo(10000000)
	print "Encontro", len(res), "numbero primo."

print 