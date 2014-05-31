#sbs-git:slp/api/common capi-base-common 0.1.0 2d37db72791bf53066ac327782d3af9e737c4718
Name:       capi-base-common
Summary:    Common header files of Tizen Native API
Version: 0.1.0
Release:   8 
Group:      TO_BE/FILLED_IN
License:    TO BE FILLED IN
Source0:    %{name}-%{version}.tar.gz
BuildRequires:  cmake

%description
Common header files of Tizen Native API
  
%package devel  
Summary:  Common header files of Tizen Native API (Development)  
Group:    TO_BE/FILLED_IN  
Requires: %{name} = %{version}-%{release}  
  
%description devel
Common header files of Tizen Native API

%prep
%setup -q


%build
cmake . -DCMAKE_INSTALL_PREFIX=/usr


make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}/usr/share/license
cp LICENSE %{buildroot}/usr/share/license/%{name}


%files
/usr/share/license/%{name}
%files devel
/usr/include/*.h
/usr/lib/pkgconfig/capi-base-common.pc
/usr/share/license/%{name}

