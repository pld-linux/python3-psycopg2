# TODO:
# - lib64 patch

%define		module	psycopg2
Summary:	psycopg is a PostgreSQL database adapter for Python
Summary(pl.UTF-8):	psycopg jest przeznaczonym dla Pythona interfejsem do bazy PostgreSQL
Name:		python3-%{module}
Version:	2.9.10
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	https://pypi.debian.net/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	3a1ed36b492a74789563577edc0b0689
#Patch0:		%{name}-lib64.patch
URL:		https://www.psycopg.org/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	autoconf
BuildRequires:	postgresql-backend-devel
BuildRequires:	postgresql-devel
BuildRequires:	python3-devel
BuildRequires:	rpm-pythonprov
Requires:	postgresql-libs
Requires:	python3-modules
Requires:	python3-pytz
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
#%if "%{_lib}" == "lib64"
#%%patch0 -p1
#%endif

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT
%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS AUTHORS doc/SUCCESS
%dir %{py3_sitedir}/%{module}
%dir %{py3_sitedir}/%{module}/__pycache__
%attr(755,root,root) %{py3_sitedir}/%{module}/*.so
%{py3_sitedir}/%{module}/*.py
%{py3_sitedir}/%{module}/__pycache__/*.py*
%{py3_sitedir}/*.egg-info
