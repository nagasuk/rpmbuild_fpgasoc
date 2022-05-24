%define name libbldcm
%define version 1.0.0
%define release 2

Summary: libbldcm (Library to control BLDCM by using mBldcm)
Name: %{name}
Version: %{version}
Release: %{release}
Group: Development/Libraries
License: MIT/GPL
Packager: Kohei Nagasu <kohei@lcarsnet.pgw.jp>
Vendor: Drone DIY Prj.

%undefine _disable_source_fetch
Source0: https://github.com/nagasuk/%{name}/archive/release-%{version}.tar.gz#/%{name}-release-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: libfpgasoc >= 1.0.1
BuildRequires: libfpgasoc >= 1.0.1 make cmake >= 3.8.0
BuildArch: cyclone5

%description
Library to control HW IP of mBldcm via libfpgasoc.

%prep
rm -rf ${RPM_BUILD_ROOT}

%setup -n %{name}-release-%{version}

%build
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release -DLIBBLDCM_BUILD_SHARED_LIBS=ON
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
/usr/lib/libbldcm.so.1.0.0
/usr/lib/libbldcm.so.1
/usr/lib/libbldcm.so
/usr/include/libbldcm.hpp
/usr/include/libbldcm/register_map.hpp
/usr/lib/cmake/bldcm/bldcm-config.cmake
/usr/lib/cmake/bldcm/bldcm-config-release.cmake
/usr/lib/cmake/bldcm/bldcm-config-version.cmake

%changelog
* Tue May 24 2022 Kohei Nagasu <kohei@lcarsnet.pgw.jp> 1.0.0-2
- Add config file of cmake for users to use find_package.

* Mon May 16 2022 Kohei Nagasu <kohei@lcarsnet.pgw.jp> 1.0.0-1
- Initial release

