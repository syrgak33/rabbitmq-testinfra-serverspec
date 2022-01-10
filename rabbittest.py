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
