### Problema
O galaxy não permite subir arquivos maires que 2GB via a ferramenta usual "Upload File". De acordo com a [página oficial](https://galaxyproject.org/ftp-upload/#file-upload-via-ftp), subir arquivos grandes usando esta ferramenta pode ser demorado demais e não confiável.

### Solução
Para contornar este problema, há duas alternativas:  
i. Configurar a instalação do Galaxy para subir arquivos via protocolo FTP  
ii. Importar os arquivos desejados para Libraries, e de lá lançar os arquivos para o History.  

Primeiramente tentamos configurar a nossa instalação para permitir subir arquivos via FTP. Porém, esta via se mostrou complicada e resolvemos partir para a segunda. Seguem as etapas executadas:  

i. A instalação do Galaxy foi configurada conforme indicado [aqui](https://galaxyproject.org/data-libraries/#import-configuration).   
ii. O arquivo teste ("1a_S1_R1_001.fastq.gz", 2.7 GB) foi subido para a respectiva pasta na máquina virtual (no nosso caso, a pasta "/home/rafaelcuadrat/galaxy/data/ti.admin@biobureau.com.br"). Por fim, seguindo as etapas descritas [neste tutorial](https://galaxyproject.org/data-libraries/#from-user-folder), os arquivos foram importados para a Library "test-large-files", e por fim para o History "Testing_Galaxy".  
