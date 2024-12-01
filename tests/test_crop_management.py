import pytest
from cropguardian.crop_management import CropManagement

def test_add_crop():
    crop_manager = CropManagement()
    crop_manager.add_crop("Wheat", "Seedling", "30 days")
    crop_info = crop_manager.get_crop_info("Wheat")
    assert crop_info["growth_stage"] == "Seedling"
    assert crop_info["harvest_schedule"] == "30 days"

def test_update_growth_stage():
    crop_manager = CropManagement()
    crop_manager.add_crop("Wheat", "Seedling", "30 days")
    crop_manager.update_growth_stage("Wheat", "Vegetative")
    crop_info = crop_manager.get_crop_info("Wheat")
    assert crop_info["growth_stage"] == "Vegetative"
