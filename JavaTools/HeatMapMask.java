package algo;

/**
 * Created by L on 2018/6/2.
 */
public class HeatMapMask {
    public static double[][] heatMapMask(int radius) {
        int len = 2 * radius - 1;
        double[] mask = new double[len * len];
        double[][] mask2 = new double[len][len];
        for (int i = 0; i < radius; i++) {
            for (int j = 0; j < radius; j++) {
                mask2[i][j] = (i + 0.5) * (j + 0.5) / (radius * radius);
                mask2[i][len - j - 1] = (i + 0.5) * (j + 0.5) / (radius * radius);
                mask2[len - i - 1][j] = (i + 0.5) * (j + 0.5) / (radius * radius);
                mask2[len - i - 1][len - j - 1] = (i + 0.5) * (j + 0.5) / (radius * radius);
//
//                mask[i * len + j] = (i + 0.5) * (j + 0.5) / (radius * radius);
//                mask[i * len + len - j - 1] = (i + 0.5) * (j + 0.5) / (radius * radius);
//                mask[(len - i - 1) * len + j] = (i + 0.5) * (j + 0.5) / (radius * radius);
//                mask[(len - i - 1) * len + len - j - 1] = (i + 0.5) * (j + 0.5) / (radius * radius);
            }
        }
        return mask2;
    }

    public static void main(String[] args) {
        int radius = 5;
        int len = 2 * radius - 1;
        double[][] res = heatMapMask(radius);
        for (int i = 0; i < len; i++) {
            for (int j = 0; j < len; j++) {
                System.out.print(res[i][j] + "\t");
            }
            System.out.println();
        }
//        System.out.println("hello");
    }
}
