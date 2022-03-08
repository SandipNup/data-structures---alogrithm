int gcdMethod(int a, int b){
	int t;
	
	if (a > b){
		t = b;
	}else {
		t = a;
	}
	
	while(a % t != 0 || b % t != 0){
		t = t - 1;
	}
	return t;
}

void main(){
	printf("The gcd is %d \n", gcdMethod(90, 30));
	printf("The gcd is %d \n", gcdMethod(30, 12));
	printf("The gcd is %d \n", gcdMethod(65, 15));

}