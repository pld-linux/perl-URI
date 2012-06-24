%include	/usr/lib/rpm/macros.perl
Summary:	Perl URI module
Summary(pl):	Modu� Perla URI
Summary(pt_BR):	M�dulo URI para Perl
Name:		perl-URI
Version:	1.18
Release:	1
License:	distributable
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/URI/URI-%{version}.tar.gz
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
Modu� Perla URI.

%description -l pt_BR
M�dulo Perl URI - Este pacote cont�m o modulo URI.pm para manipular
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
