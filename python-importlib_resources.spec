# NOTE: for versions >= 5.0 (for python 3.6+) see python3-importlib_resources.spec
#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (built from python3-importlib_resources.spec)

Summary:	Read resources from Python packages
Summary(pl.UTF-8):	Odczyt zasobów z pakietów Pythona
Name:		python-importlib_resources
# keep 3.x here for python2 support
Version:	3.3.1
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/importlib-resources/
Source0:	https://files.pythonhosted.org/packages/source/i/importlib-resources/importlib_resources-%{version}.tar.gz
# Source0-md5:	8db307bae9ec6c3c84298d75230e8043
URL:		https://pypi.org/project/importlib-resources/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm >= 3.4.1
BuildRequires:	python-toml
%if %{with tests}
BuildRequires:	python-contextlib2
BuildRequires:	python-pathlib2
BuildRequires:	python-singledispatch
BuildRequires:	python-typing
BuildRequires:	python-zipp >= 0.4
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm >= 3.4.1
BuildRequires:	python3-toml
%if %{with tests}
%if "%{py3_ver}" < "3.8"
BuildRequires:	python3-zipp >= 0.4
%endif
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python-jaraco.packaging
BuildRequires:	python-rst.linker
BuildRequires:	sphinx-pdg-2
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
importlib_resources is a backport of Python 3.9's standard library
importlib.resources module for Python 2.7, and 3.6 through 3.8. Users
of Python 3.9 and beyond should use the standard library module.
        
The key goal of this module is to replace parts of pkg_resources with
a solution in Python's stdlib that relies on well-defined APIs. This
makes reading resources included in packages easier, with more stable
and consistent semantics.

%description -l pl.UTF-8
importlib_resources to backport modułu importlib.resources z
biblioteki standardowej Pythona 3.9, przeznaczony dla Pythona 2.7 oraz
od 3.6 do 3.8. Użytkownicy Pythona 3.9 i nowszego powinni używać
modułu z biblioteki standardowej.

Głównym celem tego modułu jest zastąpienie części pkg_resources
rozwiązaniem obecnym w bibliotece standardowej Pythona, opartym na
dobrze zdefiniowanym API. Czyni to czytanie zasobów z pakietów
łatwiejszym, z bardziej stabilną i spójną semantyką.

%package -n python3-importlib_resources
Summary:	Read resources from Python packages
Summary(pl.UTF-8):	Odczyt zasobów z pakietów Pythona
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.6

%description -n python3-importlib_resources
importlib_resources is a backport of Python 3.9's standard library
importlib.resources module for Python 2.7, and 3.6 through 3.8. Users
of Python 3.9 and beyond should use the standard library module.
        
The key goal of this module is to replace parts of pkg_resources with
a solution in Python's stdlib that relies on well-defined APIs. This
makes reading resources included in packages easier, with more stable
and consistent semantics.

%description -n python3-importlib_resources -l pl.UTF-8
importlib_resources to backport modułu importlib.resources z
biblioteki standardowej Pythona 3.9, przeznaczony dla Pythona 2.7 oraz
od 3.6 do 3.8. Użytkownicy Pythona 3.9 i nowszego powinni używać
modułu z biblioteki standardowej.

Głównym celem tego modułu jest zastąpienie części pkg_resources
rozwiązaniem obecnym w bibliotece standardowej Pythona, opartym na
dobrze zdefiniowanym API. Czyni to czytanie zasobów z pakietów
łatwiejszym, z bardziej stabilną i spójną semantyką.

%package apidocs
Summary:	API documentation for Python importlib_resources module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona importlib_resources
Group:		Documentation

%description apidocs
API documentation for Python importlib_resources module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona importlib_resources.

%prep
%setup -q -n importlib_resources-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m unittest discover
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m unittest discover
%endif
%endif

%if %{with doc}
sphinx-build-2 -b html docs docs/_build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/importlib_resources
%{py_sitescriptdir}/importlib_resources-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-importlib_resources
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/importlib_resources
%{py3_sitescriptdir}/importlib_resources-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
