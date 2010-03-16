Summary:	Pentax PocketJet Printer Driver
Name:		pentaxpj
Version:	1.0.0
Release:	%mkrel 9
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
