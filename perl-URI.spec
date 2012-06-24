#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	URI
%define		pnam	URI
Summary:	URI - Uniform Resource Identifiers (absolute and relative)
Summary(pl):	URI - obs�uga ujednoliconych identyfikator�w zasob�w (bezwzgl�dnych i wzgl�dnych)
Summary(ru):	URI - Uniform Resource Identifier (URI) ������, ��� ��������� RFC 2396
Summary(uk):	URI - ��������� Uniform Resource Identifier (URI) �� ��������� � RFC 2396
Name:		perl-URI
Version:	1.35
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	1a933b1114c41a25587ee59ba8376f7c
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-MIME-Base64
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(Business::ISBN)'

%description
This package contains the URI.pm module with friends. The module
implements the URI class. Objects of this class represent Uniform
Resource Identifier (URI) references as specified in RFC 2396.

%description -l ru
���� ����� �������� URI.pm � ������������� ������. ������ ���������
Uniform Resource Identifier (URI) ������, ��� ��������� RFC 2396.

%description -l pl
Ten pakiet zawiera modu� URI dla Perla. S�u�y on do obr�bki
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
mv t/heuristic.t{,.blah}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_vendorlib}/URI
%{perl_vendorlib}/*.pm
%{_mandir}/man3/*
