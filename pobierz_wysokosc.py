import requests
URL = "https://services.gugik.gov.pl/nmt/"
wysokosci = []
#wspolrzedne XY podajemy w ukladzie 92
#wysokosc jest zwracana w ukladzie PL-KRON86-NH
with open('punkty.txt', 'r') as plik:
	for line in plik:
		x,y = line.split('\t')
		Params={'request': "GetHbyXY", 'x': x, 'y': y}
		response = requests.get(url=URL,params=Params)
		odpowiedz_txt = response.text
		wysokosci.append(x+'\t'+y.rstrip()+'\t'+odpowiedz_txt+'\n')

with open('punkty_wysokosciowe.txt', 'w') as filehandle:
	filehandle.writelines(wysokosci)
