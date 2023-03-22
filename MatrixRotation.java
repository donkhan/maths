// Rotate Matrix by 45 degree

public class MatrixRotation {

    public static void main(String args[]){
        char inx[][] = {
                {'0','0','1','0','0'},
                {'0','0','1','0','0'},
                {'1','1','1','1','1'},
                {'0','0','1','0','0'},
                {'0','0','1','0','0'}
        };
        char in[][] = {
                {'a','b','c','d','e'},
                {'f','g','h','i','j'},
                {'k','l','m','n','o'},
                {'p','q','r','s','t'},
                {'u','v','w','x','y'}
        };
        char out[][] = new char[5][5];
        print(in);
        //fn(in,out,0,4,2);
        //fn(in,out,1,3,1);
        int mid = in.length/2;
        int shift = mid;
        for(int i = 0;i<mid;i++){
            fn(in,out,i,in.length-i-1,shift);
            shift--;
        }
        out[mid][mid] = in[mid][mid];
        print(out);
    }

    private static void print(char a[][]){
        for(int i = 0;i<a.length;i++){
            for(int j = 0;j<a[i].length;j++){
                System.out.print(a[i][j]  + " ");
            }
            System.out.println();
        }
        System.out.println("----------------------------------------------");
    }

    private static void fn(char[][] in, char[][] out, int e1,int e2,int shift) {
        boolean debug = false;
        int x = e2 - e1 + 1;
        int s = 2 * x  + ( (x-2) * 2);
        char a[] = new char[s];
        char b[] = new char[s];

        int r1 = e1; int c1 = e1;
        int r2 = e2; int c2 = e2;
        int r = r1; int c = c1;
        int as = 0;
        while(c <= c2){
            a[as++] = in[r][c];
            c++;
        }
        c = c - 1;
        r = r + 1;
        while(r <= r2){
            a[as++] = in[r][c];
            r++;
        }
        r = r - 1;
        c = c - 1;
        while(c >= c1){
            a[as++] = in[r][c];
            c--;
        }
        c = c + 1;
        r = r - 1;
        while(r > r1){
            a[as++] = in[r][c];
            r--;
        }
        for(int i = 0;i<s-shift;i++){
            b[i] = a[i+shift];
        }
        int j = 0;
        for(int i = s-shift;i < s;i++){
            b[i] = a[j++];
        }
        if(debug) {
            for (int i = 0; i < s; i++)
                System.out.print(a[i] + "  ");
            System.out.println("");
            for (int i = 0; i < s; i++)
                System.out.print(b[i] + "  ");
            System.out.println("");
        }

        r1 = e1; c1 = e1;
        r2 = e2; c2 = e2;
        r = r1; c = c1;
        as = 0;
        while(c <= c2){
            out[r][c] = b[as++];
            c++;
        }
        c = c - 1;
        r = r + 1;
        while(r <= r2){
            out[r][c] = b[as++];
            r++;
        }
        r = r - 1;
        c = c - 1;
        while(c >= c1){
            out[r][c] = b[as++];
            c--;
        }
        c = c + 1;
        r = r - 1;
        while(r > r1){
            out[r][c] = b[as++];
            r--;
        }
    }

}
