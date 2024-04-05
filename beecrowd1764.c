#include <stdio.h>
#include <stdlib.h>

#define valorMaximoN 40100
#define valorMaximoM 50100

int pai[valorMaximoN];
int rank[valorMaximoN];
int n;
int m;

typedef struct {
    int primeiro;
    struct {
        int index1;
        int index2;
    } segundo;
} Pair;

Pair vetor[valorMaximoM];

int comparar(const void *a, const void *b) {
    Pair *p1 = (Pair *)a;
    Pair *p2 = (Pair *)b;
    return p1->primeiro - p2->primeiro;
}

int encontrar(int x) {
    if (x != pai[x]) {
        pai[x] = encontrar(pai[x]);
    }
    return pai[x];
}

void juntar(int x, int y) {
    int raizX = encontrar(x);
    int raizY = encontrar(y);

    if (raizX == raizY) {
        return;
    }

    if (rank[raizX] < rank[raizY]) {
        pai[raizX] = raizY;
    } else if (rank[raizX] > rank[raizY]) {
        pai[raizY] = raizX;
    } else {
        pai[raizY] = raizX;
        rank[raizX]++;
    }
}

int main() {
    while (1) {
        scanf("%d %d", &n, &m);

        if (n == 0 && m == 0) { 
            break;
        }
        
        int resposta = 0;

        for (int i = 0; i < n; i++) {
            pai[i] = i;
            rank[i] = 0;
        }

        for (int i = 0; i < m; i++) {
            int u, v, p;
            scanf("%d %d %d", &u, &v, &p);
            vetor[i].primeiro = p;
            vetor[i].segundo.index1 = u;
            vetor[i].segundo.index2 = v;
        }
        
        qsort(vetor, m, sizeof(Pair), comparar);
        
        for (int i = 0; i < m; i++) {
            if (encontrar(vetor[i].segundo.index1) != encontrar(vetor[i].segundo.index2)) {
                resposta += vetor[i].primeiro;
                juntar(vetor[i].segundo.index1, vetor[i].segundo.index2);
            }
        }

        printf("%d\n", resposta);
    }
    
    return 0;
}
