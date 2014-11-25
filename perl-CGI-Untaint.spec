#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	CGI
%define		pnam	Untaint
%include	/usr/lib/rpm/macros.perl
Summary:	CGI::Untaint - process CGI input parameters
Summary(pl.UTF-8):	CGI::Untaint - przetwarzanie parametrów wejściowych CGI
Name:		perl-CGI-Untaint
Version:	1.26
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1ed11830476470d4895b632bf2222606
URL:		http://search.cpan.org/dist/CGI-Untaint/
BuildRequires:	perl-UNIVERSAL-require
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a simple, convenient, abstracted and extensible
manner for validating and untainting the input from web forms.

%description -l pl.UTF-8
Ten moduł udostępnia prosty, wygodny, abstrakcyjny i rozszerzalny
sposób na sprawdzanie poprawności i odkażanie wejścia z formularzy
WWW.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc Changes
%{perl_vendorlib}/CGI/*.pm
%{perl_vendorlib}/CGI/Untaint
%{_mandir}/man3/*
