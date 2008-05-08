%define		plugin		include
Summary:	DokuWiki Include Plugin
Summary(pl.UTF-8):	Wtyczka Include (dołączania) dla DokuWiki
Name:		dokuwiki-plugin-%{plugin}
Version:	20070822
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://www.qwik.ch/media/include.tgz
# Source0-md5:	7487acd2765cdfd7eaf38b52e48508b6
Source1:	dokuwiki-find-lang.sh
Patch0:		http://gauret.free.fr/fichiers/dokuwiki/dokuwiki-include-odt.patch
URL:		http://www.wikidesign.ch/en/plugin/include/start
Requires:	dokuwiki >= 20061106
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
This is a very simple yet handy plugin with which you can include
another wiki page into the current one.

%description -l pl.UTF-8
To jest bardzo prosta, ale pomocna wtyczka, przy pomocy której można
dołączyć inną stronę wiki do bieżącej.

%prep
%setup -q -n %{plugin}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
rm -f $RPM_BUILD_ROOT%{plugindir}/{COPYING,README,VERSION}

# find locales
sh %{SOURCE1} %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%dir %{plugindir}
%{plugindir}/*.php
%{plugindir}/*.css
%{plugindir}/conf
%{plugindir}/images
