Summary:	Execute a command when the contents of a directory change
Summary(pl):	Wykonywanie poleceñ po zmianie zawarto¶ci katalogu
Name:		dnotify
Version:	0.17.0
Release:	1
Epoch:		1
License:	GPL
Vendor:		Oskar Liljeblad <oskar@osk.mine.nu>
Group:		Applications/File
Source0:	http://www.student.lu.se/~nbi98oli/src/%{name}-%{version}.tar.gz
# Source0-md5:	b919f53c044cf881d7d731872bbe5c1f
URL:		http://www.student.lu.se/~nbi98oli/dnotify.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dnotify is a simple program that makes it possible to execute a
command every time the contents of a specific directory change in
Linux. It is run from the command line and takes two arguments: one or
more directories to monitor and a command to execute whenever a
directory has changed. Options control what events to trigger on: when
a file was read in the directory, when one was created, deleted and so
on.

%description -l pl
dnotify to prosty program, który umo¿liwia wykonanie polecenia za
ka¿dym razem, kiedy zawarto¶æ danego katalogu pod Linuksem ulegnie
zmianie. Program jest uruchamiany z linii poleceñ i przyjmuje dwa
parametry: jeden lub wiêcej katalogów do monitorowania oraz polecenie
do wykonania po ka¿dej zmianie zawarto¶ci katalogu. Opcje kontroluj±,
jakie zdarzenia maj± spowodowaæ uruchomienie polecenia: kiedy w
katalogu jaki¶ plik by³ czytany, zosta³ utworzony lub usuniêty itp.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS NEWS TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*/*
