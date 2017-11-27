#include <stdio.h>

int main(int argc, char **argv){
        char buf[1024];
        strcpy(buf, argv[1]);
        printf(buf);
        printf("\n");
}
