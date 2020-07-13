#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xFEEF9FC2DD21D271 (security@readthedocs.org)
#
Name     : sphinx_rtd_theme
Version  : 0.4.3
Release  : 33
URL      : https://files.pythonhosted.org/packages/ed/73/7e550d6e4cf9f78a0e0b60b9d93dba295389c3d271c034bf2ea3463a79f9/sphinx_rtd_theme-0.4.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/ed/73/7e550d6e4cf9f78a0e0b60b9d93dba295389c3d271c034bf2ea3463a79f9/sphinx_rtd_theme-0.4.3.tar.gz
Source1  : https://files.pythonhosted.org/packages/ed/73/7e550d6e4cf9f78a0e0b60b9d93dba295389c3d271c034bf2ea3463a79f9/sphinx_rtd_theme-0.4.3.tar.gz.asc
Summary  : Read the Docs theme for Sphinx
Group    : Development/Tools
License  : MIT
Requires: sphinx_rtd_theme-license = %{version}-%{release}
Requires: sphinx_rtd_theme-python = %{version}-%{release}
Requires: sphinx_rtd_theme-python3 = %{version}-%{release}
Requires: Sphinx
BuildRequires : Sphinx
BuildRequires : buildreq-distutils3

%description
**************************
        Read the Docs Sphinx Theme
        **************************

%package license
Summary: license components for the sphinx_rtd_theme package.
Group: Default

%description license
license components for the sphinx_rtd_theme package.


%package python
Summary: python components for the sphinx_rtd_theme package.
Group: Default
Requires: sphinx_rtd_theme-python3 = %{version}-%{release}

%description python
python components for the sphinx_rtd_theme package.


%package python3
Summary: python3 components for the sphinx_rtd_theme package.
Group: Default
Requires: python3-core
Provides: pypi(sphinx_rtd_theme)
Requires: pypi(sphinx)

%description python3
python3 components for the sphinx_rtd_theme package.


%prep
%setup -q -n sphinx_rtd_theme-0.4.3
cd %{_builddir}/sphinx_rtd_theme-0.4.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583697838
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sphinx_rtd_theme
cp %{_builddir}/sphinx_rtd_theme-0.4.3/LICENSE %{buildroot}/usr/share/package-licenses/sphinx_rtd_theme/a1476f264c3622ce6548208ab116bf128809ddf7
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sphinx_rtd_theme/a1476f264c3622ce6548208ab116bf128809ddf7

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
