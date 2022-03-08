
public class GCDMethod1 {
    
    static int gcdMethod(int a, int b){
        int t = Math.min(a, b);
        while(a % t != 0 || b % t != 0){
            t = t - 1;
        }
        return t;
    }

    public static void main(String[] args) {
        System.out.println(GCDMethod1.gcdMethod(10, 15));
        System.out.println(GCDMethod1.gcdMethod(25, 15));
        System.out.println(GCDMethod1.gcdMethod(60, 20));
    }
}
