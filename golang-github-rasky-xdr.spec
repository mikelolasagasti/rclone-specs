# Generated by go2rpm 1.10.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/rasky/go-xdr
%global goipath         github.com/rasky/go-xdr
%global commit          1a41d1a06c93bf8a0e0385be3847a277bb793187

%gometa -L -f


%global common_description %{expand:
Implements the XDR standard as specified in RFC 4506 in pure Google Go
(Golang).}

%global golicenses      LICENSE
%global godocs          README.md

Name:           golang-github-rasky-xdr
Version:        0
Release:        %autorelease -p
Summary:        Implements the XDR standard as specified in RFC 4506 in pure Google Go (Golang)

License:        ISC
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