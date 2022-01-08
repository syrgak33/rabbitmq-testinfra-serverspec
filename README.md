# rabbitmq-testinfra-serverspec
## _Rabbitmq_check.rb
_So there are two files rabbitmq_check.rb for **Serverspec** 
and rabbittest.py for **TestInfra**_

> to use rabbitmq_check.rb we need to perfrom these steps:
1. Install ruby and ruby-serverspec packages.
2. gem install serverspec
3. perform these steps
```bash
$ serverspec-init
Select OS type:

  1) UN*X
  2) Windows

Select number: 1

Select a backend type:

  1) SSH
  2) Exec (local)

Select number: 2   

Vagrant instance y/n: n
Input target host name: www.example.jp
 + spec/
 + spec/www.example.jp/
 + spec/www.example.jp/sample_spec.rb
 + spec/spec_helper.rb
 + Rakefile
 + .rspec
```
4. It will create some folders and in **spec/localhost/sample_spec.rb** you need to replace it with **rabbitmq_check.rb**
5. use command **rake spec** or sudo **rake-spec**
6. It will check rabbitmq-server package, service, and port of rabbitmqUI.

###Rabbittest.py
> To use this file perform these steps:
1. **pip install pytest-testinfra**
2. create or download rabbittest.py from here
3. and the last command: **py.test -v rabbittest.py
4. It will check rabbitmq-server package, service, and port of rabbitmqUI.
