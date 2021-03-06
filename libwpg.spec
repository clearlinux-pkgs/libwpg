#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libwpg
Version  : 0.3.3
Release  : 4
URL      : https://dev-www.libreoffice.org/src/libwpg-0.3.3.tar.xz
Source0  : https://dev-www.libreoffice.org/src/libwpg-0.3.3.tar.xz
Summary  : Library for importing and converting Corel WordPerfect(tm) Graphics images
Group    : Development/Tools
License  : LGPL-2.1 MPL-2.0-no-copyleft-exception
Requires: libwpg-bin = %{version}-%{release}
Requires: libwpg-lib = %{version}-%{release}
Requires: libwpg-license = %{version}-%{release}
BuildRequires : doxygen
BuildRequires : pkgconfig(librevenge-0.0)
BuildRequires : pkgconfig(librevenge-generators-0.0)
BuildRequires : pkgconfig(libwpd-0.10)

%description


%package bin
Summary: bin components for the libwpg package.
Group: Binaries
Requires: libwpg-license = %{version}-%{release}

%description bin
bin components for the libwpg package.


%package dev
Summary: dev components for the libwpg package.
Group: Development
Requires: libwpg-lib = %{version}-%{release}
Requires: libwpg-bin = %{version}-%{release}
Provides: libwpg-devel = %{version}-%{release}
Requires: libwpg = %{version}-%{release}

%description dev
dev components for the libwpg package.


%package doc
Summary: doc components for the libwpg package.
Group: Documentation

%description doc
doc components for the libwpg package.


%package lib
Summary: lib components for the libwpg package.
Group: Libraries
Requires: libwpg-license = %{version}-%{release}

%description lib
lib components for the libwpg package.


%package license
Summary: license components for the libwpg package.
Group: Default

%description license
license components for the libwpg package.


%prep
%setup -q -n libwpg-0.3.3
cd %{_builddir}/libwpg-0.3.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604610002
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1604610002
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libwpg
cp %{_builddir}/libwpg-0.3.3/COPYING.LGPL %{buildroot}/usr/share/package-licenses/libwpg/3704f4680301a60004b20f94e0b5b8c7ff1484a9
cp %{_builddir}/libwpg-0.3.3/COPYING.MPL %{buildroot}/usr/share/package-licenses/libwpg/9744cedce099f727b327cd9913a1fdc58a7f5599
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/wpg2raw
/usr/bin/wpg2svg
/usr/bin/wpg2svgbatch.pl

%files dev
%defattr(-,root,root,-)
/usr/include/libwpg-0.3/libwpg/WPGraphics.h
/usr/include/libwpg-0.3/libwpg/libwpg.h
/usr/lib64/libwpg-0.3.so
/usr/lib64/pkgconfig/libwpg-0.3.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/libwpg/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libwpg-0.3.so.3
/usr/lib64/libwpg-0.3.so.3.0.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libwpg/3704f4680301a60004b20f94e0b5b8c7ff1484a9
/usr/share/package-licenses/libwpg/9744cedce099f727b327cd9913a1fdc58a7f5599
