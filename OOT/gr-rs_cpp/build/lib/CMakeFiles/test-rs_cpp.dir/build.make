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
CMAKE_SOURCE_DIR = /home/andre/investigacao/OOT/gr-rs_cpp

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/andre/investigacao/OOT/gr-rs_cpp/build

# Include any dependencies generated for this target.
include lib/CMakeFiles/test-rs_cpp.dir/depend.make

# Include the progress variables for this target.
include lib/CMakeFiles/test-rs_cpp.dir/progress.make

# Include the compile flags for this target's objects.
include lib/CMakeFiles/test-rs_cpp.dir/flags.make

lib/CMakeFiles/test-rs_cpp.dir/test_rs_cpp.cc.o: lib/CMakeFiles/test-rs_cpp.dir/flags.make
lib/CMakeFiles/test-rs_cpp.dir/test_rs_cpp.cc.o: ../lib/test_rs_cpp.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/andre/investigacao/OOT/gr-rs_cpp/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object lib/CMakeFiles/test-rs_cpp.dir/test_rs_cpp.cc.o"
	cd /home/andre/investigacao/OOT/gr-rs_cpp/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/test-rs_cpp.dir/test_rs_cpp.cc.o -c /home/andre/investigacao/OOT/gr-rs_cpp/lib/test_rs_cpp.cc

lib/CMakeFiles/test-rs_cpp.dir/test_rs_cpp.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/test-rs_cpp.dir/test_rs_cpp.cc.i"
	cd /home/andre/investigacao/OOT/gr-rs_cpp/build/lib && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/andre/investigacao/OOT/gr-rs_cpp/lib/test_rs_cpp.cc > CMakeFiles/test-rs_cpp.dir/test_rs_cpp.cc.i

lib/CMakeFiles/test-rs_cpp.dir/test_rs_cpp.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/test-rs_cpp.dir/test_rs_cpp.cc.s"
	cd /home/andre/investigacao/OOT/gr-rs_cpp/build/lib && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/andre/investigacao/OOT/gr-rs_cpp/lib/test_rs_cpp.cc -o CMakeFiles/test-rs_cpp.dir/test_rs_cpp.cc.s

lib/CMakeFiles/test-rs_cpp.dir/test_rs_cpp.cc.o.requires:

.PHONY : lib/CMakeFiles/test-rs_cpp.dir/test_rs_cpp.cc.o.requires

lib/CMakeFiles/test-rs_cpp.dir/test_rs_cpp.cc.o.provides: lib/CMakeFiles/test-rs_cpp.dir/test_rs_cpp.cc.o.requires
	$(MAKE) -f lib/CMakeFiles/test-rs_cpp.dir/build.make lib/CMakeFiles/test-rs_cpp.dir/test_rs_cpp.cc.o.provides.build
.PHONY : lib/CMakeFiles/test-rs_cpp.dir/test_rs_cpp.cc.o.provides

lib/CMakeFiles/test-rs_cpp.dir/test_rs_cpp.cc.o.provides.build: lib/CMakeFiles/test-rs_cpp.dir/test_rs_cpp.cc.o


lib/CMakeFiles/test-rs_cpp.dir/qa_rs_cpp.cc.o: lib/CMakeFiles/test-rs_cpp.dir/flags.make
lib/CMakeFiles/test-rs_cpp.dir/qa_rs_cpp.cc.o: ../lib/qa_rs_cpp.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/andre/investigacao/OOT/gr-rs_cpp/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object lib/CMakeFiles/test-rs_cpp.dir/qa_rs_cpp.cc.o"
	cd /home/andre/investigacao/OOT/gr-rs_cpp/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/test-rs_cpp.dir/qa_rs_cpp.cc.o -c /home/andre/investigacao/OOT/gr-rs_cpp/lib/qa_rs_cpp.cc

lib/CMakeFiles/test-rs_cpp.dir/qa_rs_cpp.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/test-rs_cpp.dir/qa_rs_cpp.cc.i"
	cd /home/andre/investigacao/OOT/gr-rs_cpp/build/lib && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/andre/investigacao/OOT/gr-rs_cpp/lib/qa_rs_cpp.cc > CMakeFiles/test-rs_cpp.dir/qa_rs_cpp.cc.i

lib/CMakeFiles/test-rs_cpp.dir/qa_rs_cpp.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/test-rs_cpp.dir/qa_rs_cpp.cc.s"
	cd /home/andre/investigacao/OOT/gr-rs_cpp/build/lib && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/andre/investigacao/OOT/gr-rs_cpp/lib/qa_rs_cpp.cc -o CMakeFiles/test-rs_cpp.dir/qa_rs_cpp.cc.s

lib/CMakeFiles/test-rs_cpp.dir/qa_rs_cpp.cc.o.requires:

.PHONY : lib/CMakeFiles/test-rs_cpp.dir/qa_rs_cpp.cc.o.requires

lib/CMakeFiles/test-rs_cpp.dir/qa_rs_cpp.cc.o.provides: lib/CMakeFiles/test-rs_cpp.dir/qa_rs_cpp.cc.o.requires
	$(MAKE) -f lib/CMakeFiles/test-rs_cpp.dir/build.make lib/CMakeFiles/test-rs_cpp.dir/qa_rs_cpp.cc.o.provides.build
.PHONY : lib/CMakeFiles/test-rs_cpp.dir/qa_rs_cpp.cc.o.provides

lib/CMakeFiles/test-rs_cpp.dir/qa_rs_cpp.cc.o.provides.build: lib/CMakeFiles/test-rs_cpp.dir/qa_rs_cpp.cc.o


# Object files for target test-rs_cpp
test__rs_cpp_OBJECTS = \
"CMakeFiles/test-rs_cpp.dir/test_rs_cpp.cc.o" \
"CMakeFiles/test-rs_cpp.dir/qa_rs_cpp.cc.o"

# External object files for target test-rs_cpp
test__rs_cpp_EXTERNAL_OBJECTS =

lib/test-rs_cpp: lib/CMakeFiles/test-rs_cpp.dir/test_rs_cpp.cc.o
lib/test-rs_cpp: lib/CMakeFiles/test-rs_cpp.dir/qa_rs_cpp.cc.o
lib/test-rs_cpp: lib/CMakeFiles/test-rs_cpp.dir/build.make
lib/test-rs_cpp: /usr/local/lib/libgnuradio-runtime.so
lib/test-rs_cpp: /usr/local/lib/libgnuradio-pmt.so
lib/test-rs_cpp: /usr/lib/x86_64-linux-gnu/liblog4cpp.so
lib/test-rs_cpp: /usr/lib/x86_64-linux-gnu/libboost_filesystem.so
lib/test-rs_cpp: /usr/lib/x86_64-linux-gnu/libboost_system.so
lib/test-rs_cpp: /usr/lib/x86_64-linux-gnu/libcppunit.so
lib/test-rs_cpp: lib/libgnuradio-rs_cpp-1.0.0git.so.0.0.0
lib/test-rs_cpp: /usr/local/lib/libgnuradio-runtime.so
lib/test-rs_cpp: /usr/local/lib/libgnuradio-pmt.so
lib/test-rs_cpp: /usr/lib/x86_64-linux-gnu/liblog4cpp.so
lib/test-rs_cpp: /usr/lib/x86_64-linux-gnu/libboost_filesystem.so
lib/test-rs_cpp: /usr/lib/x86_64-linux-gnu/libboost_system.so
lib/test-rs_cpp: lib/CMakeFiles/test-rs_cpp.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/andre/investigacao/OOT/gr-rs_cpp/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable test-rs_cpp"
	cd /home/andre/investigacao/OOT/gr-rs_cpp/build/lib && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/test-rs_cpp.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
lib/CMakeFiles/test-rs_cpp.dir/build: lib/test-rs_cpp

.PHONY : lib/CMakeFiles/test-rs_cpp.dir/build

lib/CMakeFiles/test-rs_cpp.dir/requires: lib/CMakeFiles/test-rs_cpp.dir/test_rs_cpp.cc.o.requires
lib/CMakeFiles/test-rs_cpp.dir/requires: lib/CMakeFiles/test-rs_cpp.dir/qa_rs_cpp.cc.o.requires

.PHONY : lib/CMakeFiles/test-rs_cpp.dir/requires

lib/CMakeFiles/test-rs_cpp.dir/clean:
	cd /home/andre/investigacao/OOT/gr-rs_cpp/build/lib && $(CMAKE_COMMAND) -P CMakeFiles/test-rs_cpp.dir/cmake_clean.cmake
.PHONY : lib/CMakeFiles/test-rs_cpp.dir/clean

lib/CMakeFiles/test-rs_cpp.dir/depend:
	cd /home/andre/investigacao/OOT/gr-rs_cpp/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/andre/investigacao/OOT/gr-rs_cpp /home/andre/investigacao/OOT/gr-rs_cpp/lib /home/andre/investigacao/OOT/gr-rs_cpp/build /home/andre/investigacao/OOT/gr-rs_cpp/build/lib /home/andre/investigacao/OOT/gr-rs_cpp/build/lib/CMakeFiles/test-rs_cpp.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : lib/CMakeFiles/test-rs_cpp.dir/depend

