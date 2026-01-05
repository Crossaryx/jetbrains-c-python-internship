#include <stdio.h>
#include <string.h>

int string_func(void) {
    char src[] = "JetBrains coding challenge";
    char dst[32];
    strcpy(dst, src);
    strcat(dst, " passed");
    printf("%s\n", dst);
    return 0;
}
