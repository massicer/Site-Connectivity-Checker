from pydantic import BaseModel


class AvailabilityRule(BaseModel):
    enabled: bool = True
    request_to_perform: int = 1
    interval_in_milliseconds: int
