#include <stdio.h>

int main(void)
{
	int T = 0; 
	scanf("%d",&T);
	int h[1000] = {0};
	
	for (int i = 0; i < T; i++){
		int r[100000] = {0};
		int nW = 1;
		int H,W,N;
		scanf("%d %d %d",&H,&W,&N);
		
		for (int k = 0; k < W; k++){
			for(int j = 0; j < H; j++){
				r[k*H+j] = (j+1)*100+nW;
			}
			nW += 1;
		}
		
		h[i] = r[N-1];
	
	}
	
	for (int i = 0; i < T; i++){
			printf("%d\n",h[i]);
	}
}