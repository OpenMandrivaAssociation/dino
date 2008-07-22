%define name	dino
%define version	0.2.1
%define release %mkrel 4

Name: 	 	%{name}
Summary: 	Pattern-based MIDI sequencer
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
Patch0:         dino-0.2.1-fix-build.patch
URL:		http://dinoseq.sourceforge.net/
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	ImageMagick
BuildRequires:	jackit-devel >= 0.102.5
BuildRequires:	libglademm2.4-devel
BuildRequires:	lash-devel
BuildRequires:	libxml++-devel
BuildRequires:	chrpath

%description
Dino is a pattern-based sequencer, which means that you write small patterns
of MIDI events that you can repeat and arrange to create a whole song. Each
track has its own patterns, so you can for example play the same drum pattern
over and over again while you play different lead synth patterns and
basslines.

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
chrpath -d %buildroot/%_bindir/%name

#menu

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
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
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 pixmaps/head.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 pixmaps/head.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 pixmaps/head.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/%name
%{_datadir}/%name
%{_datadir}/applications/mandriva-%{name}.desktop
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png

