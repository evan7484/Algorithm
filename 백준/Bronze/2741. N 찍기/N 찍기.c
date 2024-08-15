#include <stdio.h>


int main(void)
{
	int n,s;
	s = 1;
	
	scanf("%d",&n);
	
	while(s<n+1)
	{
		printf("%d\n",s);
		s++;
	} 
}