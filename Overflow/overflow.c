#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<string.h>

int exploit(void) {
	return 1;
}


int overflow(void) {
	int arr[4];
	arr[0] = 10;
	arr[1] = 11;
	arr[2] = 12;
	arr[3] = 17;
	arr[4] = 10;
	arr[5] = 0x00005555;
	arr[6] = 0x55555125;
	
	return 1;
}

int main() {
// Dummy Code
	int i;
	i = 14;
	
	overflow();
	
	return 0; 
}
