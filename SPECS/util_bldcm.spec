%define name util_bldcm
%define version 1.0.0
%define release 1

Summary: util_bldcm (Utilities to control mBldcm)
Name: %{name}
Version: %{version}
Release: %{release}
Group: Applications/System
License: MIT/GPL
Packager: Kohei Nagasu <kohei@lcarsnet.pgw.jp>
Vendor: Drone DIY Prj.

%undefine _disable_source_fetch
Source0: https://github.com/nagasuk/%{name}/archive/release-%{version}.tar.gz#/%{name}-release-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: libfpgasoc >= 1.0.1 libbldcm >= 1.0.0
BuildRequires: libfpgasoc >= 1.0.1 libbldcm >= 1.0.0 make cmake >= 3.13.0 boost-staticdev
BuildArch: cyclone5

%description
Utility set to control mBldcm.

%prep
rm -rf ${RPM_BUILD_ROOT}

%setup -n %{name}-release-%{version}

%build
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build

%install
cmake --install build --prefix ${RPM_BUILD_ROOT}/usr

%clean
rm -rf ${RPM_BUILD_ROOT}

%post

%postun

%files
%defattr(-, root, root)
/usr/bin/bldcmmon
/usr/share/doc/util_bldcm/bldcmmon.sample.cfg

%changelog
* Sat May 28 2022 Kohei Nagasu <kohei@lcarsnet.pgw.jp> 1.0.0-1
- Initial release

