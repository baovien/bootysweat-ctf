#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

void secretstorage(void)
{
	system("cat flag.txt");
}

int main(void) 
{
	char password[25];

	setvbuf(stdout, NULL, _IONBF, 0);
	printf("Welcome to Sopra Steria's super secret file storage!\nPlease enter super secret password:\n");

	read(STDIN_FILENO, password, 64);

	return 0;
}
