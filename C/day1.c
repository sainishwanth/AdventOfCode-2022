#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main(){
	FILE * FILE_ptr;
	char ch;

	FILE_ptr = fopen("day1.txt", "r");
	char * arr;
	int i = 0;
	while(ch != EOF){
		ch = fgetc(FILE_ptr);
		if(!strcmp(ch,"\n")){
			arr[i] = ch;
			i++;
		}	
	}
	arr[i] = '\0';
	fclose(FILE_ptr);
	char * ptr = &arr[0];

	while(*ptr != '\0'){
		printf("%c", *ptr);
		ptr++;
	}
	return 0;
}
