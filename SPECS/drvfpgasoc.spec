%define name drvfpgasoc
%define version 1.0.0
%define release 1
%define target_kern_ver 5.4.64-altera

Summary: Driver to access FPGA fabric (Linux kernel module)
Name: %{name}
Version: %{version}
Release: %{release}
Group: Development/Libraries
License: MIT/GPT
Packager: Kohei Nagasu <kohei@lcarsnet.pgw.jp>
Vendor: Drone DIY Prj.

%undefine _disable_source_fetch
Source0: https://git.lcarsnet.pgw.jp/gitbucket/kohei/%{name}/archive/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: kernel-image-zimage = 5.4.64+lts+git0+1f2f1ded05-r0
BuildRequires: kernel-devsrc = 1.0 make
BuildArch: cyclone5

%description
Kernel driver of Linux on FPGA SoC (e.g. Cyclone V SoC) to access FPGA fabric.

%prep
rm -rf ${RPM_BUILD_ROOT}

%setup -n %{name}-%{name}-%{version}

%build
make

%install
make DESTDIR=${RPM_BUILD_ROOT} install

%clean
rm -rf ${RPM_BUILD_ROOT}

%post
depmod
if [ -z "$(cat /etc/group | awk -F: '{ print $1 }' | grep -e 'fpga')" ]
then
	groupadd -r fpga
fi

%postun
modprobe -r fpgasoc
groupdel fpga
depmod

%files
%defattr(-, root, root)
/lib/modules/%{target_kern_ver}/extramodules/fpgasoc.ko
%config(noreplace) /etc/modules-load.d/fpgasoc.conf
%config /etc/udev/rules.d/81-fpgasoc.rules
/usr/include/%{name}.h

%changelog
* Wed Feb 25 2021 Kohei Nagasu <kohei@lcarsnet.pgw.jp> 1.0.0
- Initial release

