# TODO:
# - should package names use lang names from archive filenames or ISO-compliant
#   ll[_CC] codes?
Summary:	PHP manual
Summary(pl):	Podrêcznik do PHP
Name:		php-manual
# last updated - is there better scheme?
Version:	20030419
Release:	0.1
License:	- (enter GPL/LGPL/BSD/BSD-like/other license name here)
Group:		Documentation
Source0:	http://www.php.net/distributions/manual/php_manual_en.tar.bz2
# Source0-md5:	d89cb5124f95d2c30fb0d0e2dfe5de4e
Source1:	http://www.php.net/distributions/manual/php_manual_cs.tar.bz2
# Source1-md5:	097902514794ec729138985e0a09a658
Source2:	http://www.php.net/distributions/manual/php_manual_de.tar.bz2
# Source2-md5:	9d158cf4340bd8c74ce0de4c8e48e1a4
Source3:	http://www.php.net/distributions/manual/php_manual_es.tar.bz2
# Source3-md5:	16fbcb86e9743271edcb5aeb2d1552af
Source4:	http://www.php.net/distributions/manual/php_manual_fi.tar.bz2
# Source4-md5:	05a3be3616701a028304c57910f9d5d4
Source5:	http://www.php.net/distributions/manual/php_manual_fr.tar.bz2
# Source5-md5:	8c821cd3f0abf7822d57eaec0fb5a700
Source6:	http://www.php.net/distributions/manual/php_manual_he.tar.bz2
# Source6-md5:	ff9e86415dcd9bca3b14394828b4bfde
Source7:	http://www.php.net/distributions/manual/php_manual_hk.tar.bz2
# Source7-md5:	f968906a5e92c4ef1a79d6915b504fd1
Source8:	http://www.php.net/distributions/manual/php_manual_hu.tar.bz2
# Source8-md5:	be055d93ae0f87d92d4ccdb0cba40c18
Source9:	http://www.php.net/distributions/manual/php_manual_it.tar.bz2
# Source9-md5:	4e47c8c669bb53a643c2d018fa4462d9
Source10:	http://www.php.net/distributions/manual/php_manual_ja.tar.bz2
# Source10-md5:	17f764374906841a187072c7526e6775
Source11:	http://www.php.net/distributions/manual/php_manual_kr.tar.bz2
# Source11-md5:	c4c969b861a3e22b9001f4fcf4dfac30
Source12:	http://www.php.net/distributions/manual/php_manual_nl.tar.bz2
# Source12-md5:	073df883b6699f734f191ce16b1f151e
Source13:	http://www.php.net/distributions/manual/php_manual_pl.tar.bz2
# Source13-md5:	6396ce72e6658a3ec9f623a8dc073350
Source14:	http://www.php.net/distributions/manual/php_manual_pt_BR.tar.bz2
# Source14-md5:	f8909f5b4740a18910e1af0daad33538
Source15:	http://www.php.net/distributions/manual/php_manual_ro.tar.bz2
# Source15-md5:	19b87204dc9f0eff46111f1f101c6d1a
Source16:	http://www.php.net/distributions/manual/php_manual_ru.tar.bz2
# Source16-md5:	7136ab315c2925228f16e9571950c0e7
Source17:	http://www.php.net/distributions/manual/php_manual_sk.tar.bz2
# Source17-md5:	d23e523a4d9bfa80fd310cd3b6670fcb
Source18:	http://www.php.net/distributions/manual/php_manual_sl.tar.bz2
# Source18-md5:	cd342fab7db94dc141462410fa25cd8b
Source19:	http://www.php.net/distributions/manual/php_manual_sv.tar.bz2
# Source19-md5:	a39ac23beab84915446a603ccf22ff1a
Source20:	http://www.php.net/distributions/manual/php_manual_tr.tar.bz2
# Source20-md5:	ccc53af840a7ecccec5900437b3a18f9
Source21:	http://www.php.net/distributions/manual/php_manual_tw.tar.bz2
# Source21-md5:	c7a6a510a0314bc22201448715bcda6b
Source22:	http://www.php.net/distributions/manual/php_manual_zh.tar.bz2
# Source22-md5:	b8f4b06d7b65349f9401b49f25df103b
URL:		http://www.php.net/docs.php
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

%package hk
# hk or zh_HK?
Summary:	PHP manual translated to Chinese (Hong Kong Cantonese) language
Summary(pl):	Podrêcznik do PHP przet³umaczony na jêzyk chiñski (kantonu Hong Kong)
Group:		Documentation

%description hk
PHP manual translated to Chinese (Hong Kong Cantonese) language.

%description hk -l pl
Podrêcznik do PHP przet³umaczony na jêzyk chiñski (kantonu Hong Kong).

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

%package kr
# kr or ko?
Summary:	PHP manual translated to Korean language
Summary(pl):	Podrêcznik do PHP przet³umaczony na jêzyk koreañski
Group:		Documentation

%description kr
PHP manual translated to Korean language.

%description kr -l pl
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

%package tw
# tw or zh_TW?
Summary:	PHP manual translated to Chinese (traditional, Taiwanian) language
Summary(pl):	Podrêcznik do PHP przet³umaczony na jêzyk chiñski (tradycyjny, tajwañski)
Group:		Documentation

%description tw
PHP manual translated to Chinese (Traditional, Taiwanian) language.

%description tw -l pl
Podrêcznik do PHP przet³umaczony na jêzyk chiñski (tradycyjny,
tajwañski).

%package zh
# zh or zh_CN?
Summary:	PHP manual translated to Chinese (simplified) language
Summary(pl):	Podrêcznik do PHP przet³umaczony na jêzyk chiñski (uproszczony)
Group:		Documentation

%description zh
PHP manual translated to Chinese (simplified) language.

%description zh -l pl
Podrêcznik do PHP przet³umaczony na jêzyk chiñski (uproszczony).

%prep
%setup -q -c -T

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
