# Generated by go2rpm 1.9.0
%bcond_without check

# https://github.com/colinmarc/hdfs
%global goipath         github.com/colinmarc/hdfs/v2
Version:                2.4.0

%gometa -f


%global common_description %{expand:
This is a native golang client for hdfs. It connects directly to the namenode
using the protocol buffers API.

It tries to be idiomatic by aping the stdlib os package, where possible, and
implements the interfaces from it, including os.FileInfo and os.PathError.}

%global golicenses      LICENSE.txt
%global godocs          CODE_OF_CONDUCT.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Native go client for HDFS

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

%build
export LDFLAGS="-X main.version=%{version} "
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
# .: needs network
%gocheck -d .
%endif

%files
%license LICENSE.txt
%doc CODE_OF_CONDUCT.md README.md
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog
