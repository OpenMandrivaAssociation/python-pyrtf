%define oname	PyRTF

Name: 	 	python2-pyrtf
Summary: 	Python module to generate RTF documents
Version: 	0.45
Release: 	8
Source0:	http://downloads.sourceforge.net/pyrtf/%{oname}-%{version}.tar.bz2
URL:		http://pyrtf.sourceforge.net/
License:	GPL+
Group:		Development/Python
BuildRequires:	python-devel
%{py_requires}
BuildArch:	noarch
Obsoletes:	PyRTF < %{version}-%{release}
Provides:	PyRTF = %{version}-%{release}
%rename python-pyrtf

%description
PyRTF is a set of python classes that make it possible to produce RTF
documents from python programs. The library has no external dependencies
and has proved reliable and fast.

%prep
%setup -q -n %{oname}-%{version}

%install
python2 setup.py install --root=%{buildroot} --compile --optimize=2

%files
%{py2_puresitedir}/%{oname}
%{py2_puresitedir}/%{oname}-%{version}-py%{py2_ver}.egg-info

