Summary:	Execute a command when the contents of a directory change
Summary(pl.UTF-8):   Wykonywanie poleceń po zmianie zawartości katalogu
Name:		dnotify
Version:	0.18.0
Release:	1
Epoch:		1
License:	GPL
Vendor:		Oskar Liljeblad <oskar@osk.mine.nu>
Group:		Applications/File
Source0:	http://www.student.lu.se/~nbi98oli/src/%{name}-%{version}.tar.gz
# Source0-md5:	7af869cee7e07b10817c4e7918ad0aee
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

%description -l pl.UTF-8
dnotify to prosty program, który umożliwia wykonanie polecenia za
każdym razem, kiedy zawartość danego katalogu pod Linuksem ulegnie
zmianie. Program jest uruchamiany z linii poleceń i przyjmuje dwa
parametry: jeden lub więcej katalogów do monitorowania oraz polecenie
do wykonania po każdej zmianie zawartości katalogu. Opcje kontrolują,
jakie zdarzenia mają spowodować uruchomienie polecenia: kiedy w
katalogu jakiś plik był czytany, został utworzony lub usunięty itp.

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
