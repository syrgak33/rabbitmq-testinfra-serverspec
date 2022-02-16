
def test_service_health(host):
    serviceout = host.check_output("curl http://localhost:8500/v1/catalog/services")
# Web ордуна эже $consul catalog services деген команданы жазып consulдан кийинки любой сервисти жазып койесуз.  
    assert "web" in serviceout

def test_consulnode_health(host):
# localhosttun orduna consul master node ip addressin жазыш керек, localhost.localdomainдин ордуна $consul members командасынан server 
# дегендердин атын бир бирден жазып чыгасыз.
# канча мастер node болсо ошончо ушул кодтон жазыш керек. def test_consulnode2_health..., def test_consulnode3_health...
    masternode1 = host.check_output("curl localhost:8500/v1/health/node/localhost.localdomain")
    assert "passing" in masternode1
    
#def test_consulnode2_health(host):
#   masternode2 = host.check_output("curl 172.3.4.5:8500/v1/health/node/master2")
#   assert "passing" in masternode2

#def test_consulnode3_health(host):
#   masternode3 = host.check_output("curl localhost:8500/v1/health/node/master3")
#   assert "passing" in masternode3

