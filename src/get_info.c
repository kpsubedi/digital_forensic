#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/stat.h>
#include <sys/types.h>

int main(int argc, char *argv[]){
    struct stat filestat;

    if(argc != 2){
        fprintf(stderr, "Usage: %s <valid pathname>\n", argv[0]);
	exit(EXIT_FAILURE);
	}

    int fscode = stat(argv[1], &filestat);
    if(fscode == -1){
	perror("Unable to get status\n");
	exit(EXIT_FAILURE);
	}

    printf("File type:		\n");

    return 0;
}
	


