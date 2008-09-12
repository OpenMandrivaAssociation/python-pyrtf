%define name	PyRTF
%define version	0.45
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	Python module to generate RTF documents
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://pyrtf.sourceforge.net/
License:	GPL
Group:		Development/Python
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	python-devel
Requires:	python
BuildArch:	noarch

%description
PyRTF is a set of python classes that make it possible to produce RTF
documents from python programs. The library has no external dependencies
and has proved reliable and fast.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{py_puresitedir}/%name
%{py_puresitedir}/%name-%version-py2.5.egg-info
