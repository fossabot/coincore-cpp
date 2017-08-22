PROJECT(PackageTest)
cmake_minimum_required(VERSION 2.8.12)

set(CMAKE_CXX_STANDARD 11)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

ADD_EXECUTABLE(keygen keygen.cpp)

TARGET_LINK_LIBRARIES(keygen ${CONAN_LIBS})
