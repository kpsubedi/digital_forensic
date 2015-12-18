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
    /*switch (filestat.st_mode & S_IFMT){
	case S_IFDIR:
		printf("Directory \n");
		break;
	case S_IFREG:
		printf("Regular File\n");
		break;
	case S_IFBLK:
		printf("Block Device\n");
		break;
	case S_IFCHR:
		printf("Character Device\n");
		break;
	case S_IFFIFO:
		printf("FIFO/Pipe\n");
		break;
	case S_IFLNK:
		printf("Symbolic Link \n");
		break;
	case S_IFSOCK:
		printf("Socket\n");
		break;
	default:
		printf("Unknown\n");
		break;

	}*/
    if(S_ISREG(filestat.st_mode))
        printf("Regular File\n");
    else if(S_ISDIR(filestat.st_mode))
        printf("Directory \n");
    else if(S_ISCHR(filestat.st_mode))
	printf("Character Device\n");
    else if(S_ISBLK(filestat.st_mode))
	printf("Block Device\n");
    else if(S_ISFIFO(filestat.st_mode))
	printf("FIFO/PIPE \n");
    else if(S_ISSOCK(filestat.st_mode))
	printf("Socket\n");
    else if(S_ISLNK(filestat.st_mode))
        printf("Symbolic Link\n");		
    else
	printf("Unknown\n");
    return 0;
}
	


