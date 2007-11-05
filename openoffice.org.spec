%define unstable	0

%ifarch x86_64
%define	ooname		openoffice.org64
%define name		openoffice.org64
%define oooaltpri	25
%else
%define	ooname		openoffice.org
%define name		openoffice.org
%define oooaltpri	24
%endif

#define _binary_payload w1.gzdio
%define _binary_payload w9.bzdio
#define _source_payload w9.bzdio

%define version		2.3.0.5
%define release		%mkrel 1

%define oootagver	oog680-m7
%define ooobuildver	2.3.0.5
%define jdkver		1_5_0_11
%ifarch x86_64
%define mdvsuffix	2.3_64
%else
%define mdvsuffix	2.3
%endif
%define ooodir		%{_libdir}/ooo-%{mdvsuffix}
%define libdbver	4.2
%define ooolangs	"en-US af ar bg br bs ca cs cy da de el en-GB es et eu fi fr he hi hu it ja ko mk nb nl nn pl pt pt-BR ru sk sl sv ta tr zh-TW zh-CN zu"

%ifarch x86_64
%define ooomenu		openoffice.org64-%{mdvsuffix}
%else
%define ooomenu		openoffice.org-%{mdvsuffix}
%endif

%define oootarext	bz2

%ifarch x86_64
%define distroname      Mandriva64
%define jdkver          1.4.2
%else
%define distroname      Mandriva
%define jdkver          1_5_0_11
%endif

%ifarch x86_64
%define use_gcj		1
%else
%define	use_gcj		0
%endif
%{?_with_gcj: %global use_gcj 1}
%{?_without_gcj: %global use_gcj 0}

%define use_hunspell	1
%{?_with_hunspell: %global use_hunspell 1}
%{?_without_hunspell: %global use_hunspell 0}

%define use_icecream	0
%{?_with_icecream: %global use_icecream 1}
%{?_without_icecream: %global use_icecream 0}

%define use_ccache	1
%define ccachedir	~/.ccache-OOo%{mdvsuffix}
%{?_with_ccache: %global use_ccache 1}
%{?_without_ccache: %global use_ccache 0}

%define use_smp		1
%{?_with_smp: %global use_smp 1}
%{?_without_smp: %global use_smp 0}

%define use_mono	1
%{?_with_mono: %global use_mono 1}
%{?_without_mono: %global use_mono 0}

%define use_openclipart	1
%{?_with_clipart: %global use_openclipart 1}
%{?_without_clipart: %global use_openclipart 0}

%define use_systemdb	0
%{?_with_systemdb: %global use_systemdb 1}
%{?_without_systemdb: %global use_systemdb 0}

%define use_systemboost 0
%{?_with_systemboost: %global use_systemboost 1}
%{?_without_systemboost: %global use_systemboost 0}

%define skip_install	0
%{?_with_skipinstall: %global skip_install 1}
%{?_without_skipinstall: %global skip_install 0}

# disable for now in X86-64 (gengal segfaults)
%ifarch x86_64
%define use_systemdb	1
%define use_systemboost 1
%endif

# (fix to avoid gcc 4.0.2 produces segfaulting javaldx bin which breaks
# building process)
%define optsafe	""

%define _requires_exceptions libjawt.so\\|libmyspell.so\\|libstlport_gcc.so
%define _provides_exceptions libsndfile.so\\|libportaudio.so\\|libdb-4.2.so\\|libdb_java-4.2.so\\|libmyspell.so\\|libstlport_gcc.so

Summary:	Open source office suite (ooo-build)
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://www.go-ooo.org
License:	LGPL
Group:		Office
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
# Requres to all our packages
Requires:	%{name}-base = %{version}
Requires:	%{name}-calc = %{version}
Requires:	%{name}-draw = %{version}
Requires:	%{name}-impress = %{version}
Requires:	%{name}-math = %{version}
Requires:	%{name}-writer = %{version}
Obsoletes:	OpenOffice.org
Obsoletes:	OpenOffice.org-libs
Obsoletes:	%{ooname}-go-ooo <= %{version}
Provides:	OpenOffice.org
Provides:	OpenOffice.org-libs
#
# Requirements for building
#
%if %{use_icecream}
BuildRequires:	icecream
%endif
%if %{use_ccache}
BuildRequires:	ccache
%endif
#
BuildRequires:	automake1.8
BuildRequires:	autoconf
%if %{use_systemboost}
BuildRequires:	boost-devel
%endif
BuildRequires:	bison >= 1.32-2mdk
%if %{use_openclipart}
BuildRequires:	clipart-openclipart
%endif
BuildRequires:	cups-devel
BuildRequires:	dbus-devel >= 0.60
BuildRequires:	ed
BuildRequires:	expat-devel
BuildRequires:	flex
BuildRequires:	freetype2-devel >= 2.1.3-3mdk
BuildRequires:	gcc >= 3.2-0.3mdk
BuildRequires:	gcc-c++ >= 3.2-0.3mdk
BuildRequires:	glitz-devel
BuildRequires:	gnutls-devel
BuildRequires:	gnome-vfsmm2.6-devel
BuildRequires:	gperf
BuildRequires:	ImageMagick
BuildRequires:	kdelibs-devel
BuildRequires:	kernel-source
BuildRequires:	db1-devel
%if %{use_systemdb}
BuildRequires:	%{mklibname db 4.2} >= 4.2.5-4mdk
BuildRequires:	libdbcxx >= 4.2.5-4mdk
BuildRequires:	libdb-devel >= 4.2.5-4mdk
BuildRequires:	libdbjava >= 4.2.5-4mdk
%else
BuildConflicts: libdbjava4.2
%endif
BuildRequires:	libcurl-devel
BuildRequires:	libgtk+2-devel
BuildRequires:	libsvg-devel
BuildRequires:	libgstreamer-plugins-base-devel
BuildRequires:	libxaw-devel
BuildRequires:	libldap-devel
BuildRequires:	%{mklibname portaudio 0}-devel
BuildConflicts: %{mklibname libportaudio 2}-devel
BuildRequires:	libsndfile-devel
BuildRequires:	unixODBC-devel
BuildRequires:	libwpd-devel
BuildRequires:	libxp-devel
BuildRequires:	libxslt-proc >= 1.0.19
BuildRequires:	libxslt-devel
BuildRequires:	libxml2 >= 2.4.23
%if %{use_mono}
BuildRequires:	mono-devel
BuildRequires:	mono-data-sqlite
%endif
BuildRequires:	mozilla-firefox-devel
BuildRequires:	nss-devel
BuildRequires:	nas-devel
BuildRequires:	neon-devel >= 0.26
BuildRequires:	pam-devel
BuildRequires:	perl
BuildRequires:	perl-Archive-Zip
BuildRequires:	perl-MDK-Common
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-XML-Twig
BuildRequires:	python-devel
BuildRequires:	qt3-devel
BuildRequires:	readline-devel
BuildRequires:	recode
BuildRequires:	sane-devel
BuildRequires:	sharutils
BuildRequires:	startup-notification-devel
%if %{oootarext} == "lzma"
BuildRequires:	lzma
BuildRequires:	tar >= 1.15.1-7mdk
%endif
BuildRequires:	tcsh >= 6.12-2mdk
BuildRequires:	unzip
BuildRequires:	XFree86
BuildRequires:	x11-server-xvfb
BuildRequires:	xpm-devel
BuildRequires:	zlib-devel
BuildRequires:	zip
#
# java
%if %{use_gcj}
BuildRequires:	ant
BuildRequires:  java-gcj-compat-devel >= 1.0.76-14.8
#
BuildRequires:	xml-commons-apis
%else
BuildRequires:	jdk >= %{jdkver}
BuildRequires:	jre >= %{jdkver}
BuildRequires:	j2sdk-ant
BuildConflicts:	gcc-java
BuildConflicts:	gcj-tools
BuildConflicts: java-kaffe
%endif
BuildConflicts:	STLport-devel

# <mrl> Not yet, must check java stuff first.
#BuildRequires:	hsqldb
# <mrl> not working as external yet
#BuildRequires:	bsh
#BuildRequires:	libsablotron0-devel

BuildRequires:	libwpg-devel
BuildRequires:	libwps-devel
BuildRequires:	icu
BuildRequires:	libicu-devel
BuildRequires:	libwps-devel
BuildRequires:	libmdbtools-devel


####################################################################
#
# Sources
#
####################################################################

Source0:	http://www.go-ooo.org/packages/OOG680/ooo-build-%{ooobuildver}.tar.gz
Source1:	http://www.go-ooo.org/packages/OOG680/%{oootagver}-core.tar.%{oootarext}
Source2:	http://www.go-ooo.org/packages/OOG680/%{oootagver}-lang.tar.%{oootarext}
Source3:	http://www.go-ooo.org/packages/OOG680/%{oootagver}-binfilter.tar.%{oootarext}
Source4:	http://www.go-ooo.org/packages/OOG680/%{oootagver}-system.tar.%{oootarext}
Source5:	http://www.go-ooo.org/packages/OOG680/%{oootagver}-sdk_oo.tar.%{oootarext}
Source6:	http://download.go-oo.org/SRC680/oox.2007-09-05.tar.bz2
Source10:	http://www.go-ooo.org/packages/SRC680/ooo_tango_images-1.tar.bz2
Source11:	http://download.go-oo.org/SRC680/ooo_crystal_images-6.tar.bz2
Source12:	http://www.go-ooo.org/packages/SRC680/ooo_custom_images-13.tar.bz2
Source13:	http://www.go-ooo.org/packages/SRC680/extras-2.tar.bz2
Source17:	http://www.go-ooo.org/packages/SRC680/mdbtools-0.6pre1.tar.gz
Source18:	http://www.go-ooo.org/packages/SRC680/hunspell-1.0.8.tar.gz
Source19:	http://www.go-ooo.org/packages/SRC680/hunspell_UNO_1.1.tar.gz
Source20:	http://www.go-ooo.org/packages/SRC680/cli_types.dll
Source21:	http://www.go-ooo.org/packages/SRC680/cli_types_bridgetest.dll
Source23:	http://www.go-ooo.org/packages/xt/xt-20051206-src-only.zip
Source24:	http://www.go-ooo.org/packages/SRC680/lp_solve_5.5.0.10_source.tar.gz
Source25:	http://www.go-ooo.org/packages/SRC680/biblio.tar.bz2
Source26:	http://tools.openoffice.org/unowinreg_prebuild/680/unowinreg.dll
# splash screens
Source27:	openintro_mandriva.bmp
Source28:	openabout_mandriva.bmp
# splash screens (64bit)
Source31:	openintro_mandriva64.bmp
Source32:	openabout_mandriva64.bmp
#
Source50:	http://oooconv.free.fr/fontooo/FontOOo.sxw.bz2
Source51:	ftp://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/DicOOo.sxw
Source60:	openoffice.org.csh
Source61:	openoffice.org.sh

Patch1:		ooo-build-2.1.0-lzmatarball.patch
Patch4:		openoffice.org2-2.0.2-qstart.patch
Patch6:		openoffice.org-2.1.0-firefox-xpcom.patch
Patch8:		ooo-build-2.2.1-xdg.patch
Patch10:	openoffice.org-2.1.0-install.patch
Patch14:	ooo-build-2.2.1-kde.patch
Patch16:	oof680-m18-core-ooqstart.patch
Patch17:	ooo-build-fix-build-java-target-patch.patch
Patch19:	ooo-build-2.2.1-desktop_files.patch
# (mrl) Force document downloads. http://qa.mandriva.com/show_bug.cgi?id=26983
Patch22:	ooo-build-2.2.1-force_downloads.patch
# (mrl) Adds Angola
Patch23:	ooo-build-2.2.1-angola.patch
# (mrl) Fix Wizards FontOOo and DictOOo paths
Patch24:	ooo-build-2.2.1-wizards.patch

%description
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite. It includes the key desktop applications,
such as a word processor, spreadsheet, presentation manager, formula
editing and drawing program, with a user interface and feature set
similar to other office suites. Sophisticated and flexible,
OpenOffice.org also works transparently with a variety of file
formats, including Microsoft Office.

%ifarch x86_64
Note: this native 64bit %{ooname} package is still at alpha/beta quality
level. It is not advised to use it for production. Use instead the 32bit
version over the x86_64 installation.
%endif

%package base
Group: Office
Summary: OpenOffice.org office suite - database
Requires: %{name}-common = %{version}
Requires: %{name}-core = %{version}
# Due to the split
Conflicts: %{name} = 2.2.1

%description base
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the database component for OpenOffice.org.

You can extend the functionality of OpenOffice.org Base by installing these
packages:

 * unixodbc: ODBC database support
 * libmyodbc | odbc-postgresql | libsqliteodbc | tdsodbc | mdbtools: ODBC
   drivers for:
   - MySQL
   - PostgreSQL
   - SQLite
   - MS SQL / Sybase SQL
   - *.mdb (JET / MS Access)
 * libmysql-java | libpg-java | libsapdbc-java: JDBC Drivers
   for:
   - MySQL
   - PostgreSQL
   - MaxDB

%package calc
Group: Office
Summary: OpenOffice.org office suite - spreadsheet
Requires: %{name}-common = %{version}
Requires: %{name}-core = %{version}
# Due to the split
Conflicts: %{name} = 2.2.1

%description calc
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the spreadsheet component for OpenOffice.org.

%package common
Group: Office
Summary: OpenOffice.org office suite architecture independent files
# Require the architecture dependant stuff
Requires: %{name}-core = %{version}
# Require at least one style to be installed
Requires: %{name}-style = %{version}
# And suggest the andromeda one
Suggests: %{name}-style-andromeda = %{version}
# And then general requires for OOo follows
Requires: ghostscript
Requires: fonts-ttf-liberation
Requires: %{mklibname sane 1}
Requires: desktop-common-data >= 2008
# Due to %{_bindir}/paperconf
Requires: paper-utils
Requires(post): desktop-file-utils update-alternatives
Requires(postun): desktop-file-utils update-alternatives
# Due to the split
Conflicts: %{name} = 2.2.1

%description common
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the architecture-independent files of OpenOffice.org.

%package core
Group: Office
Summary: OpenOffice.org office suite architecture dependent files
# Due to the split
Conflicts: %{name} = 2.2.1

%description core
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the architecture-dependent core files of OpenOffice.org.
See the openoffice.org package for more information.

%package devel
Group: Office
Summary: OpenOffice.org SDK - development files
Requires: %{name}-common = %{version}
Requires: %{name}-core = %{version}
# Due to the split
Conflicts: %{name} = 2.2.1

%description devel
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the files needed to build plugins/add-ons for
OpenOffice.org (includes, IDL files, build tools, ...). It also contains the
zipped source of the UNO Java libraries for use in IDEs like eclipse.

%package devel-doc
Group: Office
Summary: OpenOffice.org SDK - documentation
Requires: %{name}-devel = %{version}
# Due to the split
Conflicts: %{name} = 2.2.1

%description devel-doc
OpenOffice.org is a full-featured office productivity suite that provides
a near drop-in replacement for Microsoft(R) Office.

This package contains the documentation of the OpenOffice.org SDK:

 * C++/Java API reference
 * IDL reference
 * C++/Java/Basic examples

It also contains the gsicheck utility.

%package draw
Group: Office
Summary: OpenOffice.org office suite - drawing
Requires: %{name}-common = %{version}
Requires: %{name}-core = %{version}
# Due to the split
Conflicts: %{name} = 2.2.1

%description draw
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the drawing component for OpenOffice.org.

%package dtd-officedocument1.0
Group: Office
Summary: OfficeDocument 1.0 DTD (OpenOffice.org 1.x)
Requires: %{name}-common = %{version}
Requires: %{name}-core = %{version}
# Due to the split
Conflicts: %{name} = 2.2.1

%description dtd-officedocument1.0
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the Document Type Definition (DTD) of the OpenOffice.org
1.x(!) XML file format.

%package evolution
Group: Office
Summary: Evolution Addressbook support for OpenOffice.org
Requires: %{name}-common = %{version}
Requires: %{name}-core = %{version}
# Due to the split
Conflicts: %{name} = 2.2.1

%description evolution
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package allows OpenOffice.org to access Evolution address books. You need
to install evolution separately.

%package filter-binfilter
Group: Office
Summary: Legacy filters (e.g. StarOffice 5.2) for OpenOffice.org
Requires: %{name}-common = %{version}
Requires: %{name}-core = %{version}
# Due to the split
Conflicts: %{name} = 2.2.1

%description filter-binfilter
OpenOffice.org is a full-featured office productivity suite that provides
a near drop-in replacement for Microsoft(R) Office.

This package contains the "binfilters", legacy filters for
 - the old StarOffice 5.2 formats
 - StarWriter 1.0/2.0
 - StarWriter/DOS
 - *Writer* filters for
   + Excel
   + Lotus

%package filter-mobiledev
Group: Office
Summary: Mobile Devices Filters for OpenOffice.org
Requires: %{name}-common = %{version}
Requires: %{name}-core = %{version}
# Due to the split
Conflicts: %{name} = 2.2.1

%description filter-mobiledev
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the filters for Mobile Devices:
 * AportisDoc (Palm)
 * PocketWord
 * PocketExcel

%package gnome
Group: Office
Summary: GNOME Integration for OpenOffice.org (VFS, GConf)
Requires: %{name}-gtk = %{version}
# Due to the split
Conflicts: %{name} = 2.2.1

%description gnome
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the GNOME VFS support and a GConf backend.

You can extend the functionality of this by installing these packages:

 * openoffice.org-evolution: Evolution addressbook support
 * evolution

%package gtk
Group: Office
Summary: GTK Integration for OpenOffice.org (Widgets, Dialogs, Quickstarter)
Requires: %{name}-common = %{version}
Requires: %{name}-core = %{version}
Suggests: %{name}-style-tango = %{version}
# Due to the split
Conflicts: %{name} = 2.2.1

%description gtk
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the Gtk plugin for drawing OOo's widgets with Gtk+ and a
Gtk/GNOMEish File Picker when running under GNOME. It also contains a
QuickStarter for the "notification area".

%package impress
Group: Office
Summary: OpenOffice.org office suite - presentation
Requires: %{name}-common = %{version}
Requires: %{name}-core = %{version}
Requires: %{name}-draw = %{version}
# Due to the split
Conflicts: %{name} = 2.2.1

%description impress
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the presentation component for OpenOffice.org.

%package kde
Group: Office
Summary: KDE Integration for OpenOffice.org (Widgets, Dialogs, Addressbook)
Requires: %{name}-common = %{version}
Requires: %{name}-core = %{version}
Suggests: %{name}-style-crystal = %{version}
# Due to the split
Conflicts: %{name} = 2.2.1

%description kde
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the KDE plugin for drawing OOo's widgets with KDE/Qt, a
KDEish File Picker when running under KDE and KDE Addressbook integration.
You can extend the functionality of this by installing these packages:

 * konqueror / kmail
 * kaddressbook

%package java-common
Group: Office
Summary: OpenOffice.org office suite Java support arch. independent files
Requires: %{name}-common = %{version}
Requires: %{name}-core = %{version}
# Due to the split
Conflicts: %{name} = 2.2.1

%description java-common
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the architecture-independent files of the Java support
for OpenOffice.org (Java classes, scripts, config snippets).

Also contains the OpenOffice.org Office Bean for embedding OpenOffice.org in
custom Java applications.

%package math
Group: Office
Summary: OpenOffice.org office suite - equation editor
Requires: %{name}-common = %{version}
Requires: %{name}-core = %{version}
# Due to the split
Conflicts: %{name} = 2.2.1

%description math
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the equation editor component for OpenOffice.org.

%package openclipart
Group: Office
Summary: OpenOffice.org Open Clipart data
Requires: %{name}-common = %{version}
Requires: %{name}-core = %{version}
Requires: clipart-openclipart
# Due to the split
Conflicts: %{name} = 2.2.1

%description openclipart
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the OpenOffice.org Open Clipart data, including images
and sounds.

#%package qa-api-tests
#Group: Office
#Summary: OpenOffice.org API Test Data
#Requires: %{name}-common = %{version}
## Due to the split
#Conflicts: %{name} = 2.2.1
#
#%description qa-api-tests
#OpenOffice.org is a full-featured office productivity suite that provides a
#near drop-in replacement for Microsoft(R) Office.
#
#This package contains the test data for the OpenOffice.org Java and Basic APIs.
#
#%package qa-tools
#Group: Office
#Summary: OpenOffice.org Automatic Test Programs
#Requires: %{name}-common = %{version}
## Due to the split
#Conflicts: %{name} = 2.2.1
#
#%description qa-tools
#OpenOffice.org is a full-featured office productivity suite that provides a
#near drop-in replacement for Microsoft(R) Office.
#
#This package contains the test tools to automatically test the OpenOffice.org
#programs.
#
#Install the openoffice.org-qa-api-tests package to get the official
#testscripts, or write your own scripts.

%package style-andromeda
Group: Office
Summary: Default symbol style for OpenOffice.org
Requires: %{name}-common = %{version}
Requires: %{name}-core = %{version}
Provides: %{name}-style = %{version}-%{release}
# Due to the split
Conflicts: %{name} = 2.2.1

%description style-andromeda
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the "Andromeda" symbol style from Sun, normally used on
MS Windows (tm) and when not using GNOME or KDE. Needs to be manually enabled
in the OpenOffice.org option menu.

%package style-crystal
Group: Office
Summary: Crystal symbol style for OpenOffice.org
Requires: %{name}-common = %{version}
Requires: %{name}-core = %{version}
Provides: %{name}-style = %{version}-%{release}
# Due to the split
Conflicts: %{name} = 2.2.1

%description style-crystal
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the "crystal" symbol style, default style for KDE.

%package style-hicontrast
Group: Office
Summary: Hicontrast symbol style for OpenOffice.org
Requires: %{name}-common = %{version}
Requires: %{name}-core = %{version}
Provides: %{name}-style = %{version}-%{release}
# Due to the split
Conflicts: %{name} = 2.2.1

%description style-hicontrast
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the "hicontrast" symbol style, needs to be manually
enabled in the OpenOffice.org option menu.

%package style-industrial
Group: Office
Summary: Industrial symbol style for OpenOffice.org
Requires: %{name}-common = %{version}
Requires: %{name}-core = %{version}
Provides: %{name}-style = %{version}-%{release}
# Due to the split
Conflicts: %{name} = 2.2.1

%description style-industrial
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the "industrial" symbol style.

%package style-tango
Group: Office
Summary: Tango symbol style for OpenOffice.org
Requires: %{name}-common = %{version}
Requires: %{name}-core = %{version}
Provides: %{name}-style = %{version}-%{release}
# Due to the split
Conflicts: %{name} = 2.2.1

%description style-tango
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the "tango" symbol style, default style for GTK/Gnome.

%package writer
Group: Office
Summary: OpenOffice.org office suite - word processor
Requires: %{name}-common = %{version}
Requires: %{name}-core = %{version}
# Due to the split
Conflicts: %{name} = 2.2.1

%description writer
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the wordprocessor component for OpenOffice.org.

%package mono
Summary:	Mono UNO Bridge for OpenOffice.org
Group:		Office
Requires:	%{ooname} = %{version}
Obsoletes:	%{ooname}-go-ooo-mono <= %{version}

%description mono
The Mono/UNO binding allows a Mono application to access the complete
set of APIs exposed by OpenOffice.org via UNO.

Currently the use of Mono for add-ins & scripting inside OO.o itself is
not supported.

%package l10n-it
Summary:	Italian language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{version}
Requires:	locales-it
Requires:	fonts-ttf-dejavu
Requires:	urw-fonts
Requires:	myspell-it
Requires:	myspell-hyph-it
Obsoletes:	%{ooname}-go-ooo-l10n-it <= %{version}

%description l10n-it
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in Italian.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

%package l10n-af
Summary:	Afrikaans language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{version}
Requires:	locales-af
Requires:	urw-fonts
Requires:	myspell-af
Obsoletes:	OpenOffice.org-l10n-af
Provides:	OpenOffice.org-l10n-af
Obsoletes:	%{ooname}-go-ooo-l10n-af <= %{version}

%description l10n-af
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in Afrikaans.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-ar
Summary:	Arabic language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{version}
Requires:	locales-ar
Requires:	fonts-ttf-arabic
Obsoletes:	OpenOffice.org-l10n-ar
Provides:	OpenOffice.org-l10n-ar
Obsoletes:	%{ooname}-go-ooo-l10n-ar <= %{version}

%description l10n-ar
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in Arabic.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-bg
Summary:	Bulgarian language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{version}
Requires:	locales-bg
Obsoletes:	OpenOffice.org-l10n-bg
Provides:	OpenOffice.org-l10n-bg
Obsoletes:	%{ooname}-go-ooo-l10n-bg <= %{version}

%description l10n-bg
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in Bulgarian.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-br
Summary:	Breton language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{version}
Requires:	locales-br
Obsoletes:	%{ooname}-go-ooo-l10n-br <= %{version}

%description l10n-br
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in Breton.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-bs
Summary:	Bosnian language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{version}
Requires:	locales-bs
Obsoletes:	%{ooname}-go-ooo-l10n-bs <= %{version}

%description l10n-bs
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in Bosnian.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-ca
Summary:	Catalan language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{version}
Requires:	locales-ca
Requires:	urw-fonts
Requires:	myspell-ca
Obsoletes:	OpenOffice.org-l10n-ca
Provides:	OpenOffice.org-l10n-ca
Obsoletes:	%{ooname}-go-ooo-l10n-ca <= %{version}

%description l10n-ca
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in Catalan.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-cs
Summary:	Czech language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{version}
Requires:	locales-cs
Requires:	urw-fonts
Requires:	myspell-cs
Requires:	myspell-hyph-cs
Obsoletes:	OpenOffice.org-l10n-cs
Obsoletes:	OpenOffice.org-help-cs
Provides:	OpenOffice.org-l10n-cs
Provides:	OpenOffice.org-help-cs
Obsoletes:	%{ooname}-go-ooo-l10n-cs <= %{version}

%description l10n-cs
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in Czech.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-cy
Summary:	Welsh language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{version}
Requires:	locales-cy
Requires:	urw-fonts
Requires:	myspell-cy
Obsoletes:	OpenOffice.org-l10n-cy
Provides:	OpenOffice.org-l10n-cy
Obsoletes:	%{ooname}-go-ooo-l10n-cy <= %{version}

%description l10n-cy
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in Welsh.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-da
Summary:	Danish language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{version}
Requires:	locales-da
Requires:	fonts-ttf-dejavu
Requires:	urw-fonts
Requires:	myspell-da, myspell-hyph-da
Obsoletes:	OpenOffice.org-l10n-da
Provides:	OpenOffice.org-l10n-da
Obsoletes:	%{ooname}-go-ooo-l10n-da <= %{version}

%description l10n-da
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in Danish.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-de
Summary:	German language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{version}
Requires:	locales-de
Requires:	fonts-ttf-dejavu
Requires:	urw-fonts
Requires:	myspell-de
Requires:	myspell-hyph-de
Obsoletes:	OpenOffice.org-l10n-de
Obsoletes:	OpenOffice.org-help-de
Provides:	OpenOffice.org-l10n-de
Provides:	OpenOffice.org-help-de
Obsoletes:	%{ooname}-go-ooo-l10n-de <= %{version}

%description l10n-de
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in German.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-el
Summary:	Greek language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{version}
Requires:	locales-el
Requires:	fonts-type1-greek
Requires:	myspell-el
Requires:	myspell-hyph-el
Obsoletes:	OpenOffice.org-l10n-el
Provides:	OpenOffice.org-l10n-el
Obsoletes:	%{ooname}-go-ooo-l10n-el <= %{version}

%description l10n-el
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in Greek.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-en_GB
Summary:	British language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{version}
Requires:	locales-en
Requires:	urw-fonts
Requires:	myspell-en_GB
Requires:	myspell-hyph-en
Obsoletes:	%{ooname}-go-ooo-l10n-en_GB <= %{version}

%description l10n-en_GB
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in British.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-es
Summary:	Spanish language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{version}
Requires:	locales-es
Requires:	fonts-ttf-dejavu
Requires:	urw-fonts
Requires:	myspell-es
Requires:	myspell-hyph-es
Obsoletes:	OpenOffice.org-l10n-es
Obsoletes:	OpenOffice.org-help-es
Provides:	OpenOffice.org-l10n-es
Provides:	OpenOffice.org-help-es
Obsoletes:	%{ooname}-go-ooo-l10n-es <= %{version}

%description l10n-es
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in Spanish.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-et
Summary:	Estonian language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{version}
Requires:	locales-et
Requires:	fonts-ttf-dejavu
Requires:	urw-fonts
Requires:	myspell-et
Requires:	myspell-hyph-et
Obsoletes:	OpenOffice.org-l10n-et
Provides:	OpenOffice.org-l10n-et
Obsoletes:	%{ooname}-go-ooo-l10n-et <= %{version}

%description l10n-et
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in Estonian.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-eu
Summary:	Basque language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{version}
Requires:	locales-eu
Requires:	fonts-ttf-dejavu
Requires:	urw-fonts
Obsoletes:	OpenOffice.org-l10n-eu
Obsoletes:	OpenOffice.org-help-eu
Provides:	OpenOffice.org-l10n-eu
Provides:	OpenOffice.org-help-eu
Obsoletes:	%{ooname}-go-ooo-l10n-eu <= %{version}

%description l10n-eu
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in Basque.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-fi
Summary:	Finnish language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{version}
Requires:	locales-fi
Requires:	fonts-ttf-dejavu
Requires:	urw-fonts
Requires:	%{ooname}-voikko
Obsoletes:	OpenOffice.org-l10n-fi
Obsoletes:	OpenOffice.org-help-fi
Provides:	OpenOffice.org-l10n-fi
Provides:	OpenOffice.org-help-fi
Obsoletes:	%{ooname}-go-ooo-l10n-fi <= %{version}

%description l10n-fi
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in Finnish.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-fr
Summary:	French language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{version}
Requires:	locales-fr
Requires:	fonts-ttf-dejavu
Requires:	urw-fonts
Requires:	myspell-fr
Requires:	myspell-hyph-fr
Obsoletes:	OpenOffice.org-l10n-fr
Obsoletes:	OpenOffice.org-help-fr
Provides:	OpenOffice.org-l10n-fr
Provides:	OpenOffice.org-help-fr
Obsoletes:	%{ooname}-go-ooo-l10n-fr <= %{version}

%description l10n-fr
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in French.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-he
Summary:	Hebrew language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{version}
Requires:	locales-he
Requires:	urw-fonts
Obsoletes:	OpenOffice.org-l10n-he
Provides:	OpenOffice.org-l10n-he
Obsoletes:	%{ooname}-go-ooo-l10n-he <= %{version}

%description l10n-he
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in Hebrew.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-hi
Summary:	Hindi language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{version}
Requires:	locales-hi
Requires:	urw-fonts
Obsoletes:	OpenOffice.org-l10n-hi
Provides:	OpenOffice.org-l10n-hi
Obsoletes:	%{ooname}-go-ooo-l10n-hi <= %{version}

%description l10n-hi
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in Hindi.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-hu
Summary:	Hungarian language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{version}
Requires:	locales-hu
Requires:	urw-fonts
Requires:	myspell-hu
Requires:	myspell-hyph-hu
Obsoletes:	OpenOffice.org-l10n-hu
Provides:	OpenOffice.org-l10n-hu
Obsoletes:	%{ooname}-go-ooo-l10n-hu <= %{version}

%description l10n-hu
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in Hungarian.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-ja
Summary:	Japanese language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{version}
Requires:	locales-ja
Requires:	fonts-ttf-japanese >= 0.20020727-1mdk
Obsoletes:	OpenOffice.org-l10n-ja
Obsoletes:	OpenOffice.org-help-ja
Provides:	OpenOffice.org-l10n-ja
Provides:	OpenOffice.org-help-ja
Obsoletes:	%{ooname}-go-ooo-l10n-ja <= %{version}

%description l10n-ja
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in Japanese.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-ko
Summary:	Korean language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{version}
Requires:	locales-ko
Requires:	fonts-ttf-korean >= 2.1
Obsoletes:	OpenOffice.org-l10n-ko
Obsoletes:	OpenOffice.org-help-ko
Provides:	OpenOffice.org-l10n-ko
Provides:	OpenOffice.org-help-ko
Obsoletes:	%{ooname}-go-ooo-l10n-ko <= %{version}

%description l10n-ko
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in Korean.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-mk
Summary:	Macedonian language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{version}
Requires:	locales-mk
Obsoletes:	%{ooname}-go-ooo-l10n-mk <= %{version}

%description l10n-mk
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in Macedonian.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-nb
Summary:	Norwegian Bokmal language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{version}
Requires:	locales-no
Requires:	urw-fonts
Obsoletes:	OpenOffice.org-l10n-nb
Provides:	OpenOffice.org-l10n-nb
Obsoletes:	%{ooname}-go-ooo-l10n-nb <= %{version}

%description l10n-nb
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in Norwegian Bokmal.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-nl
Summary:	Dutch language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{version}
Requires:	locales-nl
Requires:	fonts-ttf-dejavu
Requires:	urw-fonts
Requires:	myspell-nl
Requires:	myspell-hyph-nl
Obsoletes:	OpenOffice.org-l10n-nl
Obsoletes:	OpenOffice.org-help-nl
Provides:	OpenOffice.org-l10n-nl
Provides:	OpenOffice.org-help-nl
Obsoletes:	%{ooname}-go-ooo-l10n-nl <= %{version}

%description l10n-nl
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in Dutch.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-nn
Summary:	Norwegian Nynorsk language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{version}
Requires:	locales-no
Requires:	urw-fonts
Obsoletes:	OpenOffice.org-l10n-nn
Provides:	OpenOffice.org-l10n-nn
Obsoletes:	%{ooname}-go-ooo-l10n-nn <= %{version}

%description l10n-nn
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in Norwegian Nynorsk.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

%package l10n-pl
Summary:	Polish language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{version}
Requires:	locales-pl
Requires:	urw-fonts
Requires:	myspell-pl
Requires:	myspell-hyph-pl
Obsoletes:	OpenOffice.org-l10n-pl
Provides:	OpenOffice.org-l10n-pl
Obsoletes:	%{ooname}-go-ooo-l10n-pl <= %{version}

%description l10n-pl
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in Polish.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-pt
Summary:	Portuguese language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{version}
Requires:	locales-pt
Requires:	fonts-ttf-dejavu
Requires:	urw-fonts
Requires:	myspell-pt
Requires:	myspell-hyph-pt
Obsoletes:	OpenOffice.org-l10n-pt
Provides:	OpenOffice.org-l10n-pt
Obsoletes:	%{ooname}-go-ooo-l10n-pt <= %{version}

%description l10n-pt
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in Portuguese.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-pt_BR
Summary:	Portuguese Brazilian language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{version}
Requires:	locales-pt
Requires:	urw-fonts
Requires:	myspell-pt_BR
Obsoletes:	OpenOffice.org-l10n_pt_BR
Obsoletes:	OpenOffice.org-help-pt_BR
Provides:	OpenOffice.org-l10n_pt_BR
Provides:	OpenOffice.org-help-pt_BR
Obsoletes:	%{ooname}-go-ooo-l10n-pt_BR <= %{version}

%description l10n-pt_BR
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in Portuguese Brazilian.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-ru
Summary:	Russian language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{version}
Requires:	locales-ru
Requires:	urw-fonts >= 2.0-6mdk
Requires:	myspell-ru
Requires:	myspell-hyph-ru
Obsoletes:	OpenOffice.org-l10n-ru
Obsoletes:	OpenOffice.org-help-ru
Provides:	OpenOffice.org-l10n-ru
Provides:	OpenOffice.org-help-ru
Obsoletes:	%{ooname}-go-ooo-l10n-ru <= %{version}

%description l10n-ru
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in Russian.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-sk
Summary:	Slovak language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{version}
Requires:	locales-sk
Requires:	urw-fonts
Requires:	myspell-sk
Requires:	myspell-hyph-sk
Obsoletes:	OpenOffice.org-l10n-sk
Obsoletes:	OpenOffice.org-help-sk
Provides:	OpenOffice.org-l10n-sk
Provides:	OpenOffice.org-help-sk
Obsoletes:	%{ooname}-go-ooo-l10n-su <= %{version}

%description l10n-sk
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in Slovak.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-sl
Summary:	Slovenian language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{version}
Requires:	locales-sl
Requires:	urw-fonts
Requires:	myspell-sl, myspell-hyph-sl
Obsoletes:	OpenOffice.org-l10n-sl
Obsoletes:	OpenOffice.org-help-sl
Provides:	OpenOffice.org-l10n-sl
Provides:	OpenOffice.org-help-sl
Obsoletes:	%{ooname}-go-ooo-l10n-sl <= %{version}

%description l10n-sl
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in Slovenian.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-sv
Summary:	Swedish language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{version}
Requires:	locales-sv
Requires:	fonts-ttf-dejavu
Requires:	urw-fonts
Requires:	myspell-sv
Requires:	myspell-hyph-sv
Obsoletes:	OpenOffice.org-l10n-sv
Obsoletes:	OpenOffice.org-help-sv
Provides:	OpenOffice.org-l10n-sv
Provides:	OpenOffice.org-help-sv
Obsoletes:	%{ooname}-go-ooo-l10n-sv <= %{version}

%description l10n-sv
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in Swedish.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-ta
Summary:	Tamil language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{version}
Requires:	locales-ta
Requires:	urw-fonts
Obsoletes:	OpenOffice.org-l10n-ta
Provides:	OpenOffice.org-l10n-ta
Obsoletes:	%{ooname}-go-ooo-l10n-ta <= %{version}

%description l10n-ta
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in Tamil.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-tr
Summary:	Turkish language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{version}
Requires:	locales-tr
Requires:	urw-fonts
Obsoletes:	OpenOffice.org-l10n-tr
Obsoletes:	OpenOffice.org-help-tr
Provides:	OpenOffice.org-l10n-tr
Provides:	OpenOffice.org-help-tr
Obsoletes:	%{ooname}-go-ooo-l10n-tr <= %{version}

%description l10n-tr
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in Turkish.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-zh_CN
Summary:	Chinese Simplified language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{version}
Requires:	locales-zh
Requires:	fonts-ttf-chinese
Obsoletes:	OpenOffice.org-l10n-zh_CN
Obsoletes:	OpenOffice.org-help-zh_CN
Provides:	OpenOffice.org-l10n-zh_CN
Provides:	OpenOffice.org-help-zh_CN
Obsoletes:	%{ooname}-go-ooo-l10n-zh_CN <= %{version}

%description l10n-zh_CN
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in Chinese Simplified.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-zh_TW
Summary:	Chinese Traditional language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{version}
Requires:	locales-zh
Requires:	fonts-ttf-chinese
Obsoletes:	OpenOffice.org-l10n-zh_TW
Obsoletes:	OpenOffice.org-help-zh_TW
Provides:	OpenOffice.org-l10n-zh_TW
Provides:	OpenOffice.org-help-zh_TW
Obsoletes:	%{ooname}-go-ooo-l10n-zh_TW <= %{version}

%description l10n-zh_TW
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in Chinese Traditional.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-zu
Summary:	Zulu language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{version}
Requires:	locales-zu
Requires:	urw-fonts
Requires:	myspell-zu
Obsoletes:	OpenOffice.org-l10n-zu
Provides:	OpenOffice.org-l10n-zu
Obsoletes:	%{ooname}-go-ooo-l10n-zu <= %{version}

%description l10n-zu
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in Zulu.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

%prep
%setup -q -n ooo-build-%{ooobuildver}

# Add lzma support
%if %{oootarext} == "lzma"
%patch1 -p1 -b .lzma
%endif

%patch4 -p1 -b .qstart
%patch6 -p1 -b .xpcom
%patch8 -p1 -b .xdg
%patch10 -p1 -b .oooinst
%patch14 -p1 -b .kde
#%patch17 -p1 -b .javac
%if ! %unstable
%patch19 -p1 -b .desktop_files
%endif
%patch16 -p1 -b .ooqstart
%patch23 -p1 -b .angola
%patch24 -p0 -b .wizards

# Fix Icon tags
sed -i s/.png$// desktop/*desktop*

%patch22 -p1 -b .bug26983

# We want odk
#sed -i /disable-odk/d distro-configs/Mandriva*

%build
# Workaround for bug http://qa.mandriva.com/show_bug.cgi?id=27771
if [ -z $QTDIR ]; then
	. /etc/profile.d/qtdir3.sh
fi
%if !%{use_gcj}
if [ -z $JAVA_HOME ]; then
	. /etc/profile.d/jdk-%{jdkver}.sh
fi
%endif

# add moc in PATH
if [ ! -z $QTDIR ]; then
	export QTPATH=$QTDIR/bin
	export PATH=$PATH:$QTPATH
else
	export PATH=$PATH:%{_prefix}/lib/qt3
fi

%if %{use_gcj}
if [ "`readlink -f %{_bindir}/java`" = "%{_bindir}/jamvm" ]; then
	echo "Warning: Alternatives for java-1.4.2-gcj-compat are not installed properly."
	echo "Warning: Try running \"update-alternatives --config java\" before building this package."
	exit 1
fi
%endif

%if !%{use_icecream}
# sbin due to icu stuff there
PATH=/bin:/usr/bin:/usr/X11R6/bin:$QTPATH:/usr/sbin
export PATH
%endif

mkdir -p src
ln -sf %{SOURCE1} src/
ln -sf %{SOURCE2} src/
ln -sf %{SOURCE3} src/
ln -sf %{SOURCE4} src/
ln -sf %{SOURCE5} src/
ln -sf %{SOURCE6} src/
ln -sf %{SOURCE10} src/
ln -sf %{SOURCE11} src/
ln -sf %{SOURCE12} src/
ln -sf %{SOURCE13} src/
ln -sf %{SOURCE17} src/
%if %use_hunspell
ln -sf %{SOURCE18} src/
ln -sf %{SOURCE19} src/
%endif
%if %{use_mono}
ln -sf %{SOURCE20} src/
ln -sf %{SOURCE21} src/
ln -sf %{SOURCE26} src/
%endif
ln -sf %{SOURCE23} src/
ln -sf %{SOURCE24} src/
ln -sf %{SOURCE25} src/
# splash screen
ln -sf %{SOURCE27} src/
ln -sf %{SOURCE28} src/
ln -sf %{SOURCE31} src/
ln -sf %{SOURCE32} src/

if [ -x ./autogen.sh ]; then
	NOCONFIGURE=1 ./autogen.sh --with-distro=%{distroname}
fi

%if %{use_ccache}
export CCACHE_DIR=%{ccachedir}
export PATH=$PATH:%{_libdir}/ccache/bin
%endif

export     ARCH_FLAGS="%{optflags} %{optsafe} -fno-omit-frame-pointer -fno-strict-aliasing"
export  ARCH_FLAGS_CC="%{optflags} %{optsafe} -fno-omit-frame-pointer -fno-strict-aliasing"
export ARCH_FLAGS_CXX="%{optflags} %{optsafe} -fno-omit-frame-pointer -fno-strict-aliasing -fpermissive -fvisibility-inlines-hidden"
export ARCH_FLAGS_OPT="%{optflags} -O2 %{optsafe}"

%if %use_gcj
export JAVA=%java
export JAVAC=%javac
export ANT="%ant"
%endif

CFLAGS="%{optflags} %{optsafe} -fno-omit-frame-pointer -fno-strict-aliasing" \
CXXFLAGS="%{optflags} %{optsafe} -fno-omit-frame-pointer -fno-strict-aliasing -fpermissive -fvisibility-inlines-hidden" \
%configure2_5x \
	--with-distro=%{distroname} \
	--with-vendor=Mandriva \
        --with-tag=%{oootagver} \
	--with-build-version="%{ooobuildver}" \
        --disable-odk \
        --disable-qadevooo \
        --enable-java \
	--enable-gstreamer \
	--with-firefox \
	--with-system-mozilla=firefox \
	--with-system-libs \
	--without-system-hsqldb \
	--without-system-beanshell \
	--without-system-xml-apis \
	--without-system-xerces \
	--without-system-xalan \
	--without-system-xt \
	--without-system-xmlsec \
	--without-system-mspack \
	--with-system-libwps \
	--with-system-libwpd \
	--with-system-libwpg \
	--with-system-libsvg \
	--without-system-sablot \
%ifarch x86_64
	--with-intro-bitmaps="%{SOURCE31}" \
        --with-about-bitmaps="%{SOURCE32}" \
%else
	--with-intro-bitmaps="%{SOURCE27}" \
        --with-about-bitmaps="%{SOURCE28}" \
%endif
%if %use_gcj
	--with-jdk-home=%java_home \
	--with-java-target-version=1.5 \
%else
	--with-jdk-home=$JAVA_HOME \
%endif
%if %{use_systemdb}
        --with-system-db \
	--with-db-jar=%{_datadir}/java/db-%{libdbver}.jar \
%else
	--without-system-db \
%endif
%if %{use_systemboost}
	--with-system-boost \
%endif
        --with-system-gcc \
	--with-lang=%{ooolangs} \
	--with-binsuffix=%{mdvsuffix} \
	--with-installed-ooo-dirname=ooo-%{mdvsuffix} \
	--with-docdir=%{_datadir}/doc/packages/ooo-%{mdvsuffix} \
	--with-system-glitz \
	--with-system-sane-header \
%ifarch x86_64
	--disable-cairo \
	--disable-canvas \
%else
	--with-system-cairo \
%endif
	--with-system-nas \
	--with-dynamic-xinerama \
	--enable-binfilter \
        --enable-access \
%if %use_hunspell
        --enable-hunspell \
%else
	--disable-hunspell \
%endif
%if %{use_openclipart}
	--with-openclipart=%{_datadir}/images/openclipart \
%endif
%if %{use_mono}
	--enable-mono \
%else
	--disable-mono \
%endif
%if %{use_smp}
	--with-num-cpus=${RPM_BUILD_NCPUS:-1} \
%endif
%if %{use_ccache} && !%{use_icecream}
	--with-gcc-speedup=ccache \
%else
 %if !%{use_ccache} && %{use_icecream}
	--with-gcc-speedup=icecream \
	--with-icecream-max-jobs=10 \
	--with-icecream-bindir=%{_libdir}/icecc/bin
 %else
  %if %{use_ccache} && %{use_icecream}
	--with-gcc-speedup=ccache,icecream \
	--with-icecream-max-jobs=10 \
	--with-icecream-bindir=%{_libdir}/icecc/bin
  %endif
 %endif
%endif

make \
	ARCH_FLAGS="%{optflags} %{optsafe} -fno-omit-frame-pointer -fno-strict-aliasing" \
	ARCH_FLAGS_CC="%{optflags} %{optsafe} -fno-omit-frame-pointer -fno-strict-aliasing" \
	ARCH_FLAGS_CXX="%{optflags} %{optsafe} -fno-omit-frame-pointer -fno-strict-aliasing -fpermissive -fvisibility-inlines-hidden" \
	ARCH_FLAGS_OPT="%{optflags} -O2 %{optsafe}"


%install
# sbin due to icu stuff there
PATH=$PATH:/usr/sbin

%if ! %{skip_install}
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}/opt
# <mrl> This is buggy and duplicated.
rm -rf %{buildroot}%{ooodir}/share/template/wizard/letter/
# <mrl> Link to the shared one
rm -rf %{buildroot}%{ooodir}/share/dict/ooo
ln -s %{_datadir}/dict/ooo %{buildroot}%{ooodir}/share/dict
%else
rm -f %{buildroot}%{_menudir}/%{ooomenu}
%endif

# Generate menus
mkdir -p %{buildroot}%{_menudir}

GenerateMenu() {
[ -f "%{buildroot}%{_menudir}/%{ooomenu}" ] || touch %{buildroot}%{_menudir}/%{ooomenu}
mimetypes_item=
[ "$6" != "" ] && mimetypes_item="mimetypes=\"$6\""
cat >> %{buildroot}%{_menudir}/%{ooomenu} << EOF
?package(%{name}): needs=x11 section="$2" icon="$3" title="$4" longtitle="$5" command="oo$1%{mdvsuffix}" \
$mimetypes_item kde_opt="InitialPreference=110" \
xdg="true" \
startup_notify="true"
EOF
}

GenerateMenu calc \
  "Office/Spreadsheets" \
  "ooo-calc%{mdvsuffix}.png" \
  "OpenOffice.org Calc" \
  "OpenOffice.org Spreadsheet" \
  "application/vnd.sun.xml.calc,application/vnd.sun.xml.calc.template,application/vnd.ms-excel,application/vnd.stardivision.calc,application/vnd.stardivision.chart,application/vnd.lotus-1-2-3,text/x-comma-separated-values,application/vnd.oasis.opendocument.spreadsheet,application/vnd.oasis.opendocument.spreadsheet-template"

GenerateMenu draw \
  "Office/Drawing" \
  "ooo-draw%{mdvsuffix}.png" \
  "OpenOffice.org Draw" \
  "OpenOffice.org Drawing" \
  "application/vnd.sun.xml.draw,application/vnd.sun.xml.draw.template,application/vnd.stardivision.draw,application/vnd.oasis.opendocument.graphics,application/vnd.oasis.opendocument.graphics-template"

GenerateMenu impress \
  "Office/Presentations" \
  "ooo-impress%{mdvsuffix}.png" \
  "OpenOffice.org Impress" \
  "OpenOffice.org Presentation" \
  "application/vnd.sun.xml.impress,application/vnd.sun.xml.impress.template,application/vnd.ms-powerpoint,application/vnd.stardivision.impress,application/vnd.oasis.opendocument.presentation,application/vnd.oasis.opendocument.presentation-template"

GenerateMenu writer \
  "Office/Wordprocessors" \
  "ooo-writer%{mdvsuffix}.png" \
  "OpenOffice.org Writer" \
  "OpenOffice.org Word Processing Component" \
  "application/vnd.sun.xml.writer,application/vnd.sun.xml.writer.global,application/vnd.sun.xml.writer.template,application/vnd.ms-word,application/x-mswrite,application/vnd.stardivision.writer,application/vnd.wordperfect,application/wordperfect,application/rtf,text/rtf,application/vnd.oasis.opendocument.text,application/vnd.oasis.opendocument.text-master,application/vnd.oasis.opendocument.text-template,application/vnd.ms-works,application/x-msworks-wp,zz-application/zz-winassoc-wps"

GenerateMenu math \
  "Office/Wordprocessors" \
  "ooo-math%{mdvsuffix}.png" \
  "OpenOffice.org Math" \
  "OpenOffice.org Formula Editor" \
  "application/vnd.stardivision.math,application/vnd.sun.xml.writer.math"

# desktop files
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Office" \
  --add-category="X-MandrivaLinux-CrossDesktop" \
  --add-mime-type="application/vnd.ms-works;application/x-msworks-wp;zz-application/zz-winassoc-wps" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/writer*desktop

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Office" \
  --add-category="X-MandrivaLinux-CrossDesktop" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/calc*desktop

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --remove-category="Graphics" \
  --remove-category="VectorGraphics" \
  --add-category="Office" \
  --add-category="X-MandrivaLinux-CrossDesktop" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/draw*desktop

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Office" \
  --add-category="X-MandrivaLinux-CrossDesktop" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/impress*desktop

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Office" \
  --add-category="X-MandrivaLinux-CrossDesktop" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/math*desktop

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --remove-category="Network" \
  --remove-category="WebDevelopment" \
  --add-category="Office" \
  --add-category="X-MandrivaLinux-CrossDesktop" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/web*desktop

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Office" \
  --add-category="X-MandrivaLinux-CrossDesktop" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/template*desktop

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --remove-category="Database" \
  --add-category="Office" \
  --add-category="X-MandrivaLinux-CrossDesktop" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/base*desktop

# FontOOo|DictOOo wizard
bzcat %{SOURCE50} > %{buildroot}%{_libdir}/ooo-%{mdvsuffix}/share/dict/FontOOo.sxw
install -m 644 %{SOURCE51} %{buildroot}%{_libdir}/ooo-%{mdvsuffix}/share/dict/DicOOo.sxw
chmod 644 %{buildroot}%{_libdir}/ooo-%{mdvsuffix}/share/dict/*sxw

# fix permissions for stripping
find %{buildroot} -type f -exec chmod u+rw '{}' \;

# fix permission of .so libraries
find %{buildroot} -type f \( -name '*.so' -o -name '*.so.*' \) -exec chmod a+x '{}' \;

# remove /usr/bin/soffice (made with update-alternatives)
rm -f %{buildroot}%{_bindir}/soffice

cat build/common_list.txt | \
        grep -v gallery/htmltheme.orig | \
        grep -v ^$ | \
        sed -e 's/^\t//g' > build/common_list_fixed.txt

if [ -f %{buildroot}%{_sysconfdir}/bash_completion.d/ooo-wrapper.sh ]; then
 mv %{buildroot}%{_sysconfdir}/bash_completion.d/ooo-wrapper.sh \
 	%{buildroot}%{_sysconfdir}/bash_completion.d/ooo-wrapper%{mdvsuffix}.sh
fi

if [ -f %{buildroot}%{_sysconfdir}/bash_completion.d/ooffice.sh ]; then
 mv %{buildroot}%{_sysconfdir}/bash_completion.d/ooffice.sh \
 	%{buildroot}%{_sysconfdir}/bash_completion.d/ooffice%{mdvsuffix}.sh
fi

mv %{buildroot}%{_libdir}/pkgconfig/mono-ooo-%{mdvsuffix}.pc \
   %{buildroot}%{_libdir}/pkgconfig/mono-ooo%{mdvsuffix}-2.2.pc

# Install profile.d/ files (#33475)
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
sed 's/@VERSION@/%{mdvsuffix}/g' \
	%{_sourcedir}/openoffice.org.csh > \
	%{buildroot}%{_sysconfdir}/profile.d/openoffice.org.csh
sed 's/@VERSION@/%{mdvsuffix}/g' \
	%{_sourcedir}/openoffice.org.sh > \
	%{buildroot}%{_sysconfdir}/profile.d/openoffice.org.sh

# QA Tools not wanted for now
rm -f %{buildroot}%{ooodir}/program/libcommuni680l?.so
rm -f %{buildroot}%{ooodir}/program/libsimplecm680l?.so
rm -f %{buildroot}%{ooodir}/program/testtool.bin
rm -f %{buildroot}%{ooodir}/program/testtoolrc

%clean
%if ! %{skip_install}
rm -rf %{buildroot}
%endif

%post
%{update_menus}
%{update_desktop_database}
# <mrl> Bogus versioning in previous alternatives setup forces us to do this
# We can safelly remove it, as we are obsoleting that version anyway.
/usr/sbin/update-alternatives --remove ooffice %{_bindir}/ooffice2.1 || :
/usr/sbin/update-alternatives \
        --install %{_bindir}/soffice ooffice   %{_bindir}/ooffice%{mdvsuffix} %{oooaltpri} \
	--slave %{_bindir}/oowriter  oowriter  %{_bindir}/oowriter%{mdvsuffix} \
	--slave %{_bindir}/oobase    oobase    %{_bindir}/oobase%{mdvsuffix} \
	--slave %{_bindir}/ooimpress ooimpress %{_bindir}/ooimpress%{mdvsuffix} \
	--slave %{_bindir}/oocalc    oocalc    %{_bindir}/oocalc%{mdvsuffix} \
        --slave %{_bindir}/ootool    ootool    %{_bindir}/ootool%{mdvsuffix} \
        --slave %{_bindir}/ooweb     ooweb     %{_bindir}/ooweb%{mdvsuffix}
[ -e %{_bindir}/ooffice ] || /usr/sbin/update-alternatives --auto ooffice

%postun
%{clean_menus}
%{clean_desktop_database}
if [ ! -e "%{_bindir}/ooffice%{mdvsuffix}" ]; then
        /usr/sbin/update-alternatives --remove ooffice %{_bindir}/ooffice%{mdvsuffix}
fi

%files base
%{_bindir}/oobase%{mdvsuffix}
%{ooodir}/program/libabp680l?.so
%{ooodir}/program/libadabas2.so
%{ooodir}/program/libdbacfg680l?.so
%{ooodir}/program/libdbase680l?.so
%{ooodir}/program/libdbaxml680l?.so
%{ooodir}/program/libdbp680l?.so
%{ooodir}/program/libdbpool2.so
%{ooodir}/program/libdbu680l?.so
%{ooodir}/program/libflat680l?.so
%{ooodir}/program/libhsqldb2.so
%{ooodir}/program/libjdbc2.so
%{ooodir}/program/libmdb680l?.so
%{ooodir}/program/libmdbimpl680l?.so
%{ooodir}/program/libmysql2.so
%{ooodir}/program/libodbc2.so
%{ooodir}/program/libodbcbase2.so
%{ooodir}/program/librpt680l?.so
%{ooodir}/program/librptui680l?.so
%{ooodir}/program/librptxml680l?.so
%{ooodir}/program/libsdbc2.so
%{ooodir}/program/sbase
%{ooodir}/share/registry/modules/org/openoffice/Office/Common/Common-base.xcu
%{ooodir}/share/registry/modules/org/openoffice/Setup/Setup-base.xcu
%{ooodir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_database_filters.xcu
%{ooodir}/share/registry/modules/org/openoffice/TypeDetection/Misc/fcfg_database_others.xcu
%{ooodir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_database_types.xcu
%{ooodir}/share/xdg/base*.desktop
%{_datadir}/applications/base*.desktop
%{_mandir}/man1/oobase%{mdvsuffix}.1*

%files calc
%{_bindir}/oocalc%{mdvsuffix}
%{ooodir}/program/libanalysis680l?.so
%{ooodir}/program/libcalc680l?.so
%{ooodir}/program/libdate680l?.so
%{ooodir}/program/libsc680l?.so
%{ooodir}/program/libscd680l?.so
%{ooodir}/program/libscui680l?.so
%{ooodir}/program/libvbaobj680l?.uno.so
%{ooodir}/program/scalc
%{ooodir}/share/registry/data/org/openoffice/Office/UI/CalcCommands.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/UI/CalcWindowState.xcu
%{ooodir}/share/registry/modules/org/openoffice/Office/Common/Common-calc.xcu
%{ooodir}/share/registry/modules/org/openoffice/Office/Embedding/Embedding-calc.xcu
%{ooodir}/share/registry/modules/org/openoffice/Setup/Setup-calc.xcu
%{ooodir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_calc_filters.xcu
%{ooodir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_calc_types.xcu
%{ooodir}/share/registry/schema/org/openoffice/Office/UI/CalcCommands.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/UI/CalcWindowState.xcs
%{ooodir}/share/xdg/calc*.desktop
%{_datadir}/applications/calc*.desktop
%{_mandir}/man1/oocalc%{mdvsuffix}.1*

%files common
%{_sysconfdir}/*
%{_bindir}/ooconfig%{mdvsuffix}
%{_bindir}/ooffice%{mdvsuffix}
%{_bindir}/oofromtemplate%{mdvsuffix}
%{_bindir}/ootool%{mdvsuffix}
%{_menudir}/%{ooomenu}
%{ooodir}/LICENSE
%{ooodir}/LICENSE.html
%{ooodir}/README
%{ooodir}/README.html
%{ooodir}/THIRDPARTYLICENSEREADME.html
%dir %{ooodir}/help
%{ooodir}/help/main_transform.xsl
%{ooodir}/help/en
%{ooodir}/install-dict
%dir %{ooodir}/licenses
%{ooodir}/licenses/*_en-US*
%{ooodir}/presets/Scripts
%{ooodir}/presets/autocorr
%{ooodir}/presets/autotext
%{ooodir}/presets/backup
%{ooodir}/presets/basic/Standard/Module1.xba
%{ooodir}/presets/basic/Standard/dialog.xlb
%{ooodir}/presets/basic/Standard/script.xlb
%{ooodir}/presets/basic/dialog.xlc
%{ooodir}/presets/basic/script.xlc
%dir %{ooodir}/presets/config
%{ooodir}/presets/config/*_en-US.so*
%{ooodir}/presets/config/autotbl.fmt
%{ooodir}/presets/config/cmyk.soc
%{ooodir}/presets/config/gallery.soc
%{ooodir}/presets/config/html.soc
%{ooodir}/presets/config/standard.sob
%{ooodir}/presets/config/standard.soc
%{ooodir}/presets/config/standard.sod
%{ooodir}/presets/config/standard.soe
%{ooodir}/presets/config/standard.sog
%{ooodir}/presets/config/standard.soh
%{ooodir}/presets/config/sun-color.soc
%{ooodir}/presets/config/web.soc
%{ooodir}/presets/database
%{ooodir}/presets/gallery
%{ooodir}/presets/psprint
%{ooodir}/presets/store
%{ooodir}/presets/temp
%{ooodir}/presets/template
%{ooodir}/presets/uno_packages
%{ooodir}/presets/wordbook
#%{ooodir}/program/about.bmp
%{ooodir}/program/addin
%{ooodir}/program/bootstraprc
%{ooodir}/program/cde-open-url
%{ooodir}/program/configimport
%{ooodir}/program/configmgrrc
%{ooodir}/program/gnome-open-url
%{ooodir}/program/hid.lst
#%{ooodir}/program/intro.bmp
%{ooodir}/program/java-set-classpath
%{ooodir}/program/jvmfwk3rc
%{ooodir}/program/kde-open-url
%{ooodir}/program/libcppu.so.3
%{ooodir}/program/libcppuhelpergcc3.so.3
%if !%{use_systemdb}
%{ooodir}/program/libdb-4.2.so
%{ooodir}/program/libdb_java-4.2.so
%endif
%{ooodir}/program/libnpsoplugin.so
%{ooodir}/program/libpyuno.so
%{ooodir}/program/libsal.so.3
%{ooodir}/program/libsalhelpergcc3.so.3
%{ooodir}/program/libstlport_gcc.so
%{ooodir}/program/libt602filter680l?.so
%{ooodir}/program/libwpgimport680l?.so
%{ooodir}/program/mailmerge.py
%{ooodir}/program/msfontextract
%{ooodir}/program/nsplugin
%{ooodir}/program/officehelper.py
%{ooodir}/program/open-url
%{ooodir}/program/openabout_mandriva*.bmp
%{ooodir}/program/openintro_mandriva*.bmp
%{ooodir}/program/pagein-calc
%{ooodir}/program/pagein-common
%{ooodir}/program/pagein-draw
%{ooodir}/program/pagein-impress
%{ooodir}/program/pagein-writer
%{ooodir}/program/pkgchk
%{ooodir}/program/plugin
%{ooodir}/program/pythonloader.py
%{ooodir}/program/pythonloader.uno.so
%{ooodir}/program/pythonloader.unorc
%{ooodir}/program/pythonscript.py
%{ooodir}/program/pyuno.so
%dir %{ooodir}/program/resource
%{ooodir}/program/resource/*-US.res
%{ooodir}/program/root3.dat
%{ooodir}/program/root4.dat
%{ooodir}/program/root5.dat
%{ooodir}/program/senddoc
%{ooodir}/program/setofficelang
%{ooodir}/program/setuprc
%{ooodir}/program/soffice
%{ooodir}/program/sofficerc
%{ooodir}/program/spadmin
%{ooodir}/program/uno
%{ooodir}/program/uno.py
%{ooodir}/program/unohelper.py
%{ooodir}/program/unopkg
%{ooodir}/program/unorc
%{ooodir}/program/versionrc
%{ooodir}/program/viewdoc
%{ooodir}/readmes/README_en-US
%{ooodir}/readmes/README_en-US.html
%{ooodir}/share/Scripts/beanshell
%{ooodir}/share/Scripts/javascript
%{ooodir}/share/Scripts/python
%dir %{ooodir}/share/autocorr
# FIXME: Should be l10n
%{ooodir}/share/autocorr/*
%dir %{ooodir}/share/autotext
%{ooodir}/share/autotext/en-US
%{ooodir}/share/basic
%{ooodir}/share/config/javasettingsunopkginstall.xml
%{ooodir}/share/config/javavendors.xml
%{ooodir}/share/config/psetup.xpm
%{ooodir}/share/config/psetupl.xpm
%{ooodir}/share/config/soffice.cfg/global
%{ooodir}/share/config/soffice.cfg/modules
%{ooodir}/share/config/symbol
%{ooodir}/share/config/webcast
%{ooodir}/share/config/wizard
# FIXME: Fix hyph in l10n packages
%dir %{ooodir}/share/dict
# FIXME: Wrong place?
%{ooodir}/share/dict/*.sxw
# FIXME: Should be l10n!!
%{ooodir}/share/dict/ooo
%{ooodir}/share/extension
%{ooodir}/share/fingerprint/
%{ooodir}/share/fonts
%{ooodir}/share/psprint
%dir %{ooodir}/share/readme
%{ooodir}/share/readme/*_en-US*
%{ooodir}/share/registry/data/org/openoffice/FirstStartWizard.xcu
%{ooodir}/share/registry/data/org/openoffice/Inet.xcu
%{ooodir}/share/registry/data/org/openoffice/LDAP.xcu.sample
%{ooodir}/share/registry/data/org/openoffice/Office/Calc.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/Common.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/Compatibility.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/DataAccess.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/Embedding.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/ExtendedColorScheme.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/ExtensionManager.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/FormWizard.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/Impress.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/Jobs.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/Labels.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/Logging.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/Math.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/Paths.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/ProtocolHandler.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/SFX.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/Scripting.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/Security.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/TableWizard.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/UI.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/UI/BaseWindowState.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/UI/BasicIDECommands.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/UI/BasicIDEWindowState.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/UI/BibliographyCommands.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/UI/ChartCommands.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/UI/ChartWindowState.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/UI/Controller.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/UI/DbBrowserWindowState.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/UI/DbQueryWindowState.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/UI/DbRelationWindowState.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/UI/DbReportWindowState.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/UI/DbTableWindowState.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/UI/DbuCommands.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/UI/DrawImpressCommands.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/UI/Factories.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/UI/GenericCategories.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/UI/GenericCommands.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/UI/ReportCommands.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/UI/StartModuleCommands.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/UI/StartModuleWindowState.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/UI/WriterFormWindowState.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/UI/WriterReportWindowState.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/UI/XFormsWindowState.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/Views.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/WebWizard.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/Writer.xcu
%{ooodir}/share/registry/data/org/openoffice/Setup.xcu
%{ooodir}/share/registry/data/org/openoffice/TypeDetection
%{ooodir}/share/registry/data/org/openoffice/UserProfile.xcu
%{ooodir}/share/registry/data/org/openoffice/VCL.xcu
%{ooodir}/share/registry/data/org/openoffice/ucb
%{ooodir}/share/registry/ldap
%{ooodir}/share/registry/modules/org/openoffice/Office/Common/Common-UseOOoFileDialogs.xcu
%{ooodir}/share/registry/modules/org/openoffice/Office/Common/Common-unx.xcu
%{ooodir}/share/registry/modules/org/openoffice/Office/Embedding/Embedding-chart.xcu
%{ooodir}/share/registry/modules/org/openoffice/Office/Embedding/Embedding-report.xcu
%{ooodir}/share/registry/modules/org/openoffice/Office/Scripting
%{ooodir}/share/registry/modules/org/openoffice/Office/Writer/Writer-javamail.xcu
%{ooodir}/share/registry/modules/org/openoffice/Setup/Langpack-en-US.xcu
%{ooodir}/share/registry/modules/org/openoffice/Setup/Setup-report.xcu
%{ooodir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_base_filters.xcu
%{ooodir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_chart_filters.xcu
%{ooodir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_xslt_filters.xcu
%{ooodir}/share/registry/modules/org/openoffice/TypeDetection/GraphicFilter
%{ooodir}/share/registry/modules/org/openoffice/TypeDetection/Misc/fcfg_base_others.xcu
%{ooodir}/share/registry/modules/org/openoffice/TypeDetection/Misc/fcfg_chart_others.xcu
%{ooodir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_base_types.xcu
%{ooodir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_chart_types.xcu
%{ooodir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_internalgraphics_types.xcu
%{ooodir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_xslt_types.xcu
%{ooodir}/share/registry/modules/org/openoffice/TypeDetection/UISort
%dir %{ooodir}/share/registry/res
%{ooodir}/share/registry/res/en-US
%{ooodir}/share/registry/schema/org/openoffice/FirstStartWizard.xcs
%{ooodir}/share/registry/schema/org/openoffice/Inet.xcs
%{ooodir}/share/registry/schema/org/openoffice/LDAP.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/Addons.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/Calc.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/CalcAddIns.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/Chart.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/Commands.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/Common.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/Compatibility.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/DataAccess.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/Draw.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/Embedding.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/Events.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/ExtendedColorScheme.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/ExtensionManager.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/FormWizard.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/Impress.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/Java.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/Jobs.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/Labels.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/Linguistic.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/Logging.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/Math.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/OptionsDialog.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/Paths.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/ProtocolHandler.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/Recovery.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/ReportDesign.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/SFX.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/Scripting.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/Security.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/Substitution.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/TabBrowse.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/TableWizard.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/TypeDetection.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/UI.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/UI/BaseWindowState.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/UI/BasicIDECommands.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/UI/BasicIDEWindowState.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/UI/BibliographyCommands.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/UI/BibliographyWindowState.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/UI/Category.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/UI/ChartCommands.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/UI/ChartWindowState.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/UI/Commands.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/UI/Controller.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/UI/DbBrowserWindowState.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/UI/DbQueryWindowState.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/UI/DbRelationWindowState.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/UI/DbReportWindowState.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/UI/DbTableWindowState.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/UI/DbuCommands.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/UI/DrawImpressCommands.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/UI/Factories.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/UI/GenericCategories.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/UI/GenericCommands.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/UI/GlobalSettings.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/UI/MathWindowState.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/UI/ReportCommands.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/UI/StartModuleCommands.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/UI/StartModuleWindowState.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/UI/WindowState.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/UI/WriterFormWindowState.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/UI/WriterReportWindowState.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/UI/XFormsWindowState.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/Views.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/WebWizard.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/Writer.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/WriterWeb.xcs
%{ooodir}/share/registry/schema/org/openoffice/Setup.xcs
%{ooodir}/share/registry/schema/org/openoffice/System.xcs
%{ooodir}/share/registry/schema/org/openoffice/TypeDetection
%{ooodir}/share/registry/schema/org/openoffice/UserProfile.xcs
%{ooodir}/share/registry/schema/org/openoffice/VCL.xcs
%{ooodir}/share/registry/schema/org/openoffice/ucb
%dir %{ooodir}/share/samples
%dir %{ooodir}/share/template
%{ooodir}/share/template/en-US
%{ooodir}/share/uno_packages
%dir %{ooodir}/share/wordbook
%{ooodir}/share/wordbook/en-US
%{ooodir}/share/xdg/extension*.desktop
%{ooodir}/share/xdg/printeradmin*.desktop
%{ooodir}/share/xslt
%{_datadir}/applications/template*.desktop
%{_datadir}/icons/hicolor/*/apps/ooo-base%{mdvsuffix}.*
%{_datadir}/icons/hicolor/*/apps/ooo-calc%{mdvsuffix}.*
%{_datadir}/icons/hicolor/*/apps/ooo-draw%{mdvsuffix}.*
%{_datadir}/icons/hicolor/*/apps/ooo-gulls%{mdvsuffix}.*
%{_datadir}/icons/hicolor/*/apps/ooo-impress%{mdvsuffix}.*
%{_datadir}/icons/hicolor/*/apps/ooo-math%{mdvsuffix}.*
%{_datadir}/icons/hicolor/*/apps/ooo-printeradmin%{mdvsuffix}.*
%{_datadir}/icons/hicolor/*/apps/ooo-template%{mdvsuffix}.*
%{_datadir}/icons/hicolor/*/apps/ooo-web%{mdvsuffix}.*
%{_datadir}/icons/hicolor/*/apps/ooo-writer%{mdvsuffix}.*
%{_datadir}/pixmaps/ooo-base%{mdvsuffix}.png
%{_datadir}/pixmaps/ooo-calc%{mdvsuffix}.png
%{_datadir}/pixmaps/ooo-draw%{mdvsuffix}.png
%{_datadir}/pixmaps/ooo-gulls%{mdvsuffix}.png
%{_datadir}/pixmaps/ooo-impress%{mdvsuffix}.png
%{_datadir}/pixmaps/ooo-math%{mdvsuffix}.png
%{_datadir}/pixmaps/ooo-template%{mdvsuffix}.png
%{_datadir}/pixmaps/ooo-web%{mdvsuffix}.png
%{_datadir}/pixmaps/ooo-writer%{mdvsuffix}.png
%{_mandir}/man1/ooffice%{mdvsuffix}.1*
%{_mandir}/man1/oofromtemplate%{mdvsuffix}.1*
%{_mandir}/man1/openoffice%{mdvsuffix}.1*
%{_datadir}/mime

%files core
%{ooodir}/program/acceptor.uno.so
%{ooodir}/program/basprov680l?.uno.so
%{ooodir}/program/behelper.uno.so
%{ooodir}/program/bridgefac.uno.so
# As I don't know how to make !x86_64
%ifarch i586
%{ooodir}/program/cairocanvas.uno.so
%endif
%{ooodir}/program/canvasfactory.uno.so
%{ooodir}/program/cmdmail.uno.so
%{ooodir}/program/configimport.bin
%{ooodir}/program/configmgr2.uno.so
%{ooodir}/program/connector.uno.so
%{ooodir}/program/deployment680l?.uno.so
%{ooodir}/program/deploymentgui680l?.uno.so
%{ooodir}/program/desktopbe1.uno.so
%{ooodir}/program/dlgprov680l?.uno.so
%{ooodir}/program/fastsax.uno.so
%{ooodir}/program/fpicker.uno.so
%{ooodir}/program/fps_office.uno.so
%{ooodir}/program/fsstorage.uno.so
%{ooodir}/program/hatchwindowfactory.uno.so
%{ooodir}/program/i18npool.uno.so
%{ooodir}/program/i18nsearch.uno.so
%{ooodir}/program/implreg.uno.so
%{ooodir}/program/introspection.uno.so
%{ooodir}/program/invocadapt.uno.so
%{ooodir}/program/invocation.uno.so
%{ooodir}/program/javaldx
%{ooodir}/program/javaloader.uno.so
%{ooodir}/program/javavm.uno.so
%{ooodir}/program/ldapbe2.uno.so
%{ooodir}/program/libacc680l?.so
%{ooodir}/program/libaffine_uno_uno.so
%{ooodir}/program/libavmedia680l?.so
%{ooodir}/program/libavmediagst.so
%{ooodir}/program/libbasctl680l?.so
%{ooodir}/program/libbasebmp680l?.so
%{ooodir}/program/libbasegfx680l?.so
%{ooodir}/program/libbf_sb680l?.so
%{ooodir}/program/libbib680l?.so
%{ooodir}/program/libcached1.so
%{ooodir}/program/libcanvastools680l?.so
%{ooodir}/program/libchartcontroller680l?.so
%{ooodir}/program/libchartmodel680l?.so
%{ooodir}/program/libcharttools680l?.so
%{ooodir}/program/libchartview680l?.so
%{ooodir}/program/libcollator_data.so
%{ooodir}/program/libcomphelp4gcc3.so
%{ooodir}/program/libcppcanvas680l?.so
%{ooodir}/program/libctl680l?.so
%{ooodir}/program/libcui680l?.so
%{ooodir}/program/libdba680l?.so
%{ooodir}/program/libdbtools680l?.so
%{ooodir}/program/libdeploymentmisc680l?.so
%{ooodir}/program/libdict_ja.so
%{ooodir}/program/libdict_zh.so
%{ooodir}/program/libdtransX11680l?.so
%{ooodir}/program/libegi680l?.so
%{ooodir}/program/libembobj.so
%{ooodir}/program/libemboleobj.so
%{ooodir}/program/libeme680l?.so
%{ooodir}/program/libemp680l?.so
%{ooodir}/program/libepb680l?.so
%{ooodir}/program/libepg680l?.so
%{ooodir}/program/libepp680l?.so
%{ooodir}/program/libeps680l?.so
%{ooodir}/program/libept680l?.so
%{ooodir}/program/libera680l?.so
%{ooodir}/program/libeti680l?.so
%{ooodir}/program/libevoab1.so
%{ooodir}/program/libevtatt.so
%{ooodir}/program/libexlink680l?.so
%{ooodir}/program/libexp680l?.so
%{ooodir}/program/libfile680l?.so
%{ooodir}/program/libfileacc.so
%{ooodir}/program/libfilterconfig1.so
%{ooodir}/program/libfrm680l?.so
%{ooodir}/program/libfwe680l?.so
%{ooodir}/program/libfwi680l?.so
%{ooodir}/program/libfwk680l?.so
%{ooodir}/program/libfwl680l?.so
%{ooodir}/program/libfwm680l?.so
%{ooodir}/program/libgcc3_uno.so
%{ooodir}/program/libgo680l?.so
%{ooodir}/program/libguesslang680l?.so
%{ooodir}/program/libhunspell.so
%{ooodir}/program/libhyphen680l?.so
%{ooodir}/program/libi18nisolang1gcc3.so
%{ooodir}/program/libi18nregexpgcc3.so
%{ooodir}/program/libi18nutilgcc3.so
%{ooodir}/program/libicd680l?.so
%{ooodir}/program/libicg680l?.so
%{ooodir}/program/libidx680l?.so
%{ooodir}/program/libime680l?.so
%{ooodir}/program/libindex_data.so
%{ooodir}/program/libipb680l?.so
%{ooodir}/program/libipd680l?.so
%{ooodir}/program/libips680l?.so
%{ooodir}/program/libipt680l?.so
%{ooodir}/program/libipx680l?.so
%{ooodir}/program/libira680l?.so
%{ooodir}/program/libitg680l?.so
%{ooodir}/program/libiti680l?.so
%{ooodir}/program/libj680l?_g.so
%{ooodir}/program/libjava_uno.so
%{ooodir}/program/libjpipe.so
%{ooodir}/program/libjuh.so
%{ooodir}/program/libjuhx.so
%{ooodir}/program/libjvmaccessgcc3.so.3
%{ooodir}/program/libjvmfwk.so.3
%{ooodir}/program/liblng680l?.so
%{ooodir}/program/liblnth680l?.so
%{ooodir}/program/liblocaledata_en.so
%{ooodir}/program/liblocaledata_es.so
%{ooodir}/program/liblocaledata_euro.so
%{ooodir}/program/liblocaledata_others.so
%{ooodir}/program/liblog680l?.so
%{ooodir}/program/libmcnttype.so
%{ooodir}/program/liboffacc680l?.so
%{ooodir}/program/liboox680l?.so
%{ooodir}/program/libpackage2.so
%{ooodir}/program/libpcr680l?.so
%{ooodir}/program/libpdffilter680l?.so
%{ooodir}/program/libpl680l?.so
%{ooodir}/program/libpreload680l?.so
%{ooodir}/program/libprotocolhandler680l?.so
%{ooodir}/program/libpsp680l?.so
%{ooodir}/program/librecentfile.so
%{ooodir}/program/libreg.so.3
%{ooodir}/program/libres680l?.so
%{ooodir}/program/librmcxt.so.3
%{ooodir}/program/libsax680l?.so
%{ooodir}/program/libsb680l?.so
%{ooodir}/program/libscn680l?.so
%{ooodir}/program/libscriptframe.so
%{ooodir}/program/libsdbt680l?.so
%{ooodir}/program/libsfx680l?.so
%{ooodir}/program/libso680l?.so
%{ooodir}/program/libsot680l?.so
%{ooodir}/program/libspa680l?.so
%{ooodir}/program/libspell680l?.so
%{ooodir}/program/libspl680l?.so
%{ooodir}/program/libspl_unx680l?.so
%{ooodir}/program/libsrtrs1.so
%{ooodir}/program/libstore.so.3
%{ooodir}/program/libsts680l?.so
%{ooodir}/program/libsvl680l?.so
%{ooodir}/program/libsvt680l?.so
%{ooodir}/program/libsvx680l?.so
%{ooodir}/program/libtextcat.so
%{ooodir}/program/libtextconv_dict.so
%{ooodir}/program/libtextconversiondlgs680l?.so
%{ooodir}/program/libtfu680l?.so
%{ooodir}/program/libtk680l?.so
%{ooodir}/program/libtl680l?.so
%{ooodir}/program/libtvhlp1.so
%{ooodir}/program/libucb1.so
%{ooodir}/program/libucbhelper4gcc3.so
%{ooodir}/program/libucpchelp1.so
%{ooodir}/program/libucpdav1.so
%{ooodir}/program/libucpfile1.so
%{ooodir}/program/libucpftp1.so
%{ooodir}/program/libucphier1.so
%{ooodir}/program/libucppkg1.so
%{ooodir}/program/libuno_cppu.so.3
%{ooodir}/program/libuno_cppuhelpergcc3.so.3
%{ooodir}/program/libuno_purpenvhelpergcc3.so.3
%{ooodir}/program/libuno_sal.so.3
%{ooodir}/program/libuno_salhelpergcc3.so.3
%{ooodir}/program/libunoxml680l?.so
%{ooodir}/program/libunsafe_uno_uno.so
%{ooodir}/program/libupdchk680l?.so
%{ooodir}/program/liburp_uno.so
%{ooodir}/program/libutl680l?.so
%{ooodir}/program/libuui680l?.so
%{ooodir}/program/libvcl680l?.so
%{ooodir}/program/libvclplug_gen680l?.so
%{ooodir}/program/libvclplug_svp680l?.so
%{ooodir}/program/libvos3gcc3.so
%{ooodir}/program/libwriterfilter680l?.so
%{ooodir}/program/libxcr680l?.so
%{ooodir}/program/libxmlfa680l?.so
%{ooodir}/program/libxmlfd680l?.so
%{ooodir}/program/libxmlsec1-nss.so*
%{ooodir}/program/libxmlsec1.so*
%{ooodir}/program/libxmlsecurity.so
%{ooodir}/program/libxmx680l?.so
%{ooodir}/program/libxo680l?.so
%{ooodir}/program/libxof680l?.so
%{ooodir}/program/libxsec_fw.so
%{ooodir}/program/libxsec_xmlsec.so
%{ooodir}/program/libxsltdlg680l?.so
%{ooodir}/program/libxsltfilter680l?.so
%{ooodir}/program/libxstor.so
%{ooodir}/program/localebe1.uno.so
%{ooodir}/program/migrationoo2.uno.so
%{ooodir}/program/namingservice.uno.so
%{ooodir}/program/nestedreg.uno.so
%{ooodir}/program/oosplash.bin
%{ooodir}/program/oovbaapi.rdb
%{ooodir}/program/pagein
%{ooodir}/program/passwordcontainer.uno.so
%{ooodir}/program/pkgchk.bin
%{ooodir}/program/pluginapp.bin
%{ooodir}/program/productregistration.uno.so
%{ooodir}/program/proxyfac.uno.so
%{ooodir}/program/reflection.uno.so
%{ooodir}/program/regtypeprov.uno.so
%{ooodir}/program/remotebridge.uno.so
%{ooodir}/program/sax.uno.so
%{ooodir}/program/security.uno.so
%{ooodir}/program/servicemgr.uno.so
%{ooodir}/program/services.rdb
%{ooodir}/program/setofficelang.bin
%{ooodir}/program/shlibloader.uno.so
%{ooodir}/program/simplecanvas.uno.so
%{ooodir}/program/simplereg.uno.so
%{ooodir}/program/soffice.bin
%{ooodir}/program/spadmin.bin
%{ooodir}/program/streams.uno.so
%{ooodir}/program/stringresource680l?.uno.so
%{ooodir}/program/sunjavaplugin.so
%{ooodir}/program/svtmisc.uno.so
%{ooodir}/program/sysmgr1.uno.so
%{ooodir}/program/syssh.uno.so
%{ooodir}/program/textinstream.uno.so
%{ooodir}/program/textoutstream.uno.so
%{ooodir}/program/typeconverter.uno.so
%{ooodir}/program/typemgr.uno.so
%{ooodir}/program/types.rdb
%{ooodir}/program/ucpexpand1.uno.so
%{ooodir}/program/ucptdoc1.uno.so
%{ooodir}/program/uno.bin
%{ooodir}/program/unopkg.bin
%{ooodir}/program/updatefeed.uno.so
%{ooodir}/program/uri-encode
%{ooodir}/program/uriproc.uno.so
%{ooodir}/program/uuresolver.uno.so
%{ooodir}/program/vbaevents680l?.uno.so
%{ooodir}/program/vclcanvas.uno.so

%files devel
#%{_includedir}/*
%{ooodir}/program/gengal
%{ooodir}/program/gengal.bin
%{ooodir}/program/libcppu.so
%{ooodir}/program/libcppuhelper3gcc3.so
%{ooodir}/program/libcppuhelpergcc3.so
%{ooodir}/program/libjvmaccessgcc3.so
%{ooodir}/program/libjvmfwk.so
%{ooodir}/program/libreg.so
%{ooodir}/program/librmcxt.so
%{ooodir}/program/libsal.so
%{ooodir}/program/libsalhelper3gcc3.so
%{ooodir}/program/libsalhelpergcc3.so
%{ooodir}/program/libstore.so
%{ooodir}/program/libuno_cppu.so
%{ooodir}/program/libuno_cppuhelpergcc3.so
%{ooodir}/program/libuno_sal.so
%{ooodir}/program/libuno_salhelpergcc3.so
#%{ooodir}/sdk/classes
#%{ooodir}/sdk/config.guess
#%{ooodir}/sdk/config.sub
#%{ooodir}/sdk/configure.pl
#%{ooodir}/sdk/idl
#%{ooodir}/sdk/include
#%{ooodir}/sdk/linux
#%{ooodir}/sdk/setsdkenv_unix
#%{ooodir}/sdk/setsdkenv_unix.csh
#%{ooodir}/sdk/setsdkenv_unix.csh.in
#%{ooodir}/sdk/setsdkenv_unix.sh
#%{ooodir}/sdk/setsdkenv_unix.sh.in
#%{ooodir}/sdk/settings
#%{ooodir}/sdk/xml
#%{_datadir}/idl
#%{_datadir}/xml/ooo-%{mdvsuffix}

%files devel-doc
#%{_docdir}/packages/ooo-%{mdvsuffix}
#%{ooodir}/sdk/docs
#%{ooodir}/sdk/examples
#%{ooodir}/sdk/index.html

%files draw
%{_bindir}/oodraw%{mdvsuffix}
%{ooodir}/program/libflash680l?.so
%{ooodir}/program/libsd680l?.so
%{ooodir}/program/libsdd680l?.so
%{ooodir}/program/libsdui680l?.so
%{ooodir}/program/libsvgfilter680l?.so
%{ooodir}/program/sdraw
%{ooodir}/share/registry/data/org/openoffice/Office/UI/DrawWindowState.xcu
%{ooodir}/share/registry/modules/org/openoffice/Office/Common/Common-draw.xcu
%{ooodir}/share/registry/modules/org/openoffice/Office/Embedding/Embedding-draw.xcu
%{ooodir}/share/registry/modules/org/openoffice/Setup/Setup-draw.xcu
%{ooodir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_draw_filters.xcu
%{ooodir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_drawgraphics_filters.xcu
%{ooodir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_draw_types.xcu
%{ooodir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_drawgraphics_types.xcu
%{ooodir}/share/registry/schema/org/openoffice/Office/UI/DrawWindowState.xcs
%{ooodir}/share/xdg/draw*.desktop
%{_datadir}/applications/draw*.desktop
%{_mandir}/man1/oodraw%{mdvsuffix}.1*

%files dtd-officedocument1.0
%{ooodir}/share/dtd/officedocument

%files evolution
%{ooodir}/program/libevoab2.so

%files filter-binfilter
%{ooodir}/program/legacy_binfilters.rdb
%{ooodir}/program/libbf_frm680l?.so
%{ooodir}/program/libbf_go680l?.so
%{ooodir}/program/libbf_migratefilter680l?.so
%{ooodir}/program/libbf_ofa680l?.so
%{ooodir}/program/libbf_sc680l?.so
%{ooodir}/program/libbf_sch680l?.so
%{ooodir}/program/libbf_sd680l?.so
%{ooodir}/program/libbf_sm680l?.so
%{ooodir}/program/libbf_svx680l?.so
%{ooodir}/program/libbf_sw680l?.so
%{ooodir}/program/libbf_wrapper680l?.so
%{ooodir}/program/libbf_xo680l?.so
%{ooodir}/program/libbindet680l?.so
%{ooodir}/program/liblegacy_binfilters680l?.so

%files filter-mobiledev
%{ooodir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_palm_filters.xcu
%{ooodir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_pocketexcel_filters.xcu
%{ooodir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_pocketword_filters.xcu
%{ooodir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_palm_types.xcu
%{ooodir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_pocketexcel_types.xcu
%{ooodir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_pocketword_types.xcu

%files gnome
%{ooodir}/program/gnome-set-default-application
%{ooodir}/program/ucpgvfs1.uno.so

%files gtk
%{ooodir}/program/fps_gnome.uno.so
%{ooodir}/program/gconfbe1.uno.so
%{ooodir}/program/gnome-open-url.bin
%{ooodir}/program/libeggtray680l?.so
%{ooodir}/program/libqstart_gtk680l?.so
%{ooodir}/program/libvclplug_gtk680l?.so
%{ooodir}/share/xdg/qstart*.desktop

%files impress
%{_bindir}/ooimpress%{mdvsuffix}
%{ooodir}/program/libanimcore.so
%{ooodir}/program/libplacewarel?.so
%{ooodir}/program/simpress
%{ooodir}/program/slideshow.uno.so
%{ooodir}/share/config/soffice.cfg/simpress
%{ooodir}/share/registry/data/org/openoffice/Office/UI/Effects.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/UI/ImpressWindowState.xcu
%{ooodir}/share/registry/modules/org/openoffice/Office/Common/Common-impress.xcu
%{ooodir}/share/registry/modules/org/openoffice/Office/Embedding/Embedding-impress.xcu
%{ooodir}/share/registry/modules/org/openoffice/Setup/Setup-impress.xcu
%{ooodir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_impress_filters.xcu
%{ooodir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_impressgraphics_filters.xcu
%{ooodir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_impress_types.xcu
%{ooodir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_impressgraphics_types.xcu
%{ooodir}/share/registry/schema/org/openoffice/Office/UI/Effects.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/UI/ImpressWindowState.xcs
%{ooodir}/share/xdg/impress*.desktop
%{_datadir}/applications/impress*.desktop
%{_mandir}/man1/ooimpress%{mdvsuffix}.1*

%files java-common
%{ooodir}/program/JREProperties.class
%{ooodir}/program/classes
%{ooodir}/program/libofficebean.so
%{ooodir}/share/Scripts/java

%files kde
%{ooodir}/program/fps_kde.uno.so
%{ooodir}/program/kdebe1.uno.so
%{ooodir}/program/kdefilepicker
%{ooodir}/program/libkab1.so
%{ooodir}/program/libkabdrv1.so
%{ooodir}/program/libvclplug_kde680l?.so

%files math
%{_bindir}/oomath%{mdvsuffix}
%{ooodir}/program/libsm680l?.so
%{ooodir}/program/libsmd680l?.so
%{ooodir}/program/smath
%{ooodir}/share/dtd/math/1_01
%{ooodir}/share/registry/data/org/openoffice/Office/UI/MathCommands.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/UI/MathWindowState.xcu
%{ooodir}/share/registry/modules/org/openoffice/Office/Common/Common-math.xcu
%{ooodir}/share/registry/modules/org/openoffice/Office/Embedding/Embedding-math.xcu
%{ooodir}/share/registry/modules/org/openoffice/Setup/Setup-math.xcu
%{ooodir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_math_filters.xcu
%{ooodir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_math_types.xcu
%{ooodir}/share/registry/schema/org/openoffice/Office/UI/MathCommands.xcs
%{ooodir}/share/xdg/math*.desktop
%{_datadir}/applications/math*.desktop
%{_mandir}/man1/oomath%{mdvsuffix}.1*

%files openclipart
%{ooodir}/share/gallery

%files

#%files qa-api-tests
#%{ooodir}/qadevOOo

#%files qa-tools
#%{_bindir}/oosmoketest
#%{_bindir}/ootestapi
#%{_bindir}/ootesttool
#%{ooodir}/presets/basic/Standard/Global.xba
#%{ooodir}/presets/basic/Standard/Test_10er.xba
#%{ooodir}/presets/basic/Standard/Test_DB.xba
#%{ooodir}/presets/basic/Standard/Test_Ext.xba
#%{ooodir}/program/libcommuni680l?.so
#%{ooodir}/program/libsimplecm680l?.so
#%{ooodir}/program/testtool.bin
#%{ooodir}/program/testtoolrc
#%{ooodir}/qatesttool
#%{ooodir}/smoketest
#%{_datadir}/doc/openoffice.org-core/README.qa
#%{_datadir}/doc/openoffice.org-qa-tools
#%{_datadir}/java/openoffice/OOoRunnerLight.jar
#%{_datadir}/lintian/overrides/openoffice.org-qa-tools

%files style-andromeda
%{ooodir}/share/config/images.zip

%files style-crystal
%{ooodir}/share/config/images_crystal.zip

%files style-hicontrast
%{ooodir}/share/config/images_hicontrast.zip

%files style-industrial
%{ooodir}/share/config/images_industrial.zip

%files style-tango
%{ooodir}/share/config/images_tango.zip

%files writer
%{_bindir}/ooweb%{mdvsuffix}
%{_bindir}/oowriter%{mdvsuffix}
%{ooodir}/program/libhwp.so
%{ooodir}/program/liblwpft680l?.so
%{ooodir}/program/libmsworks680l?.so
%{ooodir}/program/libsw680l?.so
%{ooodir}/program/libswd680l?.so
%{ooodir}/program/libswui680l?.so
%{ooodir}/program/libwpft680l?.so
%{ooodir}/program/swriter
%{ooodir}/share/registry/data/org/openoffice/Office/UI/WriterCommands.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/UI/WriterGlobalWindowState.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/UI/WriterWebWindowState.xcu
%{ooodir}/share/registry/data/org/openoffice/Office/UI/WriterWindowState.xcu
%{ooodir}/share/registry/modules/org/openoffice/Office/Common/Common-dicooo.xcu
%{ooodir}/share/registry/modules/org/openoffice/Office/Common/Common-writer.xcu
%{ooodir}/share/registry/modules/org/openoffice/Office/Embedding/Embedding-writer.xcu
%{ooodir}/share/registry/modules/org/openoffice/Setup/Setup-writer.xcu
%{ooodir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_global_filters.xcu
%{ooodir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_web_filters.xcu
%{ooodir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_writer_filters.xcu
%{ooodir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_global_types.xcu
%{ooodir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_web_types.xcu
%{ooodir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_writer_types.xcu
%{ooodir}/share/registry/schema/org/openoffice/Office/UI/WriterCommands.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/UI/WriterGlobalWindowState.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/UI/WriterWebWindowState.xcs
%{ooodir}/share/registry/schema/org/openoffice/Office/UI/WriterWindowState.xcs
%{ooodir}/share/xdg/writer*.desktop
%{_datadir}/applications/writer*.desktop
%{_datadir}/applications/web*.desktop
%{_mandir}/man1/ooweb%{mdvsuffix}.1*
%{_mandir}/man1/oowriter%{mdvsuffix}.1*

############################
############################
############################
############################
############################
############################

%if %{use_mono}
%files mono -f build/mono_list.txt
%defattr(-,root,root)
%{_libdir}/pkgconfig/mono-ooo%{mdvsuffix}-2.2.pc
%endif

%files l10n-it -f build/lang_it_list.txt
%defattr(-,root,root)

%files l10n-af -f build/lang_af_list.txt
%defattr(-,root,root)

%files l10n-ar -f build/lang_ar_list.txt
%defattr(-,root,root)

%files l10n-bg -f build/lang_bg_list.txt
%defattr(-,root,root)

%files l10n-br -f build/lang_br_list.txt
%defattr(-,root,root)

%files l10n-bs -f build/lang_bs_list.txt
%defattr(-,root,root)

%files l10n-ca -f build/lang_ca_list.txt
%defattr(-,root,root)

%files l10n-cs -f build/lang_cs_list.txt
%defattr(-,root,root)

%files l10n-cy -f build/lang_cy_list.txt
%defattr(-,root,root)

%files l10n-da -f build/lang_da_list.txt
%defattr(-,root,root)

%files l10n-de -f build/lang_de_list.txt
%defattr(-,root,root)

%files l10n-el -f build/lang_el_list.txt
%defattr(-,root,root)

%files l10n-en_GB -f build/lang_en-GB_list.txt
%defattr(-,root,root)

%files l10n-es -f build/lang_es_list.txt
%defattr(-,root,root)

%files l10n-et -f build/lang_et_list.txt
%defattr(-,root,root)

%files l10n-eu -f build/lang_eu_list.txt
%defattr(-,root,root)

%files l10n-fi -f build/lang_fi_list.txt
%defattr(-,root,root)

%files l10n-fr -f build/lang_fr_list.txt
%defattr(-,root,root)

%files l10n-he -f build/lang_he_list.txt
%defattr(-,root,root)

%files l10n-hi -f build/lang_hi_list.txt
%defattr(-,root,root)

%files l10n-hu -f build/lang_hu_list.txt
%defattr(-,root,root)

%files l10n-ja -f build/lang_ja_list.txt
%defattr(-,root,root)

%files l10n-ko -f build/lang_ko_list.txt
%defattr(-,root,root)

%files l10n-mk -f build/lang_mk_list.txt
%defattr(-,root,root)

%files l10n-nb -f build/lang_nb_list.txt
%defattr(-,root,root)

%files l10n-nl -f build/lang_nl_list.txt
%defattr(-,root,root)

%files l10n-nn -f build/lang_nn_list.txt
%defattr(-,root,root)

%files l10n-pl -f build/lang_pl_list.txt
%defattr(-,root,root)

%files l10n-pt -f build/lang_pt_list.txt
%defattr(-,root,root)

%files l10n-pt_BR -f build/lang_pt-BR_list.txt
%defattr(-,root,root)

%files l10n-ru -f build/lang_ru_list.txt
%defattr(-,root,root)

%files l10n-sk -f build/lang_sk_list.txt
%defattr(-,root,root)

%files l10n-sl -f build/lang_sl_list.txt
%defattr(-,root,root)

%files l10n-sv -f build/lang_sv_list.txt
%defattr(-,root,root)

%files l10n-ta -f build/lang_ta_list.txt
%defattr(-,root,root)

%files l10n-tr -f build/lang_tr_list.txt
%defattr(-,root,root)

%files l10n-zh_CN -f build/lang_zh-CN_list.txt
%defattr(-,root,root)

%files l10n-zh_TW -f build/lang_zh-TW_list.txt
%defattr(-,root,root)

%files l10n-zu -f build/lang_zu_list.txt
%defattr(-,root,root)
