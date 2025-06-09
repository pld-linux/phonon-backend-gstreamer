%define		phonon_ver	4.7.0
%define		qt_ver		4.7.1

Summary:	GStreamer backend for Phonon
Summary(pl.UTF-8):	Wtyczka GStreamera dla Phonona
Name:		phonon-backend-gstreamer
# 4.9.x is the last supporting qt4 phonon
Version:	4.9.1
Release:	1
License:	LGPL 2.1
Group:		Libraries
Source0:	https://download.kde.org/Attic/phonon/phonon-backend-gstreamer/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	b521b0a824e4d5451e476b8127140f60
BuildRequires:	OpenGL-devel
BuildRequires:	QtCore-devel >= %{qt_ver}
BuildRequires:	QtGui-devel >= %{qt_ver}
BuildRequires:	QtOpenGL-devel >= %{qt_ver}
BuildRequires:	cmake >= 2.8.9
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gstreamer-devel >= 1.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0
BuildRequires:	libxml2-devel >= 2
BuildRequires:	phonon-devel >= %{phonon_ver}
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= %{qt_ver}
BuildRequires:	qt4-qmake >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	phonon >= %{phonon_ver}
Suggests:	gstreamer-pulseaudio >= 1.0
Provides:	qt4-phonon-backend = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GStreamer backend for Phonon.

%description -l pl.UTF-8
Wtyczka GStreamera dla Phonona.

%prep
%setup -q -n phonon-gstreamer-%{version}

# Use PHONON_NO_GRAPHICSVIEW because videographicsobject.cpp is not ready for gstreamer 1.0;
# as of 4.8.2, this setting is not exported as option, so hardcode it.
sed -i -e "15i set(PHONON_NO_GRAPHICSVIEW ON)" gstreamer/CMakeLists.txt

%build
install -d build-qt4
cd build-qt4
%cmake ..
%{__make}
cd ..

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build-qt4 install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/plugins/phonon_backend/phonon_gstreamer.so
%{_datadir}/kde4/services/phononbackends/gstreamer.desktop
%{_iconsdir}/hicolor/*x*/apps/phonon-gstreamer.png
%{_iconsdir}/hicolor/scalable/apps/phonon-gstreamer.svgz
