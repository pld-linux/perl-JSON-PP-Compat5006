#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	JSON
%define		pnam	PP-Compat5006
Summary:	JSON::PP::Compat5006 - Helper module in using JSON::PP in Perl 5.6
Name:		perl-JSON-PP-Compat5006
Version:	1.09
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/JSON/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b6a67ab02e8da76ba718b2464bb5fbd5
URL:		http://search.cpan.org/dist/JSON-PP-Compat5006/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JSON::PP calls internally.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/JSON/PP/*.pm
%{_mandir}/man3/*
