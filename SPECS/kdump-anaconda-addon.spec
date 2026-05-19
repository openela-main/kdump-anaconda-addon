%global gitcommit 960325885aa3b2b2b0af8343951ea86dcacec27a
%global gitshortcommit %(c=%{gitcommit}; echo ${c:0:7})
%global snapshotdate 20220128

Name: kdump-anaconda-addon
Version: 006
Release: 16.%{snapshotdate}git%{gitshortcommit}%{?dist}
Url: https://github.com/daveyoung/kdump-anaconda-addon
License: GPLv2
Summary: Kdump configuration anaconda addon

BuildArch: noarch
Requires: anaconda >= 34.25
Requires: hicolor-icon-theme
BuildRequires: intltool gettext
BuildRequires: make
Obsoletes: kexec-tools-anaconda-addon < 2.0.17-9
Provides: kexec-tools-anaconda-addon = %{version}-%{release}

Source0: https://github.com/daveyoung/kdump-anaconda-addon/archive/%{gitcommit}/kdump-anaconda-addon-%{gitshortcommit}.tar.gz

Patch1: 0001.patch
Patch2: 0002.patch
Patch3: 0003.patch
Patch4: 0004.patch
Patch5: 0005.patch
Patch6: 0006.patch
Patch7: 0007.patch

%description
Kdump anaconda addon

%prep
%autosetup -n %{name}-%{gitcommit} -p1

%build

%install
%make_install

%find_lang kdump-anaconda-addon

%files -f kdump-anaconda-addon.lang
%doc README
%license LICENSE
%{_datadir}/anaconda/addons/com_redhat_kdump
%{_datadir}/anaconda/dbus/confs/org.fedoraproject.Anaconda.Addons.Kdump.conf
%{_datadir}/anaconda/dbus/services/org.fedoraproject.Anaconda.Addons.Kdump.service
%{_datadir}/icons/hicolor/scalable/apps/kdump.svg

%changelog
* Mon Oct 13 2025 Coiby Xu <coxu@redhat.com> - 006-16.20220128git9603258
- Feature: Set up crypttab

* Tue Apr 29 2025 Coiby Xu <coxu@redhat.com> - 006-15.20220128git9603258
- Handle the case where systemd isn't installed (RHEL-86873)

* Tue Mar 25 2025 Coiby Xu <coxu@redhat.com> - 006-14.20220128git9603258
- Disable kdump.service explicitly if users request to (RHEL-41082)

* Thu Jan 20 2022 Coiby <coxu@redhat.com> - 006-13.20220128git9603258
- Update to latest git snapshot (20220128). Resolves: bz2046612

* Thu Jan 20 2022 Coiby <coxu@redhat.com> - 006-12.20220120git44fe737
- Update to latest git snapshot (20220120). Resolves: bz2003131

* Thu Jan 13 2022 Coiby <coxu@redhat.com> - 006-11.20220113git4c5a91d
- Update to latest git snapshot (20220113). Resolves: bz2034491

* Thu Oct 14 2021 Kairui Song <kasong@redhat.com> - 006-10.20211014git641a7b7
- Update to latest git snapshot, update encryption warning message. Resolves: bz1999662

* Thu Aug 19 2021 Kairui Song <kasong@redhat.com> - 006-9.20210819git2026d20
- Update to latest git snapshot, fix encryption warning still present after disabling encryption. Resolves: bz1937035

* Wed Aug 18 2021 Kairui Song <kasong@redhat.com> - 006-8.20210818git400359b
- Update to latest git snapshot, fix installation failure when reuse old partition. Resolves: bz1937035

* Thu Aug 12 2021 Kairui Song <kasong@redhat.com> - 006-7.20210812git5b74c1d
- Update to latest git snapshot, fix kdump spoke is incomplete after luks device is deleted. Resolves: bz1937035

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 006-6.20210805gitce26db0
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Thu Aug 05 2021 Kairui Song <kasong@redhat.com> - 006-5.20210805gitce26db0
- Update to latest git snapshot, automated installation won't be blocked. Resolves: bz1986969
- Update RHEL only patch, fix inst.kdump_addon=0 not working issue. Resolves: bz1986942

* Wed Jul 21 2021 Kairui Song <kasong@redhat.com> - 006-4.20210721gitd046d22
- Update to latest git snapshot (20210721). Resolves: bz1937035, bz1959203
- Apply RHEL only patch to enable kdump by default

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 006-3.20201128git4ba507e
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 006-2.20201128git4ba507e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 28 2020 Kairui Song <kasong@redhat.com> - 006-1.20201128git4ba507e
- Update to latest git snapshot (20201128)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 005-9.20200220git80aab11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 20 2020 Kairui Song <kasong@redhat.com> - 005-8.20200220git80aab11
- Update to latest git snapshot (20200220)

* Tue Jan 14 2020 Kairui Song <kasong@redhat.com> - 005-7.20200114git122ccd9
- Update to latest git snapshot (20200114)

* Wed Aug 7 2019 Kairui Song <kasong@redhat.com> - 005-6.20190730gitc109552
- Update to latest git snapshot (20190723)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 005-5.20190103gitb16ea2c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 005-4.20190103gitb16ea2c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 3 2019 Kairui Song <kasong@redhat.com> - 005-3.20190103gitb16ea2c
- Update to latest git snapshot (20190103)

* Tue Aug 7 2018 Kairui Song <kasong@redhat.com> - 005-2.20180730git966223e
- Bump obsoleted kexec-tools-anaconda-addon version
- Remove redundant source files

* Tue Aug 7 2018 Kairui Song <kasong@redhat.com> - 005-1.20180730git966223e
- Update to latest git snapshot (20180730)

* Mon Jul 9 2018 Kairui Song <kasong@redhat.com> - 005-1.20180626git8b243e3
- Initial package for kdump-anaconda-addon
