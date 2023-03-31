Name:		texlive-cheatsheet
Version:	45069
Release:	2
Summary:	A simple cheatsheet class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cheatsheet
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cheatsheet.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cheatsheet.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cheatsheet.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a clean, multi-column design intended for
cheat sheets. It imports the most useful packages and encloses
the document in a multicol environment.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/cheatsheet
%{_texmfdistdir}/tex/latex/cheatsheet
%doc %{_texmfdistdir}/doc/latex/cheatsheet

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
