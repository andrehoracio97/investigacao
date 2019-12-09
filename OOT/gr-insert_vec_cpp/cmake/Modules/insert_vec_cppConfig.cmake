INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_INSERT_VEC_CPP insert_vec_cpp)

FIND_PATH(
    INSERT_VEC_CPP_INCLUDE_DIRS
    NAMES insert_vec_cpp/api.h
    HINTS $ENV{INSERT_VEC_CPP_DIR}/include
        ${PC_INSERT_VEC_CPP_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    INSERT_VEC_CPP_LIBRARIES
    NAMES gnuradio-insert_vec_cpp
    HINTS $ENV{INSERT_VEC_CPP_DIR}/lib
        ${PC_INSERT_VEC_CPP_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(INSERT_VEC_CPP DEFAULT_MSG INSERT_VEC_CPP_LIBRARIES INSERT_VEC_CPP_INCLUDE_DIRS)
MARK_AS_ADVANCED(INSERT_VEC_CPP_LIBRARIES INSERT_VEC_CPP_INCLUDE_DIRS)

