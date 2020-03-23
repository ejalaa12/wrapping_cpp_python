all:
	swig -python -c++ -o _swigdemo_module.cc swigdemo.i
	python setup.py build_ext --inplace
clean:
	rm _swigdemo_module.cc _swigdemo.so swigdemo.py swigdemo.pyc
	rm -rf build
