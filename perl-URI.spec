%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	Perl URI module
Summary(pl):	Modu³ Perla URI
Name:		perl-URI
Version:	1.03
Release:	0.1
Copyright:	distributable
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/URI-%{version}.tar.gz
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Perl URI module.

%description -l pl
Modu³ Perla URI.

%prep
%setup -q -n URI-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{perl_sitearch} \
	$RPM_BUILD_ROOT%{_mandir}/man3 \
	$RPM_BUILD_ROOT/%{perl_archlib}

make \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	INSTALLMAN3DIR=$RPM_BUILD_ROOT%{_mandir}/man3 \
	install

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/URI/
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/URI
%{perl_sitelib}/*.pm

%dir %{perl_sitearch}/auto/URI

%{perl_sitearch}/auto/*/.packlist

%{_mandir}/man3/*
