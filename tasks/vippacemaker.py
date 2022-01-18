def test_haproxy_service(host):
    haproxyser = host.service("haproxy")
    assert haproxyser.is_running
    assert haproxyser.is_enabled
