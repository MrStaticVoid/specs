Name:		libffcall
Version:	1.10
Source0:	http://www.haible.de/bruno/gnu/ffcall-%{version}.tar.gz
Patch0:		libffcall-00-install-mkdir.diff

%prep
%setup -q -n ffcall-%{version}
%patch0

%build
export CC="%{cc}"
export CFLAGS="%{optflags}"
export LDFLAGS="%{_ldflags}"
./configure --prefix=%{_prefix} --libdir=%{_libdir} --mandir=%{_mandir} --enable-shared
make %{makeargs}

%install
make DESTDIR=$RPM_BUILD_ROOT %{makeargs} install

%clean
rm -rf $RPM_BUILD_ROOT
