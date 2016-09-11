require 'formula'

class Fterm < Formula
  homepage 'https://github.com/lschumm/homebrew-fTerm/'
  url 'https://github.com/lschumm/homebrew-fTerm.git'
  version '2.0.0b1'

  depends_on "xz"
  depends_on "pxz"
  depends_on "openssl"
  depends_on "thefuck"
  
  def install
     bin.install 'f'
     bin.install 'f-i'
     bin.install 'f-s'
     bin.install 'parser.py'
     bin.install 'load.py'
     bin.install 'lib'
     bin.install 'fterm-packages'
     puts "For the best experience, we recommend you use a terminal with auto-complete, such as fish (fish.sh) or zsh (zsh.org)."
  end
end
