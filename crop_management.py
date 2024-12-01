
class CropManagement:
    def __init__(self):
        self.crops = {}

    def add_crop(self, name, growth_stage, harvest_schedule):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Crop name must be a non-empty string.")
        if not isinstance(growth_stage, str) or not growth_stage.strip():
            raise ValueError("Growth stage must be a non-empty string.")
        if not isinstance(harvest_schedule, str) or not harvest_schedule.strip():
            raise ValueError("Harvest schedule must be a non-empty string.")
        self.crops[name] = {
            "growth_stage": growth_stage,
            "harvest_schedule": harvest_schedule,
        }

    def update_growth_stage(self, name, stage):
        if not isinstance(stage, str) or not stage.strip():
            raise ValueError("Growth stage must be a non-empty string.")
        if name in self.crops:
            self.crops[name]["growth_stage"] = stage
        else:
            raise ValueError(f"Crop '{name}' not found.")

    def get_crop_info(self, name):
        if name not in self.crops:
            raise ValueError(f"Crop '{name}' not found.")
        return self.crops[name]
