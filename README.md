# CoinCore
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fmnaamani%2Fcoincore-cpp.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fmnaamani%2Fcoincore-cpp?ref=badge_shield)


The core crypto library ported from [mSIGNA](https://github.com/ciphrex/mSIGNA) for managing bitcoin data structures.

conan package name: `CoinCore/0.1.2@joystream/stable`

### Dependencies

This library, has *immediate* dependencies

- Boost
- OpenSSL

and they are managed using [Conan](https://conan.io), a platform and build system agnostic C++ package manager.

### Example Usage

When working with a local copy of the sources, the simplest way is to export the package to the testing channel, `CoinCore/0.0.0@joystream/testing`. Inside the `conan_package/` directory, run the test_package command, this will export and do a test build of the package:

```
conan test_package
```

Next we need to install the library and it's dependencies into our consuming project. Move into the `example/` directory and run:

```
conan install ./ --build=missing
```

This will produce an appropriate `conanbuildinfo.cmake` file, used in the building of the library itself, which is used in the example
project CMakeLists.txt to find the library. Now we can build our project:

```
cmake .
cmake --build .
```

And finally run the built example:
```
bin/keygen
```


### Credits

CoinCore library is Copyright (c) 2013-2017 Ciphrex Corporation

### Disclaimer

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.


## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fmnaamani%2Fcoincore-cpp.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fmnaamani%2Fcoincore-cpp?ref=badge_large)