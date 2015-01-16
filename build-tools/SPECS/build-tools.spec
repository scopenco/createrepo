# vim: ft=spec

Summary: Tools for build creation
Name: build-tools
Version: 1.4.1
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
cp -a src/*.py src/*.sh src/*_template src/modules repository $RPM_BUILD_ROOT/%{_datadir}/%{name}
%{__perl} -pi -e 's;modules;%{_datadir}/%{name}/modules;g' $RPM_BUILD_ROOT/%{_datadir}/%{name}/*.py
%{__perl} -pi -e 's;project_template;%{_datadir}/%{name}/project_template;g' $RPM_BUILD_ROOT/%{_datadir}/%{name}/*.sh
%{__perl} -pi -e 's;release_template;%{_datadir}/%{name}/release_template;g' $RPM_BUILD_ROOT/%{_datadir}/%{name}/*.sh
%{__perl} -pi -e 's;repository;%{_datadir}/%{name}/repository;g' $RPM_BUILD_ROOT/%{_datadir}/%{name}/*.sh

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d
echo "pathmunge %{_datadir}/%{name}" > $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d/%{name}.sh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_datadir}/%{name}
%{_sysconfdir}/profile.d/%{name}.sh
%defattr(755,root,root,-)
%{_datadir}/%{name}/*.py
%defattr(755,root,root,-)
%{_datadir}/%{name}/*.sh

%changelog
* Fri Jan 16 2015 Andrey Scopenco <andrey@scopenco.net> - 1.4.1-1
- update to 1.4.1
* Sat Jan 10 2015 Andrey Scopenco <andrey@scopenco.net> - 1.4-2
- add path to profile
* Fri Jan 9 2015 Andrey Scopenco <andrey@scopenco.net> - 1.4-1
- 1.4 release
