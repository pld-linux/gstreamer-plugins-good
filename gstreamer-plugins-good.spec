#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc
%bcond_without	aalib		# aa videosink plugin
%bcond_without	caca		# caca videosink plugin
%bcond_without	cairo		# cairo plugin
%bcond_without	gtk		# GTK+ (3.x) elements (video sink plugin)
%bcond_without	jack		# JACK audio plugin
%bcond_with	jack1		# JACK 1 (0.12x) instead of JACK 2 (1.9.x)
%bcond_without	lame		# LAME MP2/MP3 encoding plugin
%bcond_without	mpg123		# MPG123-based MP3 plugin
%bcond_without	qt		# Qt (5.x) elements (video sink plugin)
%bcond_without	soup		# libsoup (2.4 API) http source plugin
%bcond_without	speex		# speex plugin
%bcond_without	wavpack		# wavpack plugin

%define		gstname		gst-plugins-good
%define		gstmver		1.0
%define		gst_ver		1.16.3
%define		gstpb_ver	1.16.3

Summary:	Good GStreamer Streaming-media framework plugins
Summary(pl.UTF-8):	Dobre wtyczki do środowiska obróbki strumieni GStreamer
Name:		gstreamer-plugins-good
Version:	1.16.3
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	https://gstreamer.freedesktop.org/src/gst-plugins-good/%{gstname}-%{version}.tar.xz
# Source0-md5:	c79b6c2f8eaadb2bb66615b694db399e
URL:		https://gstreamer.freedesktop.org/
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.14
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	glib2-devel >= 1:2.40
%if %(locale -a | grep -q '^C\.utf8$'; echo $?)
BuildRequires:	glibc-localedb-all
%endif
BuildRequires:	gstreamer-devel >= %{gst_ver}
BuildRequires:	gstreamer-gl-devel >= %{gstpb_ver}
BuildRequires:	gstreamer-plugins-base-devel >= %{gstpb_ver}
BuildRequires:	gtk+3-devel >= 3.0.0
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.12}
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	orc-devel >= 0.4.17
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	python >= 2.1
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.198
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
##
## plugins
##
%{?with_qt:BuildRequires:	Qt5Core-devel >= 5.4.0}
%{?with_qt:BuildRequires:	Qt5Gui-devel >= 5.4.0}
%{?with_qt:BuildRequires:	Qt5Quick-devel >= 5.4.0}
%{?with_qt:BuildRequires:	Qt5Qml-devel >= 5.4.0}
%{?with_qt:BuildRequires:	Qt5X11Extras-devel >= 5.4.0}
%{?with_qt:BuildRequires:	Qt5WaylandClient-devel >= 5.4.0}
%{?with_aalib:BuildRequires:	aalib-devel >= 0.11.0}
BuildRequires:	bzip2-devel
%{?with_cairo:BuildRequires:	cairo-devel >= 1.10.0}
%{?with_cairo:BuildRequires:	cairo-gobject-devel >= 1.10.0}
BuildRequires:	dbus-devel >= 0.91
BuildRequires:	flac-devel >= 1.1.4
BuildRequires:	gdk-pixbuf2-devel >= 2.8.0
%{?with_gtk:BuildRequires:	gtk+3-devel >= 3.15.0}
%if %{with jack}
%{?with_jack1:BuildRequires:	jack-audio-connection-kit-devel >= 0.120.1}
%{!?with_jack1:BuildRequires:	jack-audio-connection-kit-devel >= 1.9.7}
%endif
%{?with_lame:BuildRequires:	lame-libs-devel}
BuildRequires:	libavc1394-devel
%{?with_caca:BuildRequires:	libcaca-devel}
BuildRequires:	libdv-devel >= 0.104
BuildRequires:	libiec61883-devel >= 1.0.0
BuildRequires:	libjpeg-devel
%{?with_mpg123:BuildRequires:	libmpg123-devel >= 1.14}
BuildRequires:	libpng-devel >= 2:1.5.1
BuildRequires:	libraw1394-devel >= 2.0.0
BuildRequires:	libshout-devel >= 2.0
%{?with_soup:BuildRequires:	libsoup-devel >= 2.48}
BuildRequires:	libstdc++-devel
BuildRequires:	libv4l-devel
BuildRequires:	libvpx-devel >= 1.8.0
BuildRequires:	pulseaudio-devel >= 2.0
%{?with_qt:BuildRequires:	qt5-build >= 5.4.0}
%{?with_speex:BuildRequires:	speex-devel >= 1:1.1.6}
BuildRequires:	taglib-devel >= 1.5
%{?with_lame:BuildRequires:	twolame-devel >= 0.3.10}
BuildRequires:	udev-glib-devel >= 1:147
%{?with_wavpack:BuildRequires:	wavpack-devel >= 4.60.0}
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	zlib-devel
Requires:	glib2 >= 1:2.40
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	orc >= 0.4.17
Obsoletes:	gstreamer-avi < 0.10
Obsoletes:	gstreamer-flx < 0.10
Obsoletes:	gstreamer-matroska < 0.10
Obsoletes:	gstreamer-mixer < 0.10
Obsoletes:	gstreamer-navigation < 0.10
Obsoletes:	gstreamer-oss4 < 0.10
Obsoletes:	gstreamer-rtp < 0.10
Obsoletes:	gstreamer-udp < 0.10
Conflicts:	gstreamer-plugins-bad < 0.10.19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		gstlibdir 	%{_libdir}/gstreamer-%{gstmver}

%description
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related. Its plugin-based architecture means
that new data types or processing capabilities can be added simply by
installing new plugins.

%description -l pl.UTF-8
GStreamer to środowisko obróbki danych strumieniowych, bazujące na
grafie filtrów operujących na danych medialnych. Aplikacje używające
tej biblioteki mogą robić wszystko od przetwarzania dźwięku w czasie
rzeczywistym, do odtwarzania filmów i czegokolwiek innego związego z
mediami. Architektura bazująca na wtyczkach pozwala na łatwe dodawanie
nowych typów danych lub możliwości obróbki.

%package apidocs
Summary:	Good GStreamer streaming-media framework plugins API documentation
Summary(pl.UTF-8):	Dokumentacja API dobrych wtyczek środowiska obróbki strumieni GStreamer
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
Good GStreamer streaming-media framework plugins API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API dobrych wtyczek środowiska obróbki strumieni
GStreamer.

## ## Plugins ##

%package -n gstreamer-videosink-aa
Summary:	GStreamer plugin for Ascii-art output
Summary(pl.UTF-8):	Wtyczka wyjścia obrazu Ascii-art do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Provides:	gstreamer-videosink = %{version}
Obsoletes:	gstreamer-aalib < 0.10

%description -n gstreamer-videosink-aa
Plugin for viewing movies in Ascii-art using aalib library.

%description -n gstreamer-videosink-aa -l pl.UTF-8
Wtyczka wyjścia obrazu Ascii-art używająca biblioteki aalib.

%package -n gstreamer-audio-effects-good
Summary:	Good GStreamer audio effects plugins
Summary(pl.UTF-8):	Dobre wtyczki efektów dźwiękowych do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Obsoletes:	gstreamer-audio-effects < 0.10

%description -n gstreamer-audio-effects-good
Good GStreamer audio effects plugins.

%description -n gstreamer-audio-effects-good -l pl.UTF-8
Dobre wtyczki efektów dźwiękowych do GStreamera.

%package -n gstreamer-audio-formats
Summary:	GStreamer audio format plugins
Summary(pl.UTF-8):	Wtyczki formatów dźwięku
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
# for locales in wavparse module
Requires:	%{name} = %{version}-%{release}

%description -n gstreamer-audio-formats
Plugin for playback of WAV, au and mod audio files as well as MP3
type.

%description -n gstreamer-audio-formats -l pl.UTF-8
Wtyczka do odwarzania dźwięku w formacie au, WAV, mod oraz MP3.

%package -n gstreamer-cairo
Summary:	GStreamer cairo plugin
Summary(pl.UTF-8):	Wtyczka cairo do GStreamera
Group:		Libraries
Requires:	cairo >= 1.10.0
Requires:	cairo-gobject >= 1.10.0
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}

%description -n gstreamer-cairo
GStreamer cairo plugin.

%description -n gstreamer-cairo -l pl.UTF-8
Wtyczka cairo do GStreamera.

%package -n gstreamer-dv
Summary:	GStreamer dv plugin
Summary(pl.UTF-8):	Wtyczka dv do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	libdv >= 0.104

%description -n gstreamer-dv
Plugin for digital video support.

%description -n gstreamer-dv -l pl.UTF-8
Wtyczka do GStreamera obsługująca cyfrowy obraz.

%package -n gstreamer-flac
Summary:	GStreamer plugin for FLAC lossless audio format
Summary(pl.UTF-8):	Wtyczka do GStreamera obsługująca bezstratny format dźwięku FLAC
Group:		Libraries
Requires:	flac >= 1.1.4
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}

%description -n gstreamer-flac
Plugin for the free FLAC lossless audio format.

%description -n gstreamer-flac -l pl.UTF-8
Wtyczka obsługująca wolnodostępny, bezstratny format dźwięku FLAC.

%package -n gstreamer-gdkpixbuf
Summary:	GStreamer images input plugin
Summary(pl.UTF-8):	Wtyczka do GStreamera wczytująca obrazki
Group:		Libraries
Requires:	gdk-pixbuf2 >= 2.8.0
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}

%description -n gstreamer-gdkpixbuf
This GStreamer plugin load images via gdkpixbuf library.

%description -n gstreamer-gdkpixbuf -l pl.UTF-8
Ta wtyczka GStreamera wczytuje obrazki za pośrednictwem biblioteki
gdkpixbuf.

%package -n gstreamer-videosink-gtk
Summary:	GStreamer GTK+ (3.x) output plugin
Summary(pl.UTF-8):	Wtyczka wyjścia obrazu GTK+ (3.x) dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-gl-libs >= %{gstpb_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	gtk+3 >= 3.15.0
Provides:	gstreamer-videosink = %{version}

%description -n gstreamer-videosink-gtk
GStreamer GTK+ (3.x) output plugin.

%description -n gstreamer-videosink-gtk -l pl.UTF-8
Wtyczka wyjścia obrazu GTK+ (3.x) dla GStreamera.

%package -n gstreamer-jack
Summary:	GStreamer plugin for the JACK Sound Server
Summary(pl.UTF-8):	Wtyczka serwera dźwięku JACK dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
%{?with_jack1:Requires:	jack-audio-connection-kit-libs >= 0.120.1}
%{!?with_jack1:Requires:	jack-audio-connection-kit-libs >= 1.9.7}
# for locales
Requires:	%{name} = %{version}-%{release}
Provides:	gstreamer-audiosink = %{version}

%description -n gstreamer-jack
Plugin for the JACK professional sound server.

%description -n gstreamer-jack -l pl.UTF-8
Wtyczka dla profesjonalnego serwera dźwięku JACK.

%package -n gstreamer-videosink-libcaca
Summary:	GStreamer plugin for libcaca Ascii-art output
Summary(pl.UTF-8):	Wtyczka libcaca do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Provides:	gstreamer-videosink = %{version}

%description -n gstreamer-videosink-libcaca
GStreamer plug-in for libcaca Ascii-art output.

%description -n gstreamer-videosink-libcaca -l pl.UTF-8
Wtyczka libcaca do GStreamera.

%package -n gstreamer-lame
Summary:	GStreamer plugin encoding MP3 songs
Summary(pl.UTF-8):	Wtyczka do GStreamera kodująca pliki MP3
Group:		Libraries
# for NLS
Requires:	%{name} = %{version}-%{release}
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	twolame-libs >= 0.3.10

%description -n gstreamer-lame
Plugin for encoding MP3 with lame.

%description -n gstreamer-lame -l pl.UTF-8
Wtyczka do GStreamera kodująca pliki MP3 przy użyciu lame.

%package -n gstreamer-mpg123
Summary:	GStreamer mpg123 plugin
Summary(pl.UTF-8):	Wtyczka mpg123 do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	libmpg123 >= 1.14
# plugin obsoleted in 1.12.0, functionality in mpg123 plugin (or libav)
Obsoletes:	gstreamer-mad < 1.12.0

%description -n gstreamer-mpg123
GStreamer mpg123 plugin for MP3 playback.

%description -n gstreamer-mpg123 -l pl.UTF-8
Wtyczka mpg123 do GStreamera, odtwarzająca MP3.

%package -n gstreamer-libpng
Summary:	GStreamer plugin to encode png images
Summary(pl.UTF-8):	Wtyczka GStreamera kodująca pliki png
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
# for locales
Requires:	%{name} = %{version}-%{release}
Requires:	libpng >= 2:1.5.1

%description -n gstreamer-libpng
Plugin for encoding png images.

%description -n gstreamer-libpng -l pl.UTF-8
Wtyczka kodująca pliki png.

%package -n gstreamer-audiosink-oss
Summary:	GStreamer plugins for input and output using OSS
Summary(pl.UTF-8):	Wtyczki wejścia i wyjścia dźwięku OSS do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
# for locales
Requires:	%{name} = %{version}-%{release}
Provides:	gstreamer-audiosink = %{version}
Obsoletes:	gstreamer-oss < 0.10

%description -n gstreamer-audiosink-oss
Plugins for output and input to the OpenSoundSystem audio drivers
found in the Linux kernels or commercially available from OpenSound.

%description -n gstreamer-audiosink-oss -l pl.UTF-8
Wtyczki wyjścia i wejścia dźwięku używające sterowników
OpenSoundSystem obecnych w jądrach Linuksa lub dostępnych komercyjnie
od OpenSound.

%package -n gstreamer-pulseaudio
Summary:	GStreamer plugin for PulseAudio sound server
Summary(pl.UTF-8):	Wtyczka GStreamera dla serwera dźwięku PulseAudio
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	pulseaudio >= 2.0
# for locales
Requires:	%{name} = %{version}-%{release}
Provides:	gstreamer-audiosink = %{version}
Obsoletes:	gstreamer-audiosink-polypaudio < 0.10
Obsoletes:	gstreamer-polypaudio < 0.10

%description -n gstreamer-pulseaudio
GStreamer plugin for PulseAudio sound server.

%description -n gstreamer-pulseaudio -l pl.UTF-8
Wtyczka GStreamera dla serwera dźwięku PulseAudio.

%package -n gstreamer-videosink-qt
Summary:	GStreamer Qt (5.x) output plugin
Summary(pl.UTF-8):	Wtyczka wyjścia obrazu Qt (5.x) dla GStreamera
Group:		Libraries
Requires:	Qt5Core >= 5.4.0
Requires:	Qt5Gui >= 5.4.0
Requires:	Qt5Quick >= 5.4.0
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-gl-libs >= %{gstpb_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Provides:	gstreamer-videosink = %{version}

%description -n gstreamer-videosink-qt
GStreamer Qt (5.x) output plugin.

%description -n gstreamer-videosink-qt -l pl.UTF-8
Wtyczka wyjścia obrazu Qt (5.x) dla GStreamera.

%package -n gstreamer-raw1394
Summary:	GStreamer raw1394 Firewire plugin
Summary(pl.UTF-8):	Wtyczka FireWire dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}

%description -n gstreamer-raw1394
Plugin for digital video support using raw1394.

%description -n gstreamer-raw1394 -l pl.UTF-8
Wtyczka dająca dostęp do cyfrowego obrazu przy użyciu raw1394.

%package -n gstreamer-shout2
Summary:	GStreamer plugin for communicating with Shoutcast servers
Summary(pl.UTF-8):	Wtyczka do GStreamera umożliwiająca komunikację z serwerami Shoutcast
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
# for locales
Requires:	%{name} = %{version}-%{release}

%description -n gstreamer-shout2
GStreamer plugin for communicating with Shoutcast servers.

%description -n gstreamer-shout2 -l pl.UTF-8
Wtyczka do GStreamera umożliwiająca komunikację z serwerami Shoutcast.

%package -n gstreamer-soup
Summary:	GStreamer Soup plugin
Summary(pl.UTF-8):	Wtyczka biblioteki Soup dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	libsoup >= 2.48
# for locales
Requires:	%{name} = %{version}-%{release}

%description -n gstreamer-soup
GStreamer Plugin for downloading files with Soup library.

%description -n gstreamer-soup -l pl.UTF-8
Wtyczka GStreamera umożliwiająca ściąganie plików za pomocą biblioteki
Soup.

%package -n gstreamer-speex
Summary:	GStreamer speex codec decoder/encoder plugin
Summary(pl.UTF-8):	Wtyczka do GStreamera obsługująca kodek Speex
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	speex >= 1:1.1.6

%description -n gstreamer-speex
GStreamer speex codec decoder/encoder plugin.

%description -n gstreamer-speex -l pl.UTF-8
Wtyczka do GStreamera obsługująca kodek Speex.

%package -n gstreamer-taglib
Summary:	GStreamer tag writing plugin based on taglib
Summary(pl.UTF-8):	Wtyczka GStreamera zapisująca znaczniki oparta na bibliotece taglib
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	taglib >= 1.5

%description -n gstreamer-taglib
GStreamer tag writing plugin based on taglib.

%description -n gstreamer-taglib -l pl.UTF-8
Wtyczka GStreamera zapisująca znaczniki oparta na bibliotece taglib.

%package -n gstreamer-v4l2
Summary:	GStreamer Video4Linux2 input plugin
Summary(pl.UTF-8):	Wtyczka wejścia Video4Linux2 dla GStreamera
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	udev-glib >= 1:147

%description -n gstreamer-v4l2
GStreamer plugin for accessing Video4Linux2 devices.

%description -n gstreamer-v4l2 -l pl.UTF-8
Wtyczka GStreamera pozwalająca na dostęp do urządzeń Video4Linux2.

%package -n gstreamer-video-effects
Summary:	GStreamer video effects plugins
Summary(pl.UTF-8):	Wtyczki efektów wideo do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
# for locales in jpeg module
Requires:	%{name} = %{version}-%{release}

%description -n gstreamer-video-effects
GStreamer video effects plugins.

%description -n gstreamer-video-effects -l pl.UTF-8
Wtyczki efektów wideo do GStreamera.

%package -n gstreamer-visualisation
Summary:	GStreamer visualisations plugins
Summary(pl.UTF-8):	Wtyczki wizualizacji do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}

%description -n gstreamer-visualisation
Various plugins for visual effects to use with audio. Included are
monoscope, spectrum, goom (2k4) and goom2k1.

%description -n gstreamer-visualisation -l pl.UTF-8
Różne wtyczki efektów wizualnych do używania z dźwiękiem. Załączone:
monoscope, spectrum, goom (2k4) i goom2k1.

%package -n gstreamer-vpx
Summary:	GStreamer plugin for VP8/VP9 video format
Summary(pl.UTF-8):	Wtyczka do GStreamera obsługująca format obrazu VP8/VP9
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	libvpx >= 1.8.0
Obsoletes:	gstreamer-vp8 < 1.0

%description -n gstreamer-vpx
GStreamer plugin for VP8/VP9 video format using libvpx library.

%description -n gstreamer-vpx -l pl.UTF-8
Wtyczka do GStreamera obsługująca format obrazu VP8/VP9 przy użyciu
biblioteki libvpx.

%package -n gstreamer-wavpack
Summary:	GStreamer plugin for Wavpack lossless audio format
Summary(pl.UTF-8):	Wtyczka do GStreamera obsługująca bezstratny format dźwięku Wavpack
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	wavpack-libs >= 4.60.0

%description -n gstreamer-wavpack
Plugin for lossless Wavpack audio format.

%description -n gstreamer-wavpack -l pl.UTF-8
Wtyczka obsługująca bezstratny format dźwięku Wavpack.

%package -n gstreamer-ximagesrc
Summary:	GStreamer X11 video input plugin using standard Xlib calls
Summary(pl.UTF-8):	Wtyczka wejścia obrazu X11 GStreamera używająca standardowych wywołań Xlib
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}

%description -n gstreamer-ximagesrc
GStreamer X11 video input plugin using standard Xlib calls.

%description -n gstreamer-ximagesrc -l pl.UTF-8
Wtyczka wejścia obrazu X11 GStreamera używająca standardowych wywołań
Xlib.

%prep
%setup -q -n %{gstname}-%{version}

%build
%{__libtoolize}
%{__aclocal} -I m4 -I common/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	ac_cv_lib_jpeg_mmx_jpeg_set_defaults=no \
	--disable-silent-rules \
	--disable-static \
	--enable-experimental \
	%{!?with_aalib:--disable-aalib} \
	%{!?with_cairo:--disable-cairo} \
	%{!?with_gtk:--disable-gtk} \
	%{!?with_jack:--disable-jack} \
	%{!?with_lame:--disable-lame --disable-twolame} \
	%{!?with_caca:--disable-libcaca} \
	%{!?with_mpg123:--disable-mpg123} \
	%{!?with_qt:--disable-qt} \
	%{!?with_soup:--disable-soup} \
	%{!?with_speex:--disable-speex} \
	%{!?with_wavpack:--disable-wavpack} \
	--enable-gtk-doc%{!?with_apidocs:=no} \
	--enable-orc \
	--with-html-dir=%{_gtkdocdir}

LC_ALL=C.UTF-8 \
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# We don't need plugins' *.la files
%{__rm} $RPM_BUILD_ROOT%{gstlibdir}/*.la

%find_lang %{gstname}-%{gstmver}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{gstname}-%{gstmver}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README RELEASE
%attr(755,root,root) %{gstlibdir}/libgstalphacolor.so
%attr(755,root,root) %{gstlibdir}/libgstalpha.so
%attr(755,root,root) %{gstlibdir}/libgstapetag.so
%attr(755,root,root) %{gstlibdir}/libgstaudiofx.so
%attr(755,root,root) %{gstlibdir}/libgstautodetect.so
%attr(755,root,root) %{gstlibdir}/libgstavi.so
%attr(755,root,root) %{gstlibdir}/libgstdebug.so
%attr(755,root,root) %{gstlibdir}/libgstdtmf.so
%attr(755,root,root) %{gstlibdir}/libgstequalizer.so
%attr(755,root,root) %{gstlibdir}/libgstdeinterlace.so
%attr(755,root,root) %{gstlibdir}/libgstflv.so
%attr(755,root,root) %{gstlibdir}/libgstflxdec.so
%attr(755,root,root) %{gstlibdir}/libgsticydemux.so
%attr(755,root,root) %{gstlibdir}/libgstid3demux.so
%attr(755,root,root) %{gstlibdir}/libgstimagefreeze.so
%attr(755,root,root) %{gstlibdir}/libgstinterleave.so
%attr(755,root,root) %{gstlibdir}/libgstisomp4.so
%attr(755,root,root) %{gstlibdir}/libgstmatroska.so
%attr(755,root,root) %{gstlibdir}/libgstmultifile.so
%attr(755,root,root) %{gstlibdir}/libgstmultipart.so
%attr(755,root,root) %{gstlibdir}/libgstnavigationtest.so
%attr(755,root,root) %{gstlibdir}/libgstoss4.so
%attr(755,root,root) %{gstlibdir}/libgstreplaygain.so
%attr(755,root,root) %{gstlibdir}/libgstrtp.so
%attr(755,root,root) %{gstlibdir}/libgstrtpmanager.so
%attr(755,root,root) %{gstlibdir}/libgstrtsp.so
%attr(755,root,root) %{gstlibdir}/libgstshapewipe.so
%attr(755,root,root) %{gstlibdir}/libgstudp.so
%attr(755,root,root) %{gstlibdir}/libgstvideobox.so
%attr(755,root,root) %{gstlibdir}/libgstvideocrop.so
%attr(755,root,root) %{gstlibdir}/libgstvideofilter.so
%attr(755,root,root) %{gstlibdir}/libgstvideomixer.so
%attr(755,root,root) %{gstlibdir}/libgsty4menc.so
%dir %{_datadir}/gstreamer-%{gstmver}
%{_datadir}/gstreamer-%{gstmver}/presets

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gst-plugins-good-plugins-%{gstmver}
%endif

##
## Plugins
##

%if %{with aalib}
%files -n gstreamer-videosink-aa
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstaasink.so
%endif

%files -n gstreamer-audio-effects-good
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstalaw.so
%attr(755,root,root) %{gstlibdir}/libgstcutter.so
%attr(755,root,root) %{gstlibdir}/libgstlevel.so
%attr(755,root,root) %{gstlibdir}/libgstmulaw.so

%files -n gstreamer-audio-formats
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstauparse.so
%attr(755,root,root) %{gstlibdir}/libgstaudioparsers.so
%attr(755,root,root) %{gstlibdir}/libgstwavparse.so
%attr(755,root,root) %{gstlibdir}/libgstwavenc.so

%if %{with cairo}
%files -n gstreamer-cairo
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstcairo.so
%endif

%files -n gstreamer-dv
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstdv.so

%files -n gstreamer-flac
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstflac.so

%files -n gstreamer-gdkpixbuf
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstgdkpixbuf.so

%if %{with gtk}
%files -n gstreamer-videosink-gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstgtk.so
%endif

%if %{with jack}
%files -n gstreamer-jack
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstjack.so
%endif

%if %{with caca}
%files -n gstreamer-videosink-libcaca
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstcacasink.so
%endif

%files -n gstreamer-lame
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstlame.so
%attr(755,root,root) %{gstlibdir}/libgsttwolame.so

%if %{with mpg123}
%files -n gstreamer-mpg123
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstmpg123.so
%endif

%files -n gstreamer-libpng
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstpng.so

%files -n gstreamer-audiosink-oss
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstossaudio.so

%files -n gstreamer-pulseaudio
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstpulseaudio.so

%if %{with qt}
%files -n gstreamer-videosink-qt
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstqmlgl.so
%endif

%files -n gstreamer-raw1394
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgst1394.so

%files -n gstreamer-shout2
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstshout2.so

%if %{with soup}
%files -n gstreamer-soup
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstsoup.so
%endif

%if %{with speex}
%files -n gstreamer-speex
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstspeex.so
%endif

%files -n gstreamer-taglib
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgsttaglib.so

%files -n gstreamer-v4l2
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstvideo4linux2.so

%files -n gstreamer-video-effects
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgsteffectv.so
%attr(755,root,root) %{gstlibdir}/libgstjpeg.so
%attr(755,root,root) %{gstlibdir}/libgstsmpte.so

%files -n gstreamer-visualisation
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstgoom.so
%attr(755,root,root) %{gstlibdir}/libgstgoom2k1.so
%attr(755,root,root) %{gstlibdir}/libgstmonoscope.so
%attr(755,root,root) %{gstlibdir}/libgstspectrum.so

%files -n gstreamer-vpx
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstvpx.so

%if %{with wavpack}
%files -n gstreamer-wavpack
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstwavpack.so
%endif

%files -n gstreamer-ximagesrc
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstximagesrc.so
