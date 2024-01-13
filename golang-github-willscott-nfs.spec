# Generated by go2rpm 1.10.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/willscott/go-nfs
%global goipath         github.com/willscott/go-nfs
Version:                0.0.2

%gometa -L -f

# For some reason doesn't pull this dep
#%%global godevelheader %%{expand:
#
#}

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

BuildRequires:  golang-github-willscott-nfs-client-devel

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

#avoid extra deps
rm -rf example

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
