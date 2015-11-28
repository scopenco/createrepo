# Repository for CreateRepo Project (http://createrepo.com)

## Usage

Clone github repositories and run vagrant
```
git clone https://github.com/scopenco/vagrant-rpmbuilder.git
cd vagrant-rpmbuilder
vagrant up
git -C ./src clone https://github.com/scopenco/createrepo.git
```

Login and build rpm or develop your RPMS
```
vagrant ssh
cd /opt/rpmbuilder
./rpmbuild-6-x86_64.sh ./createrepo/mypackage/mypackage.spec
```
