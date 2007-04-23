# NOTE
# - Needs 840MB in RPM_BUILD_ROOT to package
Summary:	PHP manual
Summary(pl.UTF-8):	Podręcznik do PHP
Name:		php-manual
# last updated - is there better scheme?
Version:	20070417
Release:	1
License:	Open Publication License v1.0+
Group:		Documentation
# ar contains only figures
# he,tr currently available only in .chm format
Source0:	http://static.php.net/www.php.net/distributions/manual/php_manual_en.tar.gz
# Source0-md5:	a0fa7d8dd0855aea8d3ab61ee2680942
#Source1:	http://static.php.net/www.php.net/distributions/manual/php_manual_ar.tar.gz
# Source1-md5:	0057240f51f122eed3e9c7c0ed397494
Source2:	http://static.php.net/www.php.net/distributions/manual/php_manual_cs.tar.gz
# Source2-md5:	9f10c985bb4de9c283f710f1e9e2095e
Source3:	http://static.php.net/www.php.net/distributions/manual/php_manual_da.tar.gz
# Source3-md5:	93daf71b45d9aecf23166a5588614b93
Source4:	http://static.php.net/www.php.net/distributions/manual/php_manual_de.tar.gz
# Source4-md5:	2eb217e968ec001c410a29554320b9bf
Source5:	http://static.php.net/www.php.net/distributions/manual/php_manual_el.tar.gz
# Source5-md5:	d9ffb64049ea40af24c61107fbeb9d31
Source6:	http://static.php.net/www.php.net/distributions/manual/php_manual_es.tar.gz
# Source6-md5:	99188107c685ba7158b166ca5b24f244
Source7:	http://static.php.net/www.php.net/distributions/manual/php_manual_fi.tar.gz
# Source7-md5:	c2f7a86a5d05d3130d10d4282cabbbf5
Source8:	http://static.php.net/www.php.net/distributions/manual/php_manual_fr.tar.gz
# Source8-md5:	28191896bc1ebc64265c1a4044a8c00c
Source9:	php_manual_he.tar.bz2
# Source9-md5:	ff9e86415dcd9bca3b14394828b4bfde
Source10:	http://static.php.net/www.php.net/distributions/manual/php_manual_hk.tar.gz
# Source10-md5:	d120040e561e4d0ed1affe615c7a249a
Source11:	http://static.php.net/www.php.net/distributions/manual/php_manual_hu.tar.gz
# Source11-md5:	cfb3cfb99fa20dcbedbc68eb56be47a6
Source12:	http://static.php.net/www.php.net/distributions/manual/php_manual_it.tar.gz
# Source12-md5:	64d09735031be3e695954df335fafbce
Source13:	http://static.php.net/www.php.net/distributions/manual/php_manual_ja.tar.gz
# Source13-md5:	e41d957c1a88487370146f54c9e1db34
Source14:	http://static.php.net/www.php.net/distributions/manual/php_manual_kr.tar.gz
# Source14-md5:	8aca34a0456a71e5a1b5cad7bcc5fcb2
Source15:	http://static.php.net/www.php.net/distributions/manual/php_manual_nl.tar.gz
# Source15-md5:	88a920541caf81c0c4986bdaee77bd1a
Source16:	http://static.php.net/www.php.net/distributions/manual/php_manual_pl.tar.gz
# Source16-md5:	f880f2e233143d9aa691d1809a18c5d3
Source17:	http://static.php.net/www.php.net/distributions/manual/php_manual_pt_BR.tar.gz
# Source17-md5:	3983b6f514545e2e6722ee9029be1a6a
Source18:	http://static.php.net/www.php.net/distributions/manual/php_manual_ro.tar.gz
# Source18-md5:	992ace347445085cfdf20e9935535289
Source19:	http://static.php.net/www.php.net/distributions/manual/php_manual_ru.tar.gz
# Source19-md5:	710f8d74a37de20645e9927fa3fe3802
Source20:	http://static.php.net/www.php.net/distributions/manual/php_manual_sk.tar.gz
# Source20-md5:	674543f0cf7590e7636a339fac6ce823
Source21:	http://static.php.net/www.php.net/distributions/manual/php_manual_sl.tar.gz
# Source21-md5:	1f191812fced3704384da738e10423a0
Source22:	http://static.php.net/www.php.net/distributions/manual/php_manual_sv.tar.gz
# Source22-md5:	d7b142a5271d9cfd4c53e458a3f19ffd
Source23:	php_manual_tr.tar.bz2
# Source23-md5:	ccc53af840a7ecccec5900437b3a18f9
Source24:	http://static.php.net/www.php.net/distributions/manual/php_manual_tw.tar.gz
# Source24-md5:	5ccc4a2ec789f936f9c4dfeab5953606
Source25:	http://static.php.net/www.php.net/distributions/manual/php_manual_zh.tar.gz
# Source25-md5:	b392c0389e58b7a03caf7749aa358359
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

%install
if [ ! -f install.stamp -o ! -d $RPM_BUILD_ROOT ]; then
	rm -rf installed.stamp $RPM_BUILD_ROOT
	install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-{en,cs,da,de,el,es,fi,fr,he,hk,hu,it,ja,kr,nl,pl,pt_BR,ro,ru,sk,sl,sv,tr,tw,zh}

	tar xzf %{SOURCE0} -C $RPM_BUILD_ROOT%{_docdir}/%{name}-en --strip-components=1
	#tar xzf %{SOURCE1} -C $RPM_BUILD_ROOT%{_docdir}/%{name}-ar
	tar xzf %{SOURCE2} -C $RPM_BUILD_ROOT%{_docdir}/%{name}-cs --strip-components=1
	tar xzf %{SOURCE3} -C $RPM_BUILD_ROOT%{_docdir}/%{name}-da --strip-components=1
	tar xzf %{SOURCE4} -C $RPM_BUILD_ROOT%{_docdir}/%{name}-de --strip-components=1
	tar xzf %{SOURCE5} -C $RPM_BUILD_ROOT%{_docdir}/%{name}-el --strip-components=1
	tar xzf %{SOURCE6} -C $RPM_BUILD_ROOT%{_docdir}/%{name}-es --strip-components=1
	tar xzf %{SOURCE7} -C $RPM_BUILD_ROOT%{_docdir}/%{name}-fi --strip-components=1
	tar xzf %{SOURCE8} -C $RPM_BUILD_ROOT%{_docdir}/%{name}-fr --strip-components=1
	tar xjf %{SOURCE9} -C $RPM_BUILD_ROOT%{_docdir}/%{name}-he
	tar xzf %{SOURCE10} -C $RPM_BUILD_ROOT%{_docdir}/%{name}-hk
	tar xzf %{SOURCE11} -C $RPM_BUILD_ROOT%{_docdir}/%{name}-hu --strip-components=1
	tar xzf %{SOURCE12} -C $RPM_BUILD_ROOT%{_docdir}/%{name}-it --strip-components=1
	tar xzf %{SOURCE13} -C $RPM_BUILD_ROOT%{_docdir}/%{name}-ja --strip-components=1
	tar xzf %{SOURCE14} -C $RPM_BUILD_ROOT%{_docdir}/%{name}-kr
	tar xzf %{SOURCE15} -C $RPM_BUILD_ROOT%{_docdir}/%{name}-nl --strip-components=1
	tar xzf %{SOURCE16} -C $RPM_BUILD_ROOT%{_docdir}/%{name}-pl --strip-components=1
	tar xzf %{SOURCE17} -C $RPM_BUILD_ROOT%{_docdir}/%{name}-pt_BR --strip-components=1
	tar xzf %{SOURCE18} -C $RPM_BUILD_ROOT%{_docdir}/%{name}-ro
	tar xzf %{SOURCE19} -C $RPM_BUILD_ROOT%{_docdir}/%{name}-ru --strip-components=1
	tar xzf %{SOURCE20} -C $RPM_BUILD_ROOT%{_docdir}/%{name}-sk --strip-components=1
	tar xzf %{SOURCE21} -C $RPM_BUILD_ROOT%{_docdir}/%{name}-sl
	tar xzf %{SOURCE22} -C $RPM_BUILD_ROOT%{_docdir}/%{name}-sv --strip-components=1
	tar xjf %{SOURCE23} -C $RPM_BUILD_ROOT%{_docdir}/%{name}-tr
	tar xzf %{SOURCE24} -C $RPM_BUILD_ROOT%{_docdir}/%{name}-tw --strip-components=1
	tar xzf %{SOURCE25} -C $RPM_BUILD_ROOT%{_docdir}/%{name}-zh --strip-components=1

	touch install.stamp
fi

find $RPM_BUILD_ROOT%{_docdir} -name CVS | xargs rm -vrf

%clean
rm -rf $RPM_BUILD_ROOT

%files en
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-en

#%files ar
#%defattr(644,root,root,755)
#%doc %{_docdir}/%{name}-ar

%files cs
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-cs

%files da
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-da

%files de
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-de

%files el
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-el

%files es
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-es

%files fi
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-fi

%files fr
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-fr

%files he
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-he

%files hu
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-hu

%files it
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-it

%files ja
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-ja

%files ko
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-kr

%files nl
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-nl

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

%files sk
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-sk

%files sl
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-sl

%files sv
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-sv

%files tr
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-tr

%files zh_CN
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-zh

%files zh_HK
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-hk

%files zh_TW
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-tw
