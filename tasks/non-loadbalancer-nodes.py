def test_kubelet_service(host):
    kubeletser = host.service("kubelet")
    assert kubeletser.is_running
    assert kubeletser.is_enabled

def test_docker_service(host):
    dockerser = host.service("docker")
    assert dockerser.is_running
    assert dockerser.is_enabled
