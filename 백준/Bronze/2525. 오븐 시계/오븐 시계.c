#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
    /*
    int H, M, Time;

    scanf("%d %d", &H, &M);

    if (H == 0)
        H = 24;

    Time = 60 * H + M - 45;
    H = Time / 60;
    M = Time % 60;

    printf("%d %d", H, M);
    */

    int A, B, C, T;

    scanf("%d %d", &A, &B);
    scanf("%d", &C);

    
    T = (B + C) / 60;

    if (T > 0)
    {
        B = (B + C) - 60 * T;
        A += T;
    }
    else
        B += C;

    if (A > 23)
        A -= 24;


    printf("%d %d", A, B);
}