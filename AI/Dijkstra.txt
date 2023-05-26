import java.util.*;
class Edge {
    int destination, weight;

    Edge(int destination, int weight) {
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
        Edge edge = new Edge(destination, weight);
        adjacencyList.get(source).add(edge);
    }

    void dijkstraMST(int source) {
        int[] distance = new int[vertices];
        Arrays.fill(distance, Integer.MAX_VALUE);
        distance[source] = 0;

        PriorityQueue<Edge> minHeap = new PriorityQueue<>((a, b) -> a.weight - b.weight);
        minHeap.offer(new Edge(source, 0));

        while (!minHeap.isEmpty()) {
            Edge currentEdge = minHeap.poll();
            int vertex = currentEdge.destination;

            if (currentEdge.weight > distance[vertex]) {
                continue;
            }

            for (Edge edge : adjacencyList.get(vertex)) {
                int neighbor = edge.destination;
                int weight = edge.weight;

                if (distance[vertex] + weight < distance[neighbor]) {
                    distance[neighbor] = distance[vertex] + weight;
                    minHeap.offer(new Edge(neighbor, distance[neighbor]));
                }
            }
        }

        System.out.println("Minimum Spanning Tree (from source " + source + "):");
        for (int i = 0; i < vertices; i++) {
            if (i != source) {
                System.out.println(source + " - " + i + " : " + distance[i]);
            }
        }
    }
}

public class DijkstraMST {
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

        System.out.print("Enter the source vertex for MST: ");
        int sourceVertex = scanner.nextInt();

        graph.dijkstraMST(sourceVertex);
    }
}
