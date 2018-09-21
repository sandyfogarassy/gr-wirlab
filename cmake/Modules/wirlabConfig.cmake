INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_WIRLAB wirlab)

FIND_PATH(
    WIRLAB_INCLUDE_DIRS
    NAMES wirlab/api.h
    HINTS $ENV{WIRLAB_DIR}/include
        ${PC_WIRLAB_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    WIRLAB_LIBRARIES
    NAMES gnuradio-wirlab
    HINTS $ENV{WIRLAB_DIR}/lib
        ${PC_WIRLAB_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(WIRLAB DEFAULT_MSG WIRLAB_LIBRARIES WIRLAB_INCLUDE_DIRS)
MARK_AS_ADVANCED(WIRLAB_LIBRARIES WIRLAB_INCLUDE_DIRS)

