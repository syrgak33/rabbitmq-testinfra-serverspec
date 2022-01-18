def test_pacemaker_service(host):
    pacemakerser = host.service("pacemaker")
    assert pacemakerser.is_running
    assert pacemakerser.is_enabled
