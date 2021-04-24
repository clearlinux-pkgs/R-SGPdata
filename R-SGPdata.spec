#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-SGPdata
Version  : 25.0.0.0
Release  : 24
URL      : https://cran.r-project.org/src/contrib/SGPdata_25.0-0.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/SGPdata_25.0-0.0.tar.gz
Summary  : Exemplar Data Sets for Student Growth Percentiles (SGP) Analyses
Group    : Development/Tools
License  : GPL-3.0
Requires: R-crayon
Requires: R-data.table
Requires: R-toOrdinal
BuildRequires : R-crayon
BuildRequires : R-data.table
BuildRequires : R-toOrdinal
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n SGPdata
cd %{_builddir}/SGPdata

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1618845726

%install
export SOURCE_DATE_EPOCH=1618845726
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library SGPdata
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library SGPdata
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library SGPdata
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc SGPdata || :


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
