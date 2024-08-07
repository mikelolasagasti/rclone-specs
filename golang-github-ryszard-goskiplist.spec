# Generated by go2rpm 1.14.0
%bcond check 1
%bcond bootstrap 0

%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# https://github.com/ryszard/goskiplist
%global goipath         github.com/ryszard/goskiplist
%global commit          2dfbae5fcf46374f166f8969cb07e167f1be6273

%gometa -L -f

%global common_description %{expand:
A skip list implementation in Go.}

%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTORS README.markdown

Name:           golang-github-ryszard-goskiplist
Version:        0
Release:        %autorelease -p
Summary:        A skip list implementation in Go

License:        Apache-2.0
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
