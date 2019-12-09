INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_ADD_VECTOR add_vector)

FIND_PATH(
    ADD_VECTOR_INCLUDE_DIRS
    NAMES add_vector/api.h
    HINTS $ENV{ADD_VECTOR_DIR}/include
        ${PC_ADD_VECTOR_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    ADD_VECTOR_LIBRARIES
    NAMES gnuradio-add_vector
    HINTS $ENV{ADD_VECTOR_DIR}/lib
        ${PC_ADD_VECTOR_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(ADD_VECTOR DEFAULT_MSG ADD_VECTOR_LIBRARIES ADD_VECTOR_INCLUDE_DIRS)
MARK_AS_ADVANCED(ADD_VECTOR_LIBRARIES ADD_VECTOR_INCLUDE_DIRS)

