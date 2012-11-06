Name:           rfkill
Version:        0.4
Release:        0
License:        ISC
Summary:        Tool for enabling and disabling wireless devices
Url:            http://wireless.kernel.org/download/rfkill/
Group:          Productivity/Networking/Other
Source:         %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
rfkill is a small tool for accessing the Linux rfkill device interface,
which is used to enable and disable wireless networking devices, typically
WLAN, Bluetooth and mobile broadband.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
install -Dm755 rfkill %{buildroot}%{_sbindir}/rfkill
install -Dm644 rfkill.8 %{buildroot}%{_mandir}/man8/rfkill.8

%docs_package

%files
%defattr(-,root,root)
%doc COPYING
%{_sbindir}/rfkill

%changelog
