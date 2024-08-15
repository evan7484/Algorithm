#include <stdio.h>

int main (void)
{
	int m,num,sum=0;
	char n[] = "000";
	
	scanf("%d\n",&m);
	scanf("%s",&n);
	
	num = n[2]-'0';
	sum += m*num;
	printf("%d\n",m*num);
	num = n[1]-'0';
	sum += m*num*10;
	printf("%d\n",m*num);
	num = n[0]-'0';
	sum += m*num*100;
	printf("%d\n",m*num);
	printf("%d",sum);
	
	
 } 