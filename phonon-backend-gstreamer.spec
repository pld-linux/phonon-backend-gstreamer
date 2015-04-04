#
# Conditional build:
%bcond_without	qt4	# Qt4 Phonon module
%bcond_without	qt5	# Qt5 Phonon (Phonon4Qt5) module

%define		phonon_ver	4.7.0
%define		qt4_ver		4.7.1
%define		qt5_ver		5.0.0

Summary:	GStreamer backend for Phonon
Summary(pl.UTF-8):	Wtyczka GStreamera dla Phonona
Name:		phonon-backend-gstreamer
Version:	4.8.2
Release:	4
License:	LGPL 2.1
Group:		Libraries
Source0:	ftp://ftp.kde.org/pub/kde/stable/phonon/phonon-backend-gstreamer/%{version}/src/%{name}-%{version}.tar.xz
# Source0-md5:	ce441035dc5a00ffaac9a64518ab5c62
BuildRequires:	OpenGL-devel
BuildRequires:	cmake >= 2.8.6
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gstreamer-devel >= 1.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0
BuildRequires:	libxml2-devel >= 2
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	sed >= 4.0
%if %{with qt4}
BuildRequires:	QtCore-devel >= %{qt4_ver}
BuildRequires:	QtGui-devel >= %{qt4_ver}
BuildRequires:	QtOpenGL-devel >= %{qt4_ver}
BuildRequires:	phonon-devel >= %{phonon_ver}
BuildRequires:	qt4-build >= %{qt4_ver}
BuildRequires:	qt4-qmake >= %{qt4_ver}
%endif
%if %{with qt5}
BuildRequires:	Qt5Core-devel >= %{qt5_ver}
BuildRequires:	Qt5Gui-devel >= %{qt5_ver}
BuildRequires:	Qt5OpenGL-devel >= %{qt5_ver}
BuildRequires:	Qt5Widgets-devel >= %{qt5_ver}
BuildRequires:	phonon-qt5-devel >= %{phonon_ver}
BuildRequires:	qt5-build >= %{qt5_ver}
BuildRequires:	qt5-qmake >= %{qt5_ver}
%endif
Requires:	phonon >= %{phonon_ver}
Suggests:	gstreamer-pulseaudio >= 1.0
Provides:	qt4-phonon-backend = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GStreamer backend for Phonon.

%description -l pl.UTF-8
Wtyczka GStreamera dla Phonona.

%package -n phonon-qt5-backend-gstreamer
Summary:	GStreamer backend for Qt5 Phonon
Summary(pl.UTF-8):	Wtyczka GStreamera dla Phonona opartego na Qt5
Group:		Libraries
Requires:	phonon-qt5 >= %{phonon_ver}
Suggests:	gstreamer-pulseaudio >= 1.0
Provides:	qt5-phonon-backend = %{version}

%description -n phonon-qt5-backend-gstreamer
GStreamer backend for Qt5 Phonon.

%description -n phonon-qt5-backend-gstreamer -l pl.UTF-8
Wtyczka GStreamera dla Phonona opartego na Qt5.

%prep
%setup -q

# Use PHONON_NO_GRAPHICSVIEW because videographicsobject.cpp is not ready for gstreamer 1.0;
# as of 4.8.2, this setting is not exported as option, so hardcode it.
sed -i -e "15i set(PHONON_NO_GRAPHICSVIEW ON)" gstreamer/CMakeLists.txt

%build
%if %{with qt4}
install -d build-qt4
cd build-qt4
%cmake -DPHONON_NO_GRAPHICSVIEW=ON ..
%{__make}
cd ..
%endif

%if %{with qt5}
install -d build-qt5
cd build-qt5
%cmake .. \
	-DPHONON_BUILD_PHONON4QT5=ON
%{__make}
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with qt4}
%{__make} -C build-qt4 install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%if %{with qt5}
%{__make} -C build-qt5 install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with qt4}
%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/plugins/phonon_backend/phonon_gstreamer.so
%{_datadir}/kde4/services/phononbackends/gstreamer.desktop
%{_iconsdir}/hicolor/*x*/apps/phonon-gstreamer.png
%{_iconsdir}/hicolor/scalable/apps/phonon-gstreamer.svgz
%endif

%if %{with qt5}
%files -n phonon-qt5-backend-gstreamer
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt5/plugins/phonon4qt5_backend/phonon_gstreamer.so
%endif
