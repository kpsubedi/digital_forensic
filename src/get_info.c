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
    	
    printf("File stat ino_t :%ld\n", (ino_t)filestat.st_ino);
    printf("File stat mode_t :%x\n", (mode_t)filestat.st_mode);

    printf("File type:		\n");
    switch (filestat.st_mode & S_IFMT){
	case S_IFDIR:
		printf("Directory \n");
		break;
	default:
		printf("Unknown\n");
		break;

	}

    return 0;
}
	


