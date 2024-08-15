#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
    
    int H, M, Time;

    scanf("%d %d", &H, &M);

    if (H == 0)
        H = 24;

    Time = 60 * H + M - 45;
    H = Time / 60;
    M = Time % 60;

    if (H == 24)
        H = 0;

    printf("%d %d", H, M);
   
 }