public class Eculidian {

    public static int gcdFinder(int a, int b) {
       int m = Math.max(a, b);
       int n = Math.min(a, b);

       while(n != 0) {
           int r = m % n;
           m = n;
           n = r;
       }
       return m;
    }

    public static void main(String[] args) {
       System.out.println(Eculidian.gcdFinder(10, 14));
       System.out.println(Eculidian.gcdFinder(12, 60));
       System.out.println(Eculidian.gcdFinder(15, 225));
       System.out.println(Eculidian.gcdFinder(60, 225)); 
    }
}
