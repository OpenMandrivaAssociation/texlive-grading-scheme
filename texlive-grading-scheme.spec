%global tl_name grading-scheme
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1.1
Release:	%{tl_revision}.1
Summary:	Typeset grading schemes in tabular format
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/grading-scheme
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/grading-scheme.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/grading-scheme.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/grading-scheme.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package aims at an easy-to-use interface to typeset grading schemes
in tabular format, in particular grading-schemes of exercises of
mathematical olympiads where multiple solutions have to be graded and
might offer mutual exclusive ways of receiving points.

