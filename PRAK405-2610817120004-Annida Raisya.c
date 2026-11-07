#include <stdio.h>

int main() {
    int n, kelipatan;

    scanf("%d %d", &n, &kelipatan);

    int total_keseluruhan = 0;

    for (int i = 1; i <= n; i++) {
        int total_baris = 0;

        for (int j = i; j >= 1; j--) {
            printf("(%d * %d)", j, kelipatan);
            if (j > 1) {
                printf(" + ");
            }
            total_baris += j * kelipatan;
        }

        total_keseluruhan += total_baris;
        printf(" = %d\n", total_baris);
    }

    printf("%d\n", total_keseluruhan);

    return 0;
}