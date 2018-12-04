## Problema 
Como fazer quando quisermos usar um programa não disponível na Galaxy Tool Shed?  
Ou então para rodar um script desenvolvido internamente?

## Solução
A solução para esse problema é adicionar o script de interesse ao Galaxy como uma ferramenta customizada.  
Para fazer isto, basta seguir o [passo-a-passo](https://old.launch.usegalaxy.org/admin/tools/add-tool-tutorial/) do site oficial do Galaxy.  

## Teste  
Em nossa instalação Galaxy, sob a seção MyTools, foi adicionado com fins de teste o script **repeatText.py**. Esse script recebe como input um texto e um número de repetições *n*, e imprime em um arquivo de output o respectivo texto repetido *n* vezes.
