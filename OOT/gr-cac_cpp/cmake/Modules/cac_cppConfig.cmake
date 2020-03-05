INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_CAC_CPP cac_cpp)

FIND_PATH(
    CAC_CPP_INCLUDE_DIRS
    NAMES cac_cpp/api.h
    HINTS $ENV{CAC_CPP_DIR}/include
        ${PC_CAC_CPP_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    CAC_CPP_LIBRARIES
    NAMES gnuradio-cac_cpp
    HINTS $ENV{CAC_CPP_DIR}/lib
        ${PC_CAC_CPP_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(CAC_CPP DEFAULT_MSG CAC_CPP_LIBRARIES CAC_CPP_INCLUDE_DIRS)
MARK_AS_ADVANCED(CAC_CPP_LIBRARIES CAC_CPP_INCLUDE_DIRS)

