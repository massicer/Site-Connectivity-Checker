from site_connectivity_checker.services.checker.entities.endpoint import Endpoint


def test_endpoint():
    info = dict([("protocol", "http"), ("url", "google"), ("port", 8080)])

    e = Endpoint(**info)

    assert e is not None
    assert e.compose_url() == f"{info['protocol']}://{info['url']}:{info['port']}"
