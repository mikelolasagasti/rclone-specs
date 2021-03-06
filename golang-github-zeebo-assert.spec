# Generated by go2rpm 1.6.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/zeebo/assert
%global goipath         github.com/zeebo/assert
Version:                1.3.0

%gometa

%global common_description %{expand:
Helpers for tests. You don't have to like it.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Helpers for tests. You don't have to like it

# Upstream license specification: CC0-1.0
License:        CC0
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
