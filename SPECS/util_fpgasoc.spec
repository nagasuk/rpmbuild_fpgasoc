%define name util_fpgasoc
%define version 1.0.1
%define release 1

Summary: util_fpgasoc (Utilities to control FPGA fabric)
Name: %{name}
Version: %{version}
Release: %{release}
Group: Applications/System
License: MIT/GPT
Packager: Kohei Nagasu <kohei@lcarsnet.pgw.jp>
Vendor: Drone DIY Prj.

%undefine _disable_source_fetch
Source0: https://github.com/nagasuk/%{name}/archive/release-%{version}.tar.gz#/%{name}-release-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: libfpgasoc >= 1.0.0
BuildRequires: libfpgasoc >= 1.0.0 make cmake >= 3.13.0 boost-staticdev
BuildArch: cyclone5

%description
Utility set to control FPGA fabric of FPGA SoC (e.g. Cyclone V SoC).

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
/usr/bin/fpgasoc
%attr(0744,root,root) /usr/bin/tgldevmod_drvfpgasoc.sh

%changelog
* Fri Apr 02 2021 Kohei Nagasu <kohei@lcarsnet.pgw.jp> 1.0.1
- Change repository to github and licensed.
- Fixed attribute of tgldevmod_drvfpgasoc.sh.

* Thu Feb 28 2021 Kohei Nagasu <kohei@lcarsnet.pgw.jp> 1.0.0
- Initial release

