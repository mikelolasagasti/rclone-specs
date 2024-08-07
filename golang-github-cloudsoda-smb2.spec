# Generated by go2rpm 1.14.0
%bcond check 1
%bcond bootstrap 0

%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# https://github.com/cloudsoda/go-smb2
%global goipath         github.com/cloudsoda/go-smb2
%global commit          f3ec8ae2c891ee40aab4d251873aab5db51f7cf8

%gometa -L -f

%global common_description %{expand:
Client implementation of the SMB 2 & 3 protocols.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           golang-github-cloudsoda-smb2
Version:        0
Release:        %autorelease -p
Summary:        Client implementation of the SMB 2 & 3 protocols

License:        BSD-2-Clause
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep -A
%autopatch -p1

%if %{without bootstrap}
%generate_buildrequires
%go_generate_buildrequires
%endif

%install
%gopkginstall

%if %{without bootstrap}
%if %{with check}
%check
%gocheck
%endif
%endif

%gopkgfiles

%changelog
%autochangelog
