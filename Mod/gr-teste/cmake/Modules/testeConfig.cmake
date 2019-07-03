INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_TESTE teste)

FIND_PATH(
    TESTE_INCLUDE_DIRS
    NAMES teste/api.h
    HINTS $ENV{TESTE_DIR}/include
        ${PC_TESTE_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    TESTE_LIBRARIES
    NAMES gnuradio-teste
    HINTS $ENV{TESTE_DIR}/lib
        ${PC_TESTE_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(TESTE DEFAULT_MSG TESTE_LIBRARIES TESTE_INCLUDE_DIRS)
MARK_AS_ADVANCED(TESTE_LIBRARIES TESTE_INCLUDE_DIRS)

