Name:           perl-Date-Holidays-US
Version:        0.05
Release:        1%{?dist}
Summary:        Date::Holidays Adapter for US Federal holidays
License:        mit
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Date-Holidays-US/
Source0:        http://www.cpan.org/modules/by-module/Date/Date-Holidays-US-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Adapter for Date::Holidays for US Federal holidays back to 1880.

%prep
%setup -q -n Date-Holidays-US-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes LICENSE META.json README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Aug 19 2022 Michael R. Davis <mrdvt92@yahoo.com> 0.01-1
- Specfile autogenerated by cpanspec 1.78.
