#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	CGI
%define	pnam	Untaint
Summary:	CGI::Untaint - process CGI input parameters
Summary(pl):	CGI::Untaint - przetwarzanie parametrów wej¶ciowych CGI
Name:		perl-CGI-Untaint
Version:	1.00
Release:	1
# Same as Perl itself
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	02b38ef8bcdf1731ef7836503ea6f1da
BuildRequires:	perl-UNIVERSAL-exports
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a simple, convenient, abstracted and extensible
manner for validating and untainting the input from web forms.

%description -l pl
Ten modu³ udostêpnia prosty, wygodny, abstrakcyjny i rozszerzalny
sposób na sprawdzanie poprawno¶ci i odka¿anie wej¶cia z formularzy
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
