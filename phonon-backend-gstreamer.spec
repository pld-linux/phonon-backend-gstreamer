%define		qtver		4.7.1
%define		kdever		4.5.5

Summary:	GStreamer backend for Phonon
Summary(pl.UTF-8):	Wtyczka GStreamera dla Phonona
Name:		phonon-backend-gstreamer
Version:	4.6.3
Release:	1
License:	LGPL 2.1
Group:		Libraries
Source0:	ftp://ftp.kde.org/pub/kde/stable/phonon/%{name}/%{version}/src/%{name}-%{version}.tar.xz
# Source0-md5:	d7b0b6245f380347c52c09033a814931
#URL:		http://
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	gstreamer0.10-plugins-base-devel
BuildRequires:	kde4-kdebase-workspace-devel >= %{kdever}
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	phonon-devel >= 4.4.4
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Suggests:	gstreamer0.10-pulseaudio
Provides:	qt4-phonon-backend = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GStreamer backend for Phonon.

%description -l pl.UTF-8
Wtyczka GStreamera dla Phonona.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/plugins/phonon_backend/phonon_gstreamer.so
%{_datadir}/kde4/services/phononbackends/gstreamer.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*/apps/*.svgz
