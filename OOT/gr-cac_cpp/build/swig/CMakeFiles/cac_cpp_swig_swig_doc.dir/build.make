# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/andre/investigacao/OOT/gr-cac_cpp

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/andre/investigacao/OOT/gr-cac_cpp/build

# Utility rule file for cac_cpp_swig_swig_doc.

# Include the progress variables for this target.
include swig/CMakeFiles/cac_cpp_swig_swig_doc.dir/progress.make

swig/CMakeFiles/cac_cpp_swig_swig_doc: swig/cac_cpp_swig_doc.i


swig/cac_cpp_swig_doc.i: swig/cac_cpp_swig_doc_swig_docs/xml/index.xml
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/andre/investigacao/OOT/gr-cac_cpp/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating python docstrings for cac_cpp_swig_doc"
	cd /home/andre/investigacao/OOT/gr-cac_cpp/docs/doxygen && /usr/bin/python2 -B /home/andre/investigacao/OOT/gr-cac_cpp/docs/doxygen/swig_doc.py /home/andre/investigacao/OOT/gr-cac_cpp/build/swig/cac_cpp_swig_doc_swig_docs/xml /home/andre/investigacao/OOT/gr-cac_cpp/build/swig/cac_cpp_swig_doc.i

swig/cac_cpp_swig_doc_swig_docs/xml/index.xml: swig/_cac_cpp_swig_doc_tag
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/andre/investigacao/OOT/gr-cac_cpp/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Generating doxygen xml for cac_cpp_swig_doc docs"
	cd /home/andre/investigacao/OOT/gr-cac_cpp/build/swig && ./_cac_cpp_swig_doc_tag
	cd /home/andre/investigacao/OOT/gr-cac_cpp/build/swig && /usr/bin/doxygen /home/andre/investigacao/OOT/gr-cac_cpp/build/swig/cac_cpp_swig_doc_swig_docs/Doxyfile

cac_cpp_swig_swig_doc: swig/CMakeFiles/cac_cpp_swig_swig_doc
cac_cpp_swig_swig_doc: swig/cac_cpp_swig_doc.i
cac_cpp_swig_swig_doc: swig/cac_cpp_swig_doc_swig_docs/xml/index.xml
cac_cpp_swig_swig_doc: swig/CMakeFiles/cac_cpp_swig_swig_doc.dir/build.make

.PHONY : cac_cpp_swig_swig_doc

# Rule to build all files generated by this target.
swig/CMakeFiles/cac_cpp_swig_swig_doc.dir/build: cac_cpp_swig_swig_doc

.PHONY : swig/CMakeFiles/cac_cpp_swig_swig_doc.dir/build

swig/CMakeFiles/cac_cpp_swig_swig_doc.dir/clean:
	cd /home/andre/investigacao/OOT/gr-cac_cpp/build/swig && $(CMAKE_COMMAND) -P CMakeFiles/cac_cpp_swig_swig_doc.dir/cmake_clean.cmake
.PHONY : swig/CMakeFiles/cac_cpp_swig_swig_doc.dir/clean

swig/CMakeFiles/cac_cpp_swig_swig_doc.dir/depend:
	cd /home/andre/investigacao/OOT/gr-cac_cpp/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/andre/investigacao/OOT/gr-cac_cpp /home/andre/investigacao/OOT/gr-cac_cpp/swig /home/andre/investigacao/OOT/gr-cac_cpp/build /home/andre/investigacao/OOT/gr-cac_cpp/build/swig /home/andre/investigacao/OOT/gr-cac_cpp/build/swig/CMakeFiles/cac_cpp_swig_swig_doc.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : swig/CMakeFiles/cac_cpp_swig_swig_doc.dir/depend

