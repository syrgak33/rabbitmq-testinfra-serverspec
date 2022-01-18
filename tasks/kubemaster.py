def test_user(host):
    user = host.user("root")
    assert user.exists

def test_kubectl_output(host):
    output = host.check_output("kubectl get nodes")
    assert 'Ready' in output
    assert not 'NotReady' in output
    assert not 'Unknown' in output
    assert not 'MemoryPressure' in output
    assert not 'DiskPressure' in output
    assert not 'OutOfDisk' in output

def test_cluster_info(host):
    clusinfo = host.check_output("kubectl cluster-info")
    assert '\x1b[0;32mKubernetes control plane\x1b[0m is running' in clusinfo
    assert '\x1b[0;32mCoreDNS\x1b[0m is running' in clusinfo
