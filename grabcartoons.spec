Summary:	commic-summarizing utility
Summary(pl.UTF-8):   Narzędzie do streszczania komiksów
Name:		grabcartoons
Version:	1.11
Release:	0.1
License:	BSD
Group:		Applications
Source0:	http://dl.sourceforge.net/grabcartoons/%{name}-%{version}.tar.gz
# Source0-md5:	751234c5072bb4a65a8f8d9b1775cc8c
Patch0:		%{name}-DESTDIR.patch
URL:		http://grabcartoons.sourceforge.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GrabCartoons is a comic-summarizing utility. It is modular, and it is
very easy to write modules for new comics.

%description -l pl.UTF-8
GrabCartoons to narzędzie do streszczania komiksów. Jest modularne i
łatwo do niego dopisywać moduły do nowych komiksów.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_prefix}/lib/grabcartoons
