refArquivoEntrada = open('D:\Downloads\TriTrypDB-47_TcruziCLBrenerEsmeraldo-like_AnnotatedProteins.fasta')
refArquivoSaida = open("D:\Downloads\TriTrypDB-47_TcruziCLBrenerEsmeraldo-like_AnnotatedProteins", 'w')
refArquivoSaida.write('header\tseq\n')
cabecalho = refArquivoEntrada.readline()[1:-1]
sequencia = ""
for linha in refArquivoEntrada:
    sequencia+=linha.replace('\n','')
refArquivoSaida.write ('%s\t%s'% (cabecalho,sequencia))
refArquivoEntrada.close()
refArquivoSaida.close()