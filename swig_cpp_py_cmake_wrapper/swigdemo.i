%module swigdemo

%{
#include <stdio.h>
#include "hello.h"
%}

%include "hello.c"
