%include	/usr/lib/rpm/macros.perl
Summary:	Perl URI module
Summary(pl):	Modu³ Perla URI
Name:		perl-URI
Version:	1.12
Release:	2
License:	Distributable
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/URI/URI-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl >= 5.6
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-libnet
Requires:	perl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl URI module.

%description -l pl
Modu³ Perla URI.

%prep
%setup -q -n URI-%{version}

%build
perl Makefile.PL
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README Changes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/URI
%{perl_sitelib}/*.pm
%{_mandir}/man3/*
