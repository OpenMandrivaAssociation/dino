%define name	dino
%define version	0.2.2
%define release %mkrel 2

Name: 	 	%{name}
Summary: 	Pattern-based MIDI sequencer
Version: 	%{version}
Release: 	%{release}
License:	GPL
Group:		Sound
URL:		http://dino.nongnu.org/
Source:		http://download.savannah.nongnu.org/releases/dino/%{name}-%{version}.tar.gz
Patch2:         dino-0.2.2-fix-jack-api-change.patch
Patch3:         44485e712d043398fed396d010af613d79c672f4.patch
Patch4:         79742f0d08e23ee0c6737b48e242246adc065bac.patch
Patch5:		dino-0.2.2-gcc44.patch
BuildRequires:	imagemagick
BuildRequires:	jackit-devel >= 0.102.5
BuildRequires:	libglademm2.4-devel
BuildRequires:	lash-devel
BuildRequires:	libxml++-devel
BuildRequires:	chrpath
BuildRequires:	readline-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Dino is a pattern-based sequencer, which means that you write small patterns
of MIDI events that you can repeat and arrange to create a whole song. Each
track has its own patterns, so you can for example play the same drum pattern
over and over again while you play different lead synth patterns and
basslines.

%prep
%setup -q
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p0

%build
%configure2_5x
%make
										
%install
rm -rf %{buildroot}
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

%find_lang %name

%clean
rm -rf %{buildroot}

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

