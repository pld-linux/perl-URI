%include	/usr/lib/rpm/macros.perl
%define		pdir	URI
%define		pnam	URI
Summary:	Perl URI module
Summary(pl):	Modu� Perla URI
Summary(pt_BR):	M�dulo URI para Perl
Summary(ru):	URI - Uniform Resource Identifier (URI) ������, ��� ��������� RFC 2396
Summary(uk):	URI - ��������� Uniform Resource Identifier (URI) �� ��������� � RFC 2396
Name:		perl-URI
Version:	1.19
Release:	2
License:	distributable
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-libnet
BuildRequires:	rpm-perlprov >= 3.0.3-18
Requires:	perl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the URI.pm module with friends. The module
implements the URI class. Objects of this class represent Uniform
Resource Identifier (URI) references as specified in RFC 2396.

%description -l ru
���� ����� �������� URI.pm � ������������� ������. ������ ���������
Uniform Resource Identifier (URI) ������, ��� ��������� RFC 2396.

%description -l pl
Pakiet ten zawiera modu� URI dla Perla. S�u�y on do obr�bki
ujednoliconych identyfikator�w zasob�w (URI - Uniform Resource
Identifier), zgodnych z RFC 2396.

%description -l pt_BR
M�dulo Perl URI - Este pacote cont�m o modulo URI.pm para manipular
"Uniform Resource Identifier" (URI) confirme especificado na RFC 2396.

%description -l uk
��� ����� ͦ����� URI.pm �� ���Ҧ�Φ ��� ����� ����̦. ������ ���̦�դ
��������� Uniform Resource Identifier (URI) �� ��������� � RFC 2396.

%prep
%setup -q -n %{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_sitelib}/URI
%{perl_sitelib}/*.pm
%{_mandir}/man3/*
