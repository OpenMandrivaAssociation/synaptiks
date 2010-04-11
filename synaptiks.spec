%define name	synaptiks
%define version	0.4.0
%define release	%mkrel 1
%define Summary	Touchpad service for KDE 4


Summary:	%Summary
Name:		%name
Version:	%version
Release:	%release
Source0:	%name-%version.tar.bz2
License:	BSD
Group:		System/Configuration/Hardware
URL:		http://synaptiks.lunaryorn.de/
BuildRequires:	kdelibs4-devel


%description
Synaptiks is a touchpad management service for KDE. It provides a simple
configuration interface and can automatically switch off your touchpad
on keyboard activity or if mouse devices are plugged.


%files -f %{name}.lang
%defattr(-,root,root)
%_kde_libdir/kde4/kcm_synaptiks.so
%_kde_libdir/kde4/kded_synaptiks.so
%_kde_libdir/kde4/plasma_applet_synaptiks.so
%_kde_datadir/apps/%{name}/
%_kde_datadir/config.kcfg/plasma-applet-synaptiks.kcfg
%_kde_datadir/config.kcfg/synaptiks.kcfg
%_kde_datadir/dbus-1/interfaces/org.kde.Synaptiks.xml
%_kde_datadir/dbus-1/interfaces/org.kde.TouchpadManager.xml
%_kde_datadir/dbus-1/interfaces/org.kde.MouseDevicesMonitor.xml
%_kde_datadir/dbus-1/interfaces/org.kde.Touchpad.xml
%_kde_iconsdir/hicolor/scalable/apps/synaptiks.svgz
%_kde_services/kded/%{name}.desktop
%_kde_services/plasma-applet-synaptiks.desktop
%_kde_services/%{name}.desktop



#---------------------------------------------------------------------

%prep
%setup -q 

%build
%cmake_kde4 -DHAVE_XINPUT2=ON 
%make

%install
%__rm -rf %buildroot
%makeinstall_std -C build

%find_lang %{name} --with-html

%clean
%__rm -rf %buildroot
 
