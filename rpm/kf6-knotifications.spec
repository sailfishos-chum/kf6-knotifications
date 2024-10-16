%global  kf_version 6.6.0

Name:    kf6-knotifications
Version: 6.6.0
Release: 0%{?dist}
Summary: KDE Frameworks 6 Tier 2 solution with abstraction for system notifications

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/knotifications

Source0:    %{name}-%{version}.tar.bz2

BuildRequires:  kf6-extra-cmake-modules >= %{kf_version}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  libcanberra-devel
BuildRequires:  kf6-kconfig-devel

%description
KDE Frameworks 6 Tier 3 solution with abstraction for system
notifications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang_kf6 knotifications6_qt
# We own the folder
mkdir -p %{buildroot}/%{_kf6_datadir}/knotifications6

%files -f knotifications6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/knotifications.*
%{_kf6_libdir}/libKF6Notifications.so.*
%dir %{_kf6_datadir}/knotifications6
%{_libdir}/qt6/qml/org/kde/notification/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/notification/knotificationqmlplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/notification/libknotificationqmlplugin.so
%{_libdir}/qt6/qml/org/kde/notification/qmldir

%files devel
%{_kf6_includedir}/KNotifications/
%{_kf6_libdir}/libKF6Notifications.so
%{_kf6_libdir}/cmake/KF6Notifications/
%{_qt6_docdir}/*.tags

%files doc
%{_qt6_docdir}/*.qch
