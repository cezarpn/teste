refArquivo = open('D:\Downloads\TriTrypDB-47_TcruziCLBrenerEsmeraldo-like_AnnotatedProteins.fasta')
cabecalho = refArquivo.readline()[1:-1]
sequencia = ''
for linha in refArquivo:
    sequencia += linha.replace('\n', '')
print ('Cabecalho: %s'%cabecalho)
print ('Sequencia: %s'%sequencia)
refArquivo.close()