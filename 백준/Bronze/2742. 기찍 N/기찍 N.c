#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>


int main(void)
{
	int n,s;
	
	scanf("%d",&n);
	s = n;
	
	while(s>0)
	{
		printf("%d\n",s);
		s--;
	} 
}