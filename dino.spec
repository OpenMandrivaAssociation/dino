Summary:	Pattern-based MIDI sequencer
Name:	 dino
Version:	0.2.8
Release:	12
License:	GPLv2+
Group:	Sound
Url:	https://savannah.nongnu.org/projects/dino
Source0:	https://download.savannah.nongnu.org/releases/dino/%{name}-%{version}.tar.gz
Patch0:	dino-0.2.8-gcc5.patch
Patch1:	dino-0.2.8-use-ladish-in-place-of-lash.patch
BuildRequires:	chrpath
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(libglademm-2.4)
BuildRequires:	pkgconfig(liblash)
BuildRequires:	pkgconfig(libxml++-2.6)
BuildRequires:	pkgconfig(readline)

%description
Dino is a pattern-based sequencer, which means that you write small patterns
of MIDI events that you can repeat and arrange to create a whole song. Each
track has its own patterns, so you can for example play the same drum pattern
over and over again while you play different lead synth patterns and
basslines.

%files
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
export CXX="g++ -std=gnu++11"
autoreconf -vfi
%configure
%make_build


%install
%make_install

# Drop rpath
chrpath -d %buildroot/%_bindir/%name

# Provide a menu entry
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Dino
Comment=MIDI Sequencer
Exec=%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=X-OpenMandriva-Multimedia-Sound;AudioVideo;Audio;Sequencer;
EOF

# Provide icons
mkdir -p %{buildroot}/%{_liconsdir}
mkdir -p %{buildroot}/%{_iconsdir}
mkdir -p %{buildroot}/%{_miconsdir}
convert -size 48x48 pixmaps/head.png %{buildroot}/%{_liconsdir}/%{name}.png
convert -size 32x32 pixmaps/head.png %{buildroot}/%{_iconsdir}/%{name}.png
convert -size 16x16 pixmaps/head.png %{buildroot}/%{_miconsdir}/%{name}.png
