Summary:	TkInfo - a browser for info files
Summary(pl.UTF-8):   TkInfo - przeglądarka plików info
Name:		tkinfo
Version:	2.8
Release:	0.1
Epoch:		0
License:	The program itself BSD, the man page and icon GPL
Group:		Applications/System
Source0:	http://math-www.uni-paderborn.de/~axel/tkinfo/%{name}-%{version}.tar.gz
# Source0-md5:	ba798b5e38409b9461bd225646dfe651
Source1:	%{name}.desktop
URL:		http://math-www.uni-paderborn.de/~axel/tkinfo/
Requires:	tk >= 4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A graphical Tcl/Tk-based browser for documentation in the info
hypertext format which is used by the GNU project. Can also be
embedded into other Tcl/Tk programs.

%description -l pl.UTF-8
Oparta na Tcl/Tk przeglądarka dokumentacji hipertekstowej info
używanej przez projekt GNU. Może być również wbudowana w inne programy
Tcl/Tk.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -D tkinfo $RPM_BUILD_ROOT%{_bindir}/tkinfo
install -D tkinfo.1 $RPM_BUILD_ROOT%{_mandir}/man1/tkinfo.1
install -D TkInfo.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/tkinfo.xpm
install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
