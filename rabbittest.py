def test_if_rabbitmq_is_installed(host):
    rabbitmq_package = host.package('rabbitmq-server')
    assert rabbitmq_package.is_installed

def test_rabbitmq_runnnig_and_enabled(host):
    rabbitmq = host.service("rabbitmq-server")
    assert rabbitmq.is_running
    assert rabbitmq.is_enabled

def test_rabbitmqui_port(host):
    rabuiport = host.socket('tcp://0.0.0.0:15672')
    assert rabuiport.is_listening
    
def test_output_rabbitmqctl(host):
    output = host.check_output("sudo rabbitmqctl cluster_status")
    assert 'rabbit@ubserver','rabbit@localhost' in output
    
def test_passwd_file(host):
    passwd = host.file("/etc/passwd")
    assert passwd.contains("root")
    assert passwd.user == "root"
    assert passwd.group == "root"

def test_consul(host):
    consuloutput = host.check_output("curl -G http://127.0.0.1:8500/v1/health/node/nt")
    assert not "[]" in consuloutput

def test_service_health(host):
    serviceout = host.check_output("curl -G http://localhost:8500/v1/health/service/web?passing")
    assert not "[]" in serviceout
    

