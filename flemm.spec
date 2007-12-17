%define name    flemm
%define version 3.1
%define release %mkrel 5

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    Inflectional analysis on French texts
License:    GPL
Group:      Sciences/Computer science
URL:        http://www.univ-nancy2.fr/pers/namer/Telecharger_Flemm.htm
Source:     %{name}-%{version}.tar.bz2
Patch0:     %{name}.perl-modules-path.patch.bz2
Patch1:     %{name}-3.1.stdin.patch.bz2
BuildArch:  noarch

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

