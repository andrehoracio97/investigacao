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
CMAKE_SOURCE_DIR = /home/andre/investigacao/gr-scrambler_packets_same_seed

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/andre/investigacao/gr-scrambler_packets_same_seed/build

# Utility rule file for scrambler_packets_same_seed_swig_swig_doc.

# Include the progress variables for this target.
include swig/CMakeFiles/scrambler_packets_same_seed_swig_swig_doc.dir/progress.make

swig/CMakeFiles/scrambler_packets_same_seed_swig_swig_doc: swig/scrambler_packets_same_seed_swig_doc.i


swig/scrambler_packets_same_seed_swig_doc.i: swig/scrambler_packets_same_seed_swig_doc_swig_docs/xml/index.xml
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/andre/investigacao/gr-scrambler_packets_same_seed/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating python docstrings for scrambler_packets_same_seed_swig_doc"
	cd /home/andre/investigacao/gr-scrambler_packets_same_seed/docs/doxygen && /usr/bin/python2 -B /home/andre/investigacao/gr-scrambler_packets_same_seed/docs/doxygen/swig_doc.py /home/andre/investigacao/gr-scrambler_packets_same_seed/build/swig/scrambler_packets_same_seed_swig_doc_swig_docs/xml /home/andre/investigacao/gr-scrambler_packets_same_seed/build/swig/scrambler_packets_same_seed_swig_doc.i

swig/scrambler_packets_same_seed_swig_doc_swig_docs/xml/index.xml: swig/_scrambler_packets_same_seed_swig_doc_tag
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/andre/investigacao/gr-scrambler_packets_same_seed/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Generating doxygen xml for scrambler_packets_same_seed_swig_doc docs"
	cd /home/andre/investigacao/gr-scrambler_packets_same_seed/build/swig && ./_scrambler_packets_same_seed_swig_doc_tag
	cd /home/andre/investigacao/gr-scrambler_packets_same_seed/build/swig && /usr/bin/doxygen /home/andre/investigacao/gr-scrambler_packets_same_seed/build/swig/scrambler_packets_same_seed_swig_doc_swig_docs/Doxyfile

scrambler_packets_same_seed_swig_swig_doc: swig/CMakeFiles/scrambler_packets_same_seed_swig_swig_doc
scrambler_packets_same_seed_swig_swig_doc: swig/scrambler_packets_same_seed_swig_doc.i
scrambler_packets_same_seed_swig_swig_doc: swig/scrambler_packets_same_seed_swig_doc_swig_docs/xml/index.xml
scrambler_packets_same_seed_swig_swig_doc: swig/CMakeFiles/scrambler_packets_same_seed_swig_swig_doc.dir/build.make

.PHONY : scrambler_packets_same_seed_swig_swig_doc

# Rule to build all files generated by this target.
swig/CMakeFiles/scrambler_packets_same_seed_swig_swig_doc.dir/build: scrambler_packets_same_seed_swig_swig_doc

.PHONY : swig/CMakeFiles/scrambler_packets_same_seed_swig_swig_doc.dir/build

swig/CMakeFiles/scrambler_packets_same_seed_swig_swig_doc.dir/clean:
	cd /home/andre/investigacao/gr-scrambler_packets_same_seed/build/swig && $(CMAKE_COMMAND) -P CMakeFiles/scrambler_packets_same_seed_swig_swig_doc.dir/cmake_clean.cmake
.PHONY : swig/CMakeFiles/scrambler_packets_same_seed_swig_swig_doc.dir/clean

swig/CMakeFiles/scrambler_packets_same_seed_swig_swig_doc.dir/depend:
	cd /home/andre/investigacao/gr-scrambler_packets_same_seed/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/andre/investigacao/gr-scrambler_packets_same_seed /home/andre/investigacao/gr-scrambler_packets_same_seed/swig /home/andre/investigacao/gr-scrambler_packets_same_seed/build /home/andre/investigacao/gr-scrambler_packets_same_seed/build/swig /home/andre/investigacao/gr-scrambler_packets_same_seed/build/swig/CMakeFiles/scrambler_packets_same_seed_swig_swig_doc.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : swig/CMakeFiles/scrambler_packets_same_seed_swig_swig_doc.dir/depend

