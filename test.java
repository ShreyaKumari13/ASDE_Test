public class test{
    public static boolean canCrossChakravyuha(int p, int[] k, int a, int b, int bPower) {
        int n = k.length;
        for (int i = 0; i < n; i++) {
            if (i == 3 && k[2] > 0) {
                p -= k[2] / 2;
                if (p <= 0) return false;
            }
            if (i == 7 && k[6] > 0) {
                p -= k[6] / 2;
                if (p <= 0) return false;
            }
            if (p < k[i]) {
                if (a > 0) {
                    a--; 
                } else if (b > 0) {
                    p += bPower;
                    b--;
                    if (p >= k[i]) {
                        p -= k[i];
                    } else {
                        return false;
                    }
                } else {
                    return false;
                }
            } else {
                p -= k[i];
            }

            if (p <= 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {

        int p1 = 120;
        int[] k1 = {10, 20, 30, 15, 25, 35, 20, 30, 40, 50, 60};
        int a1 = 1;
        int b1 = 1;
        int bPower1 = 40;
        System.out.println(canCrossChakravyuha(p1, k1, a1, b1, bPower1));

        int p2 = 50;
        int[] k2 = {20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70};
        int a2 = 0;
        int b2 = 1;
        int bPower2 = 10;
        System.out.println(canCrossChakravyuha(p2, k2, a2, b2, bPower2));
    }
}
