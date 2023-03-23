/*
You are given a 3x3 matrix of positive integers. You have to
determine whether some row is a positive integer multiple of
another.

If row i is an integer multiple of row j, then you have
to output
p#q where p is the minimum of (i,j) and q is the maximum of (i,j).

If there are multiple possibilities for i and j, you have to print for the
smallest i and the smallest j.


Otherwise, you have to output
0#0
*/

#include <stdio.h>

int isC(int r1[3],int r2[3]){
  	if(r1[0] == 0 && r2[0] == 0
	&& r1[1] == 0 && r2[1] == 0
	&& r1[2] == 0 && r2[2] == 0 ) return 1;
	if(r1[0] == 0 || r1[1] == 0 || r1[2] == 0) return 0;
	int m1 = r2[0] % r1[0];
	int m2 = r2[1] % r1[1];
	int m3 = r2[2] % r1[2];

	int d1 = r2[0] / r1[0];
	int d2 = r2[1] / r1[1];
	int d3 = r2[2] / r1[2];

	if(m1 == 0 && m2 == 0 && m3 == 0 && d1 == d2 && d2 == d3 && d1 == d3){
		return 1;
	}
	return 0;
}

int isM(int r1[3],int r2[3]){

	if(r1[0] < r2[0]){
		return isC(r1,r2);
	}else{
		return isC(r2,r1);
	}
	return 0;

}

int main(){

	int M[3][3];

	for(int i = 0;i<3;i++){
		for(int j = 0;j<3;j++){
			scanf("%d",&M[i][j]);
		}
	}
	
	int i01 = isM(M[0],M[1]);
	int i02 = isM(M[0],M[2]);
	int i12 = isM(M[1],M[2]);

	if(i01 == 1){
		printf("0#1");
	}else if(i02 == 1){
		printf("0#2");
	}else if(i12 == 1){
		printf("1#2");
	}else{
		printf("0#0");
	}

}

