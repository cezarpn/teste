refArquivoEntrada = open("/home/vitor/Downloads/species.csv")
refArquivoEntrada.readline()
for linha in refArquivoEntrada:
    data = linha.split(",")
    if data[3].upper().rstrip() == "BIRD":
        print ("%s\t%s\t%s\t%s" %(data[0], data[1], data[2], data[3].rstrip()))
refArquivoEntrada.close()
