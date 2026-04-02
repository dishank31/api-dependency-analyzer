from pydantic import BaseModel
from typing import Dict, Any, List, Optional

class ChangeAnalysisRequest(BaseModel):
    endpoint_id: int
    new_contract: Dict[str, Any]

class BreakingChange(BaseModel):
    type: str       # "field_removed", "type_changed", "required_added"
    path: str       # e.g. "response.200.user.email"
    severity: str   # "high", "medium", "low"
    old_value: Optional[Any] = None
    new_value: Optional[Any] = None

class ImpactedService(BaseModel):
    service_id: int
    service_name: str
    break_probability: float   # 0.0 to 1.0
    call_frequency: int
    reason: str

class ChangeAnalysisResponse(BaseModel):
    is_breaking: bool
    breaking_changes: List[BreakingChange]
    impacted_services: List[ImpactedService]
    total_impacted: int
    