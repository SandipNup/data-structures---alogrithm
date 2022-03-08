const euclidian = (a,b) => {
    m = Math.max(a,b);
    n = Math.min(a,b);

    while (n!=0){
        r = m % n;
        m = n
        n = r
    }
    return m
} 

console.log(euclidian(10,11))
console.log(euclidian(15,5))
console.log(euclidian(25,5))
console.log(euclidian(45,9))