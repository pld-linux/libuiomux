Summary:	UIOMux - conflict manager for system resources, including UIO devices
Summary(pl.UTF-8):	UIOMux - zarządca konfliktów dla zasobów systemowych, w tym urządzeń UIO
Name:		libuiomux
Version:	1.6.0
Release:	1
License:	LGPL v2+
Group:		Libraries
# trailing /%{name}-%{version}.tar.gz is a hack for df
Source0:	https://oss.renesas.com/modules/document/gate.php/?way=attach&refer=libuiomux&openfile=%{name}-%{version}.tar.gz/%{name}-%{version}.tar.gz
# Source0-md5:	9a4f5025d4cabf40e9a261a978153cdc
URL:		https://oss.renesas.com/modules/document/?libuiomux
BuildRequires:	doxygen
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UIOMux is a conflict manager for system resources, including UIO
devices.

%description -l pl.UTF-8
UIOMux to zarządca konfliktów dla zasobów systemowych, w tym urządzeń
UIO.

%package devel
Summary:	Header files for UIOMux library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki UIOMux
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for UIOMux library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki UIOMux.

%package static
Summary:	Static UIOMux library
Summary(pl.UTF-8):	Statyczna biblioteka UIOMux
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static UIOMux library.

%description static -l pl.UTF-8
Statyczna biblioteka UIOMux.

%package apidocs
Summary:	UIOMux API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki UIOMux
Group:		Documentation

%description apidocs
API and internal documentation for UIOMux library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki UIOMux.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkgconfig
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libuiomux.la
# HTML packaged in -apidocs
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libuiomux

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/uiomux
%attr(755,root,root) %{_libdir}/libuiomux.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libuiomux.so.1
%{_mandir}/man1/uiomux.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libuiomux.so
%{_includedir}/uiomux
%{_pkgconfigdir}/uiomux.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libuiomux.a

%files apidocs
%defattr(644,root,root,755)
%doc doc/libuiomux/html/*
