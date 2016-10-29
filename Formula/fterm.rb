require 'formula'

class Fterm < Formula
  homepage 'https://github.com/lschumm/homebrew-fterm/'
  url 'https://github.com/lschumm/homebrew-fterm.git'

  version "3.0.0"
  
  depends_on "xz"
  depends_on "pxz"
  depends_on "openssl"
  depends_on "thefuck"
  depends_on "htop"
  
  def install
     inreplace "lib/misc.py", "{VERSION}", "3.0.0"
     bin.install 'f'
     bin.install 'f-i'
     bin.install 'parser.py'
     bin.install 'load.py'
     bin.install 'lib'
     system "mkdir ~/.fterm"
     puts "For the best experience, we recommend you use a terminal with auto-complete, such as fish (fish.sh) or zsh (zsh.org)."
  end
end
