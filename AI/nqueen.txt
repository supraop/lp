
import java.util.*;
import java.util.Scanner;

public class NQueens {
    private int[][] chessboard;
    private int boardSize;

    public NQueens(int boardSize) {
        this.chessboard = new int[boardSize][boardSize];
        this.boardSize = boardSize;
    }

    public void solve() {
        if (placeQueens(0)) {
            displayChessboard();
        } else {
            System.out.println("No solution found.");
        }
    }

    private boolean placeQueens(int column) {
        if (column >= boardSize) {
            return true; // All queens have been successfully placed
        }

        for (int row = 0; row < boardSize; row++) {
            if (isSafe(row, column)) {
                chessboard[row][column] = 1; // Place the queen at row, column

                if (placeQueens(column + 1)) {
                    return true; // Recursively place the remaining queens
                }

                // If placing the queen at row, column doesn't lead to a solution, backtrack
                chessboard[row][column] = 0;
            }
        }
        return false; // Unable to place the queen in this column
    }

    private boolean isSafe(int row, int column) {
        // Check if there is a queen in the same row
        for (int i = 0; i < column; i++) {
            if (chessboard[row][i] == 1) {
                return false;
            }
        }

        // Check upper diagonal
        for (int i = row, j = column; i >= 0 && j >= 0; i--, j--) {
            if (chessboard[i][j] == 1) {
                return false;
            }
        }

        // Check lower diagonal
        for (int i = row, j = column; i < boardSize && j >= 0; i++, j--) {
            if (chessboard[i][j] == 1) {
                return false;
            }
        }

        return true; // Safe to place a queen at row, column
    }

    private void displayChessboard() {
        for (int i = 0; i < boardSize; i++) {
            for (int j = 0; j < boardSize; j++) {
                if (chessboard[i][j] == 1) {
                    System.out.print("Q ");
                } else {
                    System.out.print("- ");
                }
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the board size: ");
        int boardSize = scanner.nextInt();

        NQueens nQueens = new NQueens(boardSize);
        nQueens.solve();

        scanner.close();
    }
}

