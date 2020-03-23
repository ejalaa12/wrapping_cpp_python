project(swig_cpp_py_wrapper)
cmake_minimum_required(VERSION 3.10)

find_package(SWIG REQUIRED)
include(${SWIG_USE_FILE})

find_package(PythonLibs)
include_directories(${PYTHON_INCLUDE_PATH})

include_directories(${CMAKE_CURRENT_SOURCE_DIR})

set(CMAKE_SWIG_FLAGS "")

# set_source_files_properties(swigdemo.i PROPERTIES CPLUSPLUS ON)
# set_source_files_properties(swigdemo.i PROPERTIES SWIG_FLAGS "-includeall")
# swig_add_module(hello python swigdemo.i hello.c)
SWIG_ADD_LIBRARY(hello
  TYPE SHARED
  LANGUAGE python
  SOURCES swigdemo.i hello.c
)
swig_link_libraries(hello ${PYTHON_LIBRARIES})
