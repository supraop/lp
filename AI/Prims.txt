import java.util.*;

class Edge {
    int source, destination, weight;

    Edge(int source, int destination, int weight) {
        this.source = source;
        this.destination = destination;
        this.weight = weight;
    }
}

class Graph {
    int vertices;
    List<List<Edge>> adjacencyList;

    Graph(int vertices) {
        this.vertices = vertices;
        this.adjacencyList = new ArrayList<>(vertices);
        for (int i = 0; i < vertices; i++) {
            adjacencyList.add(new ArrayList<>());
        }
    }

    void addEdge(int source, int destination, int weight) {
        Edge edge = new Edge(source, destination, weight);
        adjacencyList.get(source).add(edge);
        adjacencyList.get(destination).add(edge);
    }

    List<Edge> primMST() {
        boolean[] visited = new boolean[vertices];
        int[] parent = new int[vertices];
        int[] key = new int[vertices];
        Arrays.fill(key, Integer.MAX_VALUE);

        PriorityQueue<Edge> minHeap = new PriorityQueue<>(vertices, (a, b) -> a.weight - b.weight);
        List<Edge> result = new ArrayList<>();

        int startVertex = 0;
        key[startVertex] = 0;
        minHeap.offer(new Edge(-1, startVertex, 0));

        while (!minHeap.isEmpty()) {
            Edge currentEdge = minHeap.poll();
            int vertex = currentEdge.destination;

            if (visited[vertex]) {
                continue;
            }

            visited[vertex] = true;

            if (currentEdge.source != -1) {
                result.add(currentEdge);
            }

            for (Edge edge : adjacencyList.get(vertex)) {
                int neighbor = edge.destination;
                int weight = edge.weight;

                if (!visited[neighbor] && weight < key[neighbor]) {
                    parent[neighbor] = vertex;
                    key[neighbor] = weight;
                    minHeap.offer(new Edge(vertex, neighbor, weight));
                }
            }
        }

        return result;
    }
}

public class PrimMST {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of vertices: ");
        int vertices = scanner.nextInt();

        Graph graph = new Graph(vertices);

        System.out.print("Enter the number of edges: ");
        int edges = scanner.nextInt();

        System.out.println("Enter the source, destination, and weight of each edge:");
        for (int i = 0; i < edges; i++) {
            int source = scanner.nextInt();
            int destination = scanner.nextInt();
            int weight = scanner.nextInt();
            graph.addEdge(source, destination, weight);
        }

        List<Edge> mst = graph.primMST();

        System.out.println("Minimum Spanning Tree:");
        for (Edge edge : mst) {
            System.out.println(edge.source + " - " + edge.destination + " : " + edge.weight);
        }
    }
}
