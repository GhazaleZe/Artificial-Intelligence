package com.company;
import org.chocosolver.solver.Model;
//import org.chocosolver.solver.Solver;
import org.chocosolver.solver.expression.discrete.arithmetic.ArExpression;
import org.chocosolver.solver.variables.IntVar;
import org.chocosolver.solver.Solution;

import java.util.Scanner;

public class OLS_CSP {
    static Scanner  s= new Scanner(System.in);
    public static int n=s.nextInt();
    static Model model = new Model(n + "-Orthogonal Latin Square");
    static IntVar[][] a = new IntVar[n][n];
    static IntVar[][] b = new IntVar[n][n];
    static ArExpression[] pairs_int = new ArExpression[n*n];
    static IntVar[] vars = new IntVar[n*n];

    private static IntVar[] getRowVars_a(int rowIdx) {
        IntVar[] res = new IntVar[n];

        if (n >= 0) System.arraycopy(a[rowIdx], 0, res, 0, n);

        return res;
    }

    private static IntVar[] getColVars_a(int colIdx) {
        IntVar[] res = new IntVar[n];

        for ( int idx = 0; idx < n; idx++) {
            res[idx] = a[idx][colIdx];
        }

        return res;
    }

    private static IntVar[] getRowVars_b(int rowIdx) {
        IntVar[] res = new IntVar[n];

        if (n >= 0) System.arraycopy(b[rowIdx], 0, res, 0, n);

        return res;
    }

    private static IntVar[] getColVars_b(int colIdx) {
        IntVar[] res = new IntVar[n];

        for ( int idx = 0; idx < n; idx++) {
            res[idx] = b[idx][colIdx];
        }

        return res;
    }

    private static IntVar[] pairs_check() {


        int k=0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                pairs_int[k]=(a[i][j].mul(10));
                pairs_int[k]=(b[i][j].add(pairs_int[k]));
                vars[k]=pairs_int[k].intVar();
                k++;
            }
        }

        return vars;
    }

    public static void main(String[] args) {


    // The model is the main component of Choco Solver

        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++)
                a[i][j] = model.intVar("a_"+i+"_"+j, 1, n);
        }
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++)
                b[i][j] = model.intVar("b_"+i+"_"+j, 1, n);
        }



        for(int i = 0; i < n; i++){
            model.allDifferent(getRowVars_a(i)).post();

            // Add constraints on cols, all differents ...
            model.allDifferent(getColVars_a(i)).post();

            model.allDifferent(getRowVars_b(i)).post();

            // Add constraints on cols, all differents ...
            model.allDifferent(getColVars_b(i)).post();
        }
        for(int i = 0; i < n*n; i++){
            model.allDifferent( pairs_check()).post();

        }

        Solution solution = model.getSolver().findSolution();
        //Solver solver = model.getSolver();
        if(solution != null){
            //System.out.println(solution.toString());
            //solver.showStatistics();
            for(int i = 0; i < n; i++){
                for(int j = 0; j < n; j++) {
                    System.out.print("(" + a[i][j].getValue() + "," + b[i][j].getValue() + ") ");
                }
                System.out.println();
            }
        }
        else{
            System.out.println("Can't find solution :(");
        }


    }




}
