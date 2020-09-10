refArquivo = open('D:\Downloads\TriTrypDB-47_TcruziCLBrenerEsmeraldo-like_AnnotatedProteins.fasta')
arquivoFasta = refArquivo.read()
cabecalho = arquivoFasta.split('\n')[0][1:]
sequencia = ' '.join(arquivoFasta.split('\n')[1:])
print("Identificador:%s"%cabecalho)
print('Sequencia: %s'%sequencia)
refArquivo.close()


