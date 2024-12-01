import matplotlib.pyplot as plt
from datetime import datetime

class ResourceManagement:
    def __init__(self):
        self.resources = {
            "land": {"used": [], "optimal": None, "timestamps": []},
            "fertilizers": {"used": [], "optimal": None, "timestamps": []},
            "water_usage": {"used": [], "optimal": None, "timestamps": []},
            "labor": {"used": [], "optimal": None, "timestamps": []},
        }

    def update_resource(self, resource_name, used_amount, timestamp, optimal_amount=None):
        if resource_name not in self.resources:
            raise ValueError(f"Resource '{resource_name}' not found.")
        if not isinstance(used_amount, (int, float)) or used_amount < 0:
            raise ValueError("Used amount must be a non-negative number.")
        if not isinstance(timestamp, datetime):
            raise ValueError("Timestamp must be a valid datetime object.")
        if optimal_amount is not None and (not isinstance(optimal_amount, (int, float)) or optimal_amount < 0):
            raise ValueError("Optimal amount must be a non-negative number.")

        self.resources[resource_name]["used"].append(used_amount)
        self.resources[resource_name]["timestamps"].append(timestamp)

        if optimal_amount is not None:
            self.resources[resource_name]["optimal"] = optimal_amount

    def visualize_resource_trends(self, resource_name):
        if resource_name not in self.resources:
            raise ValueError(f"Resource '{resource_name}' not found.")
        resource_data = self.resources[resource_name]
        if not resource_data["used"] or not resource_data["timestamps"]:
            raise ValueError(f"No data available for resource '{resource_name}'.")

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
