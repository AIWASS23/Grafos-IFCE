#include <stdio.h>
#include <string.h>

#define MAX_R 1000
#define MAX_C 1000

char grid1[MAX_R][MAX_C];
char grid2[MAX_R][MAX_C];

int R, C;

// Function to efficiently check overlap within bounds
int checkOverlap(int x, int y) {
    int overlap = 0;
    for (int i = 0; i < R && i + x >= 0 && i + x < R; i++) {
        for (int j = 0; j < C && j + y >= 0 && j + y < C; j++) {
            if (grid1[i][j] == grid2[i + x][j + y]) {
                overlap++;
            }
        }
    }
    return overlap;
}

void printOverlap(int x, int y) {
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            if (i + x < R && j + y < C && grid1[i][j] == grid2[i + x][j + y]) {
                printf("%c", grid1[i][j]);
            } else {
                printf("%c", grid1[i][j]);
            }
        }
        printf("\n");
    }
}

int main() {
    while (1) {
        scanf("%d %d", &R, &C);
        if (R == 0 && C == 0) {
            break;
        }

        for (int i = 0; i < R; i++) {
            scanf("%s", grid1[i]);
        }

        for (int i = 0; i < R; i++) {
            scanf("%s", grid2[i]);
        }

        int maxOverlap = 0;
        int startX = 0, startY = 0;

        // Optimized loop to consider only valid shifts
        for (int x = 0; x < R; x++) {
            for (int y = 0; y < C; y++) {
                int overlap = checkOverlap(x, y);
                if (overlap > maxOverlap) {
                    maxOverlap = overlap;
                    startX = x;
                    startY = y;
                }
            }
        }

        printOverlap(startX, startY);
        for (int i = 0; i < C; i++) {
            printf("+");
        }
        printf("\n");
    }

    return 0;
}