Summary:       Temporary fix for /usr/bin/python3 requirement in OBS services
Name:          python3-symlink
Version:       0.0.1
Release:       1%{?dist}
License:       GPL-3.0+
Requires:      python3-local

%description
%{summary}

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin
ln -s ../local/bin/python3 $RPM_BUILD_ROOT/usr/bin/python3

%files
%defattr(-,root,root)
/usr/bin/python3
