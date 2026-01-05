#include <stdio.h>
#include <time.h>
#include "string.h"

int time_func(void) {
    time_t now = time(NULL);
    printf("Current timestamp: %ld\n", now);
    string_func();
    return 0;
}
