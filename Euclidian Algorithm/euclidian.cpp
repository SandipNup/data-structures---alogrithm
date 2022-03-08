#include <iostream>
using namespace std;  


int eculidian(int a, int b){
	int m, n, r;
	if (a > b){
		m = a ;
		n = b ;
	}
	else {
		m = b;
		n = a;
	}
	
	while(n != 0) {
		r = m % n;
		m = n;
		n = r;
	}
	
	return m;
}

int main()
{
    cout << "gcd is " << eculidian(5, 15) << endl;
    return 0;
}