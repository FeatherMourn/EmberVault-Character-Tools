import unittest
from embervault_sdk import ModuleContext
from src.module import compare_equipment, simulate_progression

class CharacterModuleTests(unittest.TestCase):
    def test_progression_is_plan_only(self):
        result = simulate_progression(ModuleContext("embervault.character-tools", "research", "EV-OP-1"),
                                      1, 10, ["Equip starter armor"])
        self.assertEqual(result.status, "ready")
        self.assertEqual(result.data["application_state"], "plan-only")
        self.assertEqual(result.to_dict()["contract_version"], 1)

    def test_equipment_comparison_is_plan_only(self):
        result = compare_equipment(ModuleContext("embervault.character-tools", "research", "EV-OP-2"),
                                   ["Iron Helm", "Torch"], ["Torch", "Wolf Hood"])
        self.assertEqual(result.status, "ready")
        self.assertEqual(result.data["shared"], ["Torch"])
        self.assertEqual(result.data["application_state"], "plan-only")

if __name__ == "__main__":
    unittest.main()
