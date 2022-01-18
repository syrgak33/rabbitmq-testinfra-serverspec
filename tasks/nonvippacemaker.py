def test_haproxy_service(host):
    haproxyser = host.service("haproxy")
    assert not haproxyser.is_running
    assert not haproxyser.is_enabled
