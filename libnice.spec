Summary:	The GLib ICE implementation
Name:		libnice
Version:	0.1.10
Release:	1
License:	LGPL v2 and MPL v1.1
Group:		Libraries
Source0:	http://nice.freedesktop.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	27b62d0093ce29a39df1c6fcf0bb4396
URL:		http://nice.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	gnutls-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gssdp-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	gstreamer010-plugins-base-devel
BuildRequires:	gtk-doc
BuildRequires:	gupnp-igd-devel
BuildRequires:	libsoup-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libnice is an implementation of the IETF's draft Interactive
Connectivity Establishment standard (ICE). It provides GLib-based
library and GStreamer elements.

ICE is useful for applications that want to establish peer-to-peer UDP
data streams. It automates the process of traversing NATs and provides
security against some attacks.

Existing standards that use ICE include the Session Initiation
Protocol (SIP) and Jingle, XMPP extension for audio/video calls.

%package devel
Summary:	Header files for libnice library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libnice library.

%package apidocs
Summary:	libnice library API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libnice library API documentation.

%package -n gstreamer-nice
Summary:	Nice plguin for gstreamer
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n gstreamer-nice
Nice plugin fofr gstreamer.

%prep
%setup -q

%build
%{__libtoolize}
%{__gtkdocize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--with-gstreamer-0.10=no	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/{,gstreamer*/}*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/stunbdc
%attr(755,root,root) %{_bindir}/stund
%attr(755,root,root) %ghost %{_libdir}/libnice.so.??
%attr(755,root,root) %{_libdir}/libnice.so.*.*.*
%{_libdir}/girepository-1.0/Nice-0.1.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnice.so
%{_includedir}/nice
%{_includedir}/stun
%{_pkgconfigdir}/nice.pc
%{_datadir}/gir-1.0/Nice-0.1.gir

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libnice

%files -n gstreamer-nice
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gstreamer-1.0/libgstnice.so

