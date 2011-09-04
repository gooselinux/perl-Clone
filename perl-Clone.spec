Name:           perl-Clone
Version:        0.31
Release:        3.1%{?dist}
Summary:        Recursively copy perl datatypes
Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Clone
Source0:        http://search.cpan.org/CPAN/authors/id/R/RD/RDF/Clone-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	perl(ExtUtils::ParseXS), perl(Taint::Runtime), perl(Test::More)
Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# don't "provide" private Perl libs
%global _use_internal_dependency_generator 0
%global __deploop() while read FILE; do /usr/lib/rpm/rpmdeps -%{1} ${FILE}; done | /bin/sort -u
%global __find_provides /bin/sh -c "%{__grep} -v '%_docdir' | %{__grep} -v '%{perl_vendorarch}/.*\\.so$' | %{__deploop P}"
%global __find_requires /bin/sh -c "%{__grep} -v '%_docdir' | %{__deploop R}"

%description
This module provides a clone() method which makes recursive
copies of nested hash, array, scalar and reference types,
including tied variables and objects.

clone() takes a scalar argument and an optional parameter that
can be used to limit the depth of the copy. To duplicate lists,
arrays or hashes, pass them in by reference.

%prep
%setup -q -n Clone-%{version}
find . -type f -exec chmod -c -x {} ';'

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes
%{perl_vendorarch}/auto/Clone/
%{perl_vendorarch}/Clone.pm
%{_mandir}/man3/*.3*


%changelog
* Thu Dec 03 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.31-3.1
- Rebuilt for RHEL 6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Chris Weyl <cweyl@alumni.drew.edu> - 0.31-2
- filter private Perl solibs from provides
- remove some executable bits -- keep rpmlint happy

* Fri Mar 13 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.31-1
- update to 0.31

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.28-4
- Rebuild for perl 5.10 (again)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.28-3
- Autorebuild for GCC 4.3

* Fri Jan 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.28-2
- rebuild for new perl

* Wed Nov 28 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.28-1
- bump to 0.28

* Fri Aug 24 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.27-2
- license fix

* Fri Jul 27 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.27-1
- bump to 0.27

* Wed Jan 17 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.22-1
- bump to 0.22

* Fri Sep 15 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.20-2
- bump for fc6

* Fri Mar 31 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.20-1
- bump to 0.20
- new BR: perl-Taint-Runtime

* Tue Feb 28 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.18-3
- bump for FC-5

* Fri Jan  6 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.18-2
- don't pass optflags twice
- remove .bs files

* Thu Jan  5 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.18-1
- Initial package for Fedora Extras
