%define name drvfpgasoc
%define version 1.0.1
%define release 2
%define target_kern_ver 5.4.64-altera

Summary: Driver to access FPGA fabric (Linux kernel module)
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
Requires: kernel-image-zimage = 5.4.64+lts+git0+1f2f1ded05-r0
BuildRequires: kernel-devsrc = 1.0 make
BuildArch: cyclone5

%description
Kernel driver of Linux on FPGA SoC (e.g. Cyclone V SoC) to access FPGA fabric.

%prep
rm -rf ${RPM_BUILD_ROOT}

%setup -n %{name}-release-%{version}

%build
make

%install
make DESTDIR=${RPM_BUILD_ROOT} install

%clean
rm -rf ${RPM_BUILD_ROOT}

%post
if [ -z "$(cat /etc/group | awk -F: '{ print $1 }' | grep -e 'fpga')" ]
then
	groupadd -r fpga
fi

# This routine is executed at first installation
if [ "${1}" = '1' ]
then
	depmod
	modprobe fpgasoc
fi

%preun
modprobe -r fpgasoc

%postun
depmod

# This routine is executed at update
if [ "${1}" = '1' ]
then
	modprobe fpgasoc
fi

# This routine is executed at last uninstallation
if [ "${1}" = '0' ]
then
	groupdel fpga
fi

%files
%defattr(-, root, root)
/lib/modules/%{target_kern_ver}/extramodules/fpgasoc.ko
%config(noreplace) /etc/modules-load.d/fpgasoc.conf
%config /etc/udev/rules.d/81-fpgasoc.rules
/usr/include/%{name}.h

%changelog
* Fri Apr 02 2021 Kohei Nagasu <kohei@lcarsnet.pgw.jp> 1.0.1
- Change repository to github and licensed.

* Thu Feb 25 2021 Kohei Nagasu <kohei@lcarsnet.pgw.jp> 1.0.0
- Initial release

