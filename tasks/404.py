def test_ingress1(host):
    output1 = host.check_output("curl https://dev-k8s-ingress.dev.echogl.net/this-path-is-for-testing-and-should-always-return-a-404")
    assert "404 Not Found" in output1

def test_ingress2(host):
    output2 = host.check_output("curl https://qa1-k8s-ingress.qa.echogl.net/this-path-is-for-testing-and-should-always-return-a-404")
    assert "404 Not Found" in output2

def test_ingress3(host):
    output3 = host.check_output("http://prd-k8s-ingress.hq.echogl.net/this-path-is-for-testing-and-should-always-return-a-404")
    assert "404 Not Found" in output3
