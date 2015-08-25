%define		plugin		include
Summary:	DokuWiki Include Plugin
Summary(pl.UTF-8):	Wtyczka Include (dołączania) dla DokuWiki
Name:		dokuwiki-plugin-%{plugin}
Version:	20150613
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	https://github.com/dokufreaks/plugin-include/archive/master/%{plugin}-%{version}.tar.gz
# Source0-md5:	83496db2a6fe1aef5f15aad444bff232
URL:		https://www.dokuwiki.org/plugin:include
BuildRequires:	rpmbuild(macros) >= 1.520
Requires:	dokuwiki >= 20080505
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		dokudata	/var/lib/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}
%define		find_lang 	%{_usrlibrpm}/dokuwiki-find-lang.sh %{buildroot}

%description
This is a very simple yet handy plugin with which you can include
another wiki page into the current one.

%description -l pl.UTF-8
To jest bardzo prosta, ale pomocna wtyczka, przy pomocy której można
dołączyć inną stronę wiki do bieżącej.

%prep
%setup -qc
mv *-%{plugin}-*/* .

version=$(awk '/date/{print $2}' plugin.info.txt)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
%{__rm} $RPM_BUILD_ROOT%{plugindir}/{COPYING,README}
%{__rm} -r $RPM_BUILD_ROOT%{plugindir}/_test

# find locales
%find_lang %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
# force js cache refresh
if [ -f %{dokuconf}/local.php ]; then
	touch %{dokuconf}/local.php
fi

%triggerpostun -- %{name} < 20110821
# http://www.dokuwiki.org/plugin:include says:
# It is recommended to delete all cache files in <dokuwiki>/data/cache directly
# after upgrading the plugin from an old version (before 2011)
# seems doku cache is one letter hex subdirs. nuke those
rm -rf %{dokudata}/cache/?

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%dir %{plugindir}
%{plugindir}/*.txt
%{plugindir}/*.php
%{plugindir}/*.css
%{plugindir}/*.js
%{plugindir}/conf
%{plugindir}/images
%{plugindir}/syntax
