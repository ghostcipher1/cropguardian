
import pytest
from cropguardian.resource_management import ResourceManagement
from datetime import datetime

def test_update_and_get_resource():
    resource_manager = ResourceManagement()
    resource_manager.update_resource("fertilizers", 50, datetime(2024, 11, 30), 100)
    fertilizers_info = resource_manager.get_resource_info("fertilizers")
    assert fertilizers_info["used"][-1] == 50
    assert fertilizers_info["optimal"] == 100

def test_visualize_resource_trends():
    resource_manager = ResourceManagement()
    resource_manager.update_resource("fertilizers", 50, datetime(2024, 11, 30), 100)
    resource_manager.update_resource("fertilizers", 70, datetime(2024, 12, 1))
    resource_manager.update_resource("fertilizers", 90, datetime(2024, 12, 2))
    # Visualization test: ensure no errors when plotting
    resource_manager.visualize_resource_trends("fertilizers")
