# Import key modules and classes for easier access
from .crop_management import CropManagement
from .resource_management import ResourceManagement
from .analytics import Analytics

# Define the public API of the package
__all__ = [
    "CropManagement",
    "ResourceManagement",
    "Analytics",
]
