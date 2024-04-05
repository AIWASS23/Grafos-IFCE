#include <stdio.h>
#include <string.h>

#define maximo 301

int grafo[maximo][maximo];
int vertice[maximo];
int familia = 0;

char mapa[maximo][50];

void dfs(int atual, int total){
	if(vertice[atual]) {
        return; 
    }
    vertice[atual] = 1;

	for(int i = 0; i < total; i++) {
        if(grafo[atual][i])
            dfs(i, total);
    }
	return;
}

int obterIndice(char nome[50]) {
    for(int j = 0; j < familia; j++) {
        if(strcmp(mapa[j], nome) == 0) {
            return j;
        }
    }
    strcpy(mapa[familia], nome);
    return familia++;
}

int main(){
    
    int relacoes;
    int pessoas; 

    scanf("%d %d", &relacoes, &pessoas);
    
    memset(grafo, 0, sizeof(grafo));
    memset(vertice, 0, sizeof(vertice));
    
    char nome1[50];
    char relacao[50];
    char nome2[50];

    for(int i = 0; i < pessoas; i++) {
    	scanf("%s %s %s", nome1, relacao, nome2);
    	
        int encontraNome1 = obterIndice(nome1);
        int encontraNome2 = obterIndice(nome2);
        
        grafo[encontraNome1][encontraNome2] = 1;
        grafo[encontraNome2][encontraNome1] = 1;
	}
	
	int resposta = 0;
	for(int i = 0; i < familia; i++){
		if(!vertice[i]){
			dfs(i, familia);
			resposta++;
		}
	}
	
	printf("%d\n", resposta);
    return 0;
}
