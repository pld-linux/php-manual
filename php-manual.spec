Summary:	-
Summary(pl):	-
Name:		php-manual
# last updated - is there better scheme?
Version:	20030419
Release:	0.1
License:	- (enter GPL/LGPL/BSD/BSD-like/other license name here)
Group:		Documentation
Source0:	http://www.php.net/distributions/manual/php_manual_en.tar.bz2
# Source0-md5:	d89cb5124f95d2c30fb0d0e2dfe5de4e
Source1:	http://www.php.net/distributions/manual/php_manual_pt_BR.tar.bz2
# Source1-md5:	f8909f5b4740a18910e1af0daad33538
Source2:	http://www.php.net/distributions/manual/php_manual_zh.tar.bz2
# Source2-md5:	b8f4b06d7b65349f9401b49f25df103b
Source3:	http://www.php.net/distributions/manual/php_manual_hk.tar.bz2
# Source3-md5:	f968906a5e92c4ef1a79d6915b504fd1
Source4:	http://www.php.net/distributions/manual/php_manual_tw.tar.bz2
# Source4-md5:	c7a6a510a0314bc22201448715bcda6b
Source5:	http://www.php.net/distributions/manual/php_manual_cs.tar.bz2
# Source5-md5:	097902514794ec729138985e0a09a658
Source6:	http://www.php.net/distributions/manual/php_manual_nl.tar.bz2
# Source6-md5:	073df883b6699f734f191ce16b1f151e
Source7:	http://www.php.net/distributions/manual/php_manual_fi.tar.bz2
# Source7-md5:	05a3be3616701a028304c57910f9d5d4
Source8:	http://www.php.net/distributions/manual/php_manual_fr.tar.bz2
# Source8-md5:	8c821cd3f0abf7822d57eaec0fb5a700
Source9:	http://www.php.net/distributions/manual/php_manual_de.tar.bz2
# Source9-md5:	9d158cf4340bd8c74ce0de4c8e48e1a4
Source10:	http://www.php.net/distributions/manual/php_manual_he.tar.bz2
# Source10-md5:	ff9e86415dcd9bca3b14394828b4bfde
Source11:	http://www.php.net/distributions/manual/php_manual_hu.tar.bz2
# Source11-md5:	be055d93ae0f87d92d4ccdb0cba40c18
Source12:	http://www.php.net/distributions/manual/php_manual_it.tar.bz2
# Source12-md5:	4e47c8c669bb53a643c2d018fa4462d9
Source13:	http://www.php.net/distributions/manual/php_manual_ja.tar.bz2
# Source13-md5:	17f764374906841a187072c7526e6775
Source14:	http://www.php.net/distributions/manual/php_manual_kr.tar.bz2
# Source14-md5:	c4c969b861a3e22b9001f4fcf4dfac30
Source15:	http://www.php.net/distributions/manual/php_manual_pl.tar.bz2
# Source15-md5:	6396ce72e6658a3ec9f623a8dc073350
Source16:	http://www.php.net/distributions/manual/php_manual_ro.tar.bz2
# Source16-md5:	19b87204dc9f0eff46111f1f101c6d1a
Source17:	http://www.php.net/distributions/manual/php_manual_ru.tar.bz2
# Source17-md5:	7136ab315c2925228f16e9571950c0e7
Source18:	http://www.php.net/distributions/manual/php_manual_sk.tar.bz2
# Source18-md5:	d23e523a4d9bfa80fd310cd3b6670fcb
Source19:	http://www.php.net/distributions/manual/php_manual_sl.tar.bz2
# Source19-md5:	cd342fab7db94dc141462410fa25cd8b
Source20:	http://www.php.net/distributions/manual/php_manual_es.tar.bz2
# Source20-md5:	16fbcb86e9743271edcb5aeb2d1552af
Source21:	http://www.php.net/distributions/manual/php_manual_sv.tar.bz2
# Source21-md5:	a39ac23beab84915446a603ccf22ff1a
Source22:	http://www.php.net/distributions/manual/php_manual_tr.tar.bz2
# Source22-md5:	ccc53af840a7ecccec5900437b3a18f9
URL:		http://www.php.net/docs.php
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
