class Zapcore < Formula
  desc "File management for humans."
  homepage "github.com/lschumm/zapcore"
  url "https://github.com/lschumm/zapcore/archive/v0.40.tar.gz"
  sha256 "b28f49a6c99af3a82364226ec251d157c0def4e1bcc199168f7d31635aa4a0c4"
  depends_on "openssl" #openSSL encryption
  depends_on "pngcrush" #PNG huffman table optimization
  depends_on "jpegoptim" #JPEG huffman table + lossy optimization
  depends_on "ffmpeg" #video bitrate limiting
  depends_on "pngquant" #PNG lossy compression
  depends_on "ghostscript" #PDF to Postscript
  def install
    bin.install "zap"
  end
end
