INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_SCRAMBLER_PACKETS_SAME_SEED scrambler_packets_same_seed)

FIND_PATH(
    SCRAMBLER_PACKETS_SAME_SEED_INCLUDE_DIRS
    NAMES scrambler_packets_same_seed/api.h
    HINTS $ENV{SCRAMBLER_PACKETS_SAME_SEED_DIR}/include
        ${PC_SCRAMBLER_PACKETS_SAME_SEED_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    SCRAMBLER_PACKETS_SAME_SEED_LIBRARIES
    NAMES gnuradio-scrambler_packets_same_seed
    HINTS $ENV{SCRAMBLER_PACKETS_SAME_SEED_DIR}/lib
        ${PC_SCRAMBLER_PACKETS_SAME_SEED_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(SCRAMBLER_PACKETS_SAME_SEED DEFAULT_MSG SCRAMBLER_PACKETS_SAME_SEED_LIBRARIES SCRAMBLER_PACKETS_SAME_SEED_INCLUDE_DIRS)
MARK_AS_ADVANCED(SCRAMBLER_PACKETS_SAME_SEED_LIBRARIES SCRAMBLER_PACKETS_SAME_SEED_INCLUDE_DIRS)

