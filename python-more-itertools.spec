%global tarName more-itertools

Name:           python-%{tarName}
Version:	8.0.2
Release:	3
Summary:        Implements a lazy string for python useful for use with get-text

Group:          Development/Python
License:        BSD
URL:            https://github.com/erikrose/more-itertools
Source0:	https://files.pythonhosted.org/packages/4e/b2/e9e512cccde6c54bf66a8e5820a2af779eb8235028627002ca90d4f75bea/more-itertools-8.0.2.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:	python-setuptools
BuildRequires:	python2-devel
BuildRequires:	python2-setuptools

%description
The itertools library is a gem - you can compose elegant solutions for a 
variety of problems with its functions. More-itertools is a collection 
of building blocks, recipes, and routines for working with iterables.

%package -n python2-%{tarName}

Summary:        Building blocks, recipes, and routines for working with Python iterables.
%description -n python2-%{tarName}
he itertools library is a gem - you can compose elegant solutions for a 
variety of problems with its functions. More-itertools is a collection 
of building blocks, recipes, and routines for working with iterables.

%prep
%setup -qn %{tarName}-%{version}

cp -a . %py2dir
%build
python setup.py build

pushd %py2dir
python2 setup.py build

%install
python setup.py install --root=%{buildroot}

pushd %py2dir
python2 setup.py install --root=%{buildroot}

%files
%{py_puresitedir}/*
%doc PKG-INFO

%files -n python2-%{tarName}
%{py2_puresitedir}/*
%doc PKG-INFO
