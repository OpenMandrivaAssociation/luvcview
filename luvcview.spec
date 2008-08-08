%define name luvcview
%define version 0.2.4
%define release %mkrel 2

Summary: SDL-based video grabber
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.lzma
Source1: dynctrl-logitech.h
Source2: uvcvideo.h
Source3: uvc_compat.h
License: GPLv2+
Group: Video
Url: http://www.quickcamteam.net/software/linux/v4l2-software/luvcview
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: SDL-devel

%description
luvcview is a small video capture program ideal for webcam testing and
problem debugging.

%prep
%setup -q
cp %SOURCE1 .
cp %SOURCE2 .
cp %SOURCE3 .

%build
%make

%install
rm -rf %{buildroot}
%__install -D -s -m 755 luvcview %{buildroot}/usr/bin/luvcview

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changelog ToDo
%{_bindir}/*

