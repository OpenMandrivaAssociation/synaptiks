%define name	synaptiks
%define version	0.8.1
%define release	1
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
