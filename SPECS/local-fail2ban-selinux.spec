%global debug_package %{nil}

Name:		local-fail2ban-selinux
Version:	1.0.1
Release:	2%{?dist}
Summary:	Local SELinux fail2ban module 

License:	GPL	
URL:		https://github.com/AcidScorpion
Source0:	%{name}-%{version}.tar.gz

Requires:	policycoreutils	       
BuildArch:	noarch


%description
Local SELinux fail2ban module, so fail2ban can access bind logs and run bash scripts 

%prep
%autosetup

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_tmppath}
install -p -m 0440 local-fail2ban.cil %{buildroot}/%{_tmppath}

%clean
rm -rf %{buildroot}

%files
%{_tmppath}/local-fail2ban.cil

%post
semodule -i %{_tmppath}/local-fail2ban.cil
rm -f %{_tmppath}/local-fail2ban.cil

%preun
touch %{_tmppath}/local-fail2ban.cil

if [ $1 -eq 1 ] ; then
  semodule -r local-fail2ban
fi

%postun
semodule -r local-fail2ban

%changelog
* Fri Mar 29 2024 Acid_Scorpion <dmitry@petrich.me>
- Version: 1.0.1
  (typeattributeset cil_gen_require hostname_exec_t)
  (allow fail2ban_t hostname_exec_t (file (getattr read execute open execute_no_trans map)))

* Fri Mar 29 2024 Acid_Scorpion <dmitry@petrich.me>
- Initial build
