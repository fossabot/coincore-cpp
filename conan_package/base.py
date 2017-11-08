from conans import ConanFile, CMake, tools
import os

class CoinCoreBase(ConanFile):
    name = "CoinCore"
    version="0.1.1"
    url = "https://github.com/JoyStream/coincore-cpp.git"
    repo_https_url = "https://github.com/JoyStream/coincore-cpp.git"
    repo_ssh_url = "git@github.com:JoyStream/coincore-cpp.git"

    # mSIGNA CoinCore license
    license = '''
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
    '''
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    build_policy = "missing"
    requires = "Boost/1.60.0@lasote/stable" , "OpenSSL/1.0.2j@lasote/stable"

    def source(self):
        raise Exception("abstract base package was exported")

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake repo/sources %s' % (cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="repo/sources/include/")
        self.copy("*.h", dst="include/CoinCore", src="repo/sources/src/")
        self.copy("*.h", dst="include/CoinCore/hashfunc/", src="repo/sources/src/hashfunc")
        self.copy("*.h", dst="include/CoinCore/scrypt/", src="repo/sources/src/scrypt")
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["CoinCore"]

        if str(self.settings.compiler) != "Visual Studio":
            self.cpp_info.cppflags.append("-std=c++11")
