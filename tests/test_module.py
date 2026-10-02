import unittest
from embervault_sdk import ModuleContext
from src.module import simulate_progression

class CharacterModuleTests(unittest.TestCase):
    def test_progression_is_plan_only(self):
        result = simulate_progression(ModuleContext("embervault.character-tools", "research", "EV-OP-1"),
                                      1, 10, ["Equip starter armor"])
        self.assertEqual(result.status, "ready")
        self.assertEqual(result.data["application_state"], "plan-only")
        self.assertEqual(result.to_dict()["contract_version"], 1)

if __name__ == "__main__":
    unittest.main()
