import java.util.*;

class Node implements Comparable<Node> {
    private int[][] state;
    private int cost;
    private int heuristic;
    private int moves;
    private Node parent;

    public Node(int[][] state, int moves, Node parent) {
        this.state = state;
        this.moves = moves;
        this.parent = parent;
        this.cost = calculateCost();
        this.heuristic = calculateHeuristic();
    }

    public int getCost() {
        return cost;
    }

    public int[][] getState() {
        return state;
    }

    public int getMoves() {
        return moves;
    }

    public Node getParent() {
        return parent;
    }

    public int compareTo(Node other) {
        return Integer.compare(this.cost + this.heuristic, other.cost + other.heuristic);
    }

    private int calculateCost() {
        int cost = 0;
        int[][] goalState = {{1, 2, 3}, {4, 5, 6}, {7, 8, 0}};

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (state[i][j] != goalState[i][j]) {
                    cost++;
                }
            }
        }

        return cost;
    }

    private int calculateHeuristic() {
        int heuristic = 0;
        int[][] goalState = {{1, 2, 3}, {4, 5, 6}, {7, 8, 0}};

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                int value = state[i][j];
                if (value != 0) {
                    int targetRow = (value - 1) / 3;
                    int targetCol = (value - 1) % 3;
                    heuristic += Math.abs(i - targetRow) + Math.abs(j - targetCol);
                }
            }
        }

        return heuristic;
    }
}

public class EightPuzzleSolver {
    private static final int[][] DIRECTIONS = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}}; // Up, Down, Left, Right

    public static void main(String[] args) {
        int[][] initialState = getUserInput();
        Node initialNode = new Node(initialState, 0, null);

        List<Node> path = solveEightPuzzle(initialNode);

        if (path == null) {
            System.out.println("No solution found.");
        } else {
            System.out.println("Solution found!");
            System.out.println("Number of moves: " + path.size());
            System.out.println("Path:");
            for (Node node : path) {
                printState(node.getState());
                System.out.println();
            }
        }
    }

    private static int[][] getUserInput() {
        Scanner scanner = new Scanner(System.in);
        int[][] initialState = new int[3][3];

        System.out.println("Enter the initial state of the puzzle (0 for empty space):");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                initialState[i][j] = scanner.nextInt();
            }
        }

        return initialState;
    }

    private static List<Node> solveEightPuzzle(Node initialNode) {
        Set<Node> visited = new HashSet<>();
        PriorityQueue<Node> queue = new PriorityQueue<>();
        queue.add(initialNode);

        while (!queue.isEmpty()) {
            Node currentNode = queue.poll();

            if (isGoalState(currentNode.getState())) {
                return constructPath(currentNode);
            }

            visited.add(currentNode);

            for (Node neighbor : getNeighbors(currentNode)) {
                if (!visited.contains(neighbor)) {
                    queue.add(neighbor);
                }
            }
        }

        return null;
    }

    private static boolean isGoalState(int[][] state) {
        int[][] goalState = {{1, 2, 3}, {4, 5, 6}, {7, 8, 0}};
        return Arrays.deepEquals(state, goalState);
    }

    private static List<Node> getNeighbors(Node node) {
        List<Node> neighbors = new ArrayList<>();
        int[][] state = node.getState();
        int emptyRow = 0;
        int emptyCol = 0;

        // Find the position of the empty space (0)
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (state[i][j] == 0) {
                    emptyRow = i;
                    emptyCol = j;
                }
            }
        }

        // Generate neighbors by moving the empty space
        for (int[] direction : DIRECTIONS) {
            int newRow = emptyRow + direction[0];
            int newCol = emptyCol + direction[1];

            if (newRow >= 0 && newRow < 3 && newCol >= 0 && newCol < 3) {
                int[][] newState = new int[3][3];
                for (int i = 0; i < 3; i++) {
                    for (int j = 0; j < 3; j++) {
                        newState[i][j] = state[i][j];
                    }
                }

                newState[emptyRow][emptyCol] = newState[newRow][newCol];
                newState[newRow][newCol] = 0;

                Node neighbor = new Node(newState, node.getMoves() + 1, node);
                neighbors.add(neighbor);
            }
        }

        return neighbors;
    }

    private static List<Node> constructPath(Node node) {
        List<Node> path = new ArrayList<>();

        while (node != null) {
            path.add(0, node);
            node = node.getParent();
        }

        return path;
    }

    private static void printState(int[][] state) {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print(state[i][j] + " ");
            }
            System.out.println();
        }
    }
}
