Para conectar à plataforma do Galaxy, são necessárias 3 etapas:

1) A primeira etapa é **inicializar a instância da Google Cloud** onde a plataforma está hospedada. Em outras palavras, nesta etapa estamos   
ligando a máquina onde a nossa plataforma irá rodar. Para executar esta etapa, é necessário (em ordem):
	i) logar na GCloud com o usuário ti.admin@biobureau.com.br
 		- gcloud auth login ti.admin@biobureau.com.br
	ii) migrar para o projeto de ID "galaxy-203511", onde a nossa instância de interesse fora inicializada 
 		- gcloud config set project galaxy-203511
	iii) conectar à instância de interesse (no nosso caso, é a instância "galaxy-server", hospedada na zona "us-central1-c"
 		- gcloud compute ssh ti.admin@galaxy-server --zone "us-central1-c"
		
2) Uma vez conectado à instância da GCloud, é preciso **executar o servidor do Galaxy**. Para isso devemos: 
	i) migrar para a pasta /galaxy, que se localiza dentro da pasta do usuário rafaelcuadrat
		- cd /home/rafaelcuadrat/galaxy/
	ii) disparar o script que faz rodar a plataforma Galaxy
		- screen 
		- sudo ./run.sh
		PS: o comando screen fará o Galaxy rodar em background na instância. Nese caso, é possível fechar a janela da instância e a
		plataforma continuará funcionando. 
	iii) esperar até que uma mensagem de confirmação de que o servidor está rodando apareça na tela:
		- essa mensagem deveria ser algo do tipo: "serving on ___ view at http://___"
		
3) Após a etapa anterior, a plataforma Galaxy estará pronta para ser acessada. Agora resta só:
	i) descobrir o IP externo da instância da GCloud 
		- gcloud compute instances list
	ii) acessar a instância a partir de um Browser:
		- http://IP_externo
	iii) logar no Galaxy
		- login: ti.admin@biobureau.com.br
		- senha: d@t@biomics4biobureau
