%define oname	PyRTF

Name: 	 	python-pyrtf
Summary: 	Python module to generate RTF documents
Version: 	0.45
Release: 	6
Source0:	http://downloads.sourceforge.net/pyrtf/%{oname}-%{version}.tar.bz2
URL:		http://pyrtf.sourceforge.net/
License:	GPL+
Group:		Development/Python
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
python setup.py install --root=%{buildroot} --compile --optimize=2

%files
%{py_puresitedir}/%{oname}
%{py_puresitedir}/%{oname}-%{version}-py%{py_ver}.egg-info


%changelog
* Sat Nov 06 2010 Funda Wang <fwang@mandriva.org> 0.45-5mdv2011.0
+ Revision: 593999
- rebuild for py2.7

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.45-4mdv2010.0
+ Revision: 442465
- rebuild

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 0.45-3mdv2009.1
+ Revision: 323952
- rebuild

* Fri Sep 12 2008 Adam Williamson <awilliamson@mandriva.org> 0.45-2mdv2009.0
+ Revision: 284031
- generate .pyc and .pyo files
- clean macros
- clean python requires
- new license policy
- source location
- rename to match python policy
- drop unnecessary defines
- rename spec
- rename to conform to python policy

* Thu Sep 04 2008 Jérôme Soyer <saispo@mandriva.org> 0.45-1mdv2009.0
+ Revision: 280606
- Fix files section
- New version

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request
    - use %%mkrel
    - import PyRTF

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

