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
CMAKE_SOURCE_DIR = /home/it/investigacao/OOT/gr-insert_vec_cpp

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/it/investigacao/OOT/gr-insert_vec_cpp/b

# Include any dependencies generated for this target.
include swig/CMakeFiles/_insert_vec_cpp_swig_doc_tag.dir/depend.make

# Include the progress variables for this target.
include swig/CMakeFiles/_insert_vec_cpp_swig_doc_tag.dir/progress.make

# Include the compile flags for this target's objects.
include swig/CMakeFiles/_insert_vec_cpp_swig_doc_tag.dir/flags.make

swig/CMakeFiles/_insert_vec_cpp_swig_doc_tag.dir/_insert_vec_cpp_swig_doc_tag.cpp.o: swig/CMakeFiles/_insert_vec_cpp_swig_doc_tag.dir/flags.make
swig/CMakeFiles/_insert_vec_cpp_swig_doc_tag.dir/_insert_vec_cpp_swig_doc_tag.cpp.o: swig/_insert_vec_cpp_swig_doc_tag.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/it/investigacao/OOT/gr-insert_vec_cpp/b/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object swig/CMakeFiles/_insert_vec_cpp_swig_doc_tag.dir/_insert_vec_cpp_swig_doc_tag.cpp.o"
	cd /home/it/investigacao/OOT/gr-insert_vec_cpp/b/swig && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/_insert_vec_cpp_swig_doc_tag.dir/_insert_vec_cpp_swig_doc_tag.cpp.o -c /home/it/investigacao/OOT/gr-insert_vec_cpp/b/swig/_insert_vec_cpp_swig_doc_tag.cpp

swig/CMakeFiles/_insert_vec_cpp_swig_doc_tag.dir/_insert_vec_cpp_swig_doc_tag.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/_insert_vec_cpp_swig_doc_tag.dir/_insert_vec_cpp_swig_doc_tag.cpp.i"
	cd /home/it/investigacao/OOT/gr-insert_vec_cpp/b/swig && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/it/investigacao/OOT/gr-insert_vec_cpp/b/swig/_insert_vec_cpp_swig_doc_tag.cpp > CMakeFiles/_insert_vec_cpp_swig_doc_tag.dir/_insert_vec_cpp_swig_doc_tag.cpp.i

swig/CMakeFiles/_insert_vec_cpp_swig_doc_tag.dir/_insert_vec_cpp_swig_doc_tag.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/_insert_vec_cpp_swig_doc_tag.dir/_insert_vec_cpp_swig_doc_tag.cpp.s"
	cd /home/it/investigacao/OOT/gr-insert_vec_cpp/b/swig && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/it/investigacao/OOT/gr-insert_vec_cpp/b/swig/_insert_vec_cpp_swig_doc_tag.cpp -o CMakeFiles/_insert_vec_cpp_swig_doc_tag.dir/_insert_vec_cpp_swig_doc_tag.cpp.s

swig/CMakeFiles/_insert_vec_cpp_swig_doc_tag.dir/_insert_vec_cpp_swig_doc_tag.cpp.o.requires:

.PHONY : swig/CMakeFiles/_insert_vec_cpp_swig_doc_tag.dir/_insert_vec_cpp_swig_doc_tag.cpp.o.requires

swig/CMakeFiles/_insert_vec_cpp_swig_doc_tag.dir/_insert_vec_cpp_swig_doc_tag.cpp.o.provides: swig/CMakeFiles/_insert_vec_cpp_swig_doc_tag.dir/_insert_vec_cpp_swig_doc_tag.cpp.o.requires
	$(MAKE) -f swig/CMakeFiles/_insert_vec_cpp_swig_doc_tag.dir/build.make swig/CMakeFiles/_insert_vec_cpp_swig_doc_tag.dir/_insert_vec_cpp_swig_doc_tag.cpp.o.provides.build
.PHONY : swig/CMakeFiles/_insert_vec_cpp_swig_doc_tag.dir/_insert_vec_cpp_swig_doc_tag.cpp.o.provides

swig/CMakeFiles/_insert_vec_cpp_swig_doc_tag.dir/_insert_vec_cpp_swig_doc_tag.cpp.o.provides.build: swig/CMakeFiles/_insert_vec_cpp_swig_doc_tag.dir/_insert_vec_cpp_swig_doc_tag.cpp.o


# Object files for target _insert_vec_cpp_swig_doc_tag
_insert_vec_cpp_swig_doc_tag_OBJECTS = \
"CMakeFiles/_insert_vec_cpp_swig_doc_tag.dir/_insert_vec_cpp_swig_doc_tag.cpp.o"

# External object files for target _insert_vec_cpp_swig_doc_tag
_insert_vec_cpp_swig_doc_tag_EXTERNAL_OBJECTS =

swig/_insert_vec_cpp_swig_doc_tag: swig/CMakeFiles/_insert_vec_cpp_swig_doc_tag.dir/_insert_vec_cpp_swig_doc_tag.cpp.o
swig/_insert_vec_cpp_swig_doc_tag: swig/CMakeFiles/_insert_vec_cpp_swig_doc_tag.dir/build.make
swig/_insert_vec_cpp_swig_doc_tag: swig/CMakeFiles/_insert_vec_cpp_swig_doc_tag.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/it/investigacao/OOT/gr-insert_vec_cpp/b/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable _insert_vec_cpp_swig_doc_tag"
	cd /home/it/investigacao/OOT/gr-insert_vec_cpp/b/swig && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/_insert_vec_cpp_swig_doc_tag.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
swig/CMakeFiles/_insert_vec_cpp_swig_doc_tag.dir/build: swig/_insert_vec_cpp_swig_doc_tag

.PHONY : swig/CMakeFiles/_insert_vec_cpp_swig_doc_tag.dir/build

swig/CMakeFiles/_insert_vec_cpp_swig_doc_tag.dir/requires: swig/CMakeFiles/_insert_vec_cpp_swig_doc_tag.dir/_insert_vec_cpp_swig_doc_tag.cpp.o.requires

.PHONY : swig/CMakeFiles/_insert_vec_cpp_swig_doc_tag.dir/requires

swig/CMakeFiles/_insert_vec_cpp_swig_doc_tag.dir/clean:
	cd /home/it/investigacao/OOT/gr-insert_vec_cpp/b/swig && $(CMAKE_COMMAND) -P CMakeFiles/_insert_vec_cpp_swig_doc_tag.dir/cmake_clean.cmake
.PHONY : swig/CMakeFiles/_insert_vec_cpp_swig_doc_tag.dir/clean

swig/CMakeFiles/_insert_vec_cpp_swig_doc_tag.dir/depend:
	cd /home/it/investigacao/OOT/gr-insert_vec_cpp/b && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/it/investigacao/OOT/gr-insert_vec_cpp /home/it/investigacao/OOT/gr-insert_vec_cpp/swig /home/it/investigacao/OOT/gr-insert_vec_cpp/b /home/it/investigacao/OOT/gr-insert_vec_cpp/b/swig /home/it/investigacao/OOT/gr-insert_vec_cpp/b/swig/CMakeFiles/_insert_vec_cpp_swig_doc_tag.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : swig/CMakeFiles/_insert_vec_cpp_swig_doc_tag.dir/depend

