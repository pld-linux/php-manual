Summary:	PHP manual
Summary(pl):	Podrêcznik do PHP
Name:		php-manual
# last updated - is there better scheme?
Version:	20040730
Release:	1
License:	Open Publication License v1.0+
Group:		Documentation
# ar contains only figures
# he,tr currently available only in .chm format
Source0:	http://static.php.net/www.php.net/distributions/manual/php_manual_en.tar.gz
# Source0-md5:	10953aa914f4c25083b5bc6a74cc51a5
#Source1:	http://static.php.net/www.php.net/distributions/manual/php_manual_ar.tar.gz
#XSource1-md5:	38f458a76de34a8e8a1a543dc24c60bf
Source2:	http://static.php.net/www.php.net/distributions/manual/php_manual_cs.tar.gz
# Source2-md5:	a72380655c63f0f65aab855f63eacf0b
Source3:	http://static.php.net/www.php.net/distributions/manual/php_manual_de.tar.gz
# Source3-md5:	14b78d649858ea099af7de97da927666
Source4:	http://static.php.net/www.php.net/distributions/manual/php_manual_el.tar.gz
# Source4-md5:	0426ccdd67d46b90e1f5b287da5f474a
Source5:	http://static.php.net/www.php.net/distributions/manual/php_manual_es.tar.gz
# Source5-md5:	1edf982ec19c027c6893e6735bc09604
Source6:	http://static.php.net/www.php.net/distributions/manual/php_manual_fi.tar.gz
# Source6-md5:	113bc682b1617a94e59d0bfc0b40e03d
Source7:	http://static.php.net/www.php.net/distributions/manual/php_manual_fr.tar.gz
# Source7-md5:	7acafffe2a574e3bc6efa24b5e537009
#Source8:	http://static.php.net/www.php.net/distributions/manual/php_manual_he.tar.gz
Source8:	php_manual_he.tar.bz2
# Source8-md5:	ff9e86415dcd9bca3b14394828b4bfde
Source9:	http://static.php.net/www.php.net/distributions/manual/php_manual_hk.tar.gz
# Source9-md5:	7b36a8d56679b944bc393b46a9fc2129
Source10:	http://static.php.net/www.php.net/distributions/manual/php_manual_hu.tar.gz
# Source10-md5:	e92ff2e6dfc7050327d82716400514d5
Source11:	http://static.php.net/www.php.net/distributions/manual/php_manual_it.tar.gz
# Source11-md5:	7f3b7a8f20c2c3b1ace0c029d406bf90
Source12:	http://static.php.net/www.php.net/distributions/manual/php_manual_ja.tar.gz
# Source12-md5:	7eb3e1d27a80bcbffb3aa875fc2caff8
Source13:	http://static.php.net/www.php.net/distributions/manual/php_manual_kr.tar.gz
# Source13-md5:	8aca34a0456a71e5a1b5cad7bcc5fcb2
Source14:	http://static.php.net/www.php.net/distributions/manual/php_manual_nl.tar.gz
# Source14-md5:	c7aa7e023c9956b3225b7bd6b3cae5c4
Source15:	http://static.php.net/www.php.net/distributions/manual/php_manual_pl.tar.gz
# Source15-md5:	56693f470be49c0b56a2bc11c9908bf8
Source16:	http://static.php.net/www.php.net/distributions/manual/php_manual_pt_BR.tar.gz
# Source16-md5:	edfc774c0527df8519830cce43235a64
Source17:	http://static.php.net/www.php.net/distributions/manual/php_manual_ro.tar.gz
# Source17-md5:	4f36484f13756452fd4c883839126a01
Source18:	http://static.php.net/www.php.net/distributions/manual/php_manual_ru.tar.gz
# Source18-md5:	6a26fed4204fb1e44c5820af1fe145b2
Source19:	http://static.php.net/www.php.net/distributions/manual/php_manual_sk.tar.gz
# Source19-md5:	6cff0797e94b913c79a527d7ad07cf60
Source20:	http://static.php.net/www.php.net/distributions/manual/php_manual_sl.tar.gz
# Source20-md5:	75a69f8b22177e7997266f38fca04df7
Source21:	http://static.php.net/www.php.net/distributions/manual/php_manual_sv.tar.gz
# Source21-md5:	e2f31cf7e4ec8d62d0fc4dd92e2e87d7
#Source22:	http://static.php.net/www.php.net/distributions/manual/php_manual_tr.tar.gz
Source22:	php_manual_tr.tar.bz2
# Source22-md5:	ccc53af840a7ecccec5900437b3a18f9
Source23:	http://static.php.net/www.php.net/distributions/manual/php_manual_tw.tar.gz
# Source23-md5:	c01729eaa06c56f584b6fce762b15590
Source24:	http://static.php.net/www.php.net/distributions/manual/php_manual_zh.tar.gz
# Source24-md5:	86887c5c48bb28591acce34f1e08ca04
URL:		http://www.php.net/docs.php
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHP manual.

%description -l pl
Podrêcznik do PHP.

%package en
Summary:	PHP manual in English language
Summary(pl):	Podrêcznik do PHP w jêzyku angielskim
Group:		Documentation
Obsoletes:	php-doc

%description en
PHP manual in English language.

%description en -l pl
Podrêcznik do PHP w jêzyku angielskim.

%package ar
Summary:	PHP manual translated to Arabic language
Summary(pl):	Podrêcznik do PHP przet³umaczony na jêzyk arabski
Group:		Documentation

%description ar
PHP manual translated to Arabic language.

%description ar -l pl
Podrêcznik do PHP przet³umaczony na jêzyk arabski.

%package cs
Summary:	PHP manual translated to Czech language
Summary(pl):	Podrêcznik do PHP przet³umaczony na jêzyk czeski
Group:		Documentation

%description cs
PHP manual translated to Czech language.

%description cs -l pl
Podrêcznik do PHP przet³umaczony na jêzyk czeski.

%package de
Summary:	PHP manual translated to German language
Summary(pl):	Podrêcznik do PHP przet³umaczony na jêzyk niemiecki
Group:		Documentation

%description de
PHP manual translated to German language.

%description de -l pl
Podrêcznik do PHP przet³umaczony na jêzyk niemiecki.

%package el
Summary:	PHP manual translated to Greek language
Summary(pl):	Podrêcznik do PHP przet³umaczony na jêzyk grecki
Group:		Documentation

%description el
PHP manual translated to Greek language.

%description el -l pl
Podrêcznik do PHP przet³umaczony na jêzyk grecki.

%package es
Summary:	PHP manual translated to Spanish language
Summary(pl):	Podrêcznik do PHP przet³umaczony na jêzyk hiszpañski
Group:		Documentation

%description es
PHP manual translated to Spanish language.

%description es -l pl
Podrêcznik do PHP przet³umaczony na jêzyk hiszpañski.

%package fi
Summary:	PHP manual translated to Finnish language
Summary(pl):	Podrêcznik do PHP przet³umaczony na jêzyk fiñski
Group:		Documentation

%description fi
PHP manual translated to Finnish language.

%description fi -l pl
Podrêcznik do PHP przet³umaczony na jêzyk fiñski.

%package fr
Summary:	PHP manual translated to French language
Summary(pl):	Podrêcznik do PHP przet³umaczony na jêzyk francuski
Group:		Documentation

%description fr
PHP manual translated to French language.

%description fr -l pl
Podrêcznik do PHP przet³umaczony na jêzyk francuski.

%package he
Summary:	PHP manual translated to Hebrew language
Summary(pl):	Podrêcznik do PHP przet³umaczony na jêzyk hebrajski
Group:		Documentation

%description he
PHP manual translated to Hebrew language.

%description he -l pl
Podrêcznik do PHP przet³umaczony na jêzyk hebrajski.

%package hu
Summary:	PHP manual translated to Hungarian language
Summary(pl):	Podrêcznik do PHP przet³umaczony na jêzyk wêgierski
Group:		Documentation

%description hu
PHP manual translated to Hungarian language.

%description hu -l pl
Podrêcznik do PHP przet³umaczony na jêzyk wêgierski.

%package it
Summary:	PHP manual translated to Italian language
Summary(pl):	Podrêcznik do PHP przet³umaczony na jêzyk w³oski
Group:		Documentation

%description it
PHP manual translated to Italian language.

%description it -l pl
Podrêcznik do PHP przet³umaczony na jêzyk w³oski.

%package ja
Summary:	PHP manual translated to Japanese language
Summary(pl):	Podrêcznik do PHP przet³umaczony na jêzyk japoñski
Group:		Documentation

%description ja
PHP manual translated to Japanese language.

%description ja -l pl
Podrêcznik do PHP przet³umaczony na jêzyk japoñski.

%package ko
Summary:	PHP manual translated to Korean language
Summary(pl):	Podrêcznik do PHP przet³umaczony na jêzyk koreañski
Group:		Documentation

%description ko
PHP manual translated to Korean language.

%description ko -l pl
Podrêcznik do PHP przet³umaczony na jêzyk koreañski.

%package nl
Summary:	PHP manual translated to Dutch language
Summary(pl):	Podrêcznik do PHP przet³umaczony na jêzyk holenderski
Group:		Documentation

%description nl
PHP manual translated to Dutch language.

%description nl -l pl
Podrêcznik do PHP przet³umaczony na jêzyk holenderski.

%package pl
Summary:	PHP manual translated to Polish language
Summary(pl):	Podrêcznik do PHP przet³umaczony na jêzyk polski
Group:		Documentation

%description pl
PHP manual translated to Polish language.

%description pl -l pl
Podrêcznik do PHP przet³umaczony na jêzyk polski.

%package pt_BR
Summary:	PHP manual translated to Brazilian Portuguese language
Summary(pl):	Podrêcznik do PHP przet³umaczony na jêzyk portugalski w wersji brazylijskiej
Group:		Documentation

%description pt_BR
PHP manual translated to Brazilian Portuguese language.

%description pt_BR -l pl
Podrêcznik do PHP przet³umaczony na jêzyk portugalski w wersji
brazylijskiej.

%package ro
Summary:	PHP manual translated to Romanian language
Summary(pl):	Podrêcznik do PHP przet³umaczony na jêzyk rumuñski
Group:		Documentation

%description ro
PHP manual translated to Romanian language.

%description ro -l pl
Podrêcznik do PHP przet³umaczony na jêzyk rumuñski.

%package ru
Summary:	PHP manual translated to Russian language
Summary(pl):	Podrêcznik do PHP przet³umaczony na jêzyk rosyjski
Group:		Documentation

%description ru
PHP manual translated to Russian language.

%description ru -l pl
Podrêcznik do PHP przet³umaczony na jêzyk rosyjski.

%package sk
Summary:	PHP manual translated to Slovak language
Summary(pl):	Podrêcznik do PHP przet³umaczony na jêzyk s³owacki
Group:		Documentation

%description sk
PHP manual translated to Slovak language.

%description sk -l pl
Podrêcznik do PHP przet³umaczony na jêzyk s³owacki.

%package sl
Summary:	PHP manual translated to Slovenian language
Summary(pl):	Podrêcznik do PHP przet³umaczony na jêzyk s³oweñski
Group:		Documentation

%description sl
PHP manual translated to Slovenian language.

%description sl -l pl
Podrêcznik do PHP przet³umaczony na jêzyk s³oweñski.

%package sv
Summary:	PHP manual translated to Swedish language
Summary(pl):	Podrêcznik do PHP przet³umaczony na jêzyk szwedzki
Group:		Documentation

%description sv
PHP manual translated to Swedish language.

%description sv -l pl
Podrêcznik do PHP przet³umaczony na jêzyk szwedzki.

%package tr
Summary:	PHP manual translated to Turkish language
Summary(pl):	Podrêcznik do PHP przet³umaczony na jêzyk turecki
Group:		Documentation

%description tr
PHP manual translated to Turkish language.

%description tr -l pl
Podrêcznik do PHP przet³umaczony na jêzyk turecki.

%package zh_CN
Summary:	PHP manual translated to Chinese (simplified) language
Summary(pl):	Podrêcznik do PHP przet³umaczony na jêzyk chiñski (uproszczony)
Group:		Documentation

%description zh_CN
PHP manual translated to Chinese (simplified) language.

%description zh_CN -l pl
Podrêcznik do PHP przet³umaczony na jêzyk chiñski (uproszczony).

%package zh_HK
Summary:	PHP manual translated to Chinese (Hong Kong Cantonese) language
Summary(pl):	Podrêcznik do PHP przet³umaczony na jêzyk chiñski (kantonu Hong Kong)
Group:		Documentation

%description zh_HK
PHP manual translated to Chinese (Hong Kong Cantonese) language.

%description zh_HK -l pl
Podrêcznik do PHP przet³umaczony na jêzyk chiñski (kantonu Hong Kong).

%package zh_TW
Summary:	PHP manual translated to Chinese (traditional, Taiwanian) language
Summary(pl):	Podrêcznik do PHP przet³umaczony na jêzyk chiñski (tradycyjny, tajwañski)
Group:		Documentation

%description zh_TW
PHP manual translated to Chinese (Traditional, Taiwanian) language.

%description zh_TW -l pl
Podrêcznik do PHP przet³umaczony na jêzyk chiñski (tradycyjny,
tajwañski).

%prep
%setup -q -c -T
install -d en ar cs de el es fi fr he hk hu it ja kr nl pl pt_BR ro ru sk sl sv tr tw zh
tar xzf %{SOURCE0} -C en
#tar xzf %{SOURCE1} -C ar
tar xzf %{SOURCE2} -C cs
tar xzf %{SOURCE3} -C de
tar xzf %{SOURCE4} -C el
tar xzf %{SOURCE5} -C es
tar xzf %{SOURCE6} -C fi
tar xzf %{SOURCE7} -C fr
tar xjf %{SOURCE8} -C he
tar xzf %{SOURCE9} -C hk
tar xzf %{SOURCE10} -C hu
tar xzf %{SOURCE11} -C it
tar xzf %{SOURCE12} -C ja
tar xzf %{SOURCE13} -C kr
tar xzf %{SOURCE14} -C nl
tar xzf %{SOURCE15} -C pl
tar xzf %{SOURCE16} -C pt_BR
tar xzf %{SOURCE17} -C ro
tar xzf %{SOURCE18} -C ru
tar xzf %{SOURCE19} -C sk
tar xzf %{SOURCE20} -C sl
tar xzf %{SOURCE21} -C sv
tar xjf %{SOURCE22} -C tr
tar xzf %{SOURCE23} -C tw
tar xzf %{SOURCE24} -C zh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files en
%defattr(644,root,root,755)
# workaround for "argument list too long"
%doc en/[a-m]*
%doc en/[!a-m]*

#%files ar
#%defattr(644,root,root,755)
#%doc ar/*

%files cs
%defattr(644,root,root,755)
%doc cs/*

%files de
%defattr(644,root,root,755)
%doc de/[a-m]*
%doc de/[!a-m]*

%files el
%defattr(644,root,root,755)
%doc el/[a-m]*
%doc el/[!a-m]*

%files es
%defattr(644,root,root,755)
%doc es/[a-m]*
%doc es/[!a-m]*

%files fi
%defattr(644,root,root,755)
%doc fi/[a-m]*
%doc fi/[!a-m]*

%files fr
%defattr(644,root,root,755)
%doc fr/[a-m]*
%doc fr/[!a-m]*

%files he
%defattr(644,root,root,755)
%doc he/*

%files hu
%defattr(644,root,root,755)
%doc hu/[a-m]*
%doc hu/[!a-m]*

%files it
%defattr(644,root,root,755)
%doc it/[a-m]*
%doc it/[!a-m]*

%files ja
%defattr(644,root,root,755)
%doc ja/[a-m]*
%doc ja/[!a-m]*

%files ko
%defattr(644,root,root,755)
%doc kr/*

%files nl
%defattr(644,root,root,755)
%doc nl/[a-m]*
%doc nl/[!a-m]*

%files pl
%defattr(644,root,root,755)
%doc pl/*

%files pt_BR
%defattr(644,root,root,755)
%doc pt_BR/[a-m]*
%doc pt_BR/[!a-m]*

%files ro
%defattr(644,root,root,755)
%doc ro/[a-m]*
%doc ro/[!a-m]*

%files ru
%defattr(644,root,root,755)
%doc ru/[a-m]*
%doc ru/[!a-m]*

%files sk
%defattr(644,root,root,755)
%doc sk/[a-m]*
%doc sk/[!a-m]*

%files sl
%defattr(644,root,root,755)
%doc sl/[a-m]*
%doc sl/[!a-m]*

%files sv
%defattr(644,root,root,755)
%doc sv/[a-m]*
%doc sv/[!a-m]*

%files tr
%defattr(644,root,root,755)
%doc tr/*

%files zh_CN
%defattr(644,root,root,755)
%doc zh/[a-m]*
%doc zh/[!a-m]*

%files zh_HK
%defattr(644,root,root,755)
%doc hk/[a-m]*
%doc hk/[!a-m]*

%files zh_TW
%defattr(644,root,root,755)
%doc tw/[a-m]*
%doc tw/[!a-m]*
