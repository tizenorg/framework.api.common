Name:       capi-base-common
Summary:    Common header files of Tizen Native API
Version: 0.2.2
Release:   1
Group:      Base
License:    Apache-2.0
Source0:    %{name}-%{version}.tar.gz
BuildRequires:  cmake
Requires(post): /sbin/ldconfig  
Requires(postun): /sbin/ldconfig

%description
Common header files of Tizen Native API
  
%package devel  
License:  Apache-2.0
Summary:  Common header files of Tizen Native API (Development)  
Group:    Base
Requires: %{name} = %{version}-%{release}  
  
%description devel
Common header files of Tizen Native API

%prep
%setup -q

%build

MAJORVER=`echo %{version} | awk 'BEGIN {FS="."}{print $1}'`

cmake . -DCMAKE_INSTALL_PREFIX=/usr -DLIB_INSTALL_DIR:PATH=%{_libdir} -DFULLVER=%{version} -DMAJORVER=${MAJORVER}

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}

%make_install
mkdir -p %{buildroot}/usr/share/license
cp LICENSE %{buildroot}/usr/share/license/%{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
/usr/share/license/%{name}
%{_libdir}/libcapi-base-common.so*

%files devel
/usr/include/*.h
/usr/lib/pkgconfig/capi-base-common.pc
/usr/share/license/%{name}

