Name:           geogebra-thumbnail-kde
Summary:        KDE Thumbnail Creator for GeoGebra files
Version:        0.45.1
Release:        %mkrel 1
Group:          Productivity/Scientific/Math
Url:            http://www.geogebra.org/en/wiki/index.php/GeoGebra_in_Linux
License:        LGPLv3
Source:         GeoGebra_Thumbnail_KDE.tar.gz
Source1:        geogebrathumbnail.desktop
Source2:        geogebra.xml
Source3:        GeoGebra_Thumbnail_KDE_hicolor_icons.tar.gz
%if 0%{?mandriva_version}
BuildRequires:  basekde4-devel
%if 0%{?mandriva_version} == 201000
BuildRequires:  clucene-core
BuildRequires:  clucene-core-devel
%endif
%else
%if 0%{?fedora} || 0%{?rhel_version} || 0%{?centos_version}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  basekde4-devel
BuildRequires:  kernel
%else
BuildRequires:  kdebase4-devel
%endif
%endif
Requires:       kdebase4-runtime
%if !0%{?fedora} && !0%{?rhel_version} && !0%{?centos_version}
Supplements:    packageand(mimehandler(application/vnd.geogebra.file):kdebase4-runtime)
Supplements:    packageand(mimehandler(application/vnd.geogebra.tool):kdebase4-runtime)
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package provides GeoGebraThumbnail, a KDE thumbnail-plugin that generates small images (thumbnails) for GeoGebra files, to be displayed, for example, on Konqueror and Dolphin file managers.



Authors:
--------
   Ariel Constenla-Haile (La Plata, Argentina)

%prep
%setup -q -n GeoGebraThumbnail
%{__install} -m644 %{SOURCE1} src/geogebrathumbnail.desktop
tar -xzf %{SOURCE3}

%build
%{__install} -d -m755 build
cd build
cmake -DCMAKE_INSTALL_PREFIX=`kde4-config --prefix` ..
make

%install
%{__install} -d -m755 %{buildroot}%{_docdir}/%{name}
%{__install} -m644 LICENSE %{buildroot}%{_docdir}/%{name}/COPYING
for SIZE in 16x16 22x22 32x32 48x48 64x64 128x128 256x256; do
%{__install} -d -m755 %{buildroot}%{_datadir}/icons/hicolor/$SIZE/mimetypes
%{__install} -m644 hicolor/$SIZE/mimetypes/application-vnd.geogebra.file.png %{buildroot}%{_datadir}/icons/hicolor/$SIZE/mimetypes
%{__install} -m644 hicolor/$SIZE/mimetypes/application-vnd.geogebra.tool.png %{buildroot}%{_datadir}/icons/hicolor/$SIZE/mimetypes
done
%{__install} -d -m755 %{buildroot}%{_datadir}/mime/packages
%{__install} -m644 %{SOURCE2} %{buildroot}%{_datadir}/mime/packages/geogebra.xml
%{__install} -d -m755 %{buildroot}%{_libdir}/kde4
cd build

make DESTDIR=%{?buildroot:%{buildroot}} install/fast


%clean
rm -rf %{buildroot}

%post
%if 0%{?mandriva_version}
%update_mime_database
%update_icon_cache hicolor
%else
%{_bindir}/update-mime-database %{_datadir}/mime >/dev/null
%endif

%postun
%if 0%{?mandriva_version}
%clean_mime_database
%update_icon_cache hicolor
%else
%{_bindir}/update-mime-database %{_datadir}/mime >/dev/null
%endif

%files
%defattr(-,root,root)
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/16x16
%dir %{_datadir}/icons/hicolor/22x22
%dir %{_datadir}/icons/hicolor/32x32
%dir %{_datadir}/icons/hicolor/48x48
%dir %{_datadir}/icons/hicolor/64x64
%dir %{_datadir}/icons/hicolor/128x128
%dir %{_datadir}/icons/hicolor/256x256
%dir %{_datadir}/icons/hicolor/16x16/mimetypes
%dir %{_datadir}/icons/hicolor/22x22/mimetypes
%dir %{_datadir}/icons/hicolor/32x32/mimetypes
%dir %{_datadir}/icons/hicolor/48x48/mimetypes
%dir %{_datadir}/icons/hicolor/64x64/mimetypes
%dir %{_datadir}/icons/hicolor/128x128/mimetypes
%dir %{_datadir}/icons/hicolor/256x256/mimetypes
%dir %{_libdir}/kde4
%dir %{_datadir}/kde4
%dir %{_datadir}/kde4/services
%{_docdir}/%{name}
%{_datadir}/mime/packages/geogebra.xml
%{_libdir}/kde4/geogebrathumbnail.so
%{_datadir}/kde4/services/geogebrathumbnail.desktop
%{_datadir}/icons/hicolor/*/*/*.png

