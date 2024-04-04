#include <math.h>
#include <stdio.h>

#define valorMaximoDeN 110
#define limite 9999999.0

double distancias[valorMaximoDeN][valorMaximoDeN];
double coordenadaX[valorMaximoDeN];
double coordenadaY[valorMaximoDeN];
double raio[valorMaximoDeN];

int antena;
int calculo;

int main() {
    scanf("%d", &antena);

    while (antena != 0) {
        for (int i = 1; i <= antena; i++) {
            scanf("%lf %lf %lf", &coordenadaX[i], &coordenadaY[i], &raio[i]);
        }
        for (int i = 1; i <= antena; i++) {
            for (int j = 1; j <= antena; j++) {
                double distance = sqrt(
                    pow(coordenadaX[i] - coordenadaX[j], 2) +
                    pow(coordenadaY[i] - coordenadaY[j], 2)
                );

                if (distance <= raio[i])
                    distancias[i][j] = distance;
                else
                    distancias[i][j] = limite;
            }
        }
        for (int k = 1; k <= antena; k++)
            for (int i = 1; i <= antena; i++)
                for (int j = 1; j <= antena; j++)
                    distancias[i][j] = fmin(
                        distancias[i][j],
                        distancias[i][k] + distancias[k][j]
                    );

        scanf("%d", &calculo);

        for (int i = 1; i <= calculo; i++) {
            int indice1;
            int indice2;
            scanf("%d %d", &indice1, &indice2);
            if (distancias[indice1][indice2] == limite)
                printf("-1\n");
            else
                printf("%.0lf\n", floor(distancias[indice1][indice2]));
        }

        scanf("%d", &antena);
    }
    return 0;
}