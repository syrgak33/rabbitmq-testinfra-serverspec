require 'spec_helper'


describe package('rabbitmq-server'), :if => os[:family] == 'ubuntu' do
  it { should be_installed }
end


describe service('rabbitmq-server'), :if => os[:family] == 'ubuntu' do
  it { should be_enabled }
  it { should be_running }
end

describe port(15672) do
  it { should be_listening }
end

describe command('sudo rabbitmqctl cluster_status') do 
  its(:stdout) { should contain('rabbit@localhost', 'rabbit@ubserver') }
end
