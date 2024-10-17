%define name    flemm
%define version 3.1
%define release 11

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    Inflectional analysis on French texts
License:    GPL
Group:      Sciences/Computer science
URL:        https://www.univ-nancy2.fr/pers/namer/Telecharger_Flemm.htm
Source:     %{name}-%{version}.tar.bz2
Patch0:     %{name}.perl-modules-path.patch.bz2
Patch1:     %{name}-3.1.stdin.patch.bz2
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
FLEMM is a Perl5 program that performs inflectional analysis on French texts
which have previously been tagged (eg. by the Brill tagger). This is a small
program, (60kb in a zipped format) mainly rule-based (i.e. only a 3000 words
lexicon is used in order to deal with exceptions). It runs on PCs or
Workstation, under Unix, Linux or Windows95/NT OS.

The returned Flemm result objects are likely to be displayed as
XML structures.

%prep
%setup -q
%patch0
%patch1
perl -pi -e 'tr/\r//d' LISMOI.txt tests/agatha.bll
chmod 755 *.pl

%build

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_bindir}
install -m 755 flemm.pl %{buildroot}%{_bindir}/flemm.pl

install -d -m 755 %{buildroot}%{_datadir}/%{name}
install -m 644 Flemm.pm %{buildroot}%{_datadir}/%{name}
cp -pr Flemm %{buildroot}%{_datadir}/%{name}
cp -pr EXCEP %{buildroot}%{_datadir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENCE.txt README.txt LISMOI.txt tests flem_ex?.pl
%{_bindir}/flemm.pl
%{_datadir}/%{name}



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 3.1-10mdv2011.0
+ Revision: 618306
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 3.1-9mdv2010.0
+ Revision: 428797
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 3.1-8mdv2009.0
+ Revision: 245198
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.1-6mdv2008.1
+ Revision: 132425
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import flemm


* Fri Aug 25 2006 Guillaume Rousse <guillomovitch@mandriva.org> 3.1-5mdv2007.0
- %%mkrel

* Fri Aug 19 2005 Guillaume Rousse <guillomovitch@mandriva.org> 3.1-4mdk
- rebuild
- spec cleanup
- fix doc files encoding and perms

* Fri Aug 06 2004 Guillaume Rousse <guillomovitch@mandrake.org> 3.1-3mdk 
- stdin/stdout patch

* Wed Jul 21 2004 Guillaume Rousse <guillomovitch@mandrake.org> 3.1-2mdk 
- rebuild

* Tue Apr 13 2004 Guillaume Rousse <guillomovitch@mandrake.org> 3.1-1mdk
- new version

* Thu Jan 08 2004 Guillaume Rousse <guillomovitch@mandrake.org> 2-1mdk
- first mdk release
