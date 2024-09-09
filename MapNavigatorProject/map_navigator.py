import tkinter as tk
from tkinter import messagebox
from graph import Graph
# Using tkinter in python to implementing the UI pat for this project.
class MapNavigatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Map Navigator")

        self.graph = Graph()

        # Create UI elements
        self.create_widgets()

    def create_widgets(self):
        # Add Edge Section
        tk.Label(self.root, text="Add Edge").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self.root, text="From Node:").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(self.root, text="To Node:").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(self.root, text="Weight:").grid(row=3, column=0, padx=10, pady=5)

        self.from_node_entry = tk.Entry(self.root)
        self.to_node_entry = tk.Entry(self.root)
        self.weight_entry = tk.Entry(self.root)

        self.from_node_entry.grid(row=1, column=1, padx=10, pady=5)
        self.to_node_entry.grid(row=2, column=1, padx=10, pady=5)
        self.weight_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Button(self.root, text="Add Edge", command=self.add_edge).grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Shortest Path Section
        tk.Label(self.root, text="Find Shortest Path").grid(row=5, column=0, padx=10, pady=5)
        tk.Label(self.root, text="Start Node:").grid(row=6, column=0, padx=10, pady=5)
        tk.Label(self.root, text="End Node:").grid(row=7, column=0, padx=10, pady=5)

        self.start_node_entry = tk.Entry(self.root)
        self.end_node_entry = tk.Entry(self.root)

        self.start_node_entry.grid(row=6, column=1, padx=10, pady=5)
        self.end_node_entry.grid(row=7, column=1, padx=10, pady=5)

        tk.Button(self.root, text="Find Path", command=self.find_path).grid(row=8, column=0, columnspan=2, padx=10, pady=10)

    def add_edge(self):
        from_node = self.from_node_entry.get()
        to_node = self.to_node_entry.get()
        weight = self.weight_entry.get()

        try:
            weight = int(weight)
            self.graph.add_edge(from_node, to_node, weight)
            messagebox.showinfo("Success", f"Edge from {from_node} to {to_node} with weight {weight} added.")
        except ValueError:
            messagebox.showerror("Error", "Weight must be an integer.")

    def find_path(self):
        start_node = self.start_node_entry.get()
        end_node = self.end_node_entry.get()

        distance, path = self.graph.dijkstra(start_node, end_node)

        if distance == float('inf'):
            messagebox.showinfo("Result", f"No path found from {start_node} to {end_node}.")
        else:
            path_str = " -> ".join(path)
            messagebox.showinfo("Result", f"Shortest path from {start_node} to {end_node} is {path_str} with distance {distance}.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MapNavigatorApp(root)
    root.mainloop()
