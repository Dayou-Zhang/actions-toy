cmake_minimum_required(VERSION 3.10)

project(FortranLibBuilder LANGUAGES Fortran)

find_package(BLAS REQUIRED)

file(GLOB_RECURSE sources RELATIVE ${CMAKE_SOURCE_DIR} "*_*.f" "*_*.f90")

foreach(source ${sources})
    get_filename_component(dir ${source} DIRECTORY)
    get_filename_component(name ${source} NAME_WE) # NAME without extension

    set(output_dir ${CMAKE_SOURCE_DIR}/${dir})
    set(target_name ${name})

    add_library(${name} SHARED ${source})
    target_link_libraries(${name} PRIVATE ${BLAS_LIBRARIES})

    set_target_properties(${name}
        PROPERTIES
            PREFIX ""
            LIBRARY_OUTPUT_DIRECTORY ${output_dir}
            Fortran_MODULE_DIRECTORY ${output_dir}
    )
endforeach()
