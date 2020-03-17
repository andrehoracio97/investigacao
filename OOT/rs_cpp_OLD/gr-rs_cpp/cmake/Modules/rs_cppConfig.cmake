INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_RS_CPP rs_cpp)

FIND_PATH(
    RS_CPP_INCLUDE_DIRS
    NAMES rs_cpp/api.h
    HINTS $ENV{RS_CPP_DIR}/include
        ${PC_RS_CPP_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    RS_CPP_LIBRARIES
    NAMES gnuradio-rs_cpp
    HINTS $ENV{RS_CPP_DIR}/lib
        ${PC_RS_CPP_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(RS_CPP DEFAULT_MSG RS_CPP_LIBRARIES RS_CPP_INCLUDE_DIRS)
MARK_AS_ADVANCED(RS_CPP_LIBRARIES RS_CPP_INCLUDE_DIRS)

