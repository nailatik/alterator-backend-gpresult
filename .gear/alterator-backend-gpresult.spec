%define _unpackaged_files_terminate_build 1
%define mod_name gpresult_backend

Name: alterator-backend-gpresult
Version: 0.0.1
Release: alt1

Summary: Alterator backend for reading Group Policy results
License: GPLv3+
Group: System/Configuration/Other
URL: https://altlinux.space/alterator/alterator-backend-gpresult

BuildArch: noarch

Source0: %name-%version.tar

Requires: python3-module-%mod_name = %EVR
Requires: alterator-interface-gpresult = %EVR
Requires: alterator-module-executor >= 0.1.29
Requires: alterator-manager

BuildRequires(pre): rpm-build-pyproject rpm-macros-alterator
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools

%package -n alterator-interface-gpresult
Summary: Alterator D-Bus interface for gpresult
Group: System/Configuration/Other

%description -n alterator-interface-gpresult
D-Bus introspection XML for the gpresult1 interface.

%package -n python3-module-%mod_name
Summary: Python library for reading Group Policy results
Group: Development/Python3
Requires: python3-module-pygobject3
Requires: libgvdb-gir

%description
Alterator backend that exposes Group Policy results (gpresult) over D-Bus,
allowing a domain administrator to query applied GPOs on any domain machine
without SSH access.

%description -n python3-module-%mod_name
Python library used by the gpresult-wrapper backend script to read
Group Policy data from dconf GVDB databases.

%prep
%setup

%build
%pyproject_build

%install
mkdir -p %buildroot%_datadir/dbus-1/interfaces
install -p -m 644 interface/*.xml %buildroot%_datadir/dbus-1/interfaces/
mkdir -p %buildroot%_alterator_libdir/backends
install -p -m 755 src/gpresult-wrapper %buildroot%_alterator_libdir/backends/
mkdir -p %buildroot%_alterator_datadir/backends
install -p -m 644 backend/gpresult.backend %buildroot%_alterator_datadir/backends/
%pyproject_install

%files
%doc LICENSE.md
%_alterator_libdir/backends/gpresult-wrapper
%_alterator_datadir/backends/gpresult.backend

%files -n alterator-interface-gpresult
%_datadir/dbus-1/interfaces/org.altlinux.alterator.gpresult1.xml

%files -n python3-module-%mod_name
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %mod_name}

%changelog
* Sun Jun 29 2026 Niall Tugushev <tugushev.niall@gmail.com> 0.0.1-alt1
- Initial build for ALT Linux Sisyphus.
