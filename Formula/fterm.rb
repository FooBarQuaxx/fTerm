require 'formula'

class Fterm < Formula
  homepage 'https://github.com/lschumm/homebrew-fTerm/'
  url 'https://github.com/lschumm/homebrew-fTerm.git'
  version '0.0.2a5'

  depends_on "xz"
  depends_on "pxz"
  depends_on "openssl"

  def install
     bin.install 'f'
     bin.install 'f-i'
     bin.install 'load.py'
     bin.install 'lib'
     puts "For the best experience, we recommend you use a terminal with auto-complete, such as fish (fish.sh) or zsh (zsh.org)."
     sleep(5)
  end
end
