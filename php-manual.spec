# NOTE
# - Needs 981MB in RPM_BUILD_ROOT to package
# - easy way to update all sources with new/old manuals:
#   lynx -dump http://www.php.net/distributions/manual/ | awk '/http.*php_manual.*.tar.gz/{printf("Source%d: %s\n", i++, $2)}'

Summary:	PHP manual
Summary(pl.UTF-8):	Podręcznik do PHP
Name:		php-manual
# last updated - is there better scheme?
Version:	20120727
Release:	3
License:	Open Publication License v1.0+
Group:		Documentation
Source0:	http://www.php.net/distributions/manual/php_manual_de.tar.gz
# Source0-md5:	0f0f816c4846aeedf4627bd1072424a9
Source1:	http://www.php.net/distributions/manual/php_manual_en.tar.gz
# Source1-md5:	d2a36db770c77b52d4af5fd19ab7bd41
Source2:	http://www.php.net/distributions/manual/php_manual_es.tar.gz
# Source2-md5:	9d977633dff60df121c968184b39301f
Source3:	http://www.php.net/distributions/manual/php_manual_fr.tar.gz
# Source3-md5:	b7a1c3004b085e0bf7e31fba0db7c9c8
Source4:	http://www.php.net/distributions/manual/php_manual_ja.tar.gz
# Source4-md5:	794911f18ab64f9099cc4d4cc334cb31
Source5:	http://www.php.net/distributions/manual/php_manual_pl.tar.gz
# Source5-md5:	115f1b69dabe40cf312ef9843c12777d
Source6:	http://www.php.net/distributions/manual/php_manual_pt_BR.tar.gz
# Source6-md5:	4caff2177e00ff10add3831fe125d708
Source7:	http://www.php.net/distributions/manual/php_manual_ro.tar.gz
# Source7-md5:	c1eb977f9e6c1a34518b606ad6eb143c
Source8:	http://www.php.net/distributions/manual/php_manual_ru.tar.gz
# Source8-md5:	12b3ddd775c39d2a4fc3af240944d295
Source9:	http://www.php.net/distributions/manual/php_manual_tr.tar.gz
# Source9-md5:	3ee4d8b3cddbb2ec14b650d4f19a5724
Source10:	http://www.php.net/distributions/manual/php_manual_zh.tar.gz
# Source10-md5:	2146034be53f8a669c2e27f779c57730
URL:		http://www.php.net/docs.php
BuildRequires:	tar >= 1:1.15.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHP manual.

%description -l pl.UTF-8
Podręcznik do PHP.

%package en
Summary:	PHP manual in English language
Summary(pl.UTF-8):	Podręcznik do PHP w języku angielskim
Group:		Documentation
Obsoletes:	php-doc

%description en
PHP manual in English language.

%description en -l pl.UTF-8
Podręcznik do PHP w języku angielskim.

%package ar
Summary:	PHP manual translated to Arabic language
Summary(pl.UTF-8):	Podręcznik do PHP przetłumaczony na język arabski
Group:		Documentation

%description ar
PHP manual translated to Arabic language.

%description ar -l pl.UTF-8
Podręcznik do PHP przetłumaczony na język arabski.

%package cs
Summary:	PHP manual translated to Czech language
Summary(pl.UTF-8):	Podręcznik do PHP przetłumaczony na język czeski
Group:		Documentation

%description cs
PHP manual translated to Czech language.

%description cs -l pl.UTF-8
Podręcznik do PHP przetłumaczony na język czeski.

%package da
Summary:	PHP manual translated to Danish language
Summary(pl.UTF-8):	Podręcznik do PHP przetłumaczony na język duński
Group:		Documentation

%description da
PHP manual translated to Danish language.

%description da -l pl.UTF-8
Podręcznik do PHP przetłumaczony na język duński.

%package de
Summary:	PHP manual translated to German language
Summary(pl.UTF-8):	Podręcznik do PHP przetłumaczony na język niemiecki
Group:		Documentation

%description de
PHP manual translated to German language.

%description de -l pl.UTF-8
Podręcznik do PHP przetłumaczony na język niemiecki.

%package el
Summary:	PHP manual translated to Greek language
Summary(pl.UTF-8):	Podręcznik do PHP przetłumaczony na język grecki
Group:		Documentation

%description el
PHP manual translated to Greek language.

%description el -l pl.UTF-8
Podręcznik do PHP przetłumaczony na język grecki.

%package es
Summary:	PHP manual translated to Spanish language
Summary(pl.UTF-8):	Podręcznik do PHP przetłumaczony na język hiszpański
Group:		Documentation

%description es
PHP manual translated to Spanish language.

%description es -l pl.UTF-8
Podręcznik do PHP przetłumaczony na język hiszpański.

%package fi
Summary:	PHP manual translated to Finnish language
Summary(pl.UTF-8):	Podręcznik do PHP przetłumaczony na język fiński
Group:		Documentation

%description fi
PHP manual translated to Finnish language.

%description fi -l pl.UTF-8
Podręcznik do PHP przetłumaczony na język fiński.

%package fr
Summary:	PHP manual translated to French language
Summary(pl.UTF-8):	Podręcznik do PHP przetłumaczony na język francuski
Group:		Documentation

%description fr
PHP manual translated to French language.

%description fr -l pl.UTF-8
Podręcznik do PHP przetłumaczony na język francuski.

%package he
Summary:	PHP manual translated to Hebrew language
Summary(pl.UTF-8):	Podręcznik do PHP przetłumaczony na język hebrajski
Group:		Documentation

%description he
PHP manual translated to Hebrew language.

%description he -l pl.UTF-8
Podręcznik do PHP przetłumaczony na język hebrajski.

%package hu
Summary:	PHP manual translated to Hungarian language
Summary(pl.UTF-8):	Podręcznik do PHP przetłumaczony na język węgierski
Group:		Documentation

%description hu
PHP manual translated to Hungarian language.

%description hu -l pl.UTF-8
Podręcznik do PHP przetłumaczony na język węgierski.

%package it
Summary:	PHP manual translated to Italian language
Summary(pl.UTF-8):	Podręcznik do PHP przetłumaczony na język włoski
Group:		Documentation

%description it
PHP manual translated to Italian language.

%description it -l pl.UTF-8
Podręcznik do PHP przetłumaczony na język włoski.

%package ja
Summary:	PHP manual translated to Japanese language
Summary(pl.UTF-8):	Podręcznik do PHP przetłumaczony na język japoński
Group:		Documentation

%description ja
PHP manual translated to Japanese language.

%description ja -l pl.UTF-8
Podręcznik do PHP przetłumaczony na język japoński.

%package ko
Summary:	PHP manual translated to Korean language
Summary(pl.UTF-8):	Podręcznik do PHP przetłumaczony na język koreański
Group:		Documentation

%description ko
PHP manual translated to Korean language.

%description ko -l pl.UTF-8
Podręcznik do PHP przetłumaczony na język koreański.

%package nl
Summary:	PHP manual translated to Dutch language
Summary(pl.UTF-8):	Podręcznik do PHP przetłumaczony na język holenderski
Group:		Documentation

%description nl
PHP manual translated to Dutch language.

%description nl -l pl.UTF-8
Podręcznik do PHP przetłumaczony na język holenderski.

%package pl
Summary:	PHP manual translated to Polish language
Summary(pl.UTF-8):	Podręcznik do PHP przetłumaczony na język polski
Group:		Documentation

%description pl
PHP manual translated to Polish language.

%description pl -l pl.UTF-8
Podręcznik do PHP przetłumaczony na język polski.

%package pt_BR
Summary:	PHP manual translated to Brazilian Portuguese language
Summary(pl.UTF-8):	Podręcznik do PHP przetłumaczony na język portugalski w wersji brazylijskiej
Group:		Documentation

%description pt_BR
PHP manual translated to Brazilian Portuguese language.

%description pt_BR -l pl.UTF-8
Podręcznik do PHP przetłumaczony na język portugalski w wersji
brazylijskiej.

%package ro
Summary:	PHP manual translated to Romanian language
Summary(pl.UTF-8):	Podręcznik do PHP przetłumaczony na język rumuński
Group:		Documentation

%description ro
PHP manual translated to Romanian language.

%description ro -l pl.UTF-8
Podręcznik do PHP przetłumaczony na język rumuński.

%package ru
Summary:	PHP manual translated to Russian language
Summary(pl.UTF-8):	Podręcznik do PHP przetłumaczony na język rosyjski
Group:		Documentation

%description ru
PHP manual translated to Russian language.

%description ru -l pl.UTF-8
Podręcznik do PHP przetłumaczony na język rosyjski.

%package sk
Summary:	PHP manual translated to Slovak language
Summary(pl.UTF-8):	Podręcznik do PHP przetłumaczony na język słowacki
Group:		Documentation

%description sk
PHP manual translated to Slovak language.

%description sk -l pl.UTF-8
Podręcznik do PHP przetłumaczony na język słowacki.

%package sl
Summary:	PHP manual translated to Slovenian language
Summary(pl.UTF-8):	Podręcznik do PHP przetłumaczony na język słoweński
Group:		Documentation

%description sl
PHP manual translated to Slovenian language.

%description sl -l pl.UTF-8
Podręcznik do PHP przetłumaczony na język słoweński.

%package sv
Summary:	PHP manual translated to Swedish language
Summary(pl.UTF-8):	Podręcznik do PHP przetłumaczony na język szwedzki
Group:		Documentation

%description sv
PHP manual translated to Swedish language.

%description sv -l pl.UTF-8
Podręcznik do PHP przetłumaczony na język szwedzki.

%package tr
Summary:	PHP manual translated to Turkish language
Summary(pl.UTF-8):	Podręcznik do PHP przetłumaczony na język turecki
Group:		Documentation

%description tr
PHP manual translated to Turkish language.

%description tr -l pl.UTF-8
Podręcznik do PHP przetłumaczony na język turecki.

%package zh_CN
Summary:	PHP manual translated to Chinese (simplified) language
Summary(pl.UTF-8):	Podręcznik do PHP przetłumaczony na język chiński (uproszczony)
Group:		Documentation

%description zh_CN
PHP manual translated to Chinese (simplified) language.

%description zh_CN -l pl.UTF-8
Podręcznik do PHP przetłumaczony na język chiński (uproszczony).

%package zh_HK
Summary:	PHP manual translated to Chinese (Hong Kong Cantonese) language
Summary(pl.UTF-8):	Podręcznik do PHP przetłumaczony na język chiński (kantonu Hong Kong)
Group:		Documentation

%description zh_HK
PHP manual translated to Chinese (Hong Kong Cantonese) language.

%description zh_HK -l pl.UTF-8
Podręcznik do PHP przetłumaczony na język chiński (kantonu Hong Kong).

%package zh_TW
Summary:	PHP manual translated to Chinese (traditional, Taiwanian) language
Summary(pl.UTF-8):	Podręcznik do PHP przetłumaczony na język chiński (tradycyjny, tajwański)
Group:		Documentation

%description zh_TW
PHP manual translated to Chinese (Traditional, Taiwanian) language.

%description zh_TW -l pl.UTF-8
Podręcznik do PHP przetłumaczony na język chiński (tradycyjny,
tajwański).

%prep
%setup -qcT
unpack() {
	set -x
	local src=$1
	local bn=${src##*/}
	local pn=${bn%.tar.gz}
	local ln=${pn#php_manual_}

	tar xzf $src
	install -d %{name}-$ln
	mv php-chunked-xhtml/* %{name}-$ln
	rmdir php-chunked-xhtml
}

sources="%{expand:%(echo %(seq -f '%%%%SOURCE%g' 0 10 | tr '\n' ' '))}"
for src in $sources; do
	unpack $src
done

%build
for l in %{name}-*/; do
	date=$(%{__perl} -ne '/pubdate/ && />(.+)</ and print $1' $l/index.html)
	echo "$l $date"
done | tee versions.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}

# test if we can hardlink -- %{_builddir} and $RPM_BUILD_ROOT on same partition
touch COPYING
if cp -al COPYING $RPM_BUILD_ROOT%{_docdir}/COPYING 2>/dev/null; then
	l=l
	rm -f $RPM_BUILD_ROOT%{_docdir}/COPYING
fi
rm -f COPYING

cp -a$l %{name}-* $RPM_BUILD_ROOT%{_docdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files en
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-en

%if 0
%files ar
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-ar

%files cs
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-cs
%endif

%if 0
%files da
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-da
%endif

%files de
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-de

%if 0
%files el
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-el
%endif

%files es
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-es

%if 0
%files fi
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-fi
%endif

%files fr
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-fr

%if 0
%files he
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-he

%files hu
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-hu

%files it
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-it
%endif

%files ja
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-ja

%if 0
%files ko
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-kr

%files nl
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-nl
%endif

%files pl
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-pl

%files pt_BR
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-pt_BR

%files ro
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-ro

%files ru
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-ru

%if 0
%files sk
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-sk

%files sl
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-sl

%files sv
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-sv
%endif

%files tr
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-tr

%files zh_CN
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-zh

%if 0
%files zh_HK
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-hk

%files zh_TW
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-tw
%endif
