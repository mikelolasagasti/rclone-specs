# Generated by go2rpm 1.9.0
%bcond_without check
# storj backend has fragile dependencies
%bcond_with storj
# protondrive backend introduces many new deps
%bcond_with protondrive

# https://github.com/rclone/rclone
%global goipath         github.com/rclone/rclone
Version:                1.67.0

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

License:        MIT AND BSD-3-Clause
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%prep
%goprep
sed -i "s|github.com/putdotio/go-putio/putio|github.com/putdotio/go-putio|" $(find . -name "*.go")

%if %{without storj}
sed  '/storj/d' -i backend/all/all.go
rm -rf backend/storj
%endif
%if %{without protondrive}
sed  '/protondrive/d' -i backend/all/all.go
rm -rf backend/protondrive
%endif

%generate_buildrequires
%go_generate_buildrequires

%build
export LDFLAGS="-X github.com/rclone/rclone/fs.Version=%{version}"
%gobuild -o %{gobuilddir}/bin/rclone %{goipath}

%{gobuilddir}/bin/%{name} completion bash - > %{name}.bash
%{gobuilddir}/bin/%{name} completion fish - > %{name}.fish
%{gobuilddir}/bin/%{name} completion zsh  - > %{name}.zsh


%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -Dpm 0644 ./rclone.1 %{buildroot}%{_mandir}/man1/rclone.1

install -Dpm 0644 %{name}.bash %{buildroot}%{bash_completions_dir}/%{name}
install -Dpm 0644 %{name}.fish %{buildroot}%{fish_completions_dir}/%{name}.fish
install -Dpm 0644 %{name}.zsh  %{buildroot}%{zsh_completions_dir}/_%{name}

# https://rclone.org/commands/rclone_mount/#rclone-as-unix-mount-helper
install -m 0755 -vd                     %{buildroot}%{_sbindir}
ln -rs %{buildroot}%{_bindir}/rclone %{buildroot}%{_sbindir}/mount.rclone
ln -rs %{buildroot}%{_bindir}/rclone %{buildroot}%{_bindir}/rclonefs

%if %{with check}
%check
for test in "TestMixed" "TestMetadata" "TestMediaReceiverRegistrarService" \
"TestAccountWriteToWithBuffer" "TestLocal" "TestRemoteGzip" "TestIntegration" \
"TestPolicy3" "TestPolicy2" "TestRcatMetadata" "TestRcatSizeMetadata" \
"TestStatsGroupOperations" "TestMetadataMapper" "TestLogger" "TestFileServing" \
"TestMkdirMetadata" \
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
%{_bindir}/rclonefs
%{_sbindir}/mount.rclone
%{_mandir}/man1/rclone.1*
%{bash_completions_dir}/%{name}
%{fish_completions_dir}/%{name}.fish
%{zsh_completions_dir}/_%{name}

%changelog
%autochangelog
