%define plugin	xxvautotimer

# backportability
%define _localstatedir %{_var}

Summary:	VDR plugin: Autotimer for XXV
Name:		vdr-plugin-%plugin
Version:	0.1.2
Release:	15
Group:		Video
License:	GPL
URL:		http://www.vdrtools.de/vdrxxvautotimer.html
Source:		http://www.vdrtools.de/download/vdr-%plugin-%{version}.tar.bz2
Patch0:		xxvautotimer-0.1.2-i18n-1.6.patch
Patch1:		xxvautotimer-includes.patch
Patch2:		xxvautotimer-format-string.patch
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
%patch1 -p1
%patch2 -p1
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
cd %plugin
%vdr_plugin_install

install -d -m755 %{buildroot}%{_bindir}
install -m755 Scripte/* %{buildroot}%{_bindir}

%files -f %plugin/%plugin.vdr
%doc %plugin/README %plugin/HISTORY
%{_bindir}/epg2xxvautotimer.pl


