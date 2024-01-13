# Generated by go2rpm 1.10.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/Mikubill/gofakes3
%global goipath         github.com/Mikubill/gofakes3
Version:                0.0.2
%global commit          284c0f988700cedc9a4c4f9dbfedf56351c52ef5

%gometa -L -f


%global common_description %{expand:
A simple fake AWS S3 object storage.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           golang-github-mikubill-gofakes3
Release:        %autorelease
Summary:        A simple fake AWS S3 object storage

License:        MIT
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
