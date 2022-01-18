## connections
1. After installing testinfra. At least two ways of ssh connections could be established.
2. SSHing with Ansible inventory file(/etc/ansible/hosts) ![Screenshot 2022-01-19 031143](https://user-images.githubusercontent.com/85344623/150019623-a0e039e3-5268-4bc7-8e31-8b8fb7447dd8.png)
```bash
py.test -v kubectl.py --force-ansible --hosts='ansible://testservers'  #in the end it is the name of the inventory [group]
```
3. OR via editing sshconfig file (/root/.ssh/ssh_config) **_chmod 600 ssh_config_**![Screenshot 2022-01-19 031513](https://user-images.githubusercontent.com/85344623/150019968-f1c45d2e-54e9-477d-9ed6-c668b4878fb0.png)
```bash 
py.test -v kubectl.py --ssh-config=/root/.ssh/ssh_config --hosts='ssh://34.88.124.0'
```
> Note: in .py files assert=true , assert not=false

