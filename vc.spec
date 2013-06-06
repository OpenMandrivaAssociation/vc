%define debug_package %nil
%define major 0
%define beta %{nil}
%define scmrev %{nil}
%define devname %mklibname vc -d -s

Name: vc
Version: 0.7.1
%if "%{beta}" == ""
%if "%{scmrev}" == ""
Release: 2
Source: http://code.compeng.uni-frankfurt.de/attachments/download/161/Vc-%version.tar.gz
%else
Release: 0.%{scmrev}.1
Source: %{name}-%{scmrev}.tar.xz
%endif
%else
%if "%{scmrev}" == ""
Release: 0.%{beta}.1
Source: %{name}-%{version}%{beta}.tar.bz2
%else
Release: 0.%{beta}.%{scmrev}.1
Source: %{name}-%{scmrev}.tar.xz
%endif
%endif
Summary: Library to ease explicit vectorization of C++ code
URL: http://code.compeng.uni-frankfurt.de/projects/vc
License: LGPLv3
Group: System/Libraries

%track
prog %{name} = {
	url = http://code.compeng.uni-frankfurt.de/projects/vc/files
	regex = "Vc-(__VER__)\.tar\.gz"
	version = %{version}
}

%description
Vc is a free software library to ease explicit vectorization of C++ code.

It has an intuitive API and provides portability between different
compilers and compiler versions as well as portability between different
vector instruction sets.

Thus an application written with Vc can be compiled for

    AVX
    SSE2 up to SSE4.2
    SSE4a, XOP, and FMA4
    Scalar (fallback which works everywhere)
    LRBni support disabled, waiting for MIC

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Provides: %name-devel

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%if "%{scmrev}" == ""
%setup -q -n Vc-%{version}%{beta}
%else
%setup -q -n Vc
%endif

%build
%cmake
%make

%install
%makeinstall_std -C build

%files -n %{devname}
%_includedir/Vc
%_prefix/lib/cmake/Vc
%_libdir/*.a
