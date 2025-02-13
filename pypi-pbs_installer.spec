#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v21
# autospec commit: e36a856
#
Name     : pypi-pbs_installer
Version  : 2025.2.12
Release  : 16
URL      : https://files.pythonhosted.org/packages/d6/66/390b96db3f1f455196cc85c60ec00a2c5194ec97ff228b72eb5d62a8410d/pbs_installer-2025.2.12.tar.gz
Source0  : https://files.pythonhosted.org/packages/d6/66/390b96db3f1f455196cc85c60ec00a2c5194ec97ff228b72eb5d62a8410d/pbs_installer-2025.2.12.tar.gz
Summary  : Installer for Python Build Standalone
Group    : Development/Tools
License  : MIT
Requires: pypi-pbs_installer-bin = %{version}-%{release}
Requires: pypi-pbs_installer-license = %{version}-%{release}
Requires: pypi-pbs_installer-python = %{version}-%{release}
Requires: pypi-pbs_installer-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(pdm_backend)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# pbs-installer
[![PyPI](https://img.shields.io/pypi/v/pbs-installer)](https://pypi.org/project/pbs-installer)

%package bin
Summary: bin components for the pypi-pbs_installer package.
Group: Binaries
Requires: pypi-pbs_installer-license = %{version}-%{release}

%description bin
bin components for the pypi-pbs_installer package.


%package license
Summary: license components for the pypi-pbs_installer package.
Group: Default

%description license
license components for the pypi-pbs_installer package.


%package python
Summary: python components for the pypi-pbs_installer package.
Group: Default
Requires: pypi-pbs_installer-python3 = %{version}-%{release}

%description python
python components for the pypi-pbs_installer package.


%package python3
Summary: python3 components for the pypi-pbs_installer package.
Group: Default
Requires: python3-core
Provides: pypi(pbs_installer)

%description python3
python3 components for the pypi-pbs_installer package.


%prep
%setup -q -n pbs_installer-2025.2.12
cd %{_builddir}/pbs_installer-2025.2.12

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1739471811
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation


%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pbs_installer
cp %{_builddir}/pbs_installer-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pbs_installer/c063b85ab3c5601f0eb04eba110b6e7be90fd898 || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pbs-install

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pbs_installer/c063b85ab3c5601f0eb04eba110b6e7be90fd898

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
