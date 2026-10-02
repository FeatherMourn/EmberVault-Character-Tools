from __future__ import annotations
from embervault_sdk import ModuleContext, ModuleResult

MODULE_ID = "embervault.character-tools"

def describe() -> dict:
    return {"id": MODULE_ID, "execution": "embedded", "application_state": "plan-only", "mutates_saves": False}

def simulate_progression(context: ModuleContext, from_level: int, target_level: int,
                         steps: list[str]) -> ModuleResult:
    if context.module_id != MODULE_ID or context.capability_state != "plan-only":
        return ModuleResult("blocked", "Character Tools requires a plan-only context.")
    if target_level < from_level or not 1 <= target_level <= 50:
        return ModuleResult("blocked", "Target level must be between the current level and 50.")
    return ModuleResult("ready", "Progression simulation prepared.",
                        {"from_level": from_level, "target_level": target_level,
                         "levels_to_gain": target_level - from_level, "steps": list(steps),
                         "application_state": "plan-only"})
