
%define plugin	xxvautotimer
%define name	vdr-plugin-%plugin
%define version	0.1.2
%define rel	8

# backportability
%define _localstatedir %{_var}

Summary:	VDR plugin: Autotimer for XXV
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.vdrtools.de/vdrxxvautotimer.html
Source:		http://www.vdrtools.de/download/vdr-%plugin-%version.tar.bz2
Patch0:		xxvautotimer-0.1.2-i18n-1.6.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
BuildRequires:	mysql-devel
Requires:	vdr-abi = %vdr_abi
Requires:       xxv

%description
This is a plugin for the Video Disk Recorder (VDR) to edit
Autotimers of XXV via VDR on-screen-display (OSD).

%prep
%setup -q -c
cd %plugin
%patch0 -p1
%vdr_plugin_prep

%vdr_plugin_params_begin %plugin
# xxv configuration file
var=XXVD_CFG
param=--xxvconfigfile=XXVD_CFG
default=%{_localstatedir}/lib/xxv/xxvd.cfg
%vdr_plugin_params_end

%build
cd %plugin
%vdr_plugin_build

%install
rm -rf %{buildroot}
cd %plugin
%vdr_plugin_install

install -d -m755 %{buildroot}%{_bindir}
install -m755 Scripte/* %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin/%plugin.vdr
%defattr(-,root,root)
%doc %plugin/README %plugin/HISTORY
%{_bindir}/epg2xxvautotimer.pl
