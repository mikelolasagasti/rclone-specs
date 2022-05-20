# Generated by go2rpm 1.6.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/lucas-clemente/quic-go
%global goipath         github.com/lucas-clemente/quic-go
Version:                0.27.0

%gometa

%global common_description %{expand:
A QUIC implementation in pure go.}

%global golicenses      LICENSE
%global godocs          docs example Changelog.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        QUIC implementation in pure go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

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
