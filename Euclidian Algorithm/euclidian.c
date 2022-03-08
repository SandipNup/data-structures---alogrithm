
int eculidian(int a, int b) {
	int m, n, r;
	if (a > b){
		m = a;
		n = b;
	}
	else {
		m = b ;
		n = a ;
	};
	
	while(n != 0){
		r = m % n;
		m = n;
		n = r;
	};
	return m;
}

void main(){
	printf("The first return value %d \n",eculidian(5, 15));
	printf("The first return value %d \n",eculidian(25, 225));
	printf("The first return value %d \n",eculidian(60, 225));
}