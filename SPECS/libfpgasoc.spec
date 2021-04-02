%define name libfpgasoc
%define version 1.0.1
%define release 1

Summary: libfpgasoc (Library to control FPGA fabric by using drvfpgasoc)
Name: %{name}
Version: %{version}
Release: %{release}
Group: Development/Libraries
License: MIT/GPT
Packager: Kohei Nagasu <kohei@lcarsnet.pgw.jp>
Vendor: Drone DIY Prj.

%undefine _disable_source_fetch
Source0: https://github.com/nagasuk/%{name}/archive/release-%{version}.tar.gz#/%{name}-release-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: drvfpgasoc >= 1.0.0
BuildRequires: drvfpgasoc >= 1.0.0 make cmake >= 3.8.0
BuildArch: cyclone5

%description
Library to use FPGA fabric of FPGA SoC (e.g. Cyclone V SoC) by using drvfpgasoc (Linux kernel module to access FPGA fabric).

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
ldconfig

%postun
ldconfig

%files
%defattr(-, root, root)
/usr/lib/libfpgasoc.so.1.0.1
/usr/lib/libfpgasoc.so.1
/usr/lib/libfpgasoc.so
/usr/include/libfpgasoc.h
/usr/include/libfpgasoc.hpp

%changelog
* Fri Apr 02 2021 Kohei Nagasu <kohei@lcarsnet.pgw.jp> 1.0.1
- Change repository to github and licensed.

* Thu Feb 25 2021 Kohei Nagasu <kohei@lcarsnet.pgw.jp> 1.0.0
- Initial release

