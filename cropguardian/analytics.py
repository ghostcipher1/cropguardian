
import matplotlib.pyplot as plt

class Analytics:
    def __init__(self):
        pass

    def visualize_crop_growth(self, crop_manager):
        """
        Visualizes the growth stages of crops as a bar chart.

        :param crop_manager: An instance of CropManagement.
        """
        crops = crop_manager.crops
        crop_names = list(crops.keys())
        growth_stages = [crop["growth_stage"] for crop in crops.values()]

        plt.figure(figsize=(8, 5))
        plt.bar(crop_names, range(len(growth_stages)), tick_label=growth_stages)
        plt.title("Crop Growth Stages")
        plt.xlabel("Crops")
        plt.ylabel("Growth Stages (Index)")
        plt.show()

    def visualize_resource_trends(self, resource_manager, resource_name):
        """
        Visualizes the time-series trends for a specific resource.

        :param resource_manager: An instance of ResourceManagement.
        :param resource_name: The name of the resource to visualize.
        """
        resource_data = resource_manager.get_resource_info(resource_name)
        timestamps = resource_data["timestamps"]
        used_values = resource_data["used"]
        optimal_value = resource_data["optimal"]

        plt.figure(figsize=(10, 6))
        plt.plot(timestamps, used_values, label="Used", marker="o")

        if optimal_value is not None:
            plt.axhline(optimal_value, color="red", linestyle="--", label="Optimal")

        plt.xlabel("Time")
        plt.ylabel("Usage")
        plt.title(f"Time-Series Trend for {resource_name.capitalize()}")
        plt.legend()
        plt.grid()
        plt.show()

    def visualize_resource_comparison(self, resource_manager):
        """
        Visualizes the usage of multiple resources as a bar chart.

        :param resource_manager: An instance of ResourceManagement.
        """
        resource_names = list(resource_manager.resources.keys())
        used_values = [resource_manager.resources[res]["used"][-1] if resource_manager.resources[res]["used"] else 0 for res in resource_names]
        optimal_values = [resource_manager.resources[res]["optimal"] if resource_manager.resources[res]["optimal"] else 0 for res in resource_names]

        plt.figure(figsize=(10, 6))
        bar_width = 0.35
        index = range(len(resource_names))

        plt.bar(index, used_values, bar_width, label="Used")
        plt.bar([i + bar_width for i in index], optimal_values, bar_width, label="Optimal")

        plt.xlabel("Resources")
        plt.ylabel("Amount")
        plt.title("Resource Utilization vs Optimal Usage")
        plt.xticks([i + bar_width / 2 for i in index], resource_names)
        plt.legend()

        plt.show()
