#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	URI
%define		pnam	URI
Summary:	URI - Uniform Resource Identifiers (absolute and relative)
Summary(pl.UTF-8):	URI - obsługa ujednoliconych identyfikatorów zasobów (bezwzględnych i względnych)
Summary(ru.UTF-8):	URI - Uniform Resource Identifier (URI) ссылки, как указывает RFC 2396
Summary(uk.UTF-8):	URI - посилання Uniform Resource Identifier (URI) як визначено в RFC 2396
Name:		perl-URI
Version:	5.21
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/URI/%{pnam}-%{version}.tar.gz
# Source0-md5:	9b45e7635f0968deabe377fc4c99a8b5
URL:		https://metacpan.org/release/URI
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl(Exporter) >= 5.57
BuildRequires:	perl(Net::Domain)
BuildRequires:	perl-Encode
BuildRequires:	perl-MIME-Base64 >= 2
BuildRequires:	perl-Scalar-List-Utils
BuildRequires:	perl-Test-Needs
BuildRequires:	perl-Test-Simple >= 0.96
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the URI.pm module with friends. The module
implements the URI class. Objects of this class represent Uniform
Resource Identifier (URI) references as specified in RFC 2396.

%description -l ru.UTF-8
Этот пакет содержит URI.pm и сопутствующие модули. Модуль реализует
Uniform Resource Identifier (URI) ссылки, как указывает RFC 2396.

%description -l pl.UTF-8
Ten pakiet zawiera moduł URI dla Perla. Służy on do obróbki
ujednoliconych identyfikatorów zasobów (URI - Uniform Resource
Identifier), zgodnych z RFC 2396.

%description -l pt_BR.UTF-8
Módulo Perl URI - Este pacote contém o modulo URI.pm para manipular
"Uniform Resource Identifier" (URI) confirme especificado na RFC 2396.

%description -l uk.UTF-8
Цей пакет містить URI.pm та потрібні для нього модулі. Модуль реалізує
посилання Uniform Resource Identifier (URI) як зазначено в RFC 2396.

%prep
%setup -q -n %{pnam}-%{version}
%{__mv} t/heuristic.t{,.blah}

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
%doc Changes README
%{perl_vendorlib}/URI
%{perl_vendorlib}/URI.pm
%{_mandir}/man3/URI*.3pm*
