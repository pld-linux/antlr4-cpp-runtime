Summary:	C run-time support for ANTLR-generated parsers
Summary(pl.UTF-8):	Biblioteka uruchomieniowa C wspomagająca analizatory wygenerowane przez ANTLR
Name:		antlr4-cpp-runtime
Version:	4.13.1
Release:	1
License:	BSD
Group:		Libraries
Source0:	https://www.antlr.org/download/%{name}-%{version}-source.zip
# Source0-md5:	c875c148991aacd043f733827644a76f
URL:		http://www.antlr.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C run-time support for ANTLR-generated parsers.

%description -l pl.UTF-8
Biblioteka uruchomieniowa C wspomagająca analizatory wygenerowane
przez ANTLR.

%package devel
Summary:	Header files for the C bindings for ANTLR-generated parsers
Summary(pl.UTF-8):	Pliki nagłówkowe wiązań C analizatorów wygenerowanych przez ANTLR
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for the C bindings for ANTLR-generated parsers

%description devel -l pl.UTF-8
Pliki nagłówkowe wiązań C analizatorów wygenerowanych przez ANTLR.

%package static
Summary:	Static libantlr3c library
Summary(pl.UTF-8):	Statyczna biblioteka libantlr3c
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libantlr4-runtime library.

%description static -l pl.UTF-8
Statyczna biblioteka libantlr4-runtime.

%prep
%setup -q -c

%build
mkdir -p build
cd build
%cmake ../ \
	-DANTLR_BUILD_CPP_TESTS:BOOL=OFF

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libantlr4

%clean
rm -rf $RPM_BUILD_ROOT

# even there's no SONAME symlink, run ldconfig to get library into ld.so.cache
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.md
%attr(755,root,root) %{_libdir}/libantlr4-runtime.so.4.13.1

%files devel
%defattr(644,root,root,755)
%{_libdir}/libantlr4-runtime.so
%{_includedir}/antlr4-runtime

%files static
%defattr(644,root,root,755)
%{_libdir}/libantlr4-runtime.a
