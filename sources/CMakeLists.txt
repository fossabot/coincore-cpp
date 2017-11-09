cmake_minimum_required(VERSION 3.1 FATAL_ERROR)

project(CoinCore CXX)

set(CMAKE_POSITION_INDEPENDENT_CODE ON)
set(CMAKE_CXX_STANDARD 11)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()


#stdutils header library (TEMPORARY - this will be a seperate conan package)
include_directories("${CMAKE_SOURCE_DIR}/include")

#CoinCore header files are in same directory as sources
include_directories("${CMAKE_SOURCE_DIR}/src")

set(
  core_sources
    src/IPv6
    src/CoinNodeData
    src/CoinKey
    src/hdkeys
    src/bip39
    src/BloomFilter
    src/MerkleTree
    src/secp256k1_openssl
    src/aes
    src/StandardTransactions
)

set(
  scrypt_sources
    src/scrypt/scrypt
)

set(
  hashfunc_sources
    src/hashfunc/blake
    src/hashfunc/bmw
    src/hashfunc/groestl
    src/hashfunc/jh
    src/hashfunc/keccak
    src/hashfunc/skein

)

add_library(CoinCore ${core_sources} ${hashfunc_sources} ${scrypt_sources})
