#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	URI
%define	pnam	URI
Summary:	URI - Uniform Resource Identifiers (absolute and relative)
Summary(pl):	URI - obsЁuga ujednoliconych identyfikatorСw zasobСw (bezwzglЙdnych i wzglЙdnych)
Summary(ru):	URI - Uniform Resource Identifier (URI) ссылки, как указывает RFC 2396
Summary(uk):	URI - посилання Uniform Resource Identifier (URI) як визначено в RFC 2396
Name:		perl-URI
Version:	1.23
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
%if %{?_without_test:0}%{!?_without_test:1}
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-libnet
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(Business::ISBN)'

%description
This package contains the URI.pm module with friends. The module
implements the URI class. Objects of this class represent Uniform
Resource Identifier (URI) references as specified in RFC 2396.

%description -l ru
Этот пакет содержит URI.pm и сопутствующие модули. Модуль реализует
Uniform Resource Identifier (URI) ссылки, как указывает RFC 2396.

%description -l pl
Ten pakiet zawiera moduЁ URI dla Perla. SЁu©y on do obrСbki
ujednoliconych identyfikatorСw zasobСw (URI - Uniform Resource
Identifier), zgodnych z RFC 2396.

%description -l pt_BR
MСdulo Perl URI - Este pacote contИm o modulo URI.pm para manipular
"Uniform Resource Identifier" (URI) confirme especificado na RFC 2396.

%description -l uk
Цей пакет м╕стить URI.pm та потр╕бн╕ для нього модул╕. Модуль реал╕зу╓
посилання Uniform Resource Identifier (URI) як зазначено в RFC 2396.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_vendorlib}/URI
%{perl_vendorlib}/*.pm
%{_mandir}/man3/*
