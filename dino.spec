%define name	dino
%define version	0.2.8
%define release 1

Name: 	 	%{name}
Summary: 	Pattern-based MIDI sequencer
Version: 	%{version}
Release: 	%{release}
License:	GPLv2+
Group:		Sound
URL:		http://dino.nongnu.org/
Source0:	http://download.savannah.nongnu.org/releases/dino/%{name}-%{version}.tar.gz
BuildRequires:	imagemagick
BuildRequires:	jackit-devel >= 0.102.5
BuildRequires:	libglademm2.4-devel
BuildRequires:	lash-devel
BuildRequires:	libxml++-devel
BuildRequires:	chrpath
BuildRequires:	readline-devel

%description
Dino is a pattern-based sequencer, which means that you write small patterns
of MIDI events that you can repeat and arrange to create a whole song. Each
track has its own patterns, so you can for example play the same drum pattern
over and over again while you play different lead synth patterns and
basslines.

%prep
%setup -q

%build
%configure2_5x
%make
										
%install
%makeinstall_std
chrpath -d %buildroot/%_bindir/%name

#menu
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Dino
Comment=MIDI Sequencer
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-Multimedia-Sound;AudioVideo;Audio;Sequencer;
EOF

#icons
mkdir -p %{buildroot}/%_liconsdir
convert -size 48x48 pixmaps/head.png %{buildroot}/%_liconsdir/%name.png
mkdir -p %{buildroot}/%_iconsdir
convert -size 32x32 pixmaps/head.png %{buildroot}/%_iconsdir/%name.png
mkdir -p %{buildroot}/%_miconsdir
convert -size 16x16 pixmaps/head.png %{buildroot}/%_miconsdir/%name.png

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/%name
%{_datadir}/%name
%{_datadir}/applications/mandriva-%{name}.desktop
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png



%changelog
* Mon Apr 23 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.2.8-1
+ Revision: 792808
- update to 0.2.8
- drop old patches

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.2-2mdv2011.0
+ Revision: 610244
- rebuild

* Sat May 01 2010 Funda Wang <fwang@mandriva.org> 0.2.2-1mdv2010.1
+ Revision: 541395
- fix build with gcc 4.4

* Tue Apr 14 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.2-1mdv2009.1
+ Revision: 366884
- fix build dependencies
- new version
- fix build

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request
    - import dino

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Wed Sep 13 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.2.1-2mdv2007.0
- XDG
- Add Patch0: Fix Build 

* Thu May 18 2006 Austin Acton <austin@mandriva.org> 0.2.1-1mdk
- initial package
