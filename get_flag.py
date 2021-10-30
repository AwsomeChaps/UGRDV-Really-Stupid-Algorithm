
from Crypto.Util.number import inverse

def ugrdv_challenge_2():
	with open('values.txt', 'r') as f:
		lines = f.readlines()
		lines = [line.rstrip() for line in lines]
	f.close()
	c = int(lines[0][4:])
	p = int(lines[1][4:])
	q = int(lines[2][4:])
	e = int(lines[3][4:])

	n=p*q
	phi = (p-1)*(q*1)
	d = inverse(e, phi)
	p = pow(c,d,n)



	bytes_object = bytes.fromhex(hex(p)[2:])
	print(bytes_object)
	ascii_string = bytes_object.decode("latin-1")
	print(ascii_string)


if __name__ == '__main__':
	ugrdv_challenge_2()