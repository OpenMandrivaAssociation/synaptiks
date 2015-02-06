%define name	synaptiks
%define version	0.8.1
%define release	2
%define Summary	Touchpad service for KDE 4

Summary:	%Summary
Name:		%name
Version:	%version
Release:	%release
Source0:	http://pypi.python.org/packages/source/s/synaptiks/%name-%version.tar.bz2
License:	BSD
Group:		System/Configuration/Hardware
URL:		http://synaptiks.lunaryorn.de/
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	kdelibs4-core
BuildRequires:	kde4-macros
BuildRequires:	kdesdk4-scripts
Obsoletes:	%{name} < %{version}
Requires:	python-kde4
Requires:	pyudev

%description
Synaptiks is a touchpad management service for KDE. It provides a simple
configuration interface and can automatically switch off your touchpad
on keyboard activity or if mouse devices are plugged.

%files -f %{name}.lang
%defattr(-,root,root)
%{_sysconfdir}/xdg/autostart/synaptiks_init_config.desktop
%{_bindir}/*
%{py_puresitedir}/*
%{_datadir}/applications/kde4/*.desktop
%{_kde_services}/*.desktop
%{_datadir}/autostart/*.desktop
%{_kde_appsdir}/%name
%{_iconsdir}/hicolor/*/*/*
#---------------------------------------------------------------------
%prep
%setup -q 

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%find_lang %{name} --with-html


%changelog
* Mon Mar 26 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.8.1-1
+ Revision: 787075
- version update 0.8.1

* Sun Apr 24 2011 Funda Wang <fwang@mandriva.org> 0.6.1-1
+ Revision: 658340
- obsoletes old package
- New version 0.6.1 (python based)

* Sun Oct 10 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 0.4.0-2mdv2011.0
+ Revision: 584611
- patch0: cherry pick two fingers emulation support from SVN

* Sun Apr 11 2010 John Balcaen <mikala@mandriva.org> 0.4.0-1mdv2010.1
+ Revision: 533591
- Fix files list
- Update to 0.4.0

* Wed Mar 03 2010 John Balcaen <mikala@mandriva.org> 0.3.2-2mdv2010.1
+ Revision: 513971
- Enable Xinput2 support

* Tue Mar 02 2010 John Balcaen <mikala@mandriva.org> 0.3.2-1mdv2010.1
+ Revision: 513456
- import synaptiks

