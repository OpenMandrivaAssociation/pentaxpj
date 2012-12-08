Summary:	Pentax PocketJet Printer Driver
Name:		pentaxpj
Version:	1.0.0
Release:	%mkrel 11
License:	GPL
Group:		System/Printing
URL:		http://www.pragana.net/gdiprinters.html
Source0:	http://www.pragana.net/%{name}-%{version}.tar.gz
Patch0:		pentaxpj-glibc28_fix.diff
Patch1:		pentaxpj-1.0.0-LDFLAGS.diff
Conflicts:	printer-utils = 2007
Conflicts:	printer-filters = 2007
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Pentax PocketJet Printer Driver for the families:

 o PocketJet II
 o PocketJet 200.

%prep

%setup -q -n %{name}
%patch0 -p0
%patch1 -p0

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS`  `find . -type d -name .svn` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done
    
%build

%make CFLAGS="%{optflags} -DLONG_FORM_FEED" LDFLAGS="%{ldflags}"

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_libdir}/pentaxpj
install -d %{buildroot}%{_sysconfdir}

cp -a BWidget-1.3.1 pentaxpj pentaxsetup pentax.xpm test-page.ps.gz %{buildroot}%{_libdir}/pentaxpj
ln -s %{_libdir}/pentaxpj/pentaxsetup %{buildroot}%{_sbindir}
ln -s %{_libdir}/pentaxpj/pentaxpj %{buildroot}%{_bindir}
cat > %{buildroot}%{_sysconfdir}/pentaxpj.conf <<EOF
#
set settings(driverpath) %{_libdir}/pentaxpj
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc README
%{_libdir}/pentaxpj
%config(noreplace) %{_sysconfdir}/pentaxpj.conf
%defattr(0755,root,root,0755)
%{_bindir}/pentaxpj
%{_sbindir}/pentaxsetup


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-11mdv2011.0
+ Revision: 667019
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-10mdv2011.0
+ Revision: 607087
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-9mdv2010.1
+ Revision: 521157
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.0-8mdv2010.0
+ Revision: 426404
- rebuild

* Mon Dec 29 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-7mdv2009.1
+ Revision: 321043
- use %%ldflags

* Fri Jul 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-6mdv2009.0
+ Revision: 231719
- added P0 to make it build

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-4mdv2008.1
+ Revision: 179162
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-3mdv2008.0
+ Revision: 75353
- fix deps (pixel)

* Thu Aug 16 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-2mdv2008.0
+ Revision: 64172
- use the new System/Printing RPM GROUP

* Mon Aug 13 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-1mdv2008.0
+ Revision: 62418
- Import pentaxpj



* Mon Aug 13 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-1mdv2008.0
- initial Mandriva package

* Thu Jan 15 2004 Marcelo Ricardo Leitner <mrl@conectiva.com.br>
+ 2004-01-15 16:21:38 (44870)
- Fixed Source tag.

* Thu Jan 15 2004 Marcelo Ricardo Leitner <mrl@conectiva.com.br>
+ 2004-01-15 16:18:59 (44869)
- New upstream: 1.0.0
- Fixed execute permissions at %%{_libdir}

* Thu Aug 29 2002 Gustavo Niemeyer <niemeyer@conectiva.com>
+ 2002-08-29 18:37:11 (9040)
- Imported package from 8.0.
