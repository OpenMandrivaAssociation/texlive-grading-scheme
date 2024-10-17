Name:		texlive-grading-scheme
Version:	62505
Release:	2
Summary:	Typeset grading schemes in tabular format
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/grading-scheme
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/grading-scheme.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/grading-scheme.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/grading-scheme.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package aims at an easy-to-use interface to typeset
grading schemes in tabular format, in particular
grading-schemes of exercises of mathematical olympiads where
multiple solutions have to be graded and might offer mutual
exclusive ways of receiving points.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/grading-scheme
%{_texmfdistdir}/tex/latex/grading-scheme
%doc %{_texmfdistdir}/doc/latex/grading-scheme

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
