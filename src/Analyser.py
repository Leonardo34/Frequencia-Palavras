def leArquivo(arq):
	linhas = arq.readlines()
	contaPalavrasTexto(linhas)

def contaPalavrasTexto(linhas):
	palavrasTexto = {}
	for linha in linhas:
		palavras = linha.split(' ') 
		for palavra in palavras:
			palavrasTexto[palavra] = palavrasTexto.get(palavra, 0) + 1

	print (palavrasTexto)
	
	
