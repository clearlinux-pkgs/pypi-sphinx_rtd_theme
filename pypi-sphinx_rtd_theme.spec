#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
# autospec version: v21
# autospec commit: f35655a
#
Name     : pypi-sphinx_rtd_theme
Version  : 3.0.2
Release  : 71
URL      : https://files.pythonhosted.org/packages/91/44/c97faec644d29a5ceddd3020ae2edffa69e7d00054a8c7a6021e82f20335/sphinx_rtd_theme-3.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/91/44/c97faec644d29a5ceddd3020ae2edffa69e7d00054a8c7a6021e82f20335/sphinx_rtd_theme-3.0.2.tar.gz
Summary  : Read the Docs theme for Sphinx
Group    : Development/Tools
License  : MIT OFL-1.1
Requires: pypi-sphinx_rtd_theme-license = %{version}-%{release}
Requires: pypi-sphinx_rtd_theme-python = %{version}-%{release}
Requires: pypi-sphinx_rtd_theme-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(docutils)
BuildRequires : pypi(sphinx)
BuildRequires : pypi(sphinxcontrib_jquery)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
**************************
Read the Docs Sphinx Theme
**************************

%package license
Summary: license components for the pypi-sphinx_rtd_theme package.
Group: Default

%description license
license components for the pypi-sphinx_rtd_theme package.


%package python
Summary: python components for the pypi-sphinx_rtd_theme package.
Group: Default
Requires: pypi-sphinx_rtd_theme-python3 = %{version}-%{release}

%description python
python components for the pypi-sphinx_rtd_theme package.


%package python3
Summary: python3 components for the pypi-sphinx_rtd_theme package.
Group: Default
Requires: python3-core
Provides: pypi(sphinx_rtd_theme)
Requires: pypi(docutils)
Requires: pypi(sphinx)
Requires: pypi(sphinxcontrib_jquery)

%description python3
python3 components for the pypi-sphinx_rtd_theme package.


%prep
%setup -q -n sphinx_rtd_theme-3.0.2
cd %{_builddir}/sphinx_rtd_theme-3.0.2
pushd ..
cp -a sphinx_rtd_theme-3.0.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1731509279
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . docutils
pypi-dep-fix.py . sphinx
pypi-dep-fix.py . sphinxcontrib-jquery
pypi-dep-fix.py . docutils
pypi-dep-fix.py . sphinxcontrib_jquery
python3 setup.py build

pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
pypi-dep-fix.py . docutils
pypi-dep-fix.py . sphinx
pypi-dep-fix.py . sphinxcontrib-jquery
pypi-dep-fix.py . docutils
pypi-dep-fix.py . sphinxcontrib_jquery
python3 setup.py build

popd
%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-sphinx_rtd_theme
cp %{_builddir}/sphinx_rtd_theme-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-sphinx_rtd_theme/a1476f264c3622ce6548208ab116bf128809ddf7 || :
cp %{_builddir}/sphinx_rtd_theme-%{version}/OFL-License.txt %{buildroot}/usr/share/package-licenses/pypi-sphinx_rtd_theme/515c9e4e8cd9008dd8c0685638dfe9186aaad429 || :
python3 -tt setup.py build  install --root=%{buildroot}
pypi-dep-fix.py %{buildroot} docutils
pypi-dep-fix.py %{buildroot} sphinx
pypi-dep-fix.py %{buildroot} sphinxcontrib-jquery
pypi-dep-fix.py %{buildroot} docutils
pypi-dep-fix.py %{buildroot} sphinxcontrib_jquery
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-sphinx_rtd_theme/515c9e4e8cd9008dd8c0685638dfe9186aaad429
/usr/share/package-licenses/pypi-sphinx_rtd_theme/a1476f264c3622ce6548208ab116bf128809ddf7

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
