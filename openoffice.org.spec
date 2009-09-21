%define unstable	0
%define debug_package  %{nil}

#dev300 (Alpha2): to improve building packages (wihout l10n) at first
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
#define _binary_payload w9.bzdio
%define _binary_payload w9.lzdio
#define _source_payload w9.bzdio

%define version	        3.0.1
%define release		%mkrel 2

%define oootagver	ooo300-m14
%define ooobuildver	r15224
%define jdkver		1_5_0_11
%ifarch x86_64
%define mdvsuffix	3.0.1_64
%else
%define mdvsuffix	3.0.1
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
%if %mdkversion >= 200800
%define	use_gcj		1
%else
%define	use_gcj		0
%endif
%endif
%{?_with_gcj: %global use_gcj 1}
%{?_without_gcj: %global use_gcj 0}

%define use_icecream    0	
%{?_with_icecream: %global use_icecream 1}
%{?_without_icecream: %global use_icecream 0}

%define use_ccache	0
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

%define use_systemdb	1
%{?_with_systemdb: %global use_systemdb 1}
%{?_without_systemdb: %global use_systemdb 0}

%define use_systemboost 1
%{?_with_systemboost: %global use_systemboost 1}
%{?_without_systemboost: %global use_systemboost 0}

# (fix to avoid gcc 4.0.2 produces segfaulting javaldx bin which breaks
# building process)
%define optsafe	""
%define _requires_exceptions libjawt.so\\|libmyspell.so\\|libstlport_gcc.so\\|libjpeg.so\\|libmono.so\\|mono
%define _provides_exceptions libsndfile.so\\|libportaudio.so\\|libdb-4.2.so\\|libdb_java-4.2.so\\|libmyspell.so\\|libstlport_gcc.so\\|librdf.so.0\\|libraptor.so.1\\|libxmlsec1-nss.so.1\\|libxmlsec1.so.1

%define unopkg  unopkg%{mdvsuffix}

Summary:	Office suite (ooo-build)
Name:		%{name}
Epoch:		1
Version:	%{version}
Release:	%{release}
URL:		http://www.go-ooo.org
License:	LGPL
Group:		Office
Vendor:		Mandriva
Packager:	Rafael da Veiga Cabral <cabral@mandriva.com>
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
# Requres to all our packages
Requires:	%{name}-base = %{epoch}:%{version}
Requires:	%{name}-calc = %{epoch}:%{version}
Requires:	%{name}-draw = %{epoch}:%{version}
Requires:	%{name}-impress = %{epoch}:%{version}
Requires:	%{name}-math = %{epoch}:%{version}
Requires:	%{name}-writer = %{epoch}:%{version}
# Suggests:	%{name}-dtd-officedocument1.0 = %{epoch}:%{version}
Suggests: 	%{name}-pdfimport = %{epoch}:%{version}
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
# BuildRequires:	kdelibs-devel
BuildRequires:	kernel-source
BuildRequires:	db1-devel
%if %{use_systemdb}
BuildRequires:	%{mklibname db 4.2} >= 4.2.5-4mdk
BuildRequires:	libdbcxx >= 4.2.5-4mdk
BuildRequires:	db-devel >= 4.2.5-4mdk
BuildRequires:	libdbjava >= 4.2.5-4mdk
%else
BuildConflicts: libdbjava4.2
%endif
BuildRequires:	bsh
BuildRequires:	libcurl-devel
BuildRequires:	libgtk+2-devel
BuildRequires:	libsvg-devel
BuildRequires:	libgstreamer-plugins-base-devel
BuildRequires:	libxaw-devel
BuildRequires:	libldap-devel
BuildRequires:	libportaudio-devel
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
# dev 300 (retirar essa require)
# BuildRequires:	mozilla-firefox-devel
BuildRequires:	nss-devel
BuildRequires:	nas-devel
BuildRequires:	neon-devel >= 0.27
BuildRequires:	pam-devel
BuildRequires:	perl
BuildRequires:	perl-Archive-Zip
BuildRequires:	perl-MDK-Common
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-XML-Twig
BuildRequires:	python-devel
# BuildRequires:	qt3-devel
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
%if %mdkversion >= 200810
BuildRequires:	java-rpmbuild
%else
BuildRequires:	java-1.7.0-icedtea-devel
%define java_home %{_jvmdir}/java-icedtea
%endif
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
BuildRequires:	libwpg-devel
BuildRequires:	libwps-devel
BuildRequires:	icu
BuildRequires:	libicu-devel
BuildRequires:	libmdbtools-devel
BuildRequires:  ant-apache-regexp
BuildRequires:  xulrunner-devel
BuildRequires:  %{mklibname vigra}-devel
BuildRequires:  hunspell-devel
#pdfimport extension
BuildRequires:  %{mklibname poppler}-devel

####################################################################
#
# Sources
#
####################################################################

Source0:	http://download.go-oo.org/DEV300/ooo-build-3.0.1-%{ooobuildver}.tar.gz
Source5:	http://download.go-oo.org/DEV300/%{oootagver}-sdk.tar.%{oootarext}
Source71:	 http://download.go-oo.org/OOO300/%{oootagver}-ure.tar.%{oootarext}
Source72:	 http://download.go-oo.org/OOO300/%{oootagver}-base.tar.%{oootarext}
Source73:	 http://download.go-oo.org/OOO300/%{oootagver}-calc.tar.%{oootarext}
Source74:	 http://download.go-oo.org/OOO300/%{oootagver}-impress.tar.%{oootarext}
Source75:	 http://download.go-oo.org/OOO300/%{oootagver}-writer.tar.%{oootarext}
Source76:	 http://download.go-oo.org/OOO300/%{oootagver}-l10n.tar.%{oootarext}
Source77:	 http://download.go-oo.org/OOO300/%{oootagver}-artwork.tar.%{oootarext}
Source78:	 http://download.go-oo.org/OOO300/%{oootagver}-filters.tar.%{oootarext}
Source79:	 http://download.go-oo.org/OOO300/%{oootagver}-testing.tar.%{oootarext}
Source80:	 http://download.go-oo.org/OOO300/%{oootagver}-bootstrap.tar.%{oootarext}
Source81:	 http://download.go-oo.org/OOO300/%{oootagver}-libs_gui.tar.%{oootarext}
Source82:	 http://download.go-oo.org/OOO300/%{oootagver}-libs_core.tar.%{oootarext}
Source83:	 http://download.go-oo.org/OOOV300/%{oootagver}-libs_extern.tar.%{oootarext}
Source84:	 http://download.go-oo.org/OOO300/%{oootagver}-libs_extern_sys.tar.%{oootarext}
Source85:	 http://download.go-oo.org/OOO300/%{oootagver}-components.tar.%{oootarext}
Source86:	 http://download.go-oo.org/OOO300/%{oootagver}-postprocess.tar.%{oootarext}
Source90:	 http://download.go-oo.org/DEV300/scsolver.2008-10-30.tar.bz2
Source104: 	 http://download.go-oo.org/OOO300/%{oootagver}-extensions.tar.bz2

Source6:	http://download.go-oo.org/SRC680/oox.2008-02-29.tar.bz2
Source7:	http://download.go-oo.org/SRC680/writerfilter.2008-02-29.tar.bz2
Source13:	http://download.go-oo.org/SRC680/extras-3.tar.bz2
Source17:	http://download.go-oo.org/SRC680/mdbtools-0.6pre1.tar.gz

Source20:	http://download.go-oo.org/OOO300/ooo-cli-prebuilt-3.0.1.tar.bz2
Source21:       http://download.go-oo.org/OOO300/cairo-1.4.10.tar.gz
Source22: 	http://download.go-oo.org/OOO300/libwpd-0.8.14.tar.gz

Source3: 	http://download.go-oo.org/OOO300/libwps-0.1.2.tar.gz
Source4:        http://download.go-oo.org/OOO300/libwpg-0.1.3.tar.gz

Source23:	http://download.go-oo.org/xt/xt-20051206-src-only.zip
Source24:	http://download.go-oo.org/SRC680/lp_solve_5.5.0.10_source.tar.gz
Source25:	http://download.go-oo.org/SRC680/biblio.tar.bz2
Source26:	http://tools.openoffice.org/unowinreg_prebuild/680/unowinreg.dll
# splash screens and about images
Source27:	openintro_mandriva.bmp
Source28:	openabout_mandriva.bmp

#dev300
Source87:	mdv-apply
Source89:	mdv-package-ooo
Source92:	mdv-xdgmailasmailer.diff
Source102:	mdv-desktop-japanese.patch
source103:	mdv-desktop-japanese64.patch
Source88:       mdv-sysui-disableslack.diff
Source30: 	icons.tar.bz2

# templates for kde "create new" context menu
Source31: kde-context-menu-templates.tar.bz2
Source60:	openoffice.org.csh
Source61:	openoffice.org.sh

# Patch19:	ooo-build-2.2.1-desktop_files.patch
# Patch21:	ooo-build-set-desktop-file-broffice-in-pt_BR.patch

%description
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite. It includes the key desktop applications,
such as a word processor, spreadsheet, presentation manager, formula
editing and drawing program, with a user interface and feature set
similar to other office suites. Sophisticated and flexible,
OpenOffice.org also works transparently with a variety of file
formats, including Microsoft Office.

%package base
Group: Office
Summary: OpenOffice.org office suite - database
Requires: %{name}-core = %{epoch}:%{version}
Requires: %{name}-common = %{epoch}:%{version}
# Heavy java deps
Requires: hsqldb
Suggests: %{name}-java-common = %{epoch}:%{version}
# Due to the split
Conflicts: %{name} <= 2.2.1
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
Requires: %{name}-core = %{epoch}:%{version}
Requires: %{name}-common = %{epoch}:%{version}
# Due to the split
Conflicts: %{name} <= 2.2.1
Conflicts: %{name}-common <= 2.3.0.5-1mdv

%description calc
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the spreadsheet component for OpenOffice.org.

%package common
Group: Office
Summary: OpenOffice.org office suite architecture independent files
%if %mdkversion < 200810
# On upgrades, we can't split that way or we will loose functionality.
# Requires: %{name}-gnome
# Requires: %{name}-kde
Requires: %{name}-openclipart
Requires: %{name}-style-galaxy 
Requires: %{name}-style-crystal
Requires: %{name}-style-hicontrast
Requires: %{name}-style-industrial
Requires: %{name}-style-tango
%endif
# Require the architecture dependant stuff
Requires: %{name}-core = %{epoch}:%{version}
# Require at least one style to be installed
Requires: %{name}-style = %{epoch}:%{version}
# And suggest the galaxy one
# dev 300
# Suggests: %{name}-style-galaxy = %{epoch}:%{version}
# Also suggest java-common, as it may be used by some macros
Suggests: %{name}-java-common
Suggests: %{ooname}-help-en_US
# And then general requires for OOo follows
Requires: ghostscript
Requires: fonts-ttf-liberation
Requires: %{mklibname sane 1}
Requires: desktop-common-data >= 2008
# rpm will automatically grab the require for libsane1, but there are some
# configs needed at this package, so we must require it too.
Requires: sane-backends
# Due to %{_bindir}/paperconf
Requires: paper-utils
#dev300
Requires: %{mklibname icu 40} 
Requires: %{mklibname hunspell 1.2_0}
Requires(post): desktop-file-utils update-alternatives
Requires(postun): desktop-file-utils update-alternatives

# Due to the split
Conflicts: %{name} <= 2.1.0
Conflicts: %{name}-devel <= 2.3.0.5-1mdv
Conflicts: %{name}-math <= 2.3.0.5-1mdv
Conflicts: %{name}-core <= 2.3.99.4-1mdv
Conflicts: %{name}-gnome < 3.0svn13581-2mdv

%description common
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the architecture-independent files of OpenOffice.org.

%package core
Group: Office
Summary: OpenOffice.org office suite architecture dependent files
# Due to the split
Conflicts: %{name} <= 2.1.0
Conflicts: %{name}-base <= 2.3.0.5-1mdv
Conflicts: %{name}-common <= 2.3.1-1mdv
Conflicts: %{name}-devel <= 2.3.0.5-1mdv
Conflicts: %{name}-draw <= 2.3.0.5-1mdv
Conflicts: %{name}-impress <= 2.3.0.5-1mdv
#  Conflicts: %{name}-kde <= 2.3.0.5-1mdv
Conflicts: %{name}-writer <= 2.3.0.5-1mdv

%description core
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the architecture-dependent core files of OpenOffice.org.
See the openoffice.org package for more information.

%package devel
Group: Office
Summary: OpenOffice.org SDK - development files
Requires: %{name}-core = %{epoch}:%{version}
Requires: %{name}-common = %{epoch}:%{version}
# Due to the split
Conflicts: %{name} <= 2.2.1

%description devel
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the files needed to build plugins/add-ons for
OpenOffice.org (includes, IDL files, build tools, ...). It also contains the
zipped source of the UNO Java libraries for use in IDEs like eclipse.

%package devel-doc
Group: Office
Summary: OpenOffice.org SDK - documentation
Requires: %{name}-devel = %{epoch}:%{version}
# Due to the split
Conflicts: %{name} <= 2.2.1

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
Requires: %{name}-core = %{epoch}:%{version}
Requires: %{name}-common = %{epoch}:%{version}
# Due to the split
Conflicts: %{name} <= 2.2.1
Conflicts: %{name}-common <= 2.3.0.5-1mdv
Conflicts: %{name}-impress <= 2.3.0.5-1mdv

%description draw
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the drawing component for OpenOffice.org.

# package dtd-officedocument1.0
# Group: Office
# Summary: OfficeDocument 1.0 DTD (OpenOffice.org 1.x)
## due to the split
#Conflicts: %{name} <= 2.2.1
## no need to require -core or -common, see #37559

#%description dtd-officedocument1.0
#OpenOffice.org is a full-featured office productivity suite that provides a
#near drop-in replacement for Microsoft(R) Office.

# This package contains the Document Type Definition (DTD) of the OpenOffice.org
# 1.x(!) XML file format.

%package filter-binfilter
Group: Office
Summary: Legacy filters (e.g. StarOffice 5.2) for OpenOffice.org
Requires: %{name}-core = %{epoch}:%{version}
Requires: %{name}-common = %{epoch}:%{version}
# Due to the split
Conflicts: %{name} <= 2.2.1
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
Conflicts: %{name} <= 2.2.1
Obsoletes: %{name}-gtk <= 2.3.0.5
Conflicts: %{name}-gtk <= 2.3.0.5
Obsoletes: %{name}-qstart <= 2.3.0.5
Conflicts: %{name}-qstart <= 2.3.0.5
Obsoletes: %{name}-evolution <= 2.3.0.5
Conflicts: %{name}-evolution <= 2.3.0.5
# Suggests: %{name}-style-tango = %{epoch}:%{version}

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
Requires: %{name}-core = %{epoch}:%{version}
Requires: %{name}-common = %{epoch}:%{version}
Requires: %{name}-draw = %{epoch}:%{version}
# Due to the split
Conflicts: %{name} <= 2.2.1
Conflicts: %{name}-common <= 2.3.0.5-1mdv

%description impress
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the presentation component for OpenOffice.org.

# %package kde
# Group: Office
# Summary: KDE Integration for OpenOffice.org (Widgets, Dialogs, Addressbook)
# Requires: %{name}-common = %{epoch}:%{version}
# Requires: %{name}-core = %{epoch}:%{version}
# Suggests: %{name}-style-crystal = %{epoch}:%{version}
# Due to the split
# Conflicts: %{name} <= 2.2.1

# %description kde
# OpenOffice.org is a full-featured office productivity suite that provides a
# near drop-in replacement for Microsoft(R) Office.

# This package contains the KDE plugin for drawing OOo's widgets with KDE/Qt, a
# KDEish File Picker when running under KDE and KDE Addressbook integration.
# You can extend the functionality of this by installing these packages:

# * konqueror / kmail
# * kaddressbook

%package java-common
Group: Office
Summary: OpenOffice.org office suite Java support arch. independent files
Requires: %{name}-core = %{epoch}:%{version}
Requires: %{name}-common = %{epoch}:%{version}
Requires: java
# Due to the split
Conflicts: %{name} <= 2.2.1
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
Requires: %{name}-core = %{epoch}:%{version}
Requires: %{name}-common = %{epoch}:%{version}
# Due to the split
Conflicts: %{name} <= 2.2.1
Conflicts: %{name}-common <= 2.3.0.5-1mdv

%description math
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the equation editor component for OpenOffice.org.

%package openclipart
Group: Office
Summary: OpenOffice.org Open Clipart data
Requires: %{name}-core = %{epoch}:%{version}
Requires: %{name}-common = %{epoch}:%{version}
Requires: clipart-openclipart
# Due to the split
Conflicts: %{name} <= 2.2.1
Obsoletes: %{name}-galleries <= 2.2.1

%description openclipart
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the OpenOffice.org Open Clipart data, including images
and sounds.

%package pyuno
Group: Office
Summary: Python bindings for UNO library
# FIXME: what should we require: -common, -core, both, none?
#Requires: %{name}-common = %{epoch}:%{version}
Conflicts: %{name}-common <= 2.3.0.5-1mdv

%description pyuno
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the Python bindings for the UNO library.

#%package qa-api-tests
#Group: Office
#Summary: OpenOffice.org API Test Data
#Requires: %{name}-common = %{epoch}:%{version}
## Due to the split
#Conflicts: %{name} <= 2.2.1
#
#%description qa-api-tests
#OpenOffice.org is a full-featured office productivity suite that provides a
#near drop-in replacement for Microsoft(R) Office.
#
#This package contains the test data for the OpenOffice.org Java and Basic APIs.

%package testtool
Group: Office
Summary: OpenOffice.org Automatic Test Programs
Requires: %{name}-common = %{epoch}:%{version}
# Due to the split
Conflicts: %{name} <= 2.2.1
Conflicts: %{name}-common <= 2.3.0.5-1mdv

%description testtool
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the test tools to automatically test the OpenOffice.org
programs.

%package style-galaxy
Group: Office
Summary: Default symbol style for OpenOffice.org
Requires: %{name}-core = %{epoch}:%{version}
Requires: %{name}-common = %{epoch}:%{version}
Provides: %{name}-style = %{epoch}:%{version}-%{release}
# Due to the split
Conflicts: %{name} <= 2.2.1
Obsoletes: %{name}-style-andromeda = %{epoch}:%{version}

%description style-galaxy
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the "Galaxy" symbol style from Sun, normally used on
MS Windows (tm) and when not using GNOME or KDE. Needs to be manually enabled
in the OpenOffice.org option menu.

%package style-crystal
Group: Office
Summary: Crystal symbol style for OpenOffice.org
Requires: %{name}-core = %{epoch}:%{version}
Requires: %{name}-common = %{epoch}:%{version}
Provides: %{name}-style = %{epoch}:%{version}-%{release}
# Due to the split
Conflicts: %{name} <= 2.2.1

%description style-crystal
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the "crystal" symbol style, default style for KDE.
%package style-hicontrast
Group: Office
Summary: Hicontrast symbol style for OpenOffice.org
Requires: %{name}-core = %{epoch}:%{version}
Requires: %{name}-common = %{epoch}:%{version}
Provides: %{name}-style = %{epoch}:%{version}-%{release}
# Due to the split
Conflicts: %{name} <= 2.2.1

%description style-hicontrast
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the "hicontrast" symbol style, needs to be manually
enabled in the OpenOffice.org option menu.

%package style-industrial
Group: Office
Summary: Industrial symbol style for OpenOffice.org
Requires: %{name}-core = %{epoch}:%{version}
Requires: %{name}-common = %{epoch}:%{version}
Provides: %{name}-style = %{epoch}:%{version}-%{release}
# Due to the split
Conflicts: %{name} <= 2.2.1

%description style-industrial
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the "industrial" symbol style.

%package style-tango
Group: Office
Summary: Tango symbol style for OpenOffice.org
Requires: %{name}-core = %{epoch}:%{version}
Requires: %{name}-common = %{epoch}:%{version}
Provides: %{name}-style = %{epoch}:%{version}-%{release}
# Due to the split
Conflicts: %{name} = 2.2.1

%description style-tango
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the "tango" symbol style, default style for GTK/Gnome.

%package writer
Group: Office
Summary: OpenOffice.org office suite - word processor
Requires: %{name}-core = %{epoch}:%{version}
Requires: %{name}-common = %{epoch}:%{version}
# Due to the split
Conflicts: %{name} <= 2.2.1
Conflicts: %{name}-common <= 2.3.0.5-1mdv
Conflicts: %{name}-core <= 2.3.0.5-1mdv

%description writer
OpenOffice.org is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the wordprocessor component for OpenOffice.org.

# dev300: without mono
%package mono
Summary:	Mono UNO Bridge for OpenOffice.org
Group:		Office
Requires:	%{ooname} = %{epoch}:%{version}
Obsoletes:	%{ooname}-go-ooo-mono <= %{version}

%description mono
The Mono/UNO binding allows a Mono application to access the complete
set of APIs exposed by OpenOffice.org via UNO.

Currently the use of Mono for add-ins & scripting inside OO.o itself is
not supported.

%package pdfimport
Group: Office
Summary: OpenOffice.org office suite - PDF Import extension
Requires: %{name}-core = %{epoch}:%{version}
Requires: %{name}-common = %{epoch}:%{version}
Requires: %{name}-draw = %{epoch}:%{version}
# Due to the split
Conflicts: %{name} <= 2.2.1
Conflicts: %{name}-common <= 2.3.0.5-1mdv
Conflicts: %{name}-core <= 2.3.0.5-1mdv

%description pdfimport
PDF import extension enables PDF documments importing and basic editing of PDF
documments by using OpenOffice.org-draw application.

%package presenter-screen
Group: Office
Summary: OpenOffice.org office suite - Presenter Screen extension
Requires: %{name}-core = %{epoch}:%{version}
Requires: %{name}-common = %{epoch}:%{version}
Requires: %{name}-impress = %{epoch}:%{version}
# Due to the split
Conflicts: %{name} <= 2.2.1
Conflicts: %{name}-common <= 2.3.0.5-1mdv
Conflicts: %{name}-core <= 2.3.0.5-1mdv

%description presenter-screen
Presenter Screen extension helps users to see upcoming slides and slide notes
of presentations inside a second view not visible for the spectators.

# %package report-builder
# Group: Office
# Summary: OpenOffice.org office suite - Report Builder extension
# Requires: %{name}-core = %{epoch}:%{version}
# Requires: %{name}-common = %{epoch}:%{version}
# Requires: %{name}-base = %{epoch}:%{version}
# Due to the split
# Conflicts: %{name} <= 2.2.1
# Conflicts: %{name}-common <= 2.3.0.5-1mdv
# Conflicts: %{name}-core <= 2.3.0.5-1mdv

# %description report-builder
# By using %{name}-base the Report Builder extesion enables creating of smart and 
# professional looking reports. Further the reports can be exported to PDF or 
# OpenDocuments formats.

%package wiki-publisher
Group: Office
Summary: OpenOffice.org office suite - Wiki Publisher extension
Requires: %{name}-core = %{epoch}:%{version}
Requires: %{name}-common = %{epoch}:%{version}
Requires: %{name}-writer = %{epoch}:%{version}
Requires: jakarta-commons-codec, jakarta-commons-httpclient
Requires: jakarta-commons-lang, jakarta-commons-logging
# Due to the split
Conflicts: %{name} <= 2.2.1
Conflicts: %{name}-common <= 2.3.0.5-1mdv
Conflicts: %{name}-core <= 2.3.0.5-1mdv

%description wiki-publisher
With Wiki Publisher extesion is possible by using %{name}-writer to create 
wiki page articles on MediaWiki servers without having to know the syntax of 
MediaWiki markup language. This extension also enables publishing of the
wiki pages.

%package presentation-minimizer
Group: Office
Summary: OpenOffice.org office suite - Presentation Minimizer extension
Requires: %{name}-core = %{epoch}:%{version}
Requires: %{name}-common = %{epoch}:%{version}
Requires: %{name}-impress = %{epoch}:%{version}
# Due to the split
Conflicts: %{name} <= 2.2.1
Conflicts: %{name}-common <= 2.3.0.5-1mdv
Conflicts: %{name}-core <= 2.3.0.5-1mdv

%description presentation-minimizer
With Presentation Minimizer extesion is possible to reduce the file size of the 
presentation by compressing images and removing data not needed in a automatizated
way.

Note: The Presentation Minimizer also works on Microsoft PowerPoint presentations. 

%if %l10n
%package l10n-it
Summary:	Italian language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-common = %{epoch}:%{version}
Requires:	locales-it
Requires:	fonts-ttf-dejavu
Requires:	urw-fonts
Requires:	myspell-it
Requires:	myspell-hyph-it
Obsoletes:	%{ooname}-go-ooo-l10n-it <= %{version}
Suggests:	%{ooname}-help-it

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
Provides:	%{ooname}-l10n = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-common = %{epoch}:%{version}
Requires:	locales-af
Requires:	urw-fonts
Requires:	myspell-af
Obsoletes:	OpenOffice.org-l10n-af
Provides:	OpenOffice.org-l10n-af
Obsoletes:	%{ooname}-go-ooo-l10n-af <= %{version}
Suggests:	%{ooname}-help-af

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
Provides:	%{ooname}-l10n = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-common = %{epoch}:%{version}
Requires:	locales-ar
Requires:	fonts-ttf-arabic
Obsoletes:	OpenOffice.org-l10n-ar
Provides:	OpenOffice.org-l10n-ar
Obsoletes:	%{ooname}-go-ooo-l10n-ar <= %{version}
Suggests:	%{ooname}-help-ar

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
Provides:	%{ooname}-l10n = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-common = %{epoch}:%{version}
Requires:	locales-bg
Obsoletes:	OpenOffice.org-l10n-bg
Provides:	OpenOffice.org-l10n-bg
Obsoletes:	%{ooname}-go-ooo-l10n-bg <= %{version}
Suggests:	%{ooname}-help-bg

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
Provides:	%{ooname}-l10n = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-common = %{epoch}:%{version}
Requires:	locales-br
Obsoletes:	%{ooname}-go-ooo-l10n-br <= %{version}
Suggests:	%{ooname}-help-br

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
Provides:	%{ooname}-l10n = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-common = %{epoch}:%{version}
Requires:	locales-bs
Obsoletes:	%{ooname}-go-ooo-l10n-bs <= %{version}
Suggests:	%{ooname}-help-bs

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
Provides:	%{ooname}-l10n = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-common = %{epoch}:%{version}
Requires:	locales-ca
Requires:	urw-fonts
Requires:	myspell-ca
Obsoletes:	OpenOffice.org-l10n-ca
Provides:	OpenOffice.org-l10n-ca
Obsoletes:	%{ooname}-go-ooo-l10n-ca <= %{version}
Suggests:	%{ooname}-help-ca

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
Provides:	%{ooname}-l10n = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-common = %{epoch}:%{version}
Requires:	locales-cs
Requires:	urw-fonts
Requires:	myspell-cs
Requires:	myspell-hyph-cs
Obsoletes:	%{ooname}-go-ooo-l10n-cs <= %{version}
Obsoletes:	OpenOffice.org-l10n-cs
Provides:	OpenOffice.org-l10n-cs
Suggests:	%{ooname}-help-cs

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
Provides:	%{ooname}-l10n = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-common = %{epoch}:%{version}
Requires:	locales-cy
Requires:	urw-fonts
Requires:	myspell-cy
Obsoletes:	OpenOffice.org-l10n-cy
Provides:	OpenOffice.org-l10n-cy
Obsoletes:	%{ooname}-go-ooo-l10n-cy <= %{version}
Suggests:	%{ooname}-help-cy

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
Provides:	%{ooname}-l10n = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-common = %{epoch}:%{version}
Requires:	locales-da
Requires:	fonts-ttf-dejavu
Requires:	urw-fonts
Requires:	myspell-da, myspell-hyph-da
Obsoletes:	OpenOffice.org-l10n-da
Provides:	OpenOffice.org-l10n-da
Obsoletes:	%{ooname}-go-ooo-l10n-da <= %{version}
Suggests:	%{ooname}-help-da

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
Provides:	%{ooname}-l10n = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-common = %{epoch}:%{version}
Requires:	locales-de
Requires:	fonts-ttf-dejavu
Requires:	urw-fonts
Requires:	myspell-de
Requires:	myspell-hyph-de
Obsoletes:	%{ooname}-go-ooo-l10n-de <= %{version}
Obsoletes:	OpenOffice.org-l10n-de
Provides:	OpenOffice.org-l10n-de
Suggests:	%{ooname}-help-de

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
Provides:	%{ooname}-l10n = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-common = %{epoch}:%{version}
Requires:	locales-el
Requires:	fonts-type1-greek
Requires:	myspell-el
Requires:	myspell-hyph-el
Obsoletes:	OpenOffice.org-l10n-el
Provides:	OpenOffice.org-l10n-el
Obsoletes:	%{ooname}-go-ooo-l10n-el <= %{version}
Suggests:	%{ooname}-help-el

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
Provides:	%{ooname}-l10n = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-common = %{epoch}:%{version}
Requires:	locales-en
Requires:	urw-fonts
Requires:	myspell-en_GB
Requires:	myspell-hyph-en
Obsoletes:	%{ooname}-go-ooo-l10n-en_GB <= %{version}
Suggests:	%{ooname}-help-en_GB

%description l10n-en_GB
OpenOffice.org is an Open Source, community-developed, office suite.

 package contains the localization of OpenOffice.org in British.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-es
Summary:	Spanish language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-common = %{epoch}:%{version}
Requires:	locales-es
Requires:	fonts-ttf-dejavu
Requires:	urw-fonts
Requires:	myspell-es
Requires:	myspell-hyph-es
Obsoletes:	%{ooname}-go-ooo-l10n-es <= %{version}
Obsoletes:	OpenOffice.org-l10n-es
Provides:	OpenOffice.org-l10n-es
Suggests:	%{ooname}-help-es

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
Provides:	%{ooname}-l10n = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-common = %{epoch}:%{version}
Requires:	locales-et
Requires:	fonts-ttf-dejavu
Requires:	urw-fonts
Requires:	myspell-et
Requires:	myspell-hyph-et
Obsoletes:	OpenOffice.org-l10n-et
Provides:	OpenOffice.org-l10n-et
Obsoletes:	%{ooname}-go-ooo-l10n-et <= %{version}
Suggests:	%{ooname}-help-et

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
Provides:	%{ooname}-l10n = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-common = %{epoch}:%{version}
Requires:	locales-eu
Requires:	fonts-ttf-dejavu
Requires:	urw-fonts
Obsoletes:	OpenOffice.org-l10n-eu
Provides:	OpenOffice.org-l10n-eu
Obsoletes:	%{ooname}-go-ooo-l10n-eu <= %{version}
Suggests:	%{ooname}-help-eu

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
Provides:	%{ooname}-l10n = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-common = %{epoch}:%{version}
Requires:	locales-fi
Requires:	fonts-ttf-dejavu
Requires:	urw-fonts
Requires:	%{ooname}-voikko
Obsoletes:	OpenOffice.org-l10n-fi
Provides:	OpenOffice.org-l10n-fi
Obsoletes:	%{ooname}-go-ooo-l10n-fi <= %{version}
# dev300 checking if its really necessary
# Obsoletes:	%{ooname}-voikko
Suggests:	%{ooname}-help-fi

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
Provides:	%{ooname}-l10n = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-common = %{epoch}:%{version}
Requires:	locales-fr
Requires:	fonts-ttf-dejavu
Requires:	urw-fonts
Requires:	myspell-fr
Requires:	myspell-hyph-fr
Obsoletes:	OpenOffice.org-l10n-fr
Provides:	OpenOffice.org-l10n-fr
Obsoletes:	%{ooname}-go-ooo-l10n-fr <= %{version}
Suggests:	%{ooname}-help-fr

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
Provides:	%{ooname}-l10n = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-common = %{epoch}:%{version}
Requires:	locales-he
Requires:	urw-fonts
Obsoletes:	OpenOffice.org-l10n-he
Provides:	OpenOffice.org-l10n-he
Obsoletes:	%{ooname}-go-ooo-l10n-he <= %{version}
Suggests:	%{ooname}-help-he

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
Provides:	%{ooname}-l10n = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-common = %{epoch}:%{version}
Requires:	locales-hi
Requires:	urw-fonts
Obsoletes:	OpenOffice.org-l10n-hi
Provides:	OpenOffice.org-l10n-hi
Obsoletes:	%{ooname}-go-ooo-l10n-hi <= %{version}
Suggests:	%{ooname}-help-hi

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
Provides:	%{ooname}-l10n = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-common = %{epoch}:%{version}
Requires:	locales-hu
Requires:	urw-fonts
Requires:	myspell-hu
Requires:	myspell-hyph-hu
Obsoletes:	OpenOffice.org-l10n-hu
Provides:	OpenOffice.org-l10n-hu
Obsoletes:	%{ooname}-go-ooo-l10n-hu <= %{version}
Suggests:	%{ooname}-help-hu

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
Provides:	%{ooname}-l10n = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-common = %{epoch}:%{version}
Requires:	locales-ja
Requires:	fonts-ttf-japanese >= 0.20020727-1mdk
Obsoletes:	OpenOffice.org-l10n-ja
Provides:	OpenOffice.org-l10n-ja
Obsoletes:	%{ooname}-go-ooo-l10n-ja <= %{version}
Suggests:	%{ooname}-help-ja

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
Provides:	%{ooname}-l10n = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-common = %{epoch}:%{version}
Requires:	locales-ko
Requires:	fonts-ttf-korean >= 2.1
Obsoletes:	OpenOffice.org-l10n-ko
Provides:	OpenOffice.org-l10n-ko
Obsoletes:	%{ooname}-go-ooo-l10n-ko <= %{version}
Suggests:	%{ooname}-help-ko

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
Provides:	%{ooname}-l10n = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-common = %{epoch}:%{version}
Requires:	locales-mk
Obsoletes:	%{ooname}-go-ooo-l10n-mk <= %{version}
Suggests:	%{ooname}-help-mk

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
Provides:	%{ooname}-l10n = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-common = %{epoch}:%{version}
Requires:	locales-no
Requires:	urw-fonts
Obsoletes:	OpenOffice.org-l10n-nb
Provides:	OpenOffice.org-l10n-nb
Obsoletes:	%{ooname}-go-ooo-l10n-nb <= %{version}
Suggests:	%{ooname}-help-nb

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
Provides:	%{ooname}-l10n = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-common = %{epoch}:%{version}
Requires:	locales-nl
Requires:	fonts-ttf-dejavu
Requires:	urw-fonts
Requires:	myspell-nl
Requires:	myspell-hyph-nl
Obsoletes:	OpenOffice.org-l10n-nl
Provides:	OpenOffice.org-l10n-nl
Obsoletes:	%{ooname}-go-ooo-l10n-nl <= %{version}
Suggests:	%{ooname}-help-nl

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
Provides:	%{ooname}-l10n = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-common = %{epoch}:%{version}
Requires:	locales-no
Requires:	urw-fonts
Obsoletes:	OpenOffice.org-l10n-nn
Provides:	OpenOffice.org-l10n-nn
Obsoletes:	%{ooname}-go-ooo-l10n-nn <= %{version}
Suggests:	%{ooname}-help-nn

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
Provides:	%{ooname}-l10n = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-common = %{epoch}:%{version}
Requires:	locales-pl
Requires:	urw-fonts
Requires:	myspell-pl
Requires:	myspell-hyph-pl
Obsoletes:	OpenOffice.org-l10n-pl
Provides:	OpenOffice.org-l10n-pl
Obsoletes:	%{ooname}-go-ooo-l10n-pl <= %{version}
Suggests:	%{ooname}-help-pl

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
Provides:	%{ooname}-l10n = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-common = %{epoch}:%{version}
Requires:	locales-pt
Requires:	fonts-ttf-dejavu
Requires:	urw-fonts
Requires:	myspell-pt
Requires:	myspell-hyph-pt
Obsoletes:	OpenOffice.org-l10n-pt
Provides:	OpenOffice.org-l10n-pt
Obsoletes:	%{ooname}-go-ooo-l10n-pt <= %{version}
Suggests:	%{ooname}-help-pt

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
Provides:	%{ooname}-l10n = %{epoch}:%{version}-%{release}
# Due to alternatives setup, we must have -release here. (BrOffice)
Requires:	%{ooname}-common = %{epoch}:%{version}-%{release}
Requires:	locales-pt
Requires:	urw-fonts
Requires:	myspell-pt_BR
Obsoletes:	OpenOffice.org-l10n_pt_BR
Provides:	OpenOffice.org-l10n_pt_BR
Obsoletes:	%{ooname}-go-ooo-l10n-pt_BR <= %{version}
Suggests:	%{ooname}-help-pt_BR

%description l10n-pt_BR
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in Portuguese
Brazilian.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-ru
Summary:	Russian language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-common = %{epoch}:%{version}
Requires:	locales-ru
Requires:	urw-fonts >= 2.0-6mdk
Requires:	myspell-ru
Requires:	myspell-hyph-ru
Obsoletes:	OpenOffice.org-l10n-ru
Provides:	OpenOffice.org-l10n-ru
Obsoletes:	%{ooname}-go-ooo-l10n-ru <= %{version}
Suggests:	%{ooname}-help-ru

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
Provides:	%{ooname}-l10n = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-common = %{epoch}:%{version}
Requires:	locales-sk
Requires:	urw-fonts
Requires:	myspell-sk
Requires:	myspell-hyph-sk
Obsoletes:	OpenOffice.org-l10n-sk
Provides:	OpenOffice.org-l10n-sk
Obsoletes:	%{ooname}-go-ooo-l10n-sk <= %{version}
Suggests:	%{ooname}-help-sk

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
Provides:	%{ooname}-l10n = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-common = %{epoch}:%{version}
Requires:	locales-sl
Requires:	urw-fonts
Requires:	myspell-sl, myspell-hyph-sl
Obsoletes:	OpenOffice.org-l10n-sl
Provides:	OpenOffice.org-l10n-sl
Obsoletes:	%{ooname}-go-ooo-l10n-sl <= %{version}
Suggests:	%{ooname}-help-sl

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
Provides:	%{ooname}-l10n = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-common = %{epoch}:%{version}
Requires:	locales-sv
Requires:	fonts-ttf-dejavu
Requires:	urw-fonts
Requires:	myspell-sv
Requires:	myspell-hyph-sv
Obsoletes:	OpenOffice.org-l10n-sv
Provides:	OpenOffice.org-l10n-sv
Obsoletes:	%{ooname}-go-ooo-l10n-sv <= %{version}
Suggests:	%{ooname}-help-sv

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
Provides:	%{ooname}-l10n = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-common = %{epoch}:%{version}
Requires:	locales-ta
Requires:	urw-fonts
Obsoletes:	OpenOffice.org-l10n-ta
Provides:	OpenOffice.org-l10n-ta
Obsoletes:	%{ooname}-go-ooo-l10n-ta <= %{version}
Suggests:	%{ooname}-help-ta

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
Provides:	%{ooname}-l10n = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-common = %{epoch}:%{version}
Requires:	locales-tr
Requires:	urw-fonts
Obsoletes:	OpenOffice.org-l10n-tr
Provides:	OpenOffice.org-l10n-tr
Obsoletes:	%{ooname}-go-ooo-l10n-tr <= %{version}
Suggests:	%{ooname}-help-tr

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
Provides:	%{ooname}-l10n = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-common = %{epoch}:%{version}
Requires:	locales-zh
Obsoletes:	OpenOffice.org-l10n-zh_CN
Provides:	OpenOffice.org-l10n-zh_CN
Obsoletes:	%{ooname}-go-ooo-l10n-zh_CN <= %{version}
Suggests:	%{ooname}-help-zh_CN

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
Provides:	%{ooname}-l10n = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-common = %{epoch}:%{version}
Requires:	locales-zh
Requires:	fonts-ttf-chinese
Obsoletes:	OpenOffice.org-l10n-zh_TW
Provides:	OpenOffice.org-l10n-zh_TW
Obsoletes:	%{ooname}-go-ooo-l10n-zh_TW <= %{version}
Suggests:	%{ooname}-help-zh_TW

%description l10n-zh_TW
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in Chinese
Traditional.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-zu
Summary:	Zulu language support for OpenOffice.org
Group:		Office
Provides:	%{ooname}-l10n = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-common = %{epoch}:%{version}
Requires:	locales-zu
Requires:	urw-fonts
Requires:	myspell-zu
Obsoletes:	OpenOffice.org-l10n-zu
Provides:	OpenOffice.org-l10n-zu
Obsoletes:	%{ooname}-go-ooo-l10n-zu <= %{version}
Suggests:	%{ooname}-help-zu

%description l10n-zu
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localization of OpenOffice.org in Zulu.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

%package help-it
Summary:	Italian help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-l10n-it = %{epoch}:%{version}

%description help-it
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in Italian.

%package help-af
Summary:	Afrikaans help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-l10n-af = %{epoch}:%{version}

%description help-af
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in Afrikaans.


%package help-ar
Summary:	Arabic help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-l10n-ar = %{epoch}:%{version}

%description help-ar
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in Arabic.


%package help-bg
Summary:	Bulgarian help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-l10n-bg = %{epoch}:%{version}

%description help-bg
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in Bulgarian.


%package help-br
Summary:	Breton help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-l10n-br = %{epoch}:%{version}

%description help-br
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in Breton.


%package help-bs
Summary:	Bosnian help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-l10n-bs = %{epoch}:%{version}

%description help-bs
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in Bosnian.


%package help-ca
Summary:	Catalan help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-l10n-ca = %{epoch}:%{version}

%description help-ca
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in Catalan.


%package help-cs
Summary:	Czech help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-l10n-cs = %{epoch}:%{version}
Obsoletes:	OpenOffice.org-help-cs
Provides:	OpenOffice.org-help-cs

%description help-cs
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in Czech.


%package help-cy
Summary:	Welsh help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-l10n-cy = %{epoch}:%{version}

%description help-cy
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in Welsh.


%package help-da
Summary:	Danish help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-l10n-da = %{epoch}:%{version}

%description help-da
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in Danish.


%package help-de
Summary:	German help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-l10n-de = %{epoch}:%{version}
Obsoletes:	OpenOffice.org-help-de
Provides:	OpenOffice.org-help-de

%description help-de
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in German.


%package help-el
Summary:	Greek help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-l10n-el = %{epoch}:%{version}

%description help-el
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in Greek.


%package help-en_GB
Summary:	British help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-l10n-en_GB = %{epoch}:%{version}

%description help-en_GB
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in British.


%package help-en_US
Summary:	American English help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-common = %{epoch}:%{version}

%description help-en_US
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in American English.


%package help-es
Summary:	Spanish help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-l10n-es = %{epoch}:%{version}
Obsoletes:	OpenOffice.org-help-es
Provides:	OpenOffice.org-help-es

%description help-es
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in Spanish.


%package help-et
Summary:	Estonian help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-l10n-et = %{epoch}:%{version}

%description help-et
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in Estonian.


%package help-eu
Summary:	Basque help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-l10n-eu = %{epoch}:%{version}
Obsoletes:	OpenOffice.org-help-eu
Provides:	OpenOffice.org-help-eu

%description help-eu
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in Basque.


%package help-fi
Summary:	Finnish help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-l10n-fi = %{epoch}:%{version}
Obsoletes:	OpenOffice.org-help-fi
Provides:	OpenOffice.org-help-fi

%description help-fi
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in Finnish.


%package help-fr
Summary:	French help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-l10n-fr = %{epoch}:%{version}
Obsoletes:	OpenOffice.org-help-fr
Provides:	OpenOffice.org-help-fr

%description help-fr
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in French.


%package help-he
Summary:	Hebrew help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-l10n-he = %{epoch}:%{version}

%description help-he
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in Hebrew.


%package help-hi
Summary:	Hindi help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-l10n-hi = %{epoch}:%{version}

%description help-hi
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in Hindi.


%package help-hu
Summary:	Hungarian help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-l10n-hu = %{epoch}:%{version}

%description help-hu
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in Hungarian.


%package help-ja
Summary:	Japanese help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-l10n-ja = %{epoch}:%{version}
Obsoletes:	OpenOffice.org-help-ja
Provides:	OpenOffice.org-help-ja

%description help-ja
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in Japanese.


%package help-ko
Summary:	Korean help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-l10n-ko = %{epoch}:%{version}
Obsoletes:	OpenOffice.org-help-ko
Provides:	OpenOffice.org-help-ko

%description help-ko
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in Korean.


%package help-mk
Summary:	Macedonian help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-l10n-mk = %{epoch}:%{version}

%description help-mk
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in Macedonian.


%package help-nb
Summary:	Norwegian Bokmal help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-l10n-nb = %{epoch}:%{version}

%description help-nb
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in Norwegian
Bokmal.


%package help-nl
Summary:	Dutch help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-l10n-nl = %{epoch}:%{version}
Obsoletes:	OpenOffice.org-help-nl
Provides:	OpenOffice.org-help-nl

%description help-nl
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in Dutch.


%package help-nn
Summary:	Norwegian Nynorsk help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-l10n-nn = %{epoch}:%{version}

%description help-nn
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in Norwegian
Nynorsk.

%package help-pl
Summary:	Polish help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-l10n-pl = %{epoch}:%{version}

%description help-pl
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in Polish.


%package help-pt
Summary:	Portuguese help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-l10n-pt = %{epoch}:%{version}

%description help-pt
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in Portuguese.


%package help-pt_BR
Summary:	Portuguese Brazilian help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-l10n-pt_BR = %{epoch}:%{version}
Obsoletes:	OpenOffice.org-help-pt_BR
Provides:	OpenOffice.org-help-pt_BR

%description help-pt_BR
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in Portuguese
Brazilian.


%package help-ru
Summary:	Russian help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-l10n-ru = %{epoch}:%{version}
Obsoletes:	OpenOffice.org-help-ru
Provides:	OpenOffice.org-help-ru

%description help-ru
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in Russian.


%package help-sk
Summary:	Slovak help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-l10n-sk = %{epoch}:%{version}
Obsoletes:	OpenOffice.org-help-sk
Provides:	OpenOffice.org-help-sk

%description help-sk
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in Slovak.


%package help-sl
Summary:	Slovenian help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-l10n-sl = %{epoch}:%{version}
Obsoletes:	OpenOffice.org-help-sl
Provides:	OpenOffice.org-help-sl

%description help-sl
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in Slovenian.


%package help-sv
Summary:	Swedish help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-l10n-sv = %{epoch}:%{version}
Obsoletes:	OpenOffice.org-help-sv
Provides:	OpenOffice.org-help-sv

%description help-sv
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in Swedish.


%package help-ta
Summary:	Tamil help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-l10n-ta = %{epoch}:%{version}

%description help-ta
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in Tamil.


%package help-tr
Summary:	Turkish help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-l10n-tr = %{epoch}:%{version}
Obsoletes:	OpenOffice.org-help-tr
Provides:	OpenOffice.org-help-tr

%description help-tr
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in Turkish.


%package help-zh_CN
Summary:	Chinese Simplified help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-l10n-zh_CN = %{epoch}:%{version}
Obsoletes:	OpenOffice.org-help-zh_CN
Provides:	OpenOffice.org-help-zh_CN

%description help-zh_CN
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in Chinese
Simplified.


%package help-zh_TW
Summary:	Chinese Traditional help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-l10n-zh_TW = %{epoch}:%{version}
Obsoletes:	OpenOffice.org-help-zh_TW
Provides:	OpenOffice.org-help-zh_TW

%description help-zh_TW
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in Chinese
Traditional.


%package help-zu
Summary:	Zulu help for OpenOffice.org
Group:		Office
Provides:	%{ooname}-help = %{epoch}:%{version}-%{release}
Requires:	%{ooname}-l10n-zu = %{epoch}:%{version}

%description help-zu
OpenOffice.org is an Open Source, community-developed, office suite.

This package contains the localized help files of OpenOffice.org in Zulu.
%endif

%prep
%setup -q -n ooo-build-3.0.1-%{ooobuildver}

# Add lzma support
%if %{oootarext} == "lzma"
%patch1 -p1 -b .lzma
%endif

# %if ! %unstable
# %patch19 -p1 -b .desktop_files
# %endif
# %patch20 -p1
# %patch21 -p0

# We want odk
#sed -i /disable-odk/d distro-configs/Mandriva*

%build

# Workaround for bug http://qa.mandriva.com/show_bug.cgi?id=27771
# if [ -z $QTDIR ]; then
# . /etc/profile.d/60qt4.sh
# fi
export QTDIR=%{_libdir}/qt4
export QTINC=%{_libdir}/qt4/include
export QTLIB=%{_libdir}/qt4/lib

%if !%{use_gcj}
if [ -z $JAVA_HOME ]; then
	. /etc/profile.d/jdk-%{jdkver}.sh
fi
%endif

# add moc in PATH
# if [ ! -z $QTDIR ]; then
#	export QTPATH=$QTDIR/bin
#	export PATH=$PATH:$QTPATH
#else
#	export PATH=$PATH:%{_prefix}/lib/qt3

# fi

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

# Force KDE3 support instead of KDE4 (dev 300)
# export KDEDIR=/opt/kde3

mkdir -p src

ln -sf %{SOURCE3} src/
ln -sf %{SOURCE4} src/
ln -sf %{SOURCE5} src/
ln -sf %{SOURCE6} src/
ln -sf %{SOURCE7} src/
ln -sf %{SOURCE13} src/
ln -sf %{SOURCE17} src/
%if %{use_mono}
ln -sf %{SOURCE20} src/
%endif

ln -sf %{SOURCE21} src/
ln -sf %{SOURCE22} src/

# ooo-build requests this even with mono off
ln -sf %{SOURCE26} src/
ln -sf %{SOURCE23} src/
ln -sf %{SOURCE24} src/
ln -sf %{SOURCE25} src/

# splash screen
ln -sf %{SOURCE27} src/
ln -sf %{SOURCE28} src/

# icons
ln -sf %{SOURCE30} src/

# templates for kde context menu
ln -sf %{SOURCE31} src/

ln -sf %{SOURCE71} src/
ln -sf %{SOURCE72} src/
ln -sf %{SOURCE73} src/
ln -sf %{SOURCE74} src/
ln -sf %{SOURCE75} src/
ln -sf %{SOURCE76} src/
ln -sf %{SOURCE77} src/
ln -sf %{SOURCE78} src/
ln -sf %{SOURCE79} src/
ln -sf %{SOURCE80} src/
ln -sf %{SOURCE81} src/
ln -sf %{SOURCE82} src/
ln -sf %{SOURCE83} src/
ln -sf %{SOURCE84} src/
ln -sf %{SOURCE85} src/
ln -sf %{SOURCE86} src/
ln -sf %{SOURCE90} src/
ln -sf %{SOURCE104} src/

if [ -x ./autogen.sh ]; then
	NOCONFIGURE=1 ./autogen.sh --with-distro=%{distroname}
fi

%if %{use_ccache}
export CCACHE_DIR=%{ccachedir}
%endif

export ARCH_FLAGS="%{optflags} %{optsafe} -fno-omit-frame-pointer -fno-strict-aliasing"
export ARCH_FLAGS_CC="%{optflags} %{optsafe} -fno-omit-frame-pointer -fno-strict-aliasing"
export ARCH_FLAGS_CXX="%{optflags} %{optsafe} -fno-omit-frame-pointer -fno-strict-aliasing -fpermissive -fvisibility-inlines-hidden"
export ARCH_FLAGS_OPT="%{optflags} -O2 %{optsafe}"

%if %use_gcj
export JAVA=%java
export JAVAC=%javac
export ANT="%ant"
%endif

echo "Configure start at: "`date` >> ooobuildtime.log 
# --with-jdk-home=%java_home \

CFLAGS="%{optflags} %{optsafe} -g0 -fno-omit-frame-pointer -fno-strict-aliasing" \
CXXFLAGS="%{optflags} %{optsafe} -g0 -fno-omit-frame-pointer -fno-strict-aliasing -fpermissive -fvisibility-inlines-hidden" \
%configure2_5x \
	--with-distro=%{distroname} \
	--with-vendor=Mandriva \
	--with-tag=%{oootagver} \
	--with-build-version="%{ooobuildver}" \
	--enable-odk \
	--disable-qadevooo \
	--enable-java \
	--enable-gstreamer \
	--enable-lockdown \
	--enable-opengl \
	--with-firefox \
	--with-system-mozilla \
	--with-system-hsqldb \
	--with-system-beanshell \
	--with-system-xml-apis \
	--with-system-xerces \
	--with-system-xalan \
	--with-system-xt \
	--with-system-icu \
	--with-system-xrender-headers \
	--without-system-xmlsec \
	--without-system-mspack \
	--with-system-libwps \
	--with-system-libwpd \
	--with-system-libwpg \
	--with-system-libsvg \
	--with-system-sablot \
	--with-intro-bitmaps="%{SOURCE27}" \
	--with-about-bitmaps="%{SOURCE28}" \
%if %use_gcj
	--with-java-target-version=1.5 \
%else
	--with-jdk-home=$JAVA_HOME \
%endif
%if %{use_systemdb}
	--with-system-db \
	--with-db-jar=%{_datadir}/java/db-%{libdbver}.jar \
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
	--with-system-cairo \
	--with-system-nas \
	--with-dynamic-xinerama \
	--with-system-xmlsec \
	--enable-binfilter \
	--enable-access \
	--enable-split-app-modules \
	--enable-split-opt-features \
	--without-myspell-dicts \
	--with-system-dicts \
	--with-external-dict-dir=%{_datadir}/dict/ooo \
        --with-external-hyph-dir=%{_datadir}/dict/ooo \
        --with-external-thes-dir=%{_datadir}/dict/ooo \
	--with-system-poppler \
        --disable-kde \
        --disable-kdeab \
        --enable-pdfimport \
        --enable-minimizer \
        --enable-presenter-console \
        --enable-wiki-publisher \
%if %{use_openclipart}
        --with-openclipart=%{_datadir}/images/openclipart \
%endif
%if %{use_mono}
# dev300
#	--enable-mono \
#	--with-mono-gac-root=%{_libdir} \
%else
#dev300: (--disable-mono command not foud)
#	--disable-mono \
%endif
%if %{use_smp}
#dev300: (--with-num-cpus command not found  )
#	--with-num-cpus=${RPM_BUILD_NCPUS:-1}
%endif
%if %{use_ccache} && !%{use_icecream}
	--with-gcc-speedup=ccache \
%else
 %if !%{use_ccache} && %{use_icecream}
	--with-gcc-speedup=icecream \
	--with-max-jobs=10 \
	--with-icecream-bindir=%{_libdir}/icecc/bin
 %else
  %if %{use_ccache} && %{use_icecream}
	--with-gcc-speedup=ccache,icecream \
	--with-max-jobs=10 \
	--with-icecream-bindir=%{_libdir}/icecc/bin
  %endif
 %endif
%endif


#dev300 (ooo-build fixes by now).
#This fix needs to be submmited to ooo-build
cp -f %{SOURCE87} %{_builddir}/ooo-build-3.0.1-%{ooobuildver}/patches/dev300/apply
cp -f %{SOURCE89} %{_builddir}/ooo-build-3.0.1-%{ooobuildver}/bin/package-ooo
cp -f %{SOURCE88} %{_builddir}/ooo-build-3.0.1-%{ooobuildver}/patches/dev300/
cp -f %{SOURCE92} %{_builddir}/ooo-build-3.0.1-%{ooobuildver}/patches/dev300/

echo "Configure end at: "`date` >> ooobuildtime.log 

#Patches back ported from newer ooo-builds - NONEED after 3.0.0.2
# cp -f %{SOURCE100} %{_builddir}/ooo-build-%{ooobuildver}/patches/dev300/layout-simple-dialogs-toolkit.diff
# cp -f %{SOURCE101} %{_builddir}/ooo-build-%{ooobuildver}/patches/dev300/layout-simple-dialogs-sc.diff

echo "Make start at: "`date` >> ooobuildtime.log 

# some configs  to improve build process 
# http://wiki.services.openoffice.org/wiki/Building_OpenOffice.org
# needs to check if it does any effect 
export nodep=TRUE
export NO_HIDS=TRUE 
export MAXPROCESS=4 

make \
	ARCH_FLAGS="%{optflags} %{optsafe} -fno-omit-frame-pointer -fno-strict-aliasing" \
	ARCH_FLAGS_CC="%{optflags} %{optsafe} -fno-omit-frame-pointer -fno-strict-aliasing" \
	ARCH_FLAGS_CXX="%{optflags} %{optsafe} -fno-omit-frame-pointer -fno-strict-aliasing -fpermissive -fvisibility-inlines-hidden" \
	ARCH_FLAGS_OPT="%{optflags} -O2 %{optsafe}"

echo "Make end at: "`date` >> ooobuildtime.log 

echo "Install start at: "`date` >> ooobuildtime.log 

%install
# sbin due to icu stuff there
PATH=$PATH:/usr/sbin

rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}/opt
# FIXME: there are template/<locale>wizard/letter already
#rm -rf %{buildroot}%{ooodir}/share/template/wizard/letter/

# use the dicts from myspell-<lang>
# rm -rf %{buildroot}%{ooodir}/share/dict/ooo
# ln -s %{_datadir}/dict/ooo %{buildroot}%{ooodir}/share/dict

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

# MS OOXML (#36465)
desktop-file-install \
  --add-mime-type="application/vnd.openxmlformats-officedocument.wordprocessingml.document" \
  --add-mime-type="application/vnd.ms-word.document.macroEnabled.12" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/writer*desktop

desktop-file-install \
  --add-mime-type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" \
  --add-mime-type="application/vnd.ms-excel.sheet.macroEnabled.12" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/calc*desktop

desktop-file-install \
  --add-mime-type="application/vnd.openxmlformats-officedocument.presentationml.presentation" \
  --add-mime-type="application/vnd.ms-powerpoint.presentation.macroEnabled.12" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/impress*desktop

# Remove version on names so better position on menu and give consistency under old links #43922 
for dskt in base calc draw impress math template web writer; do 
   %ifarch x86_64
	mv %{buildroot}%{_datadir}/applications/${dskt}3.0.1_64.desktop %{buildroot}%{_datadir}/applications/${dskt}64.desktop
   %else
        mv %{buildroot}%{_datadir}/applications/${dskt}3.0.1.desktop %{buildroot}%{_datadir}/applications/${dskt}.desktop
  %endif
done;

# XXX FontOOo|DictOOo wizard
# these should die soon (after 2008.1)
# dev300: including basis3.0 before share
# install -m 644 %{SOURCE50} %{buildroot}%{_libdir}/ooo-%{mdvsuffix}/basis3.0/share/dict/FontOOo.sxw
# install -m 644 %{SOURCE51} %{buildroot}%{_libdir}/ooo-%{mdvsuffix}/basis3.0/share/dict/DicOOo.sxw

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

# dev 300 2.3 ???
# %if %{use_mono}
# Versionify mono-ooo.pc
# mv %{buildroot}%{_libdir}/pkgconfig/mono-ooo-%{mdvsuffix}.pc \
#   %{buildroot}%{_libdir}/pkgconfig/mono-ooo%{mdvsuffix}-2.3.pc
# %endif

# Install versioned profile.d/ files (#33475)
# Profiles for set PYTHONPATH variables (Python Integration)
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
sed 's@%%{ooodir}@%{ooodir}@g' \
	%{_sourcedir}/openoffice.org.csh > \
	%{buildroot}%{_sysconfdir}/profile.d/openoffice.org%{mdvsuffix}.csh
sed 's@%%{ooodir}@%{ooodir}@g' \
	%{_sourcedir}/openoffice.org.sh > \
	%{buildroot}%{_sysconfdir}/profile.d/openoffice.org%{mdvsuffix}.sh

# dev300 (Alpha2) :
# BrOffice.org Support (install)
function bro() {
   exp="$1"
   f="$2"
#   mv "$f" "$f.ooo"
#   mv "$f" "$f.ooo"
#   echo -n > "$f"
  %if %l10n
#   sed "$exp" "$f.ooo" > "$f.bro"
   sed "$exp" "$f" > "$f.bro"
  %endif
#  sed -i "s@$f\$@$f.ooo@" %{_builddir}/ooo-build-%{ooobuildver}/build/*.txt
}

## Change suite name in the program itself
cd %{buildroot}%{ooodir}
 bro "s/OpenO/BrO/;s/openo/bro/" program/bootstraprc
 bro "s/en-US/pt-BR/;s/openo/bro/" program/versionrc
 bro "s/OpenO/BrO/" basis3.0/share/registry/data/org/openoffice/Setup.xcu
cd -

# Change the suite name in .desktop files for pt_BR locale
sed -i '/pt_BR/{s/OpenO/BrO/}' %{buildroot}%{_datadir}/applications/*.desktop

# Place symlinks br<app> -> oo<app>
 %if %l10n
 cd %{buildroot}%{_bindir}
 # fix me wrong brffice symb link name 
 for i in oo*; do
	ln -s $i ${i/oo/br}
 done
 cd -
 %endif
# End of BrOffice support (install)

# Change progress bar colors
sed -i '/^ProgressBarColor/d;/^ProgressFrameColor/d' \
	%{buildroot}%{ooodir}/program/sofficerc
echo 'ProgressBarColor=68,135,223' >> %{buildroot}%{ooodir}/program/sofficerc
echo 'ProgressFrameColor=112,171,229' >> %{buildroot}%{ooodir}/program/sofficerc

#dev300 fix position and size
sed -i '/^ProgressPosition/d;/^ProgressSize/d' \
	%{buildroot}%{ooodir}/program/sofficerc
echo 'ProgressPosition=10,307' >> %{buildroot}%{ooodir}/program/sofficerc
echo 'ProgressSize=377,9' >> %{buildroot}%{ooodir}/program/sofficerc

# new icons
tar xjf %{SOURCE30} -C %{buildroot}%{_datadir}

# remove old icons, 64 arch have use same icon as 586, duplicates ?
rm -rf %{buildroot}%{_datadir}/icons/hicolor/*/apps/ooo-writer3.0.1_64.png
rm -rf %{buildroot}%{_datadir}/icons/hicolor/*/apps/ooo-calc3.0.1_64.png
rm -rf %{buildroot}%{_datadir}/icons/hicolor/*/apps/ooo-impress3.0.1_64.png
rm -rf %{buildroot}%{_datadir}/icons/hicolor/*/apps/ooo-draw3.0.1_64.png
rm -rf %{buildroot}%{_datadir}/icons/hicolor/*/apps/ooo-base3.0.1_64.png
rm -rf %{buildroot}%{_datadir}/icons/hicolor/*/apps/ooo-math3.0.1_64.png
rm -rf %{buildroot}%{_datadir}/icons/hicolor/*/apps/ooo-printeradmin3.0.1_64.png

# remove icons we dont have these sizes yet
rm -rf %{buildroot}%{_datadir}/icons/hicolor/22x22/apps/*
rm -rf %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/*

# remove scalables icons since we dont have yet
rm -rf %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/*

# fix name of desktop icons on desktop files
for f in %{buildroot}%{_datadir}/applications/*desktop; do
   sed -i 's@Icon=ooo-\(base\|calc\|draw\|impress\|math\|writer\)3\.0.*@Icon=ooo-\13\.0@' $f
done

# XXX disable the menu entries for these
# besides not being real apps, we don't have new-style icons for them
# see #26311#c33
for f in %{buildroot}%{_datadir}/applications/template*desktop \
	%{buildroot}%{_datadir}/applications/web*desktop; do
	echo 'NoDisplay=true' >> $f
done

# Enable Formula - needs fixes xdg files 
# sed -i 's/NoDisplay=true//' %{buildroot}%{_datadir}/applications/math*desktop;                                             

# Fixes japanese translations on desktop files
# Find out a better solution (two patches)
%ifarch x86_64
patch -p0 -d %{buildroot} < %{SOURCE103}
%else
patch -p0 -d %{buildroot} < %{SOURCE102}
%endif 

# templates for kde "create new" context menu
tar xjf %{SOURCE31} -C %{buildroot}%{_datadir}

# unpack pdfimport extension
# install -d -m 755 %{buildroot}%{ooodir}/extensions/pdfimport.oxt
# unzip %{_builddir}/ooo-build-%{ooobuildver}/build/dev300-m28/solver/300/unxlng*/bin/pdfimport/pdfimport.oxt -d %{buildroot}%{ooodir}/extensions/pdfimport.oxt
# chmod -x %{buildroot}%{ooodir}/extensions/pdfimport.oxt/help/component.txt

# copy extensions 
cp %{_builddir}/ooo-build-3.0.1-%{ooobuildver}/build/%{oootagver}/solver/300/unxlng*/bin/pdfimport/pdfimport.oxt %{buildroot}%{ooodir}/ 
cp %{_builddir}/ooo-build-3.0.1-%{ooobuildver}/build/%{oootagver}/solver/300/unxlng*/bin/presenter/presenter-screen.oxt %{buildroot}%{ooodir}/ 
# cp %{_builddir}/ooo-build-3.0.1-%{ooobuildver}/build/%{oootagver}/solver/300/unxlng*/bin/sun-report-builder.oxt %{buildroot}%{ooodir}/ 
cp %{_builddir}/ooo-build-3.0.1-%{ooobuildver}/build/%{oootagver}/solver/300/unxlng*/bin/swext/wiki-publisher.oxt %{buildroot}%{ooodir}/ 
cp %{_builddir}/ooo-build-3.0.1-%{ooobuildver}/build/%{oootagver}/solver/300/unxlng*/bin/minimizer/sun-presentation-minimizer.oxt %{buildroot}%{ooodir}/ 

%clean
rm -rf %{buildroot}

%post common
# <mrl> Bogus versioning in previous alternatives setup forces us to do this
# We can safelly remove it, as we are obsoleting that version anyway.
/usr/sbin/update-alternatives --remove ooffice %{_bindir}/ooffice2.1 || :
# We changed the master name here.
/usr/sbin/update-alternatives --remove ooffice %{_bindir}/ooffice2.3 || :
/usr/sbin/update-alternatives \
	--install %{_bindir}/soffice soffice   %{_bindir}/ooffice%{mdvsuffix} %{oooaltpri} \
	--slave %{_bindir}/ooffice   ooffice   %{_bindir}/ooffice%{mdvsuffix} \
	--slave %{_bindir}/oowriter  oowriter  %{_bindir}/oowriter%{mdvsuffix} \
	--slave %{_bindir}/oobase    oobase    %{_bindir}/oobase%{mdvsuffix} \
	--slave %{_bindir}/oodraw    oodraw    %{_bindir}/oodraw%{mdvsuffix} \
	--slave %{_bindir}/ooimpress ooimpress %{_bindir}/ooimpress%{mdvsuffix} \
	--slave %{_bindir}/oocalc    oocalc    %{_bindir}/oocalc%{mdvsuffix} \
	--slave %{_bindir}/ootool    ootool    %{_bindir}/ootool%{mdvsuffix} \
	--slave %{_bindir}/ooweb     ooweb     %{_bindir}/ooweb%{mdvsuffix}
[ -e %{_bindir}/soffice ] || /usr/sbin/update-alternatives --auto soffice

# Dev300 without bootstraptc no interface language can be determinated
# BrOffice support %post
# for i in \
#    %{ooodir}/program/bootstraprc \
#    %{ooodir}/program/versionrc \
#    %{ooodir}/basis3.0/share/registry/data/org/openoffice/Setup.xcu
# do
#    if [ -f "$i" ]; then
#        rm -f "$i"
#    fi
# done

#dev300: including basis3.0 before program
# alternatives names follows oobr_<filename> mark, making it explicit.
 /usr/sbin/update-alternatives \
	--install %{ooodir}/program/bootstraprc oobr_bootstraprc%{mdvsuffix} \
		%{ooodir}/program/bootstraprc.ooo 1 \
	--slave %{ooodir}/program/versionrc oobr_versionrc%{mdvsuffix} \
		%{ooodir}/program/versionrc.ooo \
	--slave %{ooodir}/basis3.0/share/registry/data/org/openoffice/Setup.xcu oobr_Setup.xcu%{mdvsuffix} \
		%{ooodir}/basis3.0/share/registry/data/org/openoffice/Setup.xcu.ooo
# Always do this configuration, as the switch should be transparent.
/usr/sbin/update-alternatives --auto oobr_bootstraprc
# End of BrOffice support %post

%{update_desktop_database}
%update_icon_cache gnome
%update_icon_cache hicolor

# Remove ooobuildtime.log misplaced file
if [ -f /ooobuildtime.log ]; then
      mkdir -p /tmp/ooo.tmp.mdv.rc2/
      mv /ooobuildtime.log /tmp/ooo.tmp.mdv.rc2/
      rm -r /tmp/ooo.tmp.mdv.rc2/
fi

%postun common
if [ ! -e "%{_bindir}/ooffice%{mdvsuffix}" ]; then
        /usr/sbin/update-alternatives --remove soffice %{_bindir}/ooffice%{mdvsuffix}
fi

# BrOffice support %postun common
 if [ ! -e "%{ooodir}/program/bootstraprc.ooo" ]; then
        /usr/sbin/update-alternatives --remove oobr_bootstraprc%{mdvsuffix} %{ooodir}/program/bootstraprc.ooo
 fi
# End of BrOffice support %postun common
%{clean_desktop_database}
%clean_icon_cache gnome
%clean_icon_cache hicolor


%if %l10n
%post l10n-pt_BR
# BrOffice support %post l10n-pt_BR
# alternatives names follows oobr_<filename> mark, making it explicit.
 /usr/sbin/update-alternatives \
	--install %{ooodir}/program/bootstraprc oobr_bootstraprc%{mdvsuffix} \
		%{ooodir}/program/bootstraprc.bro 2 \
	--slave %{ooodir}/program/versionrc oobr_versionrc%{mdvsuffix} \
		%{ooodir}/program/versionrc.bro \
	--slave %{ooodir}/basis3.0/share/registry/data/org/openoffice/Setup.xcu oobr_Setup.xcu%{mdvsuffix} \
		%{ooodir}/basis3.0/share/registry/data/org/openoffice/Setup.xcu.bro
# Always do this configuration, as the switch should be transparent.
/usr/sbin/update-alternatives --auto oobr_bootstraprc
# End of BrOffice support %post l10n-pt_BR

# %{update_desktop_database}

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

%post pdfimport
# upgrade 
if [ $1 -ge 2 ];then
	# removes old installed pdfimport extension 
	idpdfimport=$(%unopkg list --shared 2> /dev/null | sed -ne 's/^Identifier: \(com.sun.star.PDFImport-linux.*\)/\1/p');
	if [ "z$idpdfimport" != "z" ]; then
		%unopkg remove --shared $idpdfimport 2> /dev/null
		%unopkg list --shared &> /dev/null
	fi
fi
#install new pdfimport version
%unopkg add --shared %{ooodir}/pdfimport.oxt 2> /dev/null
%unopkg list --shared &> /dev/null 

#uninstall
%preun pdfimport 
if [ $1 -eq 0 ];then
	idpdfimport=$(%unopkg list --shared 2> /dev/null | sed -ne 's/^Identifier: \(com.sun.star.PDFImport-linux.*\)/\1/p');
	if [ "z$idpdfimport" != "z" ]; then
		%unopkg remove --shared $idpdfimport 2> /dev/null
		#clean footprint cache
		%unopkg list --shared &> /dev/null
	fi
fi

%post presenter-screen
# upgrade 
if [ $1 -ge 2 ];then
	idextension=$(%unopkg list --shared 2> /dev/null | sed -ne 's/^Identifier: \(com.sun.PresenterScreen-linux.*\)/\1/p');
	if [ "z$idextension" ! "z" ]; then
		%unopkg remove --shared $idextension 2> /dev/null
		%unopkg list --shared &> /dev/null
	fi
fi
#install 
%unopkg add --shared %{ooodir}/presenter-screen.oxt 2> /dev/null
%unopkg list --shared &> /dev/null 


%preun presenter-screen  
if [ $1 -eq 0 ];then
	idextension=$(%unopkg list --shared 2> /dev/null | sed -ne 's/^Identifier: \(com.sun.PresenterScreen-linux.*\)/\1/p');
	if [ "z$idextension" != "z" ]; then
		%unopkg remove --shared $idextension 2> /dev/null
		%unopkg list --shared &> /dev/null
	fi
fi

# %post report-builder
# upgrade 
# if [ $1 -ge 1 ];then
#	idextension=$(%unopkg list --shared 2> /dev/null | sed -ne 's/^Identifier: \(com.sun.reportdesigner\)/\1/p');
#	if [ "z$idextension" != "z" ]; then
#		%unopkg remove --shared $idextension 2> /dev/null
#		%unopkg list --shared &> /dev/null
#	fi
# fi
#install 
# %unopkg add --shared %{ooodir}/sun-report-builder.oxt 2> /dev/null
# %unopkg list --shared &> /dev/null 

#uninstall
# %preun report-builder
# if [ $1 -eq 0 ];then
#	idextension=$(%unopkg list --shared 2> /dev/null | sed -ne 's/^Identifier: \(com.sun.reportdesigner\)/\1/p');
#	if [ "z$idextension" != "z" ]; then
#		%unopkg remove --shared $idextension 2> /dev/null
#		%unopkg list --shared &> /dev/null
#	fi
# fi

%post wiki-publisher
# upgrade 
if [ $1 -ge 2 ];then
	idextension=$(%unopkg list --shared 2> /dev/null | sed -ne 's/^Identifier: \(com.sun.wiki-publisher\)/\1/p');
	if [ "z$idextension" != "z" ]; then
		%unopkg remove --shared $idextension 2> /dev/null
		%unopkg list --shared &> /dev/null
	fi
fi	
#install 
%unopkg add --shared %{ooodir}/wiki-publisher.oxt 2> /dev/null
%unopkg list --shared &> /dev/null 

%preun wiki-publisher
if [ $1 -eq 0 ];then
	idextension=$(%unopkg list --shared 2> /dev/null | sed -ne 's/^Identifier: \(com.sun.wiki-publisher\)/\1/p');
	if [ "z$idextension" != "z" ]; then
		%unopkg remove --shared $idextension 2> /dev/null
		%unopkg list --shared &> /dev/null
	fi
fi

%post presentation-minimizer
# upgrade 
if [ $1 -ge 2 ];then
	idextension=$(%unopkg list --shared 2> /dev/null | sed -ne 's/^Identifier: \(com.sun.star.PresentationMinimizer-linux.*\)/\1/p');
	if [ "z$idextension" != "z" ]; then
		%unopkg remove --shared $idextension 2> /dev/null
		%unopkg list --shared &> /dev/null
	fi
fi
#install 
%unopkg add --shared %{ooodir}/sun-presentation-minimizer.oxt 2> /dev/null
%unopkg list --shared &> /dev/null 

%preun presentation-minimizer
if [ $1 -eq 0 ];then
	idextension=$(%unopkg list --shared 2> /dev/null | sed -ne 's/^Identifier: \(com.sun.star.PresentationMinimizer-linux.*\)/\1/p');
	if [ "z$idpdfimport" != "z" ]; then
		%unopkg remove --shared $idextension 2> /dev/null
		%unopkg list --shared &> /dev/null
	fi
fi

%files

%files base -f build/base_list.txt
%{_bindir}/oobase%{mdvsuffix}
%ifarch x86_64
%{_datadir}/applications/base64.desktop
%else
%{_datadir}/applications/base.desktop
%endif
%{_mandir}/man1/oobase%{mdvsuffix}.1*

%files calc -f build/calc_list.txt
%{_bindir}/oocalc%{mdvsuffix}
%ifarch x86_64
%{_datadir}/applications/calc64.desktop
%else
%{_datadir}/applications/calc.desktop
%endif
%{_datadir}/templates/ooo-spreadsheet.desktop
%{_datadir}/templates/.source/ooo-spreadsheet.ods
%{_mandir}/man1/oocalc%{mdvsuffix}.1*

%files common -f build/common_list.txt 
%{_sysconfdir}/bash_completion.d/ooffice%{mdvsuffix}
%{_sysconfdir}/profile.d/openoffice.org%{mdvsuffix}.*
%{_bindir}/ooconfig%{mdvsuffix}
%{_bindir}/ooffice%{mdvsuffix}
%{_bindir}/oofromtemplate%{mdvsuffix}
%{_bindir}/ootool%{mdvsuffix}
%{_bindir}/soffice%{mdvsuffix}

%{_datadir}/applications/template*.desktop

%{_datadir}/icons/hicolor/*/apps/ooo-base3.0*
%{_datadir}/icons/hicolor/*/apps/ooo-calc3.0*
%{_datadir}/icons/hicolor/*/apps/ooo-draw3.0*
%{_datadir}/icons/hicolor/*/apps/ooo-gulls3.0*
%{_datadir}/icons/hicolor/*/apps/ooo-impress3.0*
%{_datadir}/icons/hicolor/*/apps/ooo-math3.0*
%{_datadir}/icons/hicolor/*/apps/ooo-printeradmin3.0*
%{_datadir}/icons/hicolor/*/apps/ooo-template3.0*
%{_datadir}/icons/hicolor/*/apps/ooo-web3.0*
%{_datadir}/icons/hicolor/*/apps/ooo-writer3.0*
%{_datadir}/icons/hicolor/*/apps/ooo-main3.0*

# new icons
# %{_datadir}/icons/hicolor/*/apps/openofficeorg3-*.png
# moved to mandriva-kde-config 
#%{_datadir}/icons/hicolor/*/mimetypes/openofficeorg3-*.png
# %{_datadir}/icons/gnome/*/apps/openofficeorg3-*.png
# %{_datadir}/icons/gnome/*/mimetypes/openofficeorg3-*.png
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
# XXX Due to alternatives upgrade from 2.3.0.5-1mdv to -2mdv
# (.desktop files are not included because they are in their
# respective subpackages already (#38412))

#dev300 
# %ghost %{ooodir}/program/bootstraprc.ooo
# %ghost %{ooodir}/program/versionrc.ooo
# %ghost %{ooodir}/basis3.0/program/versionrc.ooo
# ghost %{ooodir}/basis3.0/share/registry/data/org/openoffice/Setup.xcu.ooo
# %ghost %{ooodir}/share/uno_packages

# XXX not sure where these came from
%{_bindir}/unopkg%{mdvsuffix}
%{_mandir}/man1/unopkg%{mdvsuffix}.1*
%{_datadir}/applications/ooo-extension-manager*.desktop


%files core -f build/core_list.txt

%files devel -f build/sdk_list_fixed.txt

%files devel-doc -f build/sdk_doc_list.txt

%files draw -f build/draw_list.txt
%{_bindir}/oodraw%{mdvsuffix}
%ifarch x86_64
%{_datadir}/applications/draw64.desktop
%else
%{_datadir}/applications/draw.desktop
%endif

%{_datadir}/templates/ooo-drawing.desktop
%{_datadir}/templates/.source/ooo-drawing.odg
%{_mandir}/man1/oodraw%{mdvsuffix}.1*

# dev300: 
# %files dtd-officedocument1.0 -f build/dtd_list.txt

# dev300: 
%files filter-binfilter -f build/filter-binfilter_list.txt

%files gnome -f build/gnome_list.txt

%files impress -f build/impress_list.txt
%{_bindir}/ooimpress%{mdvsuffix}
%ifarch x86_64 
%{_datadir}/applications/impress64.desktop
%else
%{_datadir}/applications/impress.desktop
%endif
%{_datadir}/templates/ooo-presentation.desktop
%{_datadir}/templates/.source/ooo-presentation.odp
%{_mandir}/man1/ooimpress%{mdvsuffix}.1*

%files java-common -f build/java_common_list.txt

# %files kde -f build/kde_list.txt

%files math -f build/math_list.txt
%{_bindir}/oomath%{mdvsuffix}
%ifarch x86_64
%{_datadir}/applications/math64.desktop
%else
%{_datadir}/applications/math.desktop
%endif 
%{_mandir}/man1/oomath%{mdvsuffix}.1*

%files openclipart -f build/gallery_list.txt

%files pyuno -f build/pyuno_list.txt

#%files qa-api-tests
#%{ooodir}/qadevOOo

%files testtool -f build/testtool_list.txt

#dev300: file not found
%files style-galaxy
#%{ooodir}/share/config/images.zip
%{ooodir}/basis3.0/share/config/images.zip

#dev300: file not found
%files style-crystal
#%{ooodir}/share/config/images_crystal.zip
%{ooodir}/basis3.0/share/config/images_crystal.zip

#dev300: file not found
%files style-hicontrast
#%{ooodir}/share/config/images_hicontrast.zip
%{ooodir}/basis3.0/share/config/images_hicontrast.zip

#dev300: file not found
%files style-industrial
# %{ooodir}/share/config/images_industrial.zip
%{ooodir}/basis3.0/share/config/images_industrial.zip

#dev300: file not found
%files style-tango
#%{ooodir}/share/config/images_tango.zip
%{ooodir}/basis3.0/share/config/images_tango.zip

%files writer -f build/writer_list.txt
%{_bindir}/ooweb%{mdvsuffix}
%{_bindir}/oowriter%{mdvsuffix}
%ifarch x86_64
%{_datadir}/applications/writer64.desktop
%{_datadir}/applications/web64.desktop
%else
%{_datadir}/applications/writer.desktop
%{_datadir}/applications/web.desktop
%endif 
%{_datadir}/templates/ooo-text.desktop
%{_datadir}/templates/.source/ooo-text.odt
%{_mandir}/man1/ooweb%{mdvsuffix}.1*
%{_mandir}/man1/oowriter%{mdvsuffix}.1*

%if %{use_mono}
%files mono -f build/mono_list.txt
%defattr(-,root,root)
%{_libdir}/pkgconfig/mono-ooo-%{mdvsuffix}.pc
# %{_libdir}/pkgconfig/mono-ooo%{mdvsuffix}-2.3.pc
# %{_libdir}/mono/*/*/*
# %{_libdir}/mono/ooo-%{mdvsuffix}
%endif

%files pdfimport
%defattr(-,root,root,-)
%{ooodir}/pdfimport.oxt

%files presenter-screen
%defattr(-,root,root,-)
%{ooodir}/presenter-screen.oxt

# %files report-builder
# %defattr(-,root,root,-)
# %{ooodir}/sun-report-builder.oxt

%files wiki-publisher
%defattr(-,root,root,-)
%{ooodir}/wiki-publisher.oxt

%files presentation-minimizer
%defattr(-,root,root,-)
%{ooodir}/sun-presentation-minimizer.oxt

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

%files l10n-en_GB -f build/lang_en_GB_list.txt
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

%files l10n-pt_BR -f build/lang_pt_BR_list.txt
%defattr(-,root,root)
# BrOffice support
# XXX Yes, by this way there will be broken symlinks if you don't make a full suite
# installation.
%{_bindir}/br*
%{ooodir}/program/bootstraprc.bro
%{ooodir}/program/versionrc.bro
%{ooodir}/basis3.0/share/registry/data/org/openoffice/Setup.xcu.bro

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

%files l10n-zh_CN -f build/lang_zh_CN_list.txt
%defattr(-,root,root)

%files l10n-zh_TW -f build/lang_zh_TW_list.txt
%defattr(-,root,root)

%files l10n-zu -f build/lang_zu_list.txt
%defattr(-,root,root)

%files help-it -f build/help_it_list.txt
%defattr(-,root,root)

%files help-af -f build/help_af_list.txt
%defattr(-,root,root)

%files help-ar -f build/help_ar_list.txt
%defattr(-,root,root)

%files help-bg -f build/help_bg_list.txt
%defattr(-,root,root)

%files help-br -f build/help_br_list.txt
%defattr(-,root,root)

%files help-bs -f build/help_bs_list.txt
%defattr(-,root,root)

%files help-ca -f build/help_ca_list.txt
%defattr(-,root,root)

%files help-cs -f build/help_cs_list.txt
%defattr(-,root,root)

%files help-cy -f build/help_cy_list.txt
%defattr(-,root,root)

%files help-da -f build/help_da_list.txt
%defattr(-,root,root)

%files help-de -f build/help_de_list.txt
%defattr(-,root,root)

%files help-el -f build/help_el_list.txt
%defattr(-,root,root)

%files help-en_GB -f build/help_en_GB_list.txt
%defattr(-,root,root)

%files help-es -f build/help_es_list.txt
%defattr(-,root,root)

%files help-et -f build/help_et_list.txt
%defattr(-,root,root)

%files help-eu -f build/help_eu_list.txt
%defattr(-,root,root)

%files help-fi -f build/help_fi_list.txt
%defattr(-,root,root)

%files help-fr -f build/help_fr_list.txt
%defattr(-,root,root)

%files help-he -f build/help_he_list.txt
%defattr(-,root,root)

%files help-hi -f build/help_hi_list.txt
%defattr(-,root,root)

%files help-hu -f build/help_hu_list.txt
%defattr(-,root,root)

%files help-ja -f build/help_ja_list.txt
%defattr(-,root,root)

%files help-ko -f build/help_ko_list.txt
%defattr(-,root,root)

%files help-mk -f build/help_mk_list.txt
%defattr(-,root,root)

%files help-nb -f build/help_nb_list.txt
%defattr(-,root,root)

%files help-nl -f build/help_nl_list.txt
%defattr(-,root,root)

%files help-nn -f build/help_nn_list.txt
%defattr(-,root,root)

%files help-pl -f build/help_pl_list.txt
%defattr(-,root,root)

%files help-pt -f build/help_pt_list.txt
%defattr(-,root,root)

%files help-pt_BR -f build/help_pt_BR_list.txt
%defattr(-,root,root)

%files help-ru -f build/help_ru_list.txt
%defattr(-,root,root)

%files help-sk -f build/help_sk_list.txt
%defattr(-,root,root)

%files help-sl -f build/help_sl_list.txt
%defattr(-,root,root)

%files help-sv -f build/help_sv_list.txt
%defattr(-,root,root)

%files help-ta -f build/help_ta_list.txt
%defattr(-,root,root)

%files help-tr -f build/help_tr_list.txt
%defattr(-,root,root)

%files help-zh_CN -f build/help_zh_CN_list.txt
%defattr(-,root,root)

%files help-zh_TW -f build/help_zh_TW_list.txt
%defattr(-,root,root)

%files help-zu -f build/help_zu_list.txt
%defattr(-,root,root)

%files help-en_US -f build/help_en_US_list.txt
%defattr(-,root,root)
%endif

%changelog
* Tue Mar 03 2009 Rafael Cabral <cabral@mandriva.com> 0:3.0.1-2mdv2009.1
- split out pdf import extension from common to a new package: 
  openoffice.org-pdfimport
- new enabled extension packages: 
  openoffice.org-wiki-publisher
  openoffice.org-presenter-screen
  openoffice.org-presentation-minimizer
- remove kde-libs from build requires
- change qt3-devel to qt4-devel in build requires since the build
  scream about that even we are not using qt things yet.
- rebuild to cooker 

* Fri Feb 05 2009 Rafael Cabral <cabral@mandriva.com> 0:3.0.1-1mdv2009.1
- Revision 337782
- New upstream version 3.0.1 (official stable release)

* Mon Jan 12 2009 Rafael Cabral <cabral@mandriva.com> 0:3.0.1-0.rc1.1mdv2009.0
- Revision 332829
- New upstream version 3.0.1 (ooo-build call this release as rc1)
- Changed to use libicu40 from the system (--with-system-icu)
- Rebuild for Python 2.6
- Fix build (lots of rintf aruments clean up) ooo-build patch buildfix-fmtargs.diff

* Fri Nov 20 2008 Rafael Cabral <cabral@mandriva.com> 0:3.0-1mdv2009.0
- Revision 332829 
- ooo-build OpenOffice.org 3.0 based on stable upstream
- Fix OOo Greek crash on start up - #44821
- PyUno loadComponentFromUrl comes out - regression #45445 
- It doesn't get clipart-openclipart - regression #45196.
- Suggests help-en_US which is default l10n language - releated #44809
- As suggested xdg-mail as default mailer - #43917 
- Remove misplaced ooobuildtime.log
- PDF-import extension must to work even OOo will be update

* Fri Oct 03 2008 Frederic Crozat <fcrozat@mandriva.com> 0:3.0-0.rc2.2mdv2009.0
- Add epoch to fix upgrade from Mdv 2009 RC2 and allow gnome subpackage to be installed

* Mon Sep 30 2008 Rafael da Veiga Cabral <cabral@mandriva.com> 3.0-0.rc2.1mdv2009.0
+ Revision 290159  
+ Using new ooo-build-3.0 svn branch based on OpenOffice.org rc2
+ Remove svn revision from package name
  - Ooo-build has migrated it 3.0 sources to a new stable branch and that svn 
    revision info doesn't make sense anymore for us and further naming package wasn't 
    following Mandriva standards as well. 
+ Path of Python Uno integration fixed
+ Calc fixes
   - Formulas was not being saved - #44032 
   - Formulas onto spreadsheets of old OOo versions was not being showed - #44010
+ Improving build
 -  exporting nodep, NO_HIDS, MAXPROCESS
+ Spec clean ups

* Mon Sep 22 2008 Rafael da Veiga Cabral <cabral@mandriva.com> 3.0svn13581-3mdv2009.0
+ Revision 287960
- New menu icons - #43937
- New mime types icons  
- Rename desktop icons file name - #43922
- Calc hangs on sorting (reversed sc-sort-cell-note-position.diff) - #43932
- Added conflicts on common package with gnome why libvclplug_gtkli.so 
has been moved - #43920

* Mon Sep 01 2008 Rafael da Veiga Cabral <cabral@mandriva.com> 3.0svn13581-2mdv2009.0
+ Revision 271602
- Change Andromeda theme name to Galaxy - #42801
- Vendor/Packager filled out
- Split misplaced help files out of l10n packages
- Split misplaced en_US help files out of common to a new package
- Java-common changed to base Suggests
- None writing aids fixed (using system hunspell) - #42885 
- Drop printer-properties-disable patch - #40834
- Moved librdf.so.0 to provides exception (ksnapshot) - #42927
- New splash and about banners
- Added PDF Import extension in common package (installed by default) - #42885
- New ooo-build 3.0.0 version (revision 13581)
- For a better look libvclplug_gtkli.so has been moved to common package
  We've got gtk layouts as default
- libraptor.so.1 to provides exceptions (ksnapshot/amarok) - #42927
- Linking with neon 0.27 - #43368 
- Calc hangs whenever adding a new sheet from Insert menu - #43405
- Impress and Draw hang by using zoom from menu View - #43384
- Weak dependency of Mono (mono and libmono0 is now as requires exception) - #43484
- New user directory changed to .openoffice.org3 (it'd have solve #42800, #41228)
- Default toolbar icon size was changed to small as default to a better look
- libxmlsec1-nss.so.1 and libxmlsec1.so.1 to provides exceptions

* Mon Aug 04 2008 Rafael da Veiga Cabral <cabral@mandriva.com> 3.0svn13475-1mdv2009.0
+ Revision 13471
- New Openoffice.org 3.0 beta 2.

* Fri Apr 04 2008 Ademar de Souza Reis Jr. <ademar@mandriva.com> 2.4.0.7-1mdv2008.1
+ Revision
- new ooo-build upstream version: 2.4.0.7
  Closes: #38874 (Some numbers are shown in Eastern-Arabic)
  Closes: #39799 (oowriter: broken "idents & spacing" in "format paragraph")
  Closes: #39789 (oowriter spellcheck doesn't work)
- hunspell support is upstream, so remove unecessary sources and flags

* Fri Mar 28 2008 Ademar de Souza Reis Jr. <ademar@mandriva.com> 2.4.0.4-2mdv2008.1
+ Revision 191275
- Remove some ghost entries from -common package which were causing it to
  own files from the application subpackages (Closes: #38412);
- Since we're installing icons on the system, add %%clean_icon_cache calls
  to -common %%post and %%postun sections (spotted by Frederic Crozat);
- Fix icons names on x86_64 .desktop files (Closes: #39508);
- Remove menu entries for "OpenOffice.org" and "Web/Writer". They're not
  real applications and we don't have new icons for them (see #26311#c33);
- Minor spec cleanup (XXX comments, etc).

* Wed Mar 26 2008 Ademar de Souza Reis Jr. <ademar@mandriva.com> 2.4.0.4-1mdv2008.1
+ Revision 190514
- New version: 2.4.0.4 (ooo-build 2.4.0.4, ooo 2.4.0-rc6 - same as 2.4.0)
- Added unopkg files (ooo extensions manager)
- New splash screen (Closes: #38720)
- Added OOXML mime-types to .desktop files (Closes: #36465)
- Changed some conflict rules (due to the split) from '= 2.2.1'
  to '<= 2.2.1', so that we can upgrade mdv-2007.1 (Closes: #38891)
- Added new icons for both apps and mimetypes (part of #26311)
- Added OpenDocument entries for KDE "create new" context menu
  (Closes: #16983)
- minor spec cleanup

* Fri Mar 14 2008 Ademar de Souza Reis Jr. <ademar@mandriva.com> 2.4.0.3-1mdv2008.1
+ Revision 187680
- New version: 2.4.0.3 (ooo-build 2.4.0.3, ooo 2.4.0-rc5)
- Minor spec cleanups

* Wed Feb 20 2008 Marcelo Ricardo Leitner <mrl@mandriva.com>
- Use system-db and system-boost for both archs, as gengal does not segfault anymore.
- Enabled usage of OpenGL.
- Enabled lockdown system.
- Use tons of java stuff from the system. (beanshell, xml-apis, xerces, xalan and xt)
- Use system sablot.
- Enabled cairo/canvas for x86_64.
- Imported the changelog in the meanwhile, while we don't submit the package through
  the buildsystem.
- Do not mark template*.desktop as ghost in the same package we ship it,
  otherelse it is not shipped.
- Updated oox and writerfilter to 20080229.
- Suggest java-common at openoffice.org-common, as it may be used by some macros.

* Tue Feb 19 2008 Marcelo Ricardo Leitner <mrl@mandriva.com> 2.3.99.4-1mdv2008.1
+ Revision 171536
- Merged our ooo-build with upstream ones: we submitted all our fixed to upstream.
- New version: 2.3.99.4
- New ooo-build: 2.3.99.4-20080218
- Fixed master name for main alterantives.
- Re-enabled mono bindings
- Added new mono files to %files
- Disabled debug pacakges.
- Updated conflicts tag from -core to -common prior to 2.3.1-1mdv
- Made ooo-dtd-officedocument1.0 not require ooo, and it doesn't require.
  Closes: #37559
- Made openoffice.org suggest ooo-dtd-officedocument1.0. Closes: #37559
- Added java requires to ooo-base package.
- Removed qstart patch, as we ship it in -gnome package now.
- Added proper obsoletes/conflict for upgrading old -qstart packages.
- Updated oox and writerfilter to 2008-01-29
- Updated cli_*.dll

* Thu Jan 10 2008 Marcelo Ricardo Leitner <mrl@mandriva.com> 2.3.1-2mdv2008.1
+ Revision 147621
Changes at the spec:
- Split the helps out of l10n packages.
- Added oodraw to alternatives catalog. Closes: #36618
- Forces compressing payload with lzma/maximum compression(9).
- Fixes to build with icedtea. Thanks to Anssi for helping with this move.
- Add a missing Suggests to tango style at gnome package. Closes: #36519
Changes from ooo-build tree:
- Do not merge the help listings with l10n ones.

* Fri Dec 14 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 2.3.1-1mdv2008.1
+ Revision 133876
Changes at the spec:
- New upstream: 2.3.1 Closes: #34236, #34724, #34274 and #35835
- Fixed alternatives for handling BrOffice support.
- Fixed wrong dependency for libjpeg.so. Closes: #35354
- Link against internal xmlsec, as linking with the system one is broken.
  Closes: #35067
- Fix wrong require for libjpeg.so at -draw subpackage. Closes: #35354
- Removed alternatives for handling BrOffice support: we simply don't need it.
- Added update_desktop_database/clean_desktop_database calls to all subpackages
  that holds .desktop files.
- Disabled mono bindings, as current cooker mono-devel seems broken.
- Build against system hsqldb.
- Enhanced /etc/profile.d scripts handling regarding multi-arch support.
  Closes: #35402
- Added dependencies to java stuff on ooo-base, as it depends on it.
- Fix alterantives handling for BrOffice support. They were conflicting if you
  had installed both 32 and 64b in the same box.
- From guillomovitch:
  - bash completion file don't have .sh suffix
Changes from ooo-build tree:
- Enhanced packaging. Closes: #35853
- Fixed wizards path. Closes: #35619
- Speed up Hungarian fixes processing.
- Fix msfontextract tools. Closes: #24314

* Fri Nov 23 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 2.3.0.5-2mdv2008.1
+ Revision 111340
Changes at the spec:
- Remove support for old menu system.
- Added BrOffice support.
- Moved alternatives scripts to -common package, as it must affect systems
  without the main meta-package.
- As now we are using alternatives for the .desktop files, update the desktop
  database only after dealing with alternatives.
- Added patch gtk: fixes wrong free commands in OOo. Closes: #34724
- Converted openintro_mandriva64.bmp to a 24 bit bitmap, as current splash
  can't handle anything different than that.
- Using ooo-build tarball from our soft/ repository now.
- Removed patches angola, force_downloads, ooqstart, xdg and wizards, as they
  are already merged in the tarball.
- Disable patch firefox-xpcom for now, as seems it can be handled via configure
  options.
- Place mdvsuffix in bash_completion and profile.d scripts, so we can have both
  archs installed.
- Check if PYTHONPATH is empty and properly set it, thus avoiding including the
  current dir on the path.
- Added back support to build without l10n packages (although seems not working
  100%)
- Our ooo-build 20071122
- Uncompressed FontOOo
- Merged -evolution and -gtk into -gnome
- Merged -filter-mobiledev into -filter-binfilter
- Splitted -pyuno
- Splitted -testtool
- Moved file listings to ooo-build scripts.
- Fix alternatives handling for BrOffice support
- Fix wrong dependency for libjpeg.so. Closes: #35354
Changes from ooo-build tree:
- Merged a lot of our patches from the package.
- Also apply patches from sets CairoFonts, CalcSolver, Split and NotDebian.
- Merged some patches from ooo-build upstream, including
  gnome-vfs-read-only-smb.diff for our #35183.

* Mon Nov 05 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 2.3.0.5-1mdv2008.1
+ Revision 106021
- New upstream: 2.3.0.5 (oog-m7)
- Disabled linking against system xmlsec, as it (the linking) is currently
  broken.
- Removed patch xmlsec, as it's not used.
- Added conflicts to the previous release, as thousands of files were moved.
- Remove BuildRequires to inkscape: seems to not be needed.
- Removed german dicts lines, as of commit #104173 we don't need it anymore.
- -l10n packages should require openoffice.org-common now, and not the whole
  suite.
- Removed BuildRequires for thousands of locale- packages, as they are not
  needed.
- Removed support to build the "tiny" langset, as it won't be used.
- Removed all thes/hyph/dict from the package: they should be available by
  general packages.
- Updated DicOOo and decompressed it.
- Make out -clipart package require openclipart one.
- Try to avoid urpmi question by making all application packages also require
  explicitly -core.
- Do not force requires for freetype, odbc, sndfile and portaudio, as rpm is
  getting them automatically.
- Dropped support for < 2007.1
- Fully disable QA tools for now. We will work on that after release a first
  build for cooker.
- Main package should also require -impress module.
- -impress must require -draw
- Added Suggests for the theme styles on gtk/kde packages.
- Puts proper dependencies between the subpackages
- Added libsvg-devel buildrequires.
- Removed patchs neon and neon2: already fixed in upstream.
- Removed patch CVE-2007-2834: already fixed in upstream.
- Updated patch ooqstart
- Enhanced the detection of the number of processors to use by using
  RPM_BUILD_NCPUS variable.
- Move the entire gallery collection to openclipart subpackage.
- Move FontOOo and DicOOo from share/dicts/ooo/ to share/dicts/ at least.
- Do not include the whole myspell stuff in OOo again, as we are already
  requiring myspell- packages.
- Fixed icecream paths.
- Fixed missing trailing \ on hunspell configure option.
- Do not run configure twice: do not run configure on autogen, as it was being
  done without any option.
- Enabled ccache.
- Updated FontOOo

* Thu Oct 18 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 2.2.1-4mdv2008.1
+ Revision: 99960
- Remove localwidget patch, it off already.
- Rediffed ooqstart patch.
- Fix syntax error in openoffice.org.csh. Closes: #34423

* Fri Sep 21 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 2.2.1-3mdv2008.0
+ Revision: 95418
- Fix patch22 order, as used for the build.
- Added patch force_downloads: force downloading of documents from the web
  and/or other IOs (KIOs). Closes: #26983
- Adds back '64' tag to .desktop filenames when it's build on x86_64. Closes: #33825
- Added support for /etc/profile.d/openoffice.org.{c,}sh. Closes: #33475
- Updated thes_es_ES. Closes: #33536.
- Updated thes_bg_BG_v2.tar.bz2 and thes_en_US_v2.tar.bz2 in thes-2.tar.
  Closes: #33537, #33538
- Added patch openoffice.org-2.2.1-CVE-2007-2834.patch. Closes: #33824
- Force enable gstreamer backend. Closes: #27580
- Fix Icon tag on desktop files.

  + Anssi Hannula <anssi@mandriva.org>
    - fix removal of old alternative when mdvsuffix changes

* Wed Sep 05 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 2.2.1-2mdv2008.0
+ Revision: 80050
- Added neon2 patch. Closes: #25204
- Implemented .desktop categories changes as requested by #32902
- Added patch desktop_files: do not versionate stable .desktop files.
- Use ooo-build ver 2.2.1.10110: move on step further on svn version for using
  stable libwp*.
- Added requires to fonts-ttf-liberation.
- Forced linking against libneon >= 0.26: linking against 0.24 is even more
  unstable (UI freezes).
- Removed patch libwpg: already applied on ooo-build-2.2.1-10110.
- New design for Mandriva 2008.0.
- Added neon patch: closes #32121
  Fixes handling URL's with wierd chars due to new libneon behaviour change.
- Fix path for icu tools.
- Import openoffice.org

  + Anssi Hannula <anssi@mandriva.org>
    - require openoffice.org-voikko instead of myspell-hyph-fi in
      openoffice.org-l10n-fi for better Finnish support
    - fix use_systemboost build option

  + Thierry Vignaud <tvignaud@mandriva.com>
    - convert prereq
    - kill file require on update-alternatives

  + Ademar de Souza Reis Jr <ademar@mandriva.com.br>
    - remove PreReq for chkfontpath (apparently a legacy requirement,
      since it's not used anywhere)
    - change fonts-ttf-vera requirements to fonts-ttf-dejavu
      (Dejavu is the preferred default font)

* Fri Jun 29 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 2.2.1-1mdv2008.0
- Updated to 2.2.1
- Renamed to openoffice.org
- Not using lzma for now
- Enabled SMP usage.
- Dropped support for <= 2006.0
- Added requires to paper-utils, due to paperconf.
- libwpd, libwpg, libwps, libicu and libmdbtools are now linked externally.
- Added patch xdg: fix complaiment about MultipleArgs on template2.2.desktop
- Added patch libwpg: fix missing config variable SYSTEM_LIBWPG during build
  time.
- Added patch kde: moves fps_kde.uno.so to -kde package, otherwise OOo gets
  confused about kde/gnome dialogs.
- Added patch ooqstart: fixes ooqstart.desktop exec command line.
- Many fixes for java/x86_64 from Anssi Hannula, including patch
  ooo-build-fix-build-java-target-patch

* Sat Mar 24 2007 Giuseppe Ghibò <ghibo@mandriva.com> 2.2.0-4.rc4.1mdv2007.1
- ooo-build 2.2.0_cvs20070323.
- use oof680-m14 (RC4).

* Wed Mar 21 2007 Giuseppe Ghibò <ghibo@mandriva.com> 2.2.0-3.m13.2mdv2007.1
- ooo-build 2.2.0_cvs20070321.

* Mon Mar 19 2007 Giuseppe Ghibò <ghibo@mandriva.com> 2.2.0-3.m13.1mdv2007.1
- Rebuilt against latest clipart-openclipart (fixes bug #29568).
- ooo-build 2.2.0_cvs20070319.
- use system libwpd.

* Mon Mar 12 2007 Giuseppe Ghibò <ghibo@mandriva.com> 2.2.0-2.rc3.2mdv2007.1
- ooo-build 2.2.0_cvs20070312.
- Removed X-MandrivaLinux-Office-Spreadsheet from base*.desktop (bug #29381).
- Don't use splash screens with transparencies (report by Hélène).

* Fri Mar 09 2007 Giuseppe Ghibò <ghibo@mandriva.com> 2.2.0-2.rc3.1mdv2007.1
- ooo-build 2.2.0_cvs20070309.
- use oof680-m11 (RC3).

* Tue Mar 06 2007 Giuseppe Ghibò <ghibo@mandriva.com> 2.2.0-2.m10.2mdv2007.1
- ooo-build 2.2.0_cvs20070306.
- Fixed splash screen.

* Sat Mar 03 2007 Giuseppe Ghibò <ghibo@mandriva.com> 2.2.0-2.m10.1mdv2007.1
- ooo-build 2.2.0_cvs20070304.
- merged Felipe Arruda's fixes for brazilian .desktop files translations.
- merged Funda Wang patches for VCL.xcu for chinese menus (bug #29026).
- force building with system sane.
- Updated Splash Screens (thanks to Hélène Durosini).

* Mon Feb 26 2007 Giuseppe Ghibò <ghibo@mandriva.com> 2.2.0-1mdv2007.1
- ooo-build 2.2.0_cvs2007025.
- renamed to *go-ooo to distinguish from main openoffice.org.

* Sat Feb 24 2007 Giuseppe Ghibò <ghibo@mandriva.com> 2.1.0-5mdv2007.1
- removed mimelnk subpackage
- ooo-build 2.1.6_cvs20070224 (fix problem when saving in PPT).
- added update-alternatives for ooffice links into %{_bindir}.
- moved docdir (to allow coexisting between i586 and x86_64 packages).

* Fri Feb 16 2007 Giuseppe Ghibò <ghibo@mandriva.com> 2.1.0-4mdv2007.1
- ooo-build 2.1.6_cvs20070216.
- Removed Patch8 (merged upstream).
- Removed Patch9 (merged upstream).
- Rebuilt Patch10 (partially merged upstream).

* Mon Feb 12 2007 Giuseppe Ghibò <ghibo@mandriva.com> 2.1.0-3mdv2007.1
- Updated Source15 (updates for de_DE, it_IT, pl_PL,
  new thesaurus for pt_PT, nb_NO, ru_RU).

* Sat Feb 10 2007 Giuseppe Ghibò <ghibo@mandriva.com> 2.1.0-2mdv2007.1
- ooo-build 2.1.5_cvs20070210.
- Added Patch7 for serializer.jar for problems with gcj.

* Thu Feb 08 2007 Giuseppe Ghibò <ghibo@mandriva.com> 2.1.0-1mdv2007.1
- ooo-build 2.1.3_cvs20070208.
- use 2.1 for mdvsuffix.
- Removed Patch5 (no longer needed).
- OpenOffice 2.1.0.
- Added Patch7 (temporary disable patch for chinese, as it
  doesn't apply anymore and need to be rediffed).
- Added BuildConflicts for libportaudio2 (Florian Hubold).

* Tue Jan 30 2007 Giuseppe Ghibò <ghibo@mandriva.com> 2.0.4-4mdv2007.1
- ooo-build 2.0.4.14_cvs20070130.

* Mon Jan 29 2007 Giuseppe Ghibò <ghibo@mandriva.com> 2.0.4-3mdv2007.0
- BuildRequires for libportaudio0-devel instead libportaudio-devel
  (libportaudio2-devel is broken?).

* Thu Jan 04 2007 Vincent Danen <vdanen@mandriva.com> 2.0.4-2.1mdv2007.0
- build for updates, includes the fix for CVE-2006-5870

* Wed Dec 20 2006 Giuseppe Ghibò <ghibo@mandriva.com> 2.0.4-2mdv2007.0
- added mime-types 'application/vnd.ms-works;application/x-msworks-wp;
  zz-application/zz-winassoc-wps' to writer*desktop (bug #27616).
- cosmetics to the SPEC file.

* Wed Dec 20 2006 Giuseppe Ghibò <ghibo@mandriva.com> 2.0.4-1mdv2007.0
- OpenOffice to 2.0.4.
- ooo-build 20061220 cvs.

* Tue Sep 19 2006 Giuseppe Ghibò <ghibo@mandriva.com> 2.0.3-6mdv2007.0
- ooo-build 20060919 cvs: fix cjk fonts (bug #22018, #25701).

* Fri Sep 15 2006 Giuseppe Ghibò <ghibo@mandriva.com> 2.0.3-5mdv2007.0
- Rebuilt against mozilla-firefox 1.5.0.7.

* Thu Sep 14 2006 Giuseppe Ghibò <ghibo@mandriva.com> 2.0.3-4mdv2007.0
- Changed .desktop entries categories according to bug #25641.
- Fixed splash screen (ooo-build 20060914 cvs).

* Mon Sep 11 2006 Giuseppe Ghibò <ghibo@mandriva.com> 2.0.3-3mdv2007.0
- use %mklibname for unixODBC (from Gwenole).
- added mk in language list.
- fixed csh path in setsdk_unix.csh script.
- Updated FontOOo.sxw wizard to release 1.6.
- Updated DicOOo.sxwd wizard to release 1.6.1.
- Removed Patch5,6 (unused).
- Removed Patch7, merged ooo-build upstream (ooo-build 2.0.3-20060911).
- Added mimetypes for old OpenOffice formats (missed in kdelibs-common),
  Source53 and mimelnk subpackage.
- Removed kaffe from "Conflicts" (seems not conflicting in runtime)
  (from D.Walluck).

* Mon Aug 21 2006 Giuseppe Ghibò <ghibo@mandriva.com> 2.0.3-2mdv2007.0
- ooo-build 20060821 cvs.
- Merged Anssi Hannula's fixes (and added -devel and -devel-doc subpackages).
- Added Patch7 for dbus-0.91.

* Thu Jul 06 2006 Giuseppe Ghibò <ghibo@mandriva.com> 2.0.3-1mdv2007.0
- Release 2.0.3.
- ooo-build 20060706 cvs.

* Mon Jun 26 2006 Giuseppe Ghibò <ghibo@mandriva.com> 2.0.3-0.m6.2mdv2007.0
- ooo-build 20060624 cvs.

* Wed Jun 21 2006 Giuseppe Ghibò <ghibo@mandriva.com> 2.0.3-0.m6.1mdv2006.0
- Release oooc680-m6.
- Added Breton language.

* Mon Jun 19 2006 Giuseppe Ghibò <ghibo@mandriva.com> 2.0.3-0.m5.1mdk
- 2.0.3-m5.
- ooo-build 20060619 cvs.
- Removed hunspell subpackage (was empty).
- Renamed package to OpenOffice.org (warly).

* Sat May 06 2006 Giuseppe Ghibò <ghibo@mandriva.com> 2.0.2-6mdk
- ooo-build 2.0.2.9.
- Added Patch6 to allow building with neon library version 0.26.

* Sat Apr 15 2006 Giuseppe Ghibò <ghibo@mandriva.com> 2.0.2-5mdk
- ooo-build 2.0.2.7 (fixes also bug #21869).
- fix typo in Requires when --with systemdb is used (thanks to Richard Houser).
- Disable default cairo rendering for 2006.0 (cause jittering/slow down under
  Impress presentations).

* Sat Mar 18 2006 Giuseppe Ghibò <ghibo@mandriva.com> 2.0.2-4mdk
- ooo-build 2.0.2.1.

* Sat Mar 11 2006 Giuseppe Ghibò <ghibo@mandriva.com> 2.0.2-3mdk
- Removed Patch3 (merged into ooo-build upstream).
- ooo-build 2.0.2.cvs20060311.

* Sat Mar 11 2006 Giuseppe Ghibr <ghibo@mandriva.com> 2.0.2-2mdk
- Modified Patch3 (set OOO_EXTRA_ARG to empty string which is
  not the same as unset).

* Thu Mar 09 2006 Giuseppe Ghibò <ghibo@mandriva.com> 2.0.2-1mdk
- Release 2.0.2 final.
- ooo-build 2.0.2.

* Mon Mar 06 2006 Giuseppe Ghibò <ghibo@mandriva.com> 2.0.2-0.rc4.3mdk
- moved ooqstart to a standalone subpackage (Patch4).

* Sat Mar 04 2006 Giuseppe Ghibò <ghibo@mandriva.com> 2.0.2-0.rc4.2mdk
- ooo-build 2.0.157.cvs20060304 (fixes bug #21428, IZ#62068).
- Added Patch3 (fixes OOO_EXTRA_ARG env var when it's not set and
  called from ooffice2.0 wrapper).

* Fri Mar 03 2006 Giuseppe Ghibò <ghibo@mandriva.com> 2.0.2-0.rc4.1mdk
- ooo-build 2.0.157.cvs20060302.
- Disable direct quickstart call for now.

* Thu Mar 02 2006 Giuseppe Ghibò <ghibo@mandriva.com> 2.0.2-0.m5.2mdk
- ooo-build 2.0.157.cvs20060301.
- Added Conflicts: kaffe.

* Wed Mar 01 2006 Giuseppe Ghibò <ghibo@mandriva.com> 2.0.2-0.m5.1mdk
- Release oob680-m5.

* Tue Feb 28 2006 Giuseppe Ghibò <ghibo@mandriva.com> 2.0.2-0.m4.1mdk
- Release oob680-m4.

* Mon Feb 06 2006 Giuseppe Ghibò <ghibo@mandriva.com> 2.0.1-1mdk
- Release 2.0.1
- remove --with-system-db-version in configure because doesn't exists anymore.
- added --with-systemdb conditional flag.
- added --with-tiny_langset conditional flag
- ooo-build-2.0.1.3.
- Added --with gcj switch for building with gcj instead of Sun JDK.
- Added Patch1 for supporting .lzma tarballs.
- Added Patch2 to fix bug #19111 (from Eskild Hustvedt).
- Moved Patch5 into ooo-build tree.

* Sat Jan 14 2006 Giuseppe Ghibò <ghibo@mandriva.com> 2.0-7mdk
- fixed bug IZ#47323.
- removed de-DE.tar.bz2 from Source15 not Source14.
- ooo-build-cvs20051026 (fix bug IZ#52047).
- renamed menu name to openoffice.org-2.0 (Gwenole).
- Added bulgarian l10n subpackage.
- ooo-build-cvs20060114.
- Lowered optimization to -O1, as -O2 causes segfaults (with gcc 4.0.2-1mdk) in the
  libunosal.so.3 libs from javaldx executable during package building.

* Thu Oct 20 2005 Giuseppe Ghibò <ghibo@mandriva.com> 2.0-1mdk
- 2.0 final.

* Fri Oct 14 2005 Giuseppe Ghibò <ghibo@mandriva.com> 2.0-0.rc3.1mdk
- 2.0-rc3.

* Mon Sep 26 2005 Giuseppe Ghibò <ghibo@mandriva.com> 2.0-0.m129.3mdk
- ooobuild cvs 20050924.
- moved libsndfile.so, libportaudio.so, libdb-4.2.so, libmyspell.so,
  libstlport_gcc.so to provides exceptions (Pascal Terjan).


* Sat Sep 24 2005 Giuseppe Ghibò <ghibo@mandriva.com> 2.0-0.m129.2mdk
- ooobuild cvs 20050921.
- Removed Patch4 (fixed in upstream).
- Added libdb-4.2.so, libmyspell.so, libstlport_gcc.so to require exceptions
  (bug #17262).

* Sat Sep 17 2005 Giuseppe Ghibò <ghibo@mandriva.com> 2.0-0.m129.1mdk
- 1.9.129.
- ooobuild cvs 20050918.
- Removed Patch0->3 (merged upstream).
- Added Patch4 (disable patch for i54709), because it doesn't apply correctly.
- White progressbar.
- Added Gwenole Patches for having OOo2 working under X86_64 in 32bit mode
  (Patch5).

* Wed Sep 14 2005 Giuseppe Ghibò <ghibo@mandriva.com> 2.0-0.m128.5mdk
- Fix bug #18581 (libportaudio).
- Move libkab1.so to -kde package (pterjan).

* Wed Sep 14 2005 Giuseppe Ghibò <ghibo@mandriva.com> 2.0-0.m128.4mdk
- ooobuild cvs 20050914.

* Wed Sep 14 2005 Giuseppe Ghibò <ghibo@mandriva.com> 2.0-0.m128.3mdk
- added Patch0 for spellchecker
- Updated Source16.

* Mon Sep 12 2005 Giuseppe Ghibò <ghibo@mandriva.com> 2.0-0.m128.2mdk
- binfilters, mono.

* Thu Sep 08 2005 Giuseppe Ghibò <ghibo@mandriva.com> 2.0-0.m128.1mdk
- 1.9.128.

* Mon Jul 25 2005 Giuseppe Ghibò <ghibo@mandriva.com> 2.0-0.m121.1mdk
- 1.9.121.

* Mon Jul 11 2005 Giuseppe Ghibò <ghibo@mandriva.com> 2.0-0.m116.1mdk
- 1.9.116.

* Mon Jul 11 2005 Giuseppe Ghibò <ghibo@mandriva.com> 2.0-0.m114.1mdk
- 1.9.114.

* Fri Jun 24 2005 Giuseppe Ghibò <ghibo@mandriva.com> 2.0-0.m110.1mdk
- Updated ooo-build to cvs 20050624.

* Thu Jun 23 2005 Giuseppe Ghibò <ghibo@mandriva.com> 2.0-0.m108.2mdk
- Updated ooo-build to cvs 20050623 (fixes problem with
  icon sets).

* Wed Jun 22 2005 Giuseppe Ghibò <ghibo@mandriva.com> 2.0-0.m108.1mdk
- 1.9.110.

* Wed Mar 23 2005 Giuseppe Ghibò <ghibo@mandrakesoft.com> 1.1.4-1mdk
- 1.1.4.

* Fri Jan 21 2005 Giuseppe Ghibò <ghibo@mandrakesoft.com> 1.1.3-1mdk
- Initial release.
