
%define plugin	xxvautotimer
%define name	vdr-plugin-%plugin
%define version	0.1.2
%define rel	13

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
%defattr(-,root,root)
%doc %plugin/README %plugin/HISTORY
%{_bindir}/epg2xxvautotimer.pl


%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.1.2-12mdv2010.0
+ Revision: 401088
- rebuild for new VDR
- add another missing include (update includes.patch)

* Sat Mar 21 2009 Anssi Hannula <anssi@mandriva.org> 0.1.2-11mdv2009.1
+ Revision: 359801
- fix includes (includes.patch)
- fix format strings (format-string.patch)
- rebuild for new vdr
- define %%_localstatedir locally for backportability

  + Funda Wang <fwang@mandriva.org>
    - rebuild for new mysql

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt against mysql-5.1.30 libs

  + Pixel <pixel@mandriva.com>
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.1.2-8mdv2009.0
+ Revision: 198000
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.1.2-7mdv2009.0
+ Revision: 197745
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.1.2-6mdv2008.1
+ Revision: 145268
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.1.2-5mdv2008.1
+ Revision: 103252
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.1.2-4mdv2008.0
+ Revision: 50064
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.1.2-3mdv2008.0
+ Revision: 42147
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.1.2-2mdv2008.0
+ Revision: 22726
- rebuild for new vdr

* Sat Apr 21 2007 Anssi Hannula <anssi@mandriva.org> 0.1.2-1mdv2008.0
+ Revision: 16469
- initial Mandriva release

