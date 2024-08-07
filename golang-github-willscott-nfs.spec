# Generated by go2rpm 1.14.0
%bcond check 1
%bcond bootstrap 0

%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# https://github.com/willscott/go-nfs
%global goipath         github.com/willscott/go-nfs
Version:                0.0.2

%gometa -L -f

%global godevelheader %{expand:
Requires: golang(github.com/willscott/go-nfs-client/nfs)}

%global common_description %{expand:
Golang NFSv3 server.}

%global golicenses      LICENSE
%global godocs          example CONTRIBUTING.md README.md SECURITY.md

Name:           golang-github-willscott-nfs
Release:        %autorelease
Summary:        Golang NFSv3 server

License:        Apache-2.0
URL:            %{gourl}
Source:         %{gosource}

# https://pagure.io/golist/issue/34
BuildRequires:  golang(github.com/willscott/go-nfs-client/nfs)

%description %{common_description}

%gopkg

%prep
%goprep -A
%autopatch -p1

#avoid extra deps
rm -rf example

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
