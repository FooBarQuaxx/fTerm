require 'formula'

class Fterm < Formula
  homepage 'https://github.com/lschumm/homebrew-fTerm/'
  url 'https://github.com/lschumm/homebrew-fTerm.git'
  version 'd'

  # skip_clean 'bin'

  def install
     bin.install 'f'
     bin.install 'f-i'
     bin.install 'core.py'
     bin.install 'core'

   #  bin.install 'brew-any-tap.rb'
   #  bin.install 'brew-any-untap.rb'
   #  (bin+'brew-any-tap.rb').chmod 0755
   #  (bin+'brew-any-untap.rb').chmod 0755
  end
end
