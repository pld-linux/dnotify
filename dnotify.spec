Summary:	Execute a command when the contents of a directory change
Name:		dnotify
Version:	0.12.0
Release:	1
Epoch:		1
License:	GPL
Vendor:		Oskar Liljeblad <oskar@osk.mine.nu>
Group:		Applications/File
Source0:	http://www.student.lu.se/~nbi98oli/src/%{name}-%{version}.tar.gz
URL:		http://www.student.lu.se/~nbi98oli/dnotify.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dnotify is a simple program that makes it possible to execute a
command every time the contents of a specific directory change in
linux. It is run from the command line and takes two arguments: one or
more directories to monitor and a command to execute whenever a
directory has changed. Options control what events to trigger on: when
a file was read in the directory, when one was created, deleted and so
on.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS NEWS TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*/*
