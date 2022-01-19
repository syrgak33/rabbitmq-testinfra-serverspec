require 'spec_helper'

describe user('felixgrates') do
        it { should exist}
end
describe command('kubectl get nodes') do
          its(:stdout) { should_not contain('NotReady') }
          its(:stdout) { should_not contain('Unknown') }
          its(:stdout) { should_not contain('MemoryPressure')}
          its(:stdout) { should_not contain('OutOfDisk')}
          its(:stdout) { should_not contain('DiskPressure')}
end
describe command('kubectl cluster-info') do
        its(:stdout) { should contain ("[Kubernetes control plane] [is running]")}
        its(:stdout) { should contain ('[CoreDNS][is running]')}
end
## /x1b[0;32m   && /e[0;32m  &&  [ text ]
describe command('kubectl cluster-info') do
        its(:exit_status) {should eq 0 }
end
