#
# Conditional build:
%bcond_without	aalib		# don't build aa videosink plugin
%bcond_without	caca		# don't build caca videosink plugin
%bcond_without	cairo		# don't build cairo plugin
%bcond_without	cdio		# don't build cdio plugin
%bcond_without	gconf		# don't build GConf plugin
%bcond_with	ladspa		# build ladspa plugin [currently built in plugins-bad]
%bcond_without	speex		# don't build speex plugin
#
%define		gstname		gst-plugins-good
%define		gst_major_ver	0.10
%define		gst_req_ver	0.10.11
%define		gstpb_req_ver	0.10.11
#
Summary:	Good GStreamer Streaming-media framework plugins
Summary(pl):	Dobre wtyczki do ¶rodowiska obróbki strumieni GStreamer
Name:		gstreamer-plugins-good
Version:	0.10.5
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://gstreamer.freedesktop.org/src/gst-plugins-good/%{gstname}-%{version}.tar.bz2
# Source0-md5:	c45fc9ace9feb4d3df32da0a6d262d84
Patch0:		%{name}-bashish.patch
Patch1:		%{name}-libcaca.patch
Patch2:		%{name}-flac.patch
URL:		http://gstreamer.freedesktop.org/
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake >= 1.5
BuildRequires:	glib2-devel >= 1:2.10.3
BuildRequires:	gstreamer-devel >= %{gst_req_ver}
BuildRequires:	gstreamer-plugins-base-devel >= %{gstpb_req_ver}
BuildRequires:	gtk-doc >= 1.7
BuildRequires:	gtk+2-devel >= 2:2.2.0
BuildRequires:	liboil-devel >= 1:0.3.8
BuildRequires:	libtool >= 1.4
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	python >= 2.1
BuildRequires:	python-PyXML
BuildRequires:	rpmbuild(macros) >= 1.198
##
## plugins
##
%{?with_gconf:BuildRequires:	GConf2-devel >= 2.14.0}
%{?with_aalib:BuildRequires:	aalib-devel >= 0.11.0}
%{?with_cairo:BuildRequires:	cairo-devel >= 1.0.0}
BuildRequires:	dbus-devel >= 0.62
BuildRequires:	esound-devel >= 0.2.12
BuildRequires:	flac-devel >= 1.1.3
BuildRequires:	hal-devel >= 0.5.7.1
%{?with_ladspa:BuildRequires:	ladspa-devel >= 1.12}
BuildRequires:	libavc1394-devel
%{?with_caca:BuildRequires:	libcaca-devel}
%{?with_cdio:BuildRequires:	libcdio-devel >= 0.71}
BuildRequires:	libdv-devel >= 0.104
BuildRequires:	libiec61883-devel >= 1.0.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.2.0
BuildRequires:	libraw1394-devel >= 1.2.1
BuildRequires:	libshout-devel >= 2.0
# for taglib
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel >= 1:2.6.26
%{?with_speex:BuildRequires:	speex-devel >= 1:1.1.6}
BuildRequires:	taglib-devel >= 1.4
BuildRequires:	zlib-devel
Requires:	gstreamer >= %{gst_req_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}
Obsoletes:	gstreamer-avi
Obsoletes:	gstreamer-flx
Obsoletes:	gstreamer-matroska
Obsoletes:	gstreamer-mixer
Obsoletes:	gstreamer-navigation
Obsoletes:	gstreamer-rtp
Obsoletes:	gstreamer-udp
Obsoletes:	gstreamer-v4l2
Conflicts:	gstreamer-plugins-bad < 0.10.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		gstlibdir 	%{_libdir}/gstreamer-%{gst_major_ver}

%description
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related. Its plugin-based architecture means
that new data types or processing capabilities can be added simply by
installing new plugins.

%description -l pl
GStreamer to ¶rodowisko obróbki danych strumieniowych, bazuj±ce na
grafie filtrów operuj±cych na danych medialnych. Aplikacje u¿ywaj±ce
tej biblioteki mog± robiæ wszystko od przetwarzania d¼wiêku w czasie
rzeczywistym, do odtwarzania filmów i czegokolwiek innego zwi±zego z
mediami. Architektura bazuj±ca na wtyczkach pozwala na ³atwe dodawanie
nowych typów danych lub mo¿liwo¶ci obróbki.

%package -n gstreamer-GConf
Summary:	GStreamer GConf schemas
Summary(pl):	Schematy GConf GStreamera
Group:		Libraries
Requires(post,preun):	GConf2
Requires:	gstreamer >= %{gst_req_ver}
Obsoletes:	gstreamer-GConf-devel

%description -n gstreamer-GConf
Installation of GStreamer GConf schemas. These set usable defaults
used by all GStreamer-enabled GNOME applications.

%description -n gstreamer-GConf -l pl
Schematy GConf dla GStreamera. Zestaw ten ustawia warto¶ci domy¶lne
dla wszystkich aplikacji GNOME korzystaj±cych z GStreamera

##
## Plugins
##

%package -n gstreamer-videosink-aa
Summary:	GStreamer plugin for Ascii-art output
Summary(pl):	Wtyczka wyj¶cia obrazu Ascii-art do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}
Provides:	gstreamer-videosink = %{version}
Obsoletes:	gstreamer-aalib

%description -n gstreamer-videosink-aa
Plugin for viewing movies in Ascii-art using aalib library.

%description -n gstreamer-videosink-aa -l pl
Wtyczka wyj¶cia obrazu Ascii-art u¿ywaj±ca biblioteki aalib.

%package -n gstreamer-audio-effects-good
Summary:	Good GStreamer audio effects plugins
Summary(pl):	Dobre wtyczki efektów d¼wiêkowych do GStreamera
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}
Obsoletes:	gstreamer-audio-effects

%description -n gstreamer-audio-effects-good
Good GStreamer audio effects plugins.

%description -n gstreamer-audio-effects-good -l pl
Dobre wtyczki efektów d¼wiêkowych do GStreamera.

%package -n gstreamer-audio-formats
Summary:	GStreamer audio format plugins
Summary(pl):	Wtyczki formatów d¼wiêku
Group:		Libraries
#Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}
# for locales in wavparse module
Requires:	%{name} = %{version}-%{release}

%description -n gstreamer-audio-formats
Plugin for playback of WAV, au and mod audio files as well as MP3 type.

%description -n gstreamer-audio-formats -l pl
Wtyczka do odwarzania d¼wiêku w formacie au, WAV, mod oraz MP3.

%package -n gstreamer-cairo
Summary:	GStreamer cairo plugin
Summary(pl):	Wtyczka cairo do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}

%description -n gstreamer-cairo
GStreamer cairo plugin.

%description -n gstreamer-cairo -l pl
Wtyczka cairo do GStreamera.

%package -n gstreamer-cdio
Summary:	GStreamer plugin for CD audio input using libcdio
Summary(pl):	Wtyczka do GStreamera odtwarzaj±ca p³yty CD-Audio przy u¿yciu libcdio
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}
Requires:	libcdio >= 0.71

%description -n gstreamer-cdio
Plugin for playing audio tracks using libcdio under GStreamer.

%description -n gstreamer-cdio -l pl
Wtyczka do odtwarzania ¶cie¿ek d¼wiêkowych pod GStreamerem za pomoc±
libcdio.

%package -n gstreamer-dv
Summary:	GStreamer dv plugin
Summary(pl):	Wtyczka dv do GStreamera
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}

%description -n gstreamer-dv
Plugin for digital video support.

%description -n gstreamer-dv -l pl
Wtyczka do GStreamera obs³uguj±ca cyfrowy obraz.

%package -n gstreamer-audiosink-esd
Summary:	GStreamer plugin for ESD sound output
Summary(pl):	Wtyczka wyj¶cia d¼wiêku ESD do GStreamera
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}
Provides:	gstreamer-audiosink = %{version}
Obsoletes:	gstreamer-esound

%description -n gstreamer-audiosink-esd
Output plugin for GStreamer for use with the esound package.

%description -n gstreamer-audiosink-esd -l pl
Wtyczka wyj¶cia d¼wiêku ESD (esound) dla GStreamera.

%package -n gstreamer-flac
Summary:	GStreamer plugin for FLAC lossless audio format
Summary(pl):	Wtyczka do GStreamera obs³uguj±ca bezstratny format d¼wiêku FLAC
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}

%description -n gstreamer-flac
Plugin for the free FLAC lossless audio format.

%description -n gstreamer-flac -l pl
Wtyczka obs³uguj±ca wolnodostêpny, bezstratny format d¼wiêku FLAC.

%package -n gstreamer-gdkpixbuf
Summary:	GStreamer images input plugin
Summary(pl):	Wtyczka do GStreamera wczytuj±ca obrazki
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}

%description -n gstreamer-gdkpixbuf
This GStreamer plugin load images via gdkpixbuf library.

%description -n gstreamer-gdkpixbuf -l pl
Ta wtyczka GStreamera wczytuje obrazki za po¶rednictwem biblioteki
gdkpixbuf.

%package -n gstreamer-hal
Summary:	GStreamer plugin to wrap the GStreamer/HAL audio input/output devices
Summary(pl):	Wtyczka GStreamera spinaj±ca urz±dzenia wej¶cia/wyj¶cia d¼wiêku z HAL-em
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}

%description -n gstreamer-hal
GStreamer plugin to wrap the GStreamer/HAL audio input/output devices.

%description -n gstreamer-hal -l pl
Wtyczka GStreamera spinaj±ca urz±dzenia wej¶cia/wyj¶cia d¼wiêku miêdzy
GStreamerem a HAL-em.

%package -n gstreamer-ladspa
Summary:	GStreamer wrapper for LADSPA plugins
Summary(pl):	Wrapper do wtyczek LADSPA dla GStreamera
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}

%description -n gstreamer-ladspa
Plugin which wraps LADSPA plugins for use by GStreamer applications.

%description -n gstreamer-ladspa -l pl
Wtyczka pozwalaj±ca na u¿ywanie wtyczek LADSPA przez aplikacje
GStreamera.

%package -n gstreamer-videosink-libcaca
Summary:	GStreamer plugin for libcaca Ascii-art output
Summary(pl):	Wtyczka libcaca do GStreamera
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}
Provides:	gstreamer-videosink = %{version}

%description -n gstreamer-videosink-libcaca
GStreamer plug-in for libcaca Ascii-art output.

%description -n gstreamer-videosink-libcaca -l pl
Wtyczka libcaca do GStreamera.

%package -n gstreamer-libpng
Summary:	GStreamer plugin to encode png images
Summary(pl):	Wtyczka GStreamera koduj±ca pliki png
Group:		Libraries
#Requires:	gstreamer >= %{gst_req_ver}
# for locales
Requires:	%{name} = %{version}-%{release}
Requires:	libpng >= 1.2.0

%description -n gstreamer-libpng
Plugin for encoding png images.

%description -n gstreamer-libpng -l pl
Wtyczka koduj±ca pliki png.

%package -n gstreamer-audiosink-oss
Summary:	GStreamer plugins for input and output using OSS
Summary(pl):	Wtyczki wej¶cia i wyj¶cia d¼wiêku OSS do GStreamera
Group:		Libraries
#Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}
# for locales
Requires:	%{name} = %{version}-%{release}
Provides:	gstreamer-audiosink = %{version}
Obsoletes:	gstreamer-oss

%description -n gstreamer-audiosink-oss
Plugins for output and input to the OpenSoundSystem audio drivers
found in the Linux kernels or commercially available from OpenSound.

%description -n gstreamer-audiosink-oss -l pl
Wtyczki wyj¶cia i wej¶cia d¼wiêku u¿ywaj±ce sterowników
OpenSoundSystem obecnych w j±drach Linuksa lub dostêpnych komercyjnie
od OpenSound.

%package -n gstreamer-raw1394
Summary:	GStreamer raw1394 Firewire plugin
Summary(pl):	Wtyczka FireWire dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}

%description -n gstreamer-raw1394
Plugin for digital video support using raw1394.

%description -n gstreamer-raw1394 -l pl
Wtyczka daj±ca dostêp do cyfrowego obrazu przy u¿yciu raw1394.

%package -n gstreamer-shout2
Summary:	GStreamer plugin for communicating with Shoutcast servers
Summary(pl):	Wtyczka do GStreamera umo¿liwiaj±ca komunikacjê z serwerami Shoutcast
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}

%description -n gstreamer-shout2
GStreamer plugin for communicating with Shoutcast servers.

%description -n gstreamer-shout2 -l pl
Wtyczka do GStreamera umo¿liwiaj±ca komunikacjê z serwerami Shoutcast.

%package -n gstreamer-speex
Summary:	GStreamer speex codec decoder/encoder plugin
Summary(pl):	Wtyczka do GStreamera obs³uguj±ca kodek Speex
Group:		Libraries
#Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}
Requires:	speex >= 1:1.1.6

%description -n gstreamer-speex
GStreamer speex codec decoder/encoder plugin.

%description -n gstreamer-speex -l pl
Wtyczka do GStreamera obs³uguj±ca kodek Speex.

%package -n gstreamer-taglib
Summary:	GStreamer tag writing plugin based on taglib
Summary(pl):	Wtyczka GStreamera zapisuj±ca znaczniki oparta na bibliotece taglib
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}

%description -n gstreamer-taglib
GStreamer tag writing plugin based on taglib.

%description -n gstreamer-taglib -l pl
Wtyczka GStreamera zapisuj±ca znaczniki oparta na bibliotece taglib.

%package -n gstreamer-video-effects
Summary:	GStreamer video effects plugins
Summary(pl):	Wtyczki efektów wideo do GStreamera
Group:		Libraries
# for locales in jpeg module
Requires:	%{name} = %{version}-%{release}

%description -n gstreamer-video-effects
GStreamer video effects plugins.

%description -n gstreamer-video-effects -l pl
Wtyczki efektów wideo do GStreamera.

%package -n gstreamer-visualisation
Summary:	GStreamer visualisations plugins
Summary(pl):	Wtyczki wizualizacji do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}

%description -n gstreamer-visualisation
Various plugins for visual effects to use with audio. Included are
smoothwave, spectrum, goom, chart, monoscope and synaesthesia.

%description -n gstreamer-visualisation -l pl
Ró¿ne wtyczki efektów wizualnych do u¿ywania z d¼wiêkiem. Za³±czone:
smoothwave, spectrum, goom, chart, monoscope i synaesthesia.

%package -n gstreamer-ximagesrc
Summary:	GStreamer X11 video input plugin using standard Xlib calls
Summary(pl):	Wtyczka wej¶cia obrazu X11 GStreamera u¿ywaj±ca standardowych wywo³añ Xlib
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n gstreamer-ximagesrc
GStreamer X11 video input plugin using standard Xlib calls.

%description -n gstreamer-ximagesrc -l pl
Wtyczka wej¶cia obrazu X11 GStreamera u¿ywaj±ca standardowych wywo³añ
Xlib.

%prep
%setup -q -n %{gstname}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4 -I common/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	ac_cv_lib_jpeg_mmx_jpeg_set_defaults=no \
	%{!?with_aalib:--disable-aalib} \
	%{!?with_caca:--disable-libcaca} \
	%{!?with_cairo:--disable-cairo} \
	%{!?with_cdio:--disable-cdio} \
	--enable-experimental \
	%{?with_ladspa:--enable-ladspa} \
	%{!?with_speex:--disable-speex} \
	--disable-static \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# We don't need plugins' *.la files
rm -f $RPM_BUILD_ROOT%{gstlibdir}/*.la

%find_lang %{gstname}-%{gst_major_ver}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n gstreamer-GConf
%gconf_schema_install gstreamer-0.10.schemas

%preun	-n gstreamer-GConf
%gconf_schema_uninstall gstreamer-0.10.schemas

%files -f %{gstname}-%{gst_major_ver}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README RELEASE 
%attr(755,root,root) %{gstlibdir}/libgstalphacolor.so
%attr(755,root,root) %{gstlibdir}/libgstalpha.so
%attr(755,root,root) %{gstlibdir}/libgstannodex.so
%attr(755,root,root) %{gstlibdir}/libgstapetag.so
%attr(755,root,root) %{gstlibdir}/libgstaudiofx.so
%attr(755,root,root) %{gstlibdir}/libgstautodetect.so
%attr(755,root,root) %{gstlibdir}/libgstavi.so
%attr(755,root,root) %{gstlibdir}/libgstdebug.so
%attr(755,root,root) %{gstlibdir}/libgstefence.so
%attr(755,root,root) %{gstlibdir}/libgstflxdec.so
%attr(755,root,root) %{gstlibdir}/libgsticydemux.so
%attr(755,root,root) %{gstlibdir}/libgstid3demux.so
%attr(755,root,root) %{gstlibdir}/libgstmatroska.so
%attr(755,root,root) %{gstlibdir}/libgstmultipart.so
%attr(755,root,root) %{gstlibdir}/libgstnavigationtest.so
%attr(755,root,root) %{gstlibdir}/libgstrtp.so
%attr(755,root,root) %{gstlibdir}/libgstrtsp.so
%attr(755,root,root) %{gstlibdir}/libgstudp.so
%attr(755,root,root) %{gstlibdir}/libgstvideo4linux2.so
%attr(755,root,root) %{gstlibdir}/libgstvideobalance.so
%attr(755,root,root) %{gstlibdir}/libgstvideobox.so
%attr(755,root,root) %{gstlibdir}/libgstvideomixer.so
%{_gtkdocdir}/gst-plugins-good-plugins-*

%if %{with gconf}
%files -n gstreamer-GConf
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstgconfelements.so
%{_sysconfdir}/gconf/schemas/gstreamer-0.10.schemas
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
%attr(755,root,root) %{gstlibdir}/libgstlevel.so
%attr(755,root,root) %{gstlibdir}/libgstmulaw.so
%attr(755,root,root) %{gstlibdir}/libgstcutter.so

%files -n gstreamer-audio-formats
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstauparse.so
%attr(755,root,root) %{gstlibdir}/libgstwavparse.so
%attr(755,root,root) %{gstlibdir}/libgstwavenc.so

%if %{with cairo}
%files -n gstreamer-cairo
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstcairo.so
%endif

%if %{with cdio}
%files -n gstreamer-cdio
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstcdio.so
%endif

%files -n gstreamer-dv
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstdv.so

%files -n gstreamer-audiosink-esd
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstesd.so

%files -n gstreamer-flac
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstflac.so

%files -n gstreamer-gdkpixbuf
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstgdkpixbuf.so

%files -n gstreamer-hal
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgsthalelements.so

# disabled in ext/Makefile.am, currently built in plugins-bad
#%if %{with ladspa}
#%files -n gstreamer-ladspa
#%defattr(644,root,root,755)
#%attr(755,root,root) %{gstlibdir}/libgstladspa.so
#%endif

%if %{with caca}
%files -n gstreamer-videosink-libcaca
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstcacasink.so
%endif

%files -n gstreamer-libpng
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstpng.so

%files -n gstreamer-audiosink-oss
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstossaudio.so

%files -n gstreamer-raw1394
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgst1394.so

%files -n gstreamer-shout2
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstshout2.so

%if %{with speex}
%files -n gstreamer-speex
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstspeex.so
%endif

%files -n gstreamer-taglib
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgsttaglib.so

%files -n gstreamer-video-effects
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgsteffectv.so
%attr(755,root,root) %{gstlibdir}/libgstjpeg.so
%attr(755,root,root) %{gstlibdir}/libgstsmpte.so
%attr(755,root,root) %{gstlibdir}/libgstvideoflip.so

%files -n gstreamer-visualisation
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstgoom.so

%files -n gstreamer-ximagesrc
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstximagesrc.so
