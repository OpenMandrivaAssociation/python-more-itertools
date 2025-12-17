%global tarName more-itertools

Name:           python-%{tarName}
Version:	10.8.0
Release:	1
Summary:        Implements a lazy string for python useful for use with get-text

Group:          Development/Python
License:        BSD
URL:            https://github.com/erikrose/more-itertools
Source0:        https://files.pythonhosted.org/packages/source/m/more_itertools/more_itertools-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(pip)

%description
The itertools library is a gem - you can compose elegant solutions for a 
variety of problems with its functions. More-itertools is a collection 
of building blocks, recipes, and routines for working with iterables.


%prep
%setup -qn more_itertools-%{version}

%build
%py_build

%install
%py_install

%files
%{py_puresitedir}/*
%doc PKG-INFO
