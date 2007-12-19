%define unstable	0

%define l10n   1
%{?_with_l10n: %global l10n 1}
%{?_without_l10n: %global l10n 0}

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

%define version		2.3.1
%define release		%mkrel 1

%define oootagver	oog680-m9
%define ooobuildver	2.3.1.20071218mdv
%define jdkver		1_5_0_11
%ifarch x86_64
%define mdvsuffix	2.3_64
%else
%define mdvsuffix	2.3
%endif
%define ooodir		%{_libdir}/ooo-%{mdvsuffix}
%define libdbver	4.2
%if l10n
%define ooolangs	"en-US af ar bg br bs ca cs cy da de el en-GB es et eu fi fr he hi hu it ja ko mk nb nl nn pl pt pt-BR ru sk sl sv ta tr zh-TW zh-CN zu"
%else
%define ooolangs	"en-US"
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

%define use_mono	0
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

# disable for now in X86-64 (gengal segfaults)
%ifarch x86_64
%define use_systemdb	1
%define use_systemboost 1
%endif

# (fix to avoid gcc 4.0.2 produces segfaulting javaldx bin which breaks
# building process)
%define optsafe	""

%define _requires_exceptions libjawt.so\\|libmyspell.so\\|libstlport_gcc.so\\|libjpeg.so
%define _provides_exceptions libsndfile.so\\|libportaudio.so\\|libdb-4.2.so\\|libdb_java-4.2.so\\|libmyspell.so\\|libstlport_gcc.so

Summary:	Open source office suite (ooo-build)
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://www.go-ooo.org
License:	LGPL
Group:		Office
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

BuildRequires:	hsqldb
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
# http://oooconv.free.fr/fontooo/FontOOo.sxw.bz2
Source50:	FontOOo.sxw
Source51:	ftp://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/DicOOo.sxw
Source60:	openoffice.org.csh
Source61:	openoffice.org.sh

Patch1:		ooo-build-2.1.0-lzmatarball.patch
Patch4:		openoffice.org2-2.0.2-qstart.patch
Patch6:		openoffice.org-2.1.0-firefox-xpcom.patch
Patch14:	ooo-build-2.2.1-kde.patch
Patch17:	ooo-build-fix-build-java-target-patch.patch
Patch19:	ooo-build-2.2.1-desktop_files.patch

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
# Heavy java deps
Requires: hsqldb
Requires: %{name}-java-common = %{version}
# Due to the split
Conflicts: %{name} = 2.2.1
Conflicts: %{name}-common <= 2.3.0.5-1mdv

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
Conflicts: %{name}-common <= 2.3.0.5-1mdv

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
Conflicts: %{name}-devel <= 2.3.0.5-1mdv
Conflicts: %{name}-math <= 2.3.0.5-1mdv

%description common
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the architecture-independent files of OpenOffice.org.

%package core
Group: Office
Summary: OpenOffice.org office suite architecture dependent files
# Due to the split
Conflicts: %{name} = 2.2.1
Conflicts: %{name}-base <= 2.3.0.5-1mdv
Conflicts: %{name}-common <= 2.3.0.5-1mdv
Conflicts: %{name}-devel <= 2.3.0.5-1mdv
Conflicts: %{name}-draw <= 2.3.0.5-1mdv
Conflicts: %{name}-impress <= 2.3.0.5-1mdv
Conflicts: %{name}-kde <= 2.3.0.5-1mdv
Conflicts: %{name}-writer <= 2.3.0.5-1mdv

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
Conflicts: %{name}-common <= 2.3.0.5-1mdv
Conflicts: %{name}-impress <= 2.3.0.5-1mdv

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

%package filter-binfilter
Group: Office
Summary: Legacy filters (e.g. StarOffice 5.2) for OpenOffice.org
Requires: %{name}-common = %{version}
Requires: %{name}-core = %{version}
# Due to the split
Conflicts: %{name} = 2.2.1
Obsoletes: %{name}-filter-mobiledev <= 2.3.0.5
Conflicts: %{name}-filter-mobiledev <= 2.3.0.5
Conflicts: %{name}-common <= 2.3.0.5-1mdv
Conflicts: %{name}-core <= 2.3.0.5-1mdv

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

%package gnome
Group: Office
Summary: GNOME Integration for OpenOffice.org (VFS, GConf)
# Due to the split
Conflicts: %{name} = 2.2.1
Obsoletes: %{name}-gtk <= 2.3.0.5
Conflicts: %{name}-gtk <= 2.3.0.5
Obsoletes: %{name}-evolution <= 2.3.0.5
Conflicts: %{name}-evolution <= 2.3.0.5

%description gnome
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the GNOME VFS support and a GConf backend.

You can extend the functionality of this by installing these packages:

 * openoffice.org-evolution: Evolution addressbook support
 * evolution

%package impress
Group: Office
Summary: OpenOffice.org office suite - presentation
Requires: %{name}-common = %{version}
Requires: %{name}-core = %{version}
Requires: %{name}-draw = %{version}
# Due to the split
Conflicts: %{name} = 2.2.1
Conflicts: %{name}-common <= 2.3.0.5-1mdv

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
Conflicts: %{name}-common <= 2.3.0.5-1mdv

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
Conflicts: %{name}-common <= 2.3.0.5-1mdv

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

%package pyuno
Group: Office
Summary: Python bindings for UNO library
# FIXME
#Requires: %{name}-common = %{version}
Conflicts: %{name}-common <= 2.3.0.5-1mdv

%description pyuno
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the Python bindings for the UNO library.

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

%package testtool
Group: Office
Summary: OpenOffice.org Automatic Test Programs
Requires: %{name}-common = %{version}
# Due to the split
Conflicts: %{name} = 2.2.1
Conflicts: %{name}-common <= 2.3.0.5-1mdv

%description testtool
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the test tools to automatically test the OpenOffice.org
programs.

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
Conflicts: %{name}-common <= 2.3.0.5-1mdv
Conflicts: %{name}-core <= 2.3.0.5-1mdv

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

%if %l10n
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
# Due to alternatives setup, we must have -release here. (BrOffice)
Requires:	%{ooname}-common = %{version}-%{release}
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
%endif

%prep
%setup -q -n ooo-build-%{ooobuildver}

# Add lzma support
%if %{oootarext} == "lzma"
%patch1 -p1 -b .lzma
%endif

%patch4 -p1 -b .qstart
# Seems not needed
#patch6 -p1 -b .xpcom
%patch14 -p1 -b .kde
#%patch17 -p1 -b .javac
%if ! %unstable
%patch19 -p1 -b .desktop_files
%endif

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
#PATH=/bin:/usr/bin:/usr/X11R6/bin:$QTPATH:/usr/sbin:$PATH
PATH=$PATH:/usr/sbin
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
%endif
# ooo-build requests this even with mono off
ln -sf %{SOURCE26} src/
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
        --enable-odk \
        --disable-qadevooo \
        --enable-java \
	--enable-gstreamer \
	--with-firefox \
	--with-system-mozilla=firefox \
	--with-system-libs \
	--with-system-hsqldb \
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
	--enable-split-app-modules \
	--enable-split-opt-features \
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

rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}/opt
# <mrl> This is buggy and duplicated.
#rm -rf %{buildroot}%{ooodir}/share/template/wizard/letter/
# <mrl> Link to the shared one
rm -rf %{buildroot}%{ooodir}/share/dict/ooo
ln -s %{_datadir}/dict/ooo %{buildroot}%{ooodir}/share/dict

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
install -m 644 %{SOURCE50} %{buildroot}%{_libdir}/ooo-%{mdvsuffix}/share/dict/FontOOo.sxw
install -m 644 %{SOURCE51} %{buildroot}%{_libdir}/ooo-%{mdvsuffix}/share/dict/DicOOo.sxw

# fix permissions for stripping
find %{buildroot} -type f -exec chmod u+rw '{}' \;

# fix permission of .so libraries
find %{buildroot} -type f \( -name '*.so' -o -name '*.so.*' \) -exec chmod a+x '{}' \;

# remove /usr/bin/soffice (made with update-alternatives)
rm -f %{buildroot}%{_bindir}/soffice

# Fix sdk listing
sort -u build/sdk_list.txt > build/sdk_list_fixed.txt

# Versionify bash_completion (ooo-wrapper.sh)
if [ -f %{buildroot}%{_sysconfdir}/bash_completion.d/ooo-wrapper.sh ]; then
 mv %{buildroot}%{_sysconfdir}/bash_completion.d/ooo-wrapper.sh \
 	%{buildroot}%{_sysconfdir}/bash_completion.d/ooo-wrapper%{mdvsuffix}
fi

# Versionify bash_completion (ooffice.sh)
if [ -f %{buildroot}%{_sysconfdir}/bash_completion.d/ooffice*.sh ]; then
 mv %{buildroot}%{_sysconfdir}/bash_completion.d/ooffice*.sh \
 	%{buildroot}%{_sysconfdir}/bash_completion.d/ooffice%{mdvsuffix}
fi

%if %{use_mono}
# Versionify mono-ooo.pc
mv %{buildroot}%{_libdir}/pkgconfig/mono-ooo-%{mdvsuffix}.pc \
   %{buildroot}%{_libdir}/pkgconfig/mono-ooo%{mdvsuffix}-2.3.pc
%endif

# Install versioned profile.d/ files (#33475)
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
sed 's@%%{ooodir}@%{ooodir}@g' \
	%{_sourcedir}/openoffice.org.csh > \
	%{buildroot}%{_sysconfdir}/profile.d/openoffice.org%{mdvsuffix}.csh
sed 's@%%{ooodir}@%{ooodir}@g' \
	%{_sourcedir}/openoffice.org.sh > \
	%{buildroot}%{_sysconfdir}/profile.d/openoffice.org%{mdvsuffix}.sh

# BrOffice.org Support (install)
function bro() {
  exp="$1"
  f="$2"
  mv "$f" "$f.ooo"
  echo -n > "$f"
%if %l10n
  sed "$exp" "$f.ooo" > "$f.bro"
%endif
  sed -i "s@$f\$@$f.ooo@" %{_builddir}/ooo-build-%{ooobuildver}/build/*.txt
}

# Change suite name in the program itself
cd %{buildroot}%{ooodir}
bro "s/OpenO/BrO/;s/openo/bro/" program/bootstraprc
bro "s/en-US/pt-BR/;s/openo/bro/" program/versionrc
bro "s/OpenO/BrO/" share/registry/data/org/openoffice/Setup.xcu
cd -

# Change the suite name in .desktop files for pt_BR locale
sed -i '/pt_BR/{s/OpenO/BrO/}' %{buildroot}%{_datadir}/applications/*.desktop

# Place symlinks br<app> -> oo<app>
%if %l10n
cd %{buildroot}%{_bindir}
for i in oo*; do
  ln -s $i ${i/oo/br}
done
cd -
%endif
# End of BrOffice support (install)

%clean
rm -rf %{buildroot}

%post common
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

# BrOffice support %post
for i in \
    %{ooodir}/program/bootstraprc \
    %{ooodir}/program/versionrc \
    %{ooodir}/share/registry/data/org/openoffice/Setup.xcu
do
    if [ -f "$i" ]; then
	rm -f "$i"
    fi
done

# alternatives names follows oobr_<filename> mark, making it explicit.
/usr/sbin/update-alternatives \
        --install %{ooodir}/program/bootstraprc oobr_bootstraprc%{mdvsuffix} \
		%{ooodir}/program/bootstraprc.ooo 1 \
        --slave %{ooodir}/program/versionrc oobr_versionrc%{mdvsuffix} \
		%{ooodir}/program/versionrc.ooo \
        --slave %{ooodir}/share/registry/data/org/openoffice/Setup.xcu oobr_Setup.xcu%{mdvsuffix} \
		%{ooodir}/share/registry/data/org/openoffice/Setup.xcu.ooo
# Always do this configuration, as the switch should be transparent.
/usr/sbin/update-alternatives --auto oobr_bootstraprc
# End of BrOffice support %post

%{update_desktop_database}

%postun common
if [ ! -e "%{_bindir}/ooffice%{mdvsuffix}" ]; then
        /usr/sbin/update-alternatives --remove ooffice %{_bindir}/ooffice%{mdvsuffix}
fi

# BrOffice support %postun common
if [ ! -e "%{ooodir}/program/bootstraprc.ooo" ]; then
        /usr/sbin/update-alternatives --remove oobr_bootstraprc%{mdvsuffix} %{ooodir}/program/bootstraprc.ooo
fi
# End of BrOffice support %postun common

%{clean_desktop_database}

%if %l10n
%post l10n-pt_BR
# BrOffice support %post l10n-pt_BR
# alternatives names follows oobr_<filename> mark, making it explicit.
/usr/sbin/update-alternatives \
        --install %{ooodir}/program/bootstraprc oobr_bootstraprc%{mdvsuffix} \
		%{ooodir}/program/bootstraprc.bro 2 \
        --slave %{ooodir}/program/versionrc oobr_versionrc%{mdvsuffix} \
		%{ooodir}/program/versionrc.bro \
        --slave %{ooodir}/share/registry/data/org/openoffice/Setup.xcu oobr_Setup.xcu%{mdvsuffix} \
		%{ooodir}/share/registry/data/org/openoffice/Setup.xcu.bro
# Always do this configuration, as the switch should be transparent.
/usr/sbin/update-alternatives --auto oobr_bootstraprc
# End of BrOffice support %post l10n-pt_BR

%{update_desktop_database}

%postun l10n-pt_BR
# BrOffice support %postun l10n-pt_BR
if [ ! -e "%{ooodir}/program/bootstraprc.bro" ]; then
        /usr/sbin/update-alternatives --remove oobr_bootstraprc%{mdvsuffix} %{ooodir}/program/bootstraprc.bro
fi
# End of BrOffice support %postun l10n-pt_BR

%{clean_desktop_database}
%endif

%post base
%{update_desktop_database}
%postun base
%{clean_desktop_database}
%post calc
%{update_desktop_database}
%postun calc
%{clean_desktop_database}
%post draw
%{update_desktop_database}
%postun draw
%{clean_desktop_database}
%post impress
%{update_desktop_database}
%postun impress
%{clean_desktop_database}
%post math
%{update_desktop_database}
%postun math
%{clean_desktop_database}
%post writer
%{update_desktop_database}
%postun writer
%{clean_desktop_database}

%files base -f build/base_list.txt
%{_bindir}/oobase%{mdvsuffix}
### <mrl> Please note ? at filenames. They are needed because 32b builds produces
### "li" files while 64b builds produces "lx" files.
%{_datadir}/applications/base*.desktop
%{_mandir}/man1/oobase%{mdvsuffix}.1*

%files calc -f build/calc_list.txt
%{_bindir}/oocalc%{mdvsuffix}
%{_datadir}/applications/calc*.desktop
%{_mandir}/man1/oocalc%{mdvsuffix}.1*

%files common -f build/common_list.txt
%{_sysconfdir}/bash_completion.d/ooffice%{mdvsuffix}
%{_sysconfdir}/profile.d/openoffice.org%{mdvsuffix}.*
%{_bindir}/ooconfig%{mdvsuffix}
%{_bindir}/ooffice%{mdvsuffix}
%{_bindir}/oofromtemplate%{mdvsuffix}
%{_bindir}/ootool%{mdvsuffix}
%dir %{ooodir}/share/dict
# FIXME: Wrong place?
%{ooodir}/share/dict/*.sxw
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
# Due to alternatives upgrade from 2.3.0.5-1mdv to -2mdv
%ghost %{ooodir}/program/bootstraprc
%ghost %{ooodir}/program/versionrc
%ghost %{ooodir}/share/registry/data/org/openoffice/Setup.xcu
%ghost %{_datadir}/applications/base*.desktop
%ghost %{_datadir}/applications/calc*.desktop
%ghost %{_datadir}/applications/draw*.desktop
%ghost %{_datadir}/applications/impress*.desktop
%ghost %{_datadir}/applications/math*.desktop
%ghost %{_datadir}/applications/template*.desktop
%ghost %{_datadir}/applications/web*.desktop
%ghost %{_datadir}/applications/writer*.desktop

%files core -f build/core_list.txt

%files devel -f build/sdk_list_fixed.txt

%files devel-doc -f build/sdk_doc_list.txt

%files draw -f build/draw_list.txt
%{_bindir}/oodraw%{mdvsuffix}
%{_datadir}/applications/draw*.desktop
%{_mandir}/man1/oodraw%{mdvsuffix}.1*

%files dtd-officedocument1.0 -f build/dtd_list.txt

%files filter-binfilter -f build/filter-binfilter_list.txt

%files gnome -f build/gnome_list.txt

%files impress -f build/impress_list.txt
%{_bindir}/ooimpress%{mdvsuffix}
%{_datadir}/applications/impress*.desktop
%{_mandir}/man1/ooimpress%{mdvsuffix}.1*

%files java-common -f build/java_common_list.txt

%files kde -f build/kde_list.txt

%files math -f build/math_list.txt
%{_bindir}/oomath%{mdvsuffix}
%{_datadir}/applications/math*.desktop
%{_mandir}/man1/oomath%{mdvsuffix}.1*

%files openclipart -f build/gallery_list.txt

%files pyuno -f build/pyuno_list.txt

%files

#%files qa-api-tests
#%{ooodir}/qadevOOo

%files testtool -f build/testtool_list.txt

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

%files writer -f build/writer_list.txt
%{_bindir}/ooweb%{mdvsuffix}
%{_bindir}/oowriter%{mdvsuffix}
%{_datadir}/applications/writer*.desktop
%{_datadir}/applications/web*.desktop
%{_mandir}/man1/ooweb%{mdvsuffix}.1*
%{_mandir}/man1/oowriter%{mdvsuffix}.1*

%if %{use_mono}
%files mono -f build/mono_list.txt
%defattr(-,root,root)
%{_libdir}/pkgconfig/mono-ooo%{mdvsuffix}-2.3.pc
%endif

%if %l10n
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
# BrOffice support
# Yes, by this way there will be broken symlinks if you don't make a full suite
# installation.
%{_bindir}/br*
%{ooodir}/program/bootstraprc.bro
%{ooodir}/program/versionrc.bro
%{ooodir}/share/registry/data/org/openoffice/Setup.xcu.bro

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
%endif
