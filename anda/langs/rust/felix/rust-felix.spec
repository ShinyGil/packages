# Generated by rust2rpm 23
%global crate felix

Name:           rust-felix
Version:        2.14.0
Release:        1%?dist
Summary:        Tui file manager with vim-like key mapping

License:        MIT
URL:            https://crates.io/crates/felix
Source:         %{crates_source}

BuildRequires:  anda-srpm-macros rust-packaging >= 21

%global _description %{expand:
Tui file manager with vim-like key mapping.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%doc CHANGELOG.md
%doc README.md
%{_bindir}/fx

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep_online

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
