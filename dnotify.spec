%define package @PACKAGE@
%define version @VERSION@
%define prefix /usr
%define release 1

Summary:   Execute a command when the contents of a directory change
Name:      %{package}
Version:   %{version}
Release:   %{release}
Serial:    1
Copyright: GPL
Group:     Applications/File
Vendor:    Oskar Liljeblad <oskar@osk.mine.nu>
URL:       http://www.student.lu.se/~nbi98oli/dnotify.html
Source:    %{package}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
dnotify is a simple program that makes it possible to execute a command
every time the contents of a specific directory change in linux. It is run
from the command line and takes two arguments: one or more directories to
monitor and a command to execute whenever a directory has changed. Options
control what events to trigger on: when a file was read in the directory,
when one was created, deleted and so on.

%prep
%setup -q

%build
export CFLAGS="${RPM_OPT_FLAGS}" CPPFLAGS="${RPM_OPT_FLAGS}";
./configure --prefix=%{prefix};
make;

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
make prefix=%{buildroot}%{prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	sysconfdir=%{buildroot}/etc \
	install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README AUTHORS COPYING NEWS TODO
%{_mandir}/*/*
%{_bindir}/*
