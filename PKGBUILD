
pkgname="logibt-linux-fn-conf"
_pkgname="logibt-linux-fn-conf"
pkgver=12.da29e52
pkgrel=1
pkgdesc="Logitech BT Keyboard Configurator, change function keys (F-keys) behavior. Read USAGE at https://aur.archlinux.org/cgit/aur.git/tree/README.md?h=logibt-linux-fn-conf"
arch=("i686" "x86_64")
url="http://www.trial-n-error.de/posts/2012/12/31/logitech-k810-keyboard-configurator"
license=("Unkown")
makedepends=('git')
backup=("etc/udev/rules.d/00-logibt_conf.rules")
provides=('logibt_conf')
source=("$pkgname"::'git+https://github.com/nos1609/logibt-linux-fn-conf.git')
md5sums=('SKIP')

pkgver() {
cd "$srcdir/${pkgname}"
printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
cd "$srcdir/${pkgname}"
./build.sh
}

package() {
cd "$srcdir/${pkgname}"

install -D -m755 logibt_conf "$pkgdir/usr/bin/logibt_conf"
install -D -m644 00-logibt_conf.rules "$pkgdir/etc/udev/rules.d/00-logibt_conf.rules"
}

# vim:set ts=2 sw=2 et: 
