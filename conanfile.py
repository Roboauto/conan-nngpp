import os
from conans import ConanFile

class NngppConan(ConanFile):
    name = "nngpp"
    version = "0.0.1"
    sha = "3351f54e6e774505d8d8b88064d04eb98e0b1cda"
    source_folder = "source"
    license = "MIT"
    url = "https://git.artin.cz/jan.bartusek/conan-nngpp"
    description = "nngpp conan receipe with nng roboauto dependency"
    requires = "nng/1.1.1@roboauto/stable"

    def source(self):
        self.run("git clone https://github.com/cwzx/nngpp.git " + self.source_folder)
        self.run("cd %s && git checkout %s" % (self.source_folder, self.sha))

    def package(self):
        self.copy("*.h")

    def package_info(self):
        self.cpp_info.includedirs = [os.path.join(self.source_folder, "include")]