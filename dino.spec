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

