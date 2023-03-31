%define debug_package %nil
%define major 0
%define beta %{nil}
%define scmrev %{nil}
%define devname %mklibname vc -d -s

# static only
%define _disable_lto 1

Name: vc
Version:	1.4.3
%if "%{beta}" == ""
%if "%{scmrev}" == ""
Release:	2
Source0: https://github.com/VcDevel/Vc/archive/%{version}.tar.gz
%else
Release:	2
Source0: %{name}-%{scmrev}.tar.xz
%endif
%else
%if "%{scmrev}" == ""
Release:	2
Source0: %{name}-%{version}%{beta}.tar.bz2
%else
Release:	2
Source0: %{name}-%{scmrev}.tar.xz
%endif
%endif
Patch0: Vc-1.2.0-x86_32.patch
Patch1: vc-1.4.2-dont-explicitly-disable-vc-instructions.patch
BuildRequires: cmake ninja
Summary: Library to ease explicit vectorization of C++ code
URL: https://github.com/VcDevel/Vc
License: LGPLv3
Group: System/Libraries

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
%autosetup -p1 -n Vc-%{version}%{beta}
%else
%autosetup -p1 -n Vc
%endif
%cmake -DBUILD_TESTING=OFF -DUSE_LIBC++:BOOL=OFF -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{devname}
%_includedir/Vc
%_libdir/cmake/Vc
%_libdir/*.a
