function gcdMethod1(a , b) {
    t = Math.min(a, b)

    while( a % t != 0 || b % t != 0){
        t = t - 1
    }
    return t
}


console.log(gcdMethod1(10, 15));
console.log(gcdMethod1(20, 60));
console.log(gcdMethod1(15, 60));

