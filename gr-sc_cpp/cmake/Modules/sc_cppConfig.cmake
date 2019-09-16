INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_SC_CPP sc_cpp)

FIND_PATH(
    SC_CPP_INCLUDE_DIRS
    NAMES sc_cpp/api.h
    HINTS $ENV{SC_CPP_DIR}/include
        ${PC_SC_CPP_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    SC_CPP_LIBRARIES
    NAMES gnuradio-sc_cpp
    HINTS $ENV{SC_CPP_DIR}/lib
        ${PC_SC_CPP_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(SC_CPP DEFAULT_MSG SC_CPP_LIBRARIES SC_CPP_INCLUDE_DIRS)
MARK_AS_ADVANCED(SC_CPP_LIBRARIES SC_CPP_INCLUDE_DIRS)

