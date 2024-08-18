#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>


int main(void)
{
	int n,s,A,B;
	s = 0;
	
	scanf("%d",&n);
	
	while(s<n)
	{
		scanf("%d %d",&A,&B);
		printf("Case #%d: %d\n",s+1,A+B);
		s++;
	} 
}