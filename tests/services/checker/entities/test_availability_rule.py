from site_connectivity_checker.services.checker.entities.rule import AvailabilityRule


def test_availability_rule():
    info = dict(
        [
            ("enabled", True),
            ("request_to_perform", 20),
            ("interval_in_milliseconds", 8080),
        ]
    )
    r = AvailabilityRule(**info)
    assert r.dict() == info
