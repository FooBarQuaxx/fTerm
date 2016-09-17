require 'formula'

class Fterm < Formula
  homepage 'https://github.com/lschumm/homebrew-fTerm/'
  url 'https://github.com/lschumm/homebrew-fTerm.git'

  # sets version variable in fterm code
  # DRY: do not change
  current_version="1.2.0b6"

  depends_on "xz"
  depends_on "pxz"
  depends_on "openssl"
  depends_on "thefuck"
  
  def install
     inreplace "lib/misc.py", "{VERSION}", "1.2.0b6"
     bin.install 'f'
     bin.install 'f-i'
     bin.install 'f-s'
     bin.install 'parser.py'
     bin.install 'load.py'
     bin.install 'lib'
     puts "For the best experience, we recommend you use a terminal with auto-complete, such as fish (fish.sh) or zsh (zsh.org)."
  end
end
