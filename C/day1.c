#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main(){
	FILE * FILE_ptr;
	char ch;

	FILE_ptr = fopen("day1.txt", "r");
	printf("File opened");
	char arr[2500];
	int i = 0;
	int c;
	while((c = fgetc(FILE_ptr)) != EOF){
		arr[i] = c;
		i += 1;
	}
	printf("Lines: %d\n", i+1);
	for(i = 0; i < 10477 ; ++i){
		printf("%c", arr[i]);
	}
	fclose(FILE_ptr);
	return 0;
}
