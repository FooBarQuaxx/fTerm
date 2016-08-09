require 'formula'

class Fterm < Formula
  homepage 'https://github.com/lschumm/homebrew-fTerm/'
  url 'https://github.com/lschumm/homebrew-fTerm.git'
  version '0.0.2a4'

  # skip_clean 'bin'

  def install
     bin.install 'f'
     bin.install 'f-i'
     bin.install 'load.py'
     bin.install 'core'
     puts "For the best experience, we recommend you use a terminal with auto-complete, such as fish (fish.sh) or zsh (zsh.org)."
     sleep(5)

   #  bin.install 'brew-any-tap.rb'
   #  bin.install 'brew-any-untap.rb'
   #  (bin+'brew-any-tap.rb').chmod 0755
   #  (bin+'brew-any-untap.rb').chmod 0755
  end
end
