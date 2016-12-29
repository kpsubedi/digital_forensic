

#include <endian.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char **argv){

    union {
	uint32_t u32;
	uint8_t value[4];
	} myunion;

    myunion.value[0] = 0x41; // Lowest Address Byte
    myunion.value[1] = 0x42;
    myunion.value[2] = 0x43;
    myunion.value[3] = 0x44; // Highest-Address Byte

printf("myunion.u32 = 0x%x\n", myunion.u32);
printf("htole32(myunion.u32) = 0x%x\n", htole32(myunion.u32));
printf("htobe32(myunion.u32) = 0x%x\n", htobe32(myunion.u32));
	
exit(EXIT_SUCCESS);
}

