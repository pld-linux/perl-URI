%include	/usr/lib/rpm/macros.perl
Summary:	Perl URI module
Summary(pl):	Modu³ Perla URI
Name:		perl-URI
Version:	1.05
Release:	1
Copyright:	distributable
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/URI/URI-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-libnet
Requires:	perl
Requires:	%{perl_sitearch}
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

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/URI/
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
	README Changes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,Changes}.gz
%{perl_sitelib}/URI
%{perl_sitelib}/*.pm

%dir %{perl_sitearch}/auto/URI

%{perl_sitearch}/auto/URI/.packlist

%{_mandir}/man3/*
