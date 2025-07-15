Name:		py_slvs
Version:	1.0.6
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/py_slvs/py_slvs-%{version}.tar.gz
Summary:	Python binding of SOLVESPACE geometry constraint solver
URL:		https://pypi.org/project/py_slvs/
License:	Gnu General Public License 3.0
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	cmake
BuildRequires:	python-scikit-build
BuildRequires:	swig
BuildSystem:	python

%description
Python binding of SOLVESPACE geometry constraint solver
for use with the assembly3 workbench in Freecad 1.x

%files
%{py_platsitedir}/py_slvs
%{py_platsitedir}/py_slvs-*.*-info
