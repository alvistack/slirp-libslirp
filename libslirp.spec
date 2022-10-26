# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: libslirp
Epoch: 100
Version: 4.6.1
Release: 1%{?dist}
Summary: A general purpose TCP-IP emulator
License: MIT
URL: https://gitlab.freedesktop.org/slirp/libslirp/-/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: gcc
BuildRequires: glib2-devel
BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: pkgconfig
BuildRequires: valgrind-devel

%description
A general purpose TCP-IP emulator used by virtual machine hypervisors
to provide virtual networking services.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%meson
%meson_build

%install
%meson_install

%if 0%{?suse_version} > 1500 || 0%{?sle_version} > 150000
%package devel
Summary: Development files for libslirp
Group: Development/Libraries/C and C++
Requires: libslirp0 = %{epoch}:%{version}-%{release}

%description devel
The libslirp-devel package contains libraries and header files for
developing applications that use libslirp.

%package -n libslirp0
Summary: A networking Library
Group: System/Libraries

%description -n libslirp0
A user-mode networking library used by virtual machines, containers
or various tools.

%post -n libslirp0 -p /sbin/ldconfig
%postun -n libslirp0 -p /sbin/ldconfig

%files devel
%dir %{_includedir}/slirp/
%{_includedir}/slirp/*
%{_libdir}/libslirp.so
%{_libdir}/pkgconfig/slirp.pc

%files -n libslirp0
%license COPYRIGHT
%{_libdir}/libslirp.so.0*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package devel
Summary: Development files for libslirp
Requires: libslirp = %epoch:%{version}-%{release}

%description  devel
The libslirp-devel package contains libraries and header files for
developing applications that use libslirp.

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYRIGHT
%{_libdir}/libslirp.so.0*

%files devel
%dir %{_includedir}/slirp/
%{_includedir}/slirp/*
%{_libdir}/libslirp.so
%{_libdir}/pkgconfig/slirp.pc
%endif

%changelog
