CMAKE_MINIMUM_REQUIRED(VERSION 2.6)

PROJECT("capi-base-common")
SET(fw_name "capi-base-common")
SET(CMAKE_INSTALL_PREFIX "/usr")
SET(PREFIX ${CMAKE_INSTALL_PREFIX})
SET(VERSION ${FULLVER})
SET(PC_LDFLAGS -l${fw_name})

INSTALL(FILES include/tizen.h DESTINATION include)
INSTALL(FILES include/tizen_error.h DESTINATION include)
INSTALL(FILES include/tizen_type.h DESTINATION include)

INSTALL(FILES ${CMAKE_CURRENT_SOURCE_DIR}/capi-base-common.pc DESTINATION lib/pkgconfig)
SET(INC_DIR include)
INCLUDE_DIRECTORIES(${INC_DIR})

SET(SOURCES
        src/tizen_error.c
)

ADD_LIBRARY(${fw_name} SHARED ${SOURCES})

SET_TARGET_PROPERTIES(${fw_name} PROPERTIES VERSION ${FULLVER})
SET_TARGET_PROPERTIES(${fw_name} PROPERTIES SOVERSION 0)
INSTALL(TARGETS ${fw_name} DESTINATION ${LIB_INSTALL_DIR})
CONFIGURE_FILE(${fw_name}.pc.in ${fw_name}.pc @ONLY)

IF(UNIX)

ADD_CUSTOM_TARGET (distclean @echo cleaning for source distribution)
ADD_CUSTOM_COMMAND(
        DEPENDS clean 
        COMMENT "distribution clean"
        COMMAND find
        ARGS    . 
        -not -name config.cmake -and \(
        -name tester.c -or
        -name Testing -or
        -name CMakeFiles -or
        -name cmake.depends -or
        -name cmake.check_depends -or
        -name CMakeCache.txt -or
        -name cmake.check_cache -or
        -name *.cmake -or
        -name Makefile -or
        -name core -or
        -name core.* -or
        -name gmon.out -or
        -name install_manifest.txt -or
        -name *.pc -or
        -name *~ \)
        | grep -v TC | xargs rm -rf
        TARGET  distclean
        VERBATIM
)

ENDIF(UNIX)
