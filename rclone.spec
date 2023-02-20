# Generated by go2rpm 1.8.0
%bcond_without check

# https://github.com/rclone/rclone
%global goipath         github.com/rclone/rclone
Version:                1.61.1

%gometa -f

%global goname rclone

%global common_description %{expand:
Rclone is a command line program to sync files and directories to and
from various cloud services.}

# This package uses gold. Tell package-notes implementation about this.
%global _package_note_linker gold

Name:           %{goname}
Release:        %autorelease
Summary:        Rsync for cloud storage

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep
sed -i "s|github.com/putdotio/go-putio/putio|github.com/putdotio/go-putio|" $(find . -name "*.go")

%generate_buildrequires
%go_generate_buildrequires

%build
export LDFLAGS="-X github.com/rclone/rclone/fs.Version=%{version}"
%gobuild -o %{gobuilddir}/bin/rclone %{goipath}

%{gobuilddir}/bin/%{name} completion bash > %{name}.bash
%{gobuilddir}/bin/%{name} completion fish > %{name}.fish
%{gobuilddir}/bin/%{name} completion zsh  > %{name}.zsh


%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -Dpm 0644 ./rclone.1 %{buildroot}%{_mandir}/man1/rclone.1

install -Dp %{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dp %{name}.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish
install -Dp %{name}.zsh  %{buildroot}%{_datadir}/zsh/site-functions/_%{name}


%if %{with check}
%check
for test in "TestMixed" "TestMetadata" "TestMediaReceiverRegistrarService" \
"TestAccountWriteToWithBuffer" "TestLocal" "TestRemoteGzip" "TestIntegration" \
"TestPolicy3" "TestPolicy2" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
# Skip checks requiring docker or fuse
%gocheck -d backend/crypt \
         -d backend/ftp \
         -d backend/hdfs \
         -d backend/seafile \
         -d backend/sftp \
         -d backend/sia \
         -d backend/swift \
         -d backend/union \
         -d backend/webdav \
         -d cmd/mount \
         -d cmd/mount2 \
         -d cmd/selfupdate \
         -d cmd/serve/docker \
         -d fs/rc/webgui
%endif

%files
%license COPYING
%doc MAINTAINERS.md MANUAL.html RELEASE.md CONTRIBUTING.md MANUAL.md README.md
%doc docs/
%{_bindir}/rclone
%{_mandir}/man1/rclone.1*
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/%{name}.fish
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}
%gopkgfiles

%changelog
%autochangelog
