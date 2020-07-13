#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-gamlss.data
Version  : 5.1.4
Release  : 4
URL      : https://cran.r-project.org/src/contrib/gamlss.data_5.1-4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/gamlss.data_5.1-4.tar.gz
Summary  : GAMLSS Data
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n gamlss.data
cd %{_builddir}/gamlss.data

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589534047

%install
export SOURCE_DATE_EPOCH=1589534047
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gamlss.data
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gamlss.data
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gamlss.data
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc gamlss.data || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/gamlss.data/DESCRIPTION
/usr/lib64/R/library/gamlss.data/INDEX
/usr/lib64/R/library/gamlss.data/Meta/Rd.rds
/usr/lib64/R/library/gamlss.data/Meta/data.rds
/usr/lib64/R/library/gamlss.data/Meta/features.rds
/usr/lib64/R/library/gamlss.data/Meta/hsearch.rds
/usr/lib64/R/library/gamlss.data/Meta/links.rds
/usr/lib64/R/library/gamlss.data/Meta/nsInfo.rds
/usr/lib64/R/library/gamlss.data/Meta/package.rds
/usr/lib64/R/library/gamlss.data/NAMESPACE
/usr/lib64/R/library/gamlss.data/R/gamlss.data
/usr/lib64/R/library/gamlss.data/R/gamlss.data.rdb
/usr/lib64/R/library/gamlss.data/R/gamlss.data.rdx
/usr/lib64/R/library/gamlss.data/data/Rdata.rdb
/usr/lib64/R/library/gamlss.data/data/Rdata.rds
/usr/lib64/R/library/gamlss.data/data/Rdata.rdx
/usr/lib64/R/library/gamlss.data/data/datalist
/usr/lib64/R/library/gamlss.data/help/AnIndex
/usr/lib64/R/library/gamlss.data/help/aliases.rds
/usr/lib64/R/library/gamlss.data/help/gamlss.data.rdb
/usr/lib64/R/library/gamlss.data/help/gamlss.data.rdx
/usr/lib64/R/library/gamlss.data/help/paths.rds
/usr/lib64/R/library/gamlss.data/html/00Index.html
/usr/lib64/R/library/gamlss.data/html/R.css
