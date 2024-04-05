#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

int bairros;
int conexoes;
int perguntas;
int matriz[404][404];

int main(){
	
	scanf("%d %d %d", &bairros, &conexoes, &perguntas);
	int i, j, k, u, v;
	for(int i = 0; i < conexoes; i++) {
		scanf("%d %d", &u, &v); 
        u--;
        v--;
		matriz[u][v] = matriz[v][u] = 1;
	}
	
	for(int k = 0; k < bairros; k++) {
        for(int i = 0; i < bairros; i++) { 
            for(int j = 0; j < bairros; j++){
		        if (matriz[i][k] && matriz[k][j]) {
                    matriz[i][j] = 1;
                }
            }
        }
	}
	
	for(int i = 0; i < perguntas; i++){
		scanf("%d %d", &u, &v); 
        u--; 
        v--;

		if(matriz[u][v]) {
            printf("Lets que lets \n");
        }
		else {
            printf("Deu ruim \n");
        }
	}
    return  0;
}