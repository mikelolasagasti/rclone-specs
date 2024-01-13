# Generated by go2rpm 1.10.0
%bcond_without check
%global debug_package %{nil}

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
%goprep
%autopatch -p1

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog