# Generated by rust2rpm 27
%bcond check 0

%global crate mise

Name:           rust-mise
Version:        2025.1.13
Release:        1%?dist
Summary:        Front-end to your dev env

License:        MIT
URL:            https://crates.io/crates/mise
Source:         %{crates_source}
Source1:        https://raw.githubusercontent.com/jdx/mise/refs/tags/v%version/man/man1/mise.1
Source2:        https://raw.githubusercontent.com/jdx/mise/refs/tags/v%version/completions/mise.bash
Source3:        https://raw.githubusercontent.com/jdx/mise/refs/tags/v%version/completions/mise.fish
Source4:        https://raw.githubusercontent.com/jdx/mise/refs/tags/v%version/completions/_mise
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          mise-fix-metadata-auto.diff
Packager:       madonuko <mado@fyralabs.com>

BuildRequires:  anda-srpm-macros mold cargo-rpm-macros >= 24
BuildRequires:  pkgconfig(openssl)

%global _description %{expand:
The front-end to your dev env.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
License:        ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-3-Clause AND BSL-1.0 AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND MIT AND (MIT AND (MIT OR Apache-2.0)) AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR BSD-1-Clause) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND Unicode-3.0 AND (Unlicense OR MIT)
URL:            https://mise.jdx.dev/

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%license src/assets/bash_zsh_support/LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/mise
%_mandir/man1/mise.1.gz


%package -n %crate-bash-completion
Summary:        Bash completion for %crate
Requires:       %{crate} = %{version}-%{release}
Requires:       bash-completion
Supplements:    (%{crate} and bash-completion)

%description -n %crate-bash-completion
Bash command line completion support for %{crate}.

%package -n %crate-fish-completion
Summary:        Fish completion for %{crate}
Requires:       %{crate} = %{version}-%{release}
Requires:       fish
Supplements:    (%{crate} and fish)

%description -n %crate-fish-completion
Fish command line completion support for %{crate}.

%package -n %crate-zsh-completion
Summary:        Zsh completion for %{crate}
Requires:       %{crate} = %{version}-%{release}
Requires:       zsh
Supplements:    (%{crate} and zsh)

%description -n %crate-zsh-completion
Zsh command line completion support for %{crate}.


%files -n %crate-bash-completion
%bash_completions_dir/mise.bash

%files -n %crate-fish-completion
%fish_completions_dir/mise.fish

%files -n %crate-zsh-completion
%zsh_completions_dir/_mise


%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep_online

%build
%{cargo_license_summary_online}
%{cargo_license_online} > LICENSE.dependencies

%install
%cargo_install
install -Dm644 %SOURCE1 %buildroot%_mandir/man1/mise.1
install -Dm644 %SOURCE2 %buildroot%bash_completions_dir/mise.bash
install -Dm644 %SOURCE3 %buildroot%fish_completions_dir/mise.fish
install -Dm644 %SOURCE4 %buildroot%zsh_completions_dir/_mise

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Fri Dec 20 2024 madonuko <mado@fyralabs.com> - 2024.12.14-1
- Initial package
