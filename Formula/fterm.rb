require 'formula'

class Fterm < Formula
  homepage 'https://github.com/fterm/fterm/'
  url 'https://github.com/fterm/fterm.git'

  version "2.0.1b1"
  
  depends_on "xz"
  depends_on "pxz"
  depends_on "openssl"
  depends_on "thefuck"
  
  def install
     inreplace "lib/misc.py", "{VERSION}", "2.0.0"
     bin.install 'f'
     bin.install 'f-i'
     bin.install 'parser.py'
     bin.install 'load.py'
     bin.install 'lib'
     system "mkdir ~/.fterm"
     puts "For the best experience, we recommend you use a terminal with auto-complete, such as fish (fish.sh) or zsh (zsh.org)."
  end
end
