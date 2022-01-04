Name: gdrive
Version:    %{_version}
Release:    %{_release}
Summary:    Google Drive Command Line Tools
License:    MIT
BuildArch:  x86_64
URL:        https://github.com/doctorfree/gdrive
Vendor:     Doctorwhen's Bodacious Laboratory
Packager:   ronaldrecord@gmail.com

%description
Manage your Google Drive from the command line

%prep
cp -a %{_sourcedir}/usr %{_sourcedir}/BUILDROOT/usr

%build

%install

%pre

%post

%preun

%files
/usr

%changelog
