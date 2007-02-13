Summary:	PHP manual
Summary(pl.UTF-8):	Podręcznik do PHP
Name:		php-manual
# last updated - is there better scheme?
Version:	20051028
Release:	1
License:	Open Publication License v1.0+
Group:		Documentation
# ar contains only figures
# he,tr currently available only in .chm format
Source0:	http://static.php.net/www.php.net/distributions/manual/php_manual_en.tar.gz
# Source0-md5:	adc81a5f1fefed416dca674af288bf31
#Source1:	http://static.php.net/www.php.net/distributions/manual/php_manual_ar.tar.gz
#XSource1-md5:	38f458a76de34a8e8a1a543dc24c60bf
Source2:	http://static.php.net/www.php.net/distributions/manual/php_manual_cs.tar.gz
# Source2-md5:	52c3946a9811b379afb28098125ca14e
Source3:	http://static.php.net/www.php.net/distributions/manual/php_manual_da.tar.gz
# Source3-md5:	f42ff141d86440389b06f7697d1c9184
Source4:	http://static.php.net/www.php.net/distributions/manual/php_manual_de.tar.gz
# Source4-md5:	c082af879d1c9837b7c7cbc8ef03b9bb
Source5:	http://static.php.net/www.php.net/distributions/manual/php_manual_el.tar.gz
# Source5-md5:	c23c4bc6871aa8688e23e9a865fe2ac8
Source6:	http://static.php.net/www.php.net/distributions/manual/php_manual_es.tar.gz
# Source6-md5:	abf3b4d00816145b51885bf9901a63fe
Source7:	http://static.php.net/www.php.net/distributions/manual/php_manual_fi.tar.gz
# Source7-md5:	c2f7a86a5d05d3130d10d4282cabbbf5
Source8:	http://static.php.net/www.php.net/distributions/manual/php_manual_fr.tar.gz
# Source8-md5:	32167fbb9c11ff3fc250d2d73d5b289d
#Source9:	http://static.php.net/www.php.net/distributions/manual/php_manual_he.tar.gz
Source9:	php_manual_he.tar.bz2
# Source9-md5:	ff9e86415dcd9bca3b14394828b4bfde
Source10:	http://static.php.net/www.php.net/distributions/manual/php_manual_hk.tar.gz
# Source10-md5:	d120040e561e4d0ed1affe615c7a249a
Source11:	http://static.php.net/www.php.net/distributions/manual/php_manual_hu.tar.gz
# Source11-md5:	cfcd29cd2bd7821e6dc119c9f93c5988
Source12:	http://static.php.net/www.php.net/distributions/manual/php_manual_it.tar.gz
# Source12-md5:	64d09735031be3e695954df335fafbce
Source13:	http://static.php.net/www.php.net/distributions/manual/php_manual_ja.tar.gz
# Source13-md5:	1edccba1bcb243da96f2f2054222bbe3
Source14:	http://static.php.net/www.php.net/distributions/manual/php_manual_kr.tar.gz
# Source14-md5:	8aca34a0456a71e5a1b5cad7bcc5fcb2
Source15:	http://static.php.net/www.php.net/distributions/manual/php_manual_nl.tar.gz
# Source15-md5:	6df97713946c0f516c40578dd96391a0
Source16:	http://static.php.net/www.php.net/distributions/manual/php_manual_pl.tar.gz
# Source16-md5:	ead6378f52088d1e2806b046d61a1fb9
Source17:	http://static.php.net/www.php.net/distributions/manual/php_manual_pt_BR.tar.gz
# Source17-md5:	b779d0819163ec291eca53d5ac3b4fe7
Source18:	http://static.php.net/www.php.net/distributions/manual/php_manual_ro.tar.gz
# Source18-md5:	992ace347445085cfdf20e9935535289
Source19:	http://static.php.net/www.php.net/distributions/manual/php_manual_ru.tar.gz
# Source19-md5:	998a42b40099438dd121b54c1129e231
Source20:	http://static.php.net/www.php.net/distributions/manual/php_manual_sk.tar.gz
# Source20-md5:	674543f0cf7590e7636a339fac6ce823
Source21:	http://static.php.net/www.php.net/distributions/manual/php_manual_sl.tar.gz
# Source21-md5:	1f191812fced3704384da738e10423a0
Source22:	http://static.php.net/www.php.net/distributions/manual/php_manual_sv.tar.gz
# Source22-md5:	d7b142a5271d9cfd4c53e458a3f19ffd
Source23:	php_manual_tr.tar.bz2
# Source23-md5:	ccc53af840a7ecccec5900437b3a18f9
Source24:	http://static.php.net/www.php.net/distributions/manual/php_manual_tw.tar.gz
# Source24-md5:	f291766e2e5321eda72f891f90d18d99
Source25:	http://static.php.net/www.php.net/distributions/manual/php_manual_zh.tar.gz
# Source25-md5:	76f3e8d8812b60d4de66b3be7a8a4423
URL:		http://www.php.net/docs.php
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
%setup -q -c -T
install -d en ar cs da de el es fi fr he hk hu it ja kr nl pl pt_BR ro ru sk sl sv tr tw zh
tar xzf %{SOURCE0} -C en
#tar xzf %{SOURCE1} -C ar
tar xzf %{SOURCE2} -C cs
tar xzf %{SOURCE3} -C da
tar xzf %{SOURCE4} -C de
tar xzf %{SOURCE5} -C el
tar xzf %{SOURCE6} -C es
tar xzf %{SOURCE7} -C fi
tar xzf %{SOURCE8} -C fr
tar xjf %{SOURCE9} -C he
tar xzf %{SOURCE10} -C hk
tar xzf %{SOURCE11} -C hu
tar xzf %{SOURCE12} -C it
tar xzf %{SOURCE13} -C ja
tar xzf %{SOURCE14} -C kr
tar xzf %{SOURCE15} -C nl
tar xzf %{SOURCE16} -C pl
tar xzf %{SOURCE17} -C pt_BR
tar xzf %{SOURCE18} -C ro
tar xzf %{SOURCE19} -C ru
tar xzf %{SOURCE20} -C sk
tar xzf %{SOURCE21} -C sl
tar xzf %{SOURCE22} -C sv
tar xjf %{SOURCE23} -C tr
tar xzf %{SOURCE24} -C tw
tar xzf %{SOURCE25} -C zh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files en
%defattr(644,root,root,755)
%doc en/html

#%files ar
#%defattr(644,root,root,755)
#%doc ar/*

%files cs
%defattr(644,root,root,755)
%doc cs/html

%files da
%defattr(644,root,root,755)
%doc da/html

%files de
%defattr(644,root,root,755)
%doc de/html

%files el
%defattr(644,root,root,755)
%doc el/html

%files es
%defattr(644,root,root,755)
%doc es/html

%files fi
%defattr(644,root,root,755)
%doc fi/html

%files fr
%defattr(644,root,root,755)
%doc fr/html

%files he
%defattr(644,root,root,755)
%doc he/*

%files hu
%defattr(644,root,root,755)
%doc hu/html

%files it
%defattr(644,root,root,755)
%doc it/html

%files ja
%defattr(644,root,root,755)
%doc ja/html

%files ko
%defattr(644,root,root,755)
%doc kr/*

%files nl
%defattr(644,root,root,755)
%doc nl/[a-m]*
%doc nl/[!a-m]*

%files pl
%defattr(644,root,root,755)
%doc pl/html

%files pt_BR
%defattr(644,root,root,755)
%doc pt_BR/html

%files ro
%defattr(644,root,root,755)
%doc ro/[a-m]*
%doc ro/[!a-m]*

%files ru
%defattr(644,root,root,755)
%doc ru/html

%files sk
%defattr(644,root,root,755)
%doc sk/html

%files sl
%defattr(644,root,root,755)
%doc sl/[a-m]*
%doc sl/[!a-m]*

%files sv
%defattr(644,root,root,755)
%doc sv/html

%files tr
%defattr(644,root,root,755)
%doc tr/*

%files zh_CN
%defattr(644,root,root,755)
%doc zh/html

%files zh_HK
%defattr(644,root,root,755)
%doc hk/[a-m]*
%doc hk/[!a-m]*

%files zh_TW
%defattr(644,root,root,755)
%doc tw/html
