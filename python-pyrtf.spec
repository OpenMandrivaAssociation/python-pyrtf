%define oname	PyRTF

Name: 	 	python-pyrtf
Summary: 	Python module to generate RTF documents
Version: 	0.45
Release: 	%mkrel 4
Source0:	http://downloads.sourceforge.net/pyrtf/%{oname}-%{version}.tar.bz2
URL:		http://pyrtf.sourceforge.net/
License:	GPL+
Group:		Development/Python
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	python-devel
%{py_requires}
BuildArch:	noarch
Obsoletes:	PyRTF < %{version}-%{release}
Provides:	PyRTF = %{version}-%{release}

%description
PyRTF is a set of python classes that make it possible to produce RTF
documents from python programs. The library has no external dependencies
and has proved reliable and fast.

%prep
%setup -q -n %{oname}-%{version}

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot} --compile --optimize=2

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{py_puresitedir}/%{oname}
%{py_puresitedir}/%{oname}-%{version}-py%{pyver}.egg-info
