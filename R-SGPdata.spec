#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v16
# autospec commit: b858a2a
#
Name     : R-SGPdata
Version  : 28.0.0.0
Release  : 46
URL      : https://cran.r-project.org/src/contrib/SGPdata_28.0-0.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/SGPdata_28.0-0.0.tar.gz
Summary  : Exemplar Data Sets for Student Growth Percentiles (SGP) Analyses
Group    : Development/Tools
License  : GPL-3.0
Requires: R-crayon
Requires: R-data.table
BuildRequires : R-crayon
BuildRequires : R-data.table
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%prep
%setup -q -n SGPdata
pushd ..
cp -a SGPdata buildavx2
popd
pushd ..
cp -a SGPdata buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1721065379

%install
export SOURCE_DATE_EPOCH=1721065379
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/SGPdata/CITATION
/usr/lib64/R/library/SGPdata/DESCRIPTION
/usr/lib64/R/library/SGPdata/INDEX
/usr/lib64/R/library/SGPdata/Meta/Rd.rds
/usr/lib64/R/library/SGPdata/Meta/data.rds
/usr/lib64/R/library/SGPdata/Meta/features.rds
/usr/lib64/R/library/SGPdata/Meta/hsearch.rds
/usr/lib64/R/library/SGPdata/Meta/links.rds
/usr/lib64/R/library/SGPdata/Meta/nsInfo.rds
/usr/lib64/R/library/SGPdata/Meta/package.rds
/usr/lib64/R/library/SGPdata/Meta/vignette.rds
/usr/lib64/R/library/SGPdata/NAMESPACE
/usr/lib64/R/library/SGPdata/NEWS
/usr/lib64/R/library/SGPdata/R/SGPdata
/usr/lib64/R/library/SGPdata/R/SGPdata.rdb
/usr/lib64/R/library/SGPdata/R/SGPdata.rdx
/usr/lib64/R/library/SGPdata/data/Rdata.rdb
/usr/lib64/R/library/SGPdata/data/Rdata.rds
/usr/lib64/R/library/SGPdata/data/Rdata.rdx
/usr/lib64/R/library/SGPdata/data/datalist
/usr/lib64/R/library/SGPdata/doc/SGPdata.R
/usr/lib64/R/library/SGPdata/doc/SGPdata.Rmd
/usr/lib64/R/library/SGPdata/doc/SGPdata.html
/usr/lib64/R/library/SGPdata/doc/index.html
/usr/lib64/R/library/SGPdata/help/AnIndex
/usr/lib64/R/library/SGPdata/help/SGPdata.rdb
/usr/lib64/R/library/SGPdata/help/SGPdata.rdx
/usr/lib64/R/library/SGPdata/help/aliases.rds
/usr/lib64/R/library/SGPdata/help/paths.rds
/usr/lib64/R/library/SGPdata/html/00Index.html
/usr/lib64/R/library/SGPdata/html/R.css
