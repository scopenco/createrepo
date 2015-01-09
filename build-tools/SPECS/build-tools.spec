Summary: Tools for build creation
Name: build-tools
Version: 1.4
Release: 1
Packager: Andrey Scopenco <andrey@scopenco.net>
License: GPL
Group: Applications/System
Source: http://github.com/scopenco/build-tools/archive/%{version}.zip

Requires: bash, grep
Requires: yum, python, createrepo, repoview

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%description
Tools for build creation

%prep
%setup

%install
rm -rf $RPM_BUILD_ROOT

# Install the code
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}
cp -a src/*.py src/*.sh src/modules repository $RPM_BUILD_ROOT/%{_datadir}/%{name}
%{__perl} -pi -e 's;modules;%{_datadir}/%{name}/modules;g' $RPM_BUILD_ROOT/%{_datadir}/%{name}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_datadir}/%{name}

%changelog
* Fri Jan 9 2015 Andrey Scopenco <andrey@scopenco.net> - 1.4-1
- 1.4 release
