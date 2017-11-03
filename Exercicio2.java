//Exercício dois, letra Cs
//     a) larg ordem visita partindo do c
//     b) profundidade ordem visita partindo do c   
// --> c)larg, prof, a*  c-> a   

package Previo;

	import es.usc.citius.hipster.algorithm.Hipster;
	import es.usc.citius.hipster.graph.GraphBuilder;
	import es.usc.citius.hipster.graph.GraphSearchProblem;
	import es.usc.citius.hipster.graph.HipsterDirectedGraph;
	import es.usc.citius.hipster.model.problem.SearchProblem;
	import es.usc.citius.hipster.graph.HipsterGraph;

public class Ex2 {

	public static void main(String[] args) {
		//Grafo A
			HipsterGraph<String, Double> grafoA = GraphBuilder.<String,Double>create()
					.connect("A").to("B").withEdge(1d)
					.connect("A").to("C").withEdge(1d)
					.connect("A").to("D").withEdge(1d)
					.connect("B").to("C").withEdge(1d)
					.connect("B").to("E").withEdge(1d)
					.connect("B").to("G").withEdge(1d)
					.connect("C").to("E").withEdge(1d)
					.connect("C").to("F").withEdge(1d)
					.connect("D").to("F").withEdge(1d)
					.connect("E").to("F").withEdge(1d)
					.connect("E").to("G").withEdge(1d)
					.connect("F").to("H").withEdge(1d)
					.connect("G").to("H").withEdge(1d)
					.connect("G").to("J").withEdge(1d)
					.connect("H").to("I").withEdge(1d)
					.connect("I").to("J").withEdge(1d)
					.createUndirectedGraph();

			//Grafo B
			HipsterDirectedGraph<String, Double> grafoB = GraphBuilder.<String,Double>create()
					.connect("A").to("B").withEdge(1d)
					.connect("A").to("C").withEdge(1d)
					.connect("A").to("D").withEdge(1d)
					.connect("C").to("B").withEdge(1d)
					.connect("C").to("E").withEdge(1d)
					.connect("C").to("G").withEdge(1d)
					.connect("D").to("A").withEdge(1d)
					.connect("D").to("E").withEdge(1d)
					.connect("E").to("H").withEdge(1d)
					.connect("F").to("B").withEdge(1d)
					.connect("G").to("D").withEdge(1d)
					.connect("G").to("F").withEdge(1d)
					.connect("G").to("H").withEdge(1d)
					.createDirectedGraph();

			SearchProblem problema = GraphSearchProblem.startingFrom("C")
					.in(grafoA)
					.takeCostsFromEdges()
					.build();
			System.out.println("Undirected Graph *******************************\n");
			System.out.println("BreadthFirstSearch \n");
			System.out.println(Hipster.createBreadthFirstSearch(problema).search("A"));
			System.out.print("\n");
	        System.out.println("DepthFirstSearch \n");
			System.out.println(Hipster.createDepthFirstSearch(problema).search("A"));
			System.out.print("\n");
			System.out.println("Busca em AStar \n");
			System.out.println(Hipster.createAStar(problema).search("A"));
			System.out.print("\n");

			problema = GraphSearchProblem.startingFrom("C")
					.in(grafoB)
					.takeCostsFromEdges()
					.build();
			System.out.println("Directed Graph *******************************\n");
			System.out.println("BreadthFirstSearch \n");
			System.out.println(Hipster.createBreadthFirstSearch(problema).search("A"));
			System.out.print("\n");
	        System.out.println("DepthFirstSearch \n");
			System.out.println(Hipster.createDepthFirstSearch(problema).search("A"));
			System.out.print("\n");
			System.out.println("Busca em AStar \n");
			System.out.println(Hipster.createAStar(problema).search("A"));
			System.out.print("\n");
	}
}

