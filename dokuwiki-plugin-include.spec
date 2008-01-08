%define		_plugin		include
Summary:	Dokuwiki Include Plugin
Name:		dokuwiki-plugin-%{_plugin}
Version:	20070822
Release:	0.3
License:	GPL v2
Group:		Applications/WWW
Source0:	http://www.qwik.ch/media/include.tgz
# Source0-md5:	7487acd2765cdfd7eaf38b52e48508b6
Source1:	dokuwiki-find-lang.sh
URL:		http://www.wikidesign.ch/en/plugin/include/start
Requires:	dokuwiki >= 20061106
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_dokudir	/usr/share/dokuwiki
%define		_plugindir	%{_dokudir}/lib/plugins/%{_plugin}

%description
This is a very simple yet handy plugin with which you can include
another wiki page into the current one.

%prep
%setup -q -n %{_plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir}
cp -a . $RPM_BUILD_ROOT%{_plugindir}
rm -f $RPM_BUILD_ROOT%{_plugindir}/{COPYING,README,VERSION}

# find locales
sh %{SOURCE1} %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%dir %{_plugindir}
%{_plugindir}/*.php
%{_plugindir}/*.css
%{_plugindir}/conf
%{_plugindir}/images
