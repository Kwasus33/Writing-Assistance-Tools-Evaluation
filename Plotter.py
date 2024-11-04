import matplotlib.pyplot as plt


class Plotter:
    def __init__(self, metrics):
        self._metrics = metrics
        
    def plotBarChart(self, module_name, values):
        plt.figure(figsize=(10, 8))

        bars = plt.bar(self._metrics, values, color=['navy', 'red', 'lime', 'purple'])
        plt.ylim(0, 1)
        plt.ylabel("Score")
        plt.title(f"{module_name} Performance Metrics")

        for bar in bars:
            y_value = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, y_value + 0.02, f"{y_value:.2f}", ha="center", va="bottom")

        plt.savefig(f"{module_name}_Metrics.png", format="png", dpi=300)
        
        plt.close()
