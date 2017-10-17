from conans import ConanFile, tools, os

class WebsocketPPConan(ConanFile):
    name = "websocketpp"
    version = "0.7.0"
    url = "https://github.com/bincrafters/conan-websocketpp"
    description = "Header only C++ library that implements RFC6455 The WebSocket Protocol"
    license = "https://github.com/zaphoyd/websocketpp/blob/master/COPYING"

    def requirements(self):
        self.requires.add("OpenSSL/1.0.2l@conan/stable")
        self.requires.add("zlib/1.2.11@conan/stable")
        self.requires.add("Boost.Random/[>1.64.0]@%s/%s" % (self.user, self.channel))
        self.requires.add("Boost.Random/[>1.64.0]@%s/%s" % (self.user, self.channel))
        self.requires.add("Boost.System/[>1.64.0]@%s/%s" % (self.user, self.channel))
        self.requires.add("Boost.Thread/[>1.64.0]@%s/%s" % (self.user, self.channel))
        self.requires.add("Boost.Asio/[>1.64.0]@%s/%s" % (self.user, self.channel))
                      
    def source(self):
        source_url = "https://github.com/zaphoyd/websocketpp"
        tools.get("{0}/archive/{1}.tar.gz".format(source_url, self.version))

    def package(self):
        include_dir = os.path.join("{0}-{1}".format(self.name, self.version), self.name)
        self.copy(pattern="*", dst="include", src=include_dir)		

    def package_id(self):
        self.info.header_only()