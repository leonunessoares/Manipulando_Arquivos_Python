import os

dir_path = 'e:/'
contador=0

#gerar arquivo .txt
arquivo = open("Arquivos_Gerados_Rede_Via_Python.txt", "w")
arquivo.write("********** ARQIVOS GERADOS - MAIORES QUE 200 MB ****************")
arquivo.write("\n")
arquivo.write("\n")
for (dirpath, dirnames, filenames) in os.walk(dir_path): 
    for f in filenames: 
        f_path = os.path.join(dirpath, f)
        f_size = os.path.getsize(f_path)
        f_size_kb = (f_size/1024)/1024 # obter resultado em KB/MB
        #print(f_path, round(f_size_kb,2))
        path_completo = f_path, round(f_size_kb,2)
        if round(f_size_kb,2) >= 200:
            arquivo.write(str(path_completo))
            arquivo.write("\n")
            contador = contador +1
#print(contador)
arquivo.write("\n")
arquivo.write('Total de arquivos encontrados: ' + str(contador))
arquivo.close()