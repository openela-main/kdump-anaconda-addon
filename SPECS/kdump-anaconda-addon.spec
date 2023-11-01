%global gitcommit ffd365e8b1885b6f7dd285685f3b94ac0bc83e52
%global gitshortcommit %(c=%{gitcommit}; echo ${c:0:7})
%global snapshotdate 20220519

Name: kdump-anaconda-addon
Version: 003
Release: 8.%{snapshotdate}git%{gitshortcommit}%{?dist}
Url: https://github.com/daveyoung/kdump-anaconda-addon
License: GPLv2
Summary: Kdump configuration anaconda addon

BuildArch: noarch
Requires: anaconda >= 32.18
Requires: hicolor-icon-theme
BuildRequires: intltool gettext
Obsoletes: kexec-tools-anaconda-addon < 2.0.17-12
Provides: kexec-tools-anaconda-addon = %{version}-%{release}

Source0: https://github.com/daveyoung/kdump-anaconda-addon/archive/%{gitcommit}/kdump-anaconda-addon-%{gitshortcommit}.tar.gz

%description
Kdump anaconda addon

%prep
%autosetup -n %{name}-%{gitcommit}

%build

%install
%make_install

%find_lang kdump-anaconda-addon

%files -f kdump-anaconda-addon.lang
%doc README
%license LICENSE
%{_datadir}/anaconda/addons/com_redhat_kdump
%{_datadir}/icons/hicolor/scalable/apps/kdump.svg

%changelog
* Thu May 19 2022 Coiby Xu <coxu@redhat.com> - 003-8.20220519gitffd365e
- return False instead of None for the mandatory property

* Thu Oct 21 2021 Kairui Song <kasong@redhat.com> - 003-7.20211021gitcb5edde
- Warn the user when encrypted storage is in-use

* Thu Feb 04 2021 Kairui Song <kasong@redhat.com> - 003-6.20210204git43c39c1
- Set default crashkernel value to 'auto'

* Mon Aug 10 2020 Kairui Song <kasong@redhat.com> - 003-5.20200810git0202fa1
- Update kdump icon

* Fri Jul 10 2020 Kairui Song <kasong@redhat.com> - 003-4.20200526gita0c4527
- Fix CI gating

* Tue May 26 2020 Kairui Song <kasong@redhat.com> - 003-3.20200526gita0c4527
- Rebase to latest upstream

* Wed Nov 07 2018 Kairui Song <kasong@redhat.com> - 003-2.20181107git443d7ed
- Define help_id for Kdump spokes (#1637546)

* Wed Aug 29 2018 Kairui Song <kasong@redhat.com> - 003-1.20180730git06ad891
- Initial package for kdump-anaconda-addon
