# fiapCap1fase3

### Objetivo
O objetivo dessa atividade é a construção de um sistema de irrigação de uma lavoura, para isso utilizaremos um esp32 que atuará como a interface principal de controle, recebendo os dados dos sensores e enviando comandos ao sistema de irrigação, os componentes que utilizamos são: um sensor dht22 que captura a umidade e a temperatura do ambiente, dois botões que simula o fosforo e o potássio do solo, e um sensor LDR que irá simular o valor do ph  um rele que irá ligar um LED vermelho sinalizando que o processo de irrigação começou, o processo de irrigação começa quando a temperatura estiver maior que 35°C ou a umidade estiver menor que 75%.
E por fim tem um banco de dados Oracle com um sistema CRUD simples que guardaria os valores que os componentes do esp32 mediria.


### Banco de dados
Volume esperado:5 linhas, e volume diario de 72 linha (uma medição a cada 30 minutos) 
Tempo de retenção: Permantente  
Rotina de limpeza: Não se aplica
|Atributo   |Tipo do Atributo   |Cardinalidade Minima|Cardinalidade Maxima | 
|-----------|-------------------|--------------------|---------------------|
|ID(number ) 				| simples, determinante | 1 | 1 |
|VALOR_PH(FLOAT) 			| simples				| 1 | 1 |
|VALOR_POTASSIO(number 10) 				| simples  			 	| 1 | 1 |
|VALOR_FOSFORO(number 10) 			| simples  			 	| 1 | 1 |
|BOMBA_LIGADA(NUMBER10) |simples|1|1|

### Como usar
Ir no site [wokwi](https://wokwi.com/) e selecionar a placa esp32, o código fonte está no arquivo sketch.ino e a biblioteca utilizada está no arquivo libraries.txt que estão na pasta src, o diagrama do projeto está na pasta docs, lá está um arquivo json que pode ser utilizado no site [wokwi](https://wokwi.com/) e um aquivo .png com a foto do diagrama.
Possuir um banco de dados igual ao descrito acima e rodar o arquivo main.py
