#include <stdio.h>
int file_func(void) {
    FILE *f = fopen("some.txt", "w");
    if (!f) return 1;
    fprintf(f, "Hello, world!\n");
    fclose(f);
    printf("File written successfully.\n");
    return 0;
}
