# Generated by go2rpm 1.6.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/Max-Sum/base32768
%global goipath         github.com/Max-Sum/base32768
%global commit          7937843c71d5ca06277cdafe587ce1e13dc05791

%gometa

%global common_description %{expand:
Go implementation of base32768, optimized for UTF-16.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        %autorelease -p
Summary:        Go implementation of base32768, optimized for UTF-16

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
