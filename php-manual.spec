Summary:	PHP manual
Summary(pl):	Podr�cznik do PHP
Name:		php-manual
# last updated - is there better scheme?
Version:	20030419
Release:	0.1
License:	GPL v2+ (except "Extending PHP 4.0" section on Open Publication License)
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
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHP manual.

%description -l pl
Podr�cznik do PHP.

%package en
Summary:	PHP manual in English language
Summary(pl):	Podr�cznik do PHP w j�zyku angielskim
Group:		Documentation
Obsoletes:	php-doc

%description en
PHP manual in English language.

%description en -l pl
Podr�cznik do PHP w j�zyku angielskim.

%package cs
Summary:	PHP manual translated to Czech language
Summary(pl):	Podr�cznik do PHP przet�umaczony na j�zyk czeski
Group:		Documentation

%description cs
PHP manual translated to Czech language.

%description cs -l pl
Podr�cznik do PHP przet�umaczony na j�zyk czeski.

%package de
Summary:	PHP manual translated to German language
Summary(pl):	Podr�cznik do PHP przet�umaczony na j�zyk niemiecki
Group:		Documentation

%description de
PHP manual translated to German language.

%description de -l pl
Podr�cznik do PHP przet�umaczony na j�zyk niemiecki.

%package es
Summary:	PHP manual translated to Spanish language
Summary(pl):	Podr�cznik do PHP przet�umaczony na j�zyk hiszpa�ski
Group:		Documentation

%description es
PHP manual translated to Spanish language.

%description es -l pl
Podr�cznik do PHP przet�umaczony na j�zyk hiszpa�ski.

%package fi
Summary:	PHP manual translated to Finnish language
Summary(pl):	Podr�cznik do PHP przet�umaczony na j�zyk fi�ski
Group:		Documentation

%description fi
PHP manual translated to Finnish language.

%description fi -l pl
Podr�cznik do PHP przet�umaczony na j�zyk fi�ski.

%package fr
Summary:	PHP manual translated to French language
Summary(pl):	Podr�cznik do PHP przet�umaczony na j�zyk francuski
Group:		Documentation

%description fr
PHP manual translated to French language.

%description fr -l pl
Podr�cznik do PHP przet�umaczony na j�zyk francuski.

%package he
Summary:	PHP manual translated to Hebrew language
Summary(pl):	Podr�cznik do PHP przet�umaczony na j�zyk hebrajski
Group:		Documentation

%description he
PHP manual translated to Hebrew language.

%description he -l pl
Podr�cznik do PHP przet�umaczony na j�zyk hebrajski.

%package hu
Summary:	PHP manual translated to Hungarian language
Summary(pl):	Podr�cznik do PHP przet�umaczony na j�zyk w�gierski
Group:		Documentation

%description hu
PHP manual translated to Hungarian language.

%description hu -l pl
Podr�cznik do PHP przet�umaczony na j�zyk w�gierski.

%package it
Summary:	PHP manual translated to Italian language
Summary(pl):	Podr�cznik do PHP przet�umaczony na j�zyk w�oski
Group:		Documentation

%description it
PHP manual translated to Italian language.

%description it -l pl
Podr�cznik do PHP przet�umaczony na j�zyk w�oski.

%package ja
Summary:	PHP manual translated to Japanese language
Summary(pl):	Podr�cznik do PHP przet�umaczony na j�zyk japo�ski
Group:		Documentation

%description ja
PHP manual translated to Japanese language.

%description ja -l pl
Podr�cznik do PHP przet�umaczony na j�zyk japo�ski.

%package ko
Summary:	PHP manual translated to Korean language
Summary(pl):	Podr�cznik do PHP przet�umaczony na j�zyk korea�ski
Group:		Documentation

%description ko
PHP manual translated to Korean language.

%description ko -l pl
Podr�cznik do PHP przet�umaczony na j�zyk korea�ski.

%package nl
Summary:	PHP manual translated to Dutch language
Summary(pl):	Podr�cznik do PHP przet�umaczony na j�zyk holenderski
Group:		Documentation

%description nl
PHP manual translated to Dutch language.

%description nl -l pl
Podr�cznik do PHP przet�umaczony na j�zyk holenderski.

%package pl
Summary:	PHP manual translated to Polish language
Summary(pl):	Podr�cznik do PHP przet�umaczony na j�zyk polski
Group:		Documentation

%description pl
PHP manual translated to Polish language.

%description pl -l pl
Podr�cznik do PHP przet�umaczony na j�zyk polski.

%package pt_BR
Summary:	PHP manual translated to Brazilian Portuguese language
Summary(pl):	Podr�cznik do PHP przet�umaczony na j�zyk portugalski w wersji brazylijskiej
Group:		Documentation

%description pt_BR
PHP manual translated to Brazilian Portuguese language.

%description pt_BR -l pl
Podr�cznik do PHP przet�umaczony na j�zyk portugalski w wersji
brazylijskiej.

%package ro
Summary:	PHP manual translated to Romanian language
Summary(pl):	Podr�cznik do PHP przet�umaczony na j�zyk rumu�ski
Group:		Documentation

%description ro
PHP manual translated to Romanian language.

%description ro -l pl
Podr�cznik do PHP przet�umaczony na j�zyk rumu�ski.

%package ru
Summary:	PHP manual translated to Russian language
Summary(pl):	Podr�cznik do PHP przet�umaczony na j�zyk rosyjski
Group:		Documentation

%description ru
PHP manual translated to Russian language.

%description ru -l pl
Podr�cznik do PHP przet�umaczony na j�zyk rosyjski.

%package sk
Summary:	PHP manual translated to Slovak language
Summary(pl):	Podr�cznik do PHP przet�umaczony na j�zyk s�owacki
Group:		Documentation

%description sk
PHP manual translated to Slovak language.

%description sk -l pl
Podr�cznik do PHP przet�umaczony na j�zyk s�owacki.

%package sl
Summary:	PHP manual translated to Slovenian language
Summary(pl):	Podr�cznik do PHP przet�umaczony na j�zyk s�owe�ski
Group:		Documentation

%description sl
PHP manual translated to Slovenian language.

%description sl -l pl
Podr�cznik do PHP przet�umaczony na j�zyk s�owe�ski.

%package sv
Summary:	PHP manual translated to Swedish language
Summary(pl):	Podr�cznik do PHP przet�umaczony na j�zyk szwedzki
Group:		Documentation

%description sv
PHP manual translated to Swedish language.

%description sv -l pl
Podr�cznik do PHP przet�umaczony na j�zyk szwedzki.

%package tr
Summary:	PHP manual translated to Turkish language
Summary(pl):	Podr�cznik do PHP przet�umaczony na j�zyk turecki
Group:		Documentation

%description tr
PHP manual translated to Turkish language.

%description tr -l pl
Podr�cznik do PHP przet�umaczony na j�zyk turecki.

%package zh_CN
Summary:	PHP manual translated to Chinese (simplified) language
Summary(pl):	Podr�cznik do PHP przet�umaczony na j�zyk chi�ski (uproszczony)
Group:		Documentation

%description zh_CN
PHP manual translated to Chinese (simplified) language.

%description zh_CN -l pl
Podr�cznik do PHP przet�umaczony na j�zyk chi�ski (uproszczony).

%package zh_HK
Summary:	PHP manual translated to Chinese (Hong Kong Cantonese) language
Summary(pl):	Podr�cznik do PHP przet�umaczony na j�zyk chi�ski (kantonu Hong Kong)
Group:		Documentation

%description zh_HK
PHP manual translated to Chinese (Hong Kong Cantonese) language.

%description zh_HK -l pl
Podr�cznik do PHP przet�umaczony na j�zyk chi�ski (kantonu Hong Kong).

%package zh_TW
Summary:	PHP manual translated to Chinese (traditional, Taiwanian) language
Summary(pl):	Podr�cznik do PHP przet�umaczony na j�zyk chi�ski (tradycyjny, tajwa�ski)
Group:		Documentation

%description zh_TW
PHP manual translated to Chinese (Traditional, Taiwanian) language.

%description zh_TW -l pl
Podr�cznik do PHP przet�umaczony na j�zyk chi�ski (tradycyjny,
tajwa�ski).

%prep
%setup -q -c -T
install -d en cs de es fi fr he hk hu it ja kr nl pl pt_BR ro ru sk sl sv tr tw zh
tar xjf %{SOURCE0} -C en
tar xjf %{SOURCE1} -C cs
tar xjf %{SOURCE2} -C de
tar xjf %{SOURCE3} -C es
tar xjf %{SOURCE4} -C fi
tar xjf %{SOURCE5} -C fr
tar xjf %{SOURCE6} -C he
tar xjf %{SOURCE7} -C hk
tar xjf %{SOURCE8} -C hu
tar xjf %{SOURCE9} -C it
tar xjf %{SOURCE10} -C ja
tar xjf %{SOURCE11} -C kr
tar xjf %{SOURCE12} -C nl
tar xjf %{SOURCE13} -C pl
tar xjf %{SOURCE14} -C pt_BR
tar xjf %{SOURCE15} -C ro
tar xjf %{SOURCE16} -C ru
tar xjf %{SOURCE17} -C sk
tar xjf %{SOURCE18} -C sl
tar xjf %{SOURCE19} -C sv
tar xjf %{SOURCE20} -C tr
tar xjf %{SOURCE21} -C tw
tar xjf %{SOURCE22} -C zh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files en
%defattr(644,root,root,755)
%doc en/*

%files cs
%defattr(644,root,root,755)
%doc cs/*

%files de
%defattr(644,root,root,755)
%doc de/*

%files es
%defattr(644,root,root,755)
%doc es/*

%files fi
%defattr(644,root,root,755)
%doc fi/*

%files fr
%defattr(644,root,root,755)
%doc fr/*

%files he
%defattr(644,root,root,755)
%doc he/*

%files hu
%defattr(644,root,root,755)
%doc hu/*

%files it
%defattr(644,root,root,755)
%doc it/*

%files ja
%defattr(644,root,root,755)
%doc ja/*

%files ko
%defattr(644,root,root,755)
%doc kr/*

%files nl
%defattr(644,root,root,755)
%doc nl/*

%files pl
%defattr(644,root,root,755)
%doc pl/*

%files pt_BR
%defattr(644,root,root,755)
%doc pt_BR/*

%files ro
%defattr(644,root,root,755)
%doc ro/*

%files ru
%defattr(644,root,root,755)
%doc ru/*

%files sk
%defattr(644,root,root,755)
%doc sk/*

%files sl
%defattr(644,root,root,755)
%doc sl/*

%files sv
%defattr(644,root,root,755)
%doc sv/*

%files tr
%defattr(644,root,root,755)
%doc tr/*

%files zh_CN
%defattr(644,root,root,755)
%doc zh/*

%files zh_HK
%defattr(644,root,root,755)
%doc hk/*

%files zh_TW
%defattr(644,root,root,755)
%doc tw/*
