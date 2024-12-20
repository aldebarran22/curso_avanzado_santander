

#include <stdio.h>
#include <string.h>


int main(){
	char cad[50] = {"hola que tal"};
	
	char *ptr = strchr(cad, 'x');
	if (ptr == NULL)
		puts("No existe la letra");
		
	else 
		puts(ptr);
}
