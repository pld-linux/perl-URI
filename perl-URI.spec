%include	/usr/lib/rpm/macros.perl
Summary:	Perl URI module
Summary(pl):	Modu³ Perla URI
Summary(pt_BR):	Módulo URI para Perl
Name:		perl-URI
Version:	1.18
Release:	2
License:	distributable
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/URI/URI-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-libnet
Requires:	perl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl module URI - This package contains the URI.pm module to
manipulate Uniform Resource Identifier (URI) from RFC 2396.

%description -l pl
Modu³ Perla URI.

%description -l pt_BR
Módulo Perl URI - Este pacote contém o modulo URI.pm para manipular
"Uniform Resource Identifier" (URI) confirme especificado na RFC 2396.

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
