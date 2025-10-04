# TODO: finish apidocs
#
# Conditional build:
%bcond_with	doc	# Sphinx documentation

%define		module	psycopg2
Summary:	psycopg is a PostgreSQL database adapter for Python
Summary(pl.UTF-8):	psycopg jest przeznaczonym dla Pythona interfejsem do bazy PostgreSQL
Name:		python3-%{module}
Version:	2.9.10
Release:	2
License:	LGPL v3+ with OpenSSL exception
Group:		Libraries/Python
Source0:	https://pypi.debian.net/psycopg2/%{module}-%{version}.tar.gz
# Source0-md5:	3a1ed36b492a74789563577edc0b0689
URL:		https://www.psycopg.org/
BuildRequires:	postgresql-backend-devel
BuildRequires:	postgresql-devel
BuildRequires:	python3-devel >= 1:3.8
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-sphinx-better-theme
BuildRequires:	sphinx-pdg-3
%endif
Requires:	postgresql-libs
Requires:	python3-modules >= 1:3.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
psycopg is a PostgreSQL database adapter for the Python programming
language (just like pygresql and popy.) It was written from scratch
with the aim of being very small and fast, and stable as a rock. The
main advantages of psycopg are that it supports the full Python
DBAPI-2.0 and being thread safe at level 2.

%description -l pl.UTF-8
psycopg jest przeznaczonym dla Pythona interfejsem do bazy danych
PostgreSQL (tak jak pygresql i popy). Został zakodowany od początku z
założeniem że ma być bardzo mały, szybki i stabilny. Główna zaletą
psycopg jest, że w jest pełni zgodny z standardem DBAPI-2.0 i jest
'thread safe' na poziomie 2.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE NEWS README.rst
%dir %{py3_sitedir}/%{module}
%{py3_sitedir}/%{module}/__pycache__
%attr(755,root,root) %{py3_sitedir}/%{module}/_psycopg.cpython-*.so
%{py3_sitedir}/%{module}/*.py
%{py3_sitedir}/psycopg2-%{version}-py*.egg-info
