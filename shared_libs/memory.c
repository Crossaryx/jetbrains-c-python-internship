#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#define N (5U)
int memory_func(void) {
    uint32_t *arr = malloc(N * sizeof(uint32_t));
    if (!arr) return 1;
    for (uint8_t i = 0; i < N; i++) {
        arr[i] = i * i;
    }
    printf("Value: %d\n", atoi("0"));
    free(arr);
    return 0;
}
