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
CMAKE_SOURCE_DIR = /home/andre/investigacao/OOT/gr-insert_vec_cpp

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/andre/investigacao/OOT/gr-insert_vec_cpp/build

# Include any dependencies generated for this target.
include swig/CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/depend.make

# Include the progress variables for this target.
include swig/CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/progress.make

# Include the compile flags for this target's objects.
include swig/CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/flags.make

swig/insert_vec_cpp_swig_swig_2d0df.cpp: ../swig/insert_vec_cpp_swig.i
swig/insert_vec_cpp_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/tagged_stream_block.i
swig/insert_vec_cpp_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/gnuradio.i
swig/insert_vec_cpp_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/realtime.i
swig/insert_vec_cpp_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/block.i
swig/insert_vec_cpp_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/block_detail.i
swig/insert_vec_cpp_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/constants.i
swig/insert_vec_cpp_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/sync_block.i
swig/insert_vec_cpp_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/gr_shared_ptr.i
swig/insert_vec_cpp_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/block_gateway.i
swig/insert_vec_cpp_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/sync_interpolator.i
swig/insert_vec_cpp_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/gr_types.i
swig/insert_vec_cpp_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/basic_block.i
swig/insert_vec_cpp_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/gr_ctrlport.i
swig/insert_vec_cpp_swig_swig_2d0df.cpp: ../swig/insert_vec_cpp_swig.i
swig/insert_vec_cpp_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/io_signature.i
swig/insert_vec_cpp_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/top_block.i
swig/insert_vec_cpp_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/gr_extras.i
swig/insert_vec_cpp_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/message.i
swig/insert_vec_cpp_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/tags.i
swig/insert_vec_cpp_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/msg_handler.i
swig/insert_vec_cpp_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/runtime_swig.i
swig/insert_vec_cpp_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/msg_queue.i
swig/insert_vec_cpp_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/buffer.i
swig/insert_vec_cpp_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/gr_swig_block_magic.i
swig/insert_vec_cpp_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/hier_block2.i
swig/insert_vec_cpp_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/runtime_swig_doc.i
swig/insert_vec_cpp_swig_swig_2d0df.cpp: swig/insert_vec_cpp_swig_doc.i
swig/insert_vec_cpp_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/feval.i
swig/insert_vec_cpp_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/sync_decimator.i
swig/insert_vec_cpp_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/gr_logger.i
swig/insert_vec_cpp_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/prefs.i
swig/insert_vec_cpp_swig_swig_2d0df.cpp: swig/insert_vec_cpp_swig.tag
	cd /home/andre/investigacao/OOT/gr-insert_vec_cpp/build/swig && /usr/bin/cmake -E copy /home/andre/investigacao/OOT/gr-insert_vec_cpp/build/swig/insert_vec_cpp_swig_swig_2d0df.cpp.in /home/andre/investigacao/OOT/gr-insert_vec_cpp/build/swig/insert_vec_cpp_swig_swig_2d0df.cpp

swig/insert_vec_cpp_swig_doc.i: swig/insert_vec_cpp_swig_doc_swig_docs/xml/index.xml
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/andre/investigacao/OOT/gr-insert_vec_cpp/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating python docstrings for insert_vec_cpp_swig_doc"
	cd /home/andre/investigacao/OOT/gr-insert_vec_cpp/docs/doxygen && /usr/bin/python2 -B /home/andre/investigacao/OOT/gr-insert_vec_cpp/docs/doxygen/swig_doc.py /home/andre/investigacao/OOT/gr-insert_vec_cpp/build/swig/insert_vec_cpp_swig_doc_swig_docs/xml /home/andre/investigacao/OOT/gr-insert_vec_cpp/build/swig/insert_vec_cpp_swig_doc.i

swig/insert_vec_cpp_swig.tag: swig/_insert_vec_cpp_swig_swig_tag
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/andre/investigacao/OOT/gr-insert_vec_cpp/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Generating insert_vec_cpp_swig.tag"
	cd /home/andre/investigacao/OOT/gr-insert_vec_cpp/build/swig && ./_insert_vec_cpp_swig_swig_tag
	cd /home/andre/investigacao/OOT/gr-insert_vec_cpp/build/swig && /usr/bin/cmake -E touch /home/andre/investigacao/OOT/gr-insert_vec_cpp/build/swig/insert_vec_cpp_swig.tag

swig/insert_vec_cpp_swig_doc_swig_docs/xml/index.xml: swig/_insert_vec_cpp_swig_doc_tag
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/andre/investigacao/OOT/gr-insert_vec_cpp/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Generating doxygen xml for insert_vec_cpp_swig_doc docs"
	cd /home/andre/investigacao/OOT/gr-insert_vec_cpp/build/swig && ./_insert_vec_cpp_swig_doc_tag
	cd /home/andre/investigacao/OOT/gr-insert_vec_cpp/build/swig && /usr/bin/doxygen /home/andre/investigacao/OOT/gr-insert_vec_cpp/build/swig/insert_vec_cpp_swig_doc_swig_docs/Doxyfile

swig/CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/insert_vec_cpp_swig_swig_2d0df.cpp.o: swig/CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/flags.make
swig/CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/insert_vec_cpp_swig_swig_2d0df.cpp.o: swig/insert_vec_cpp_swig_swig_2d0df.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/andre/investigacao/OOT/gr-insert_vec_cpp/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building CXX object swig/CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/insert_vec_cpp_swig_swig_2d0df.cpp.o"
	cd /home/andre/investigacao/OOT/gr-insert_vec_cpp/build/swig && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/insert_vec_cpp_swig_swig_2d0df.cpp.o -c /home/andre/investigacao/OOT/gr-insert_vec_cpp/build/swig/insert_vec_cpp_swig_swig_2d0df.cpp

swig/CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/insert_vec_cpp_swig_swig_2d0df.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/insert_vec_cpp_swig_swig_2d0df.cpp.i"
	cd /home/andre/investigacao/OOT/gr-insert_vec_cpp/build/swig && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/andre/investigacao/OOT/gr-insert_vec_cpp/build/swig/insert_vec_cpp_swig_swig_2d0df.cpp > CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/insert_vec_cpp_swig_swig_2d0df.cpp.i

swig/CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/insert_vec_cpp_swig_swig_2d0df.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/insert_vec_cpp_swig_swig_2d0df.cpp.s"
	cd /home/andre/investigacao/OOT/gr-insert_vec_cpp/build/swig && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/andre/investigacao/OOT/gr-insert_vec_cpp/build/swig/insert_vec_cpp_swig_swig_2d0df.cpp -o CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/insert_vec_cpp_swig_swig_2d0df.cpp.s

swig/CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/insert_vec_cpp_swig_swig_2d0df.cpp.o.requires:

.PHONY : swig/CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/insert_vec_cpp_swig_swig_2d0df.cpp.o.requires

swig/CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/insert_vec_cpp_swig_swig_2d0df.cpp.o.provides: swig/CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/insert_vec_cpp_swig_swig_2d0df.cpp.o.requires
	$(MAKE) -f swig/CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/build.make swig/CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/insert_vec_cpp_swig_swig_2d0df.cpp.o.provides.build
.PHONY : swig/CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/insert_vec_cpp_swig_swig_2d0df.cpp.o.provides

swig/CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/insert_vec_cpp_swig_swig_2d0df.cpp.o.provides.build: swig/CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/insert_vec_cpp_swig_swig_2d0df.cpp.o


# Object files for target insert_vec_cpp_swig_swig_2d0df
insert_vec_cpp_swig_swig_2d0df_OBJECTS = \
"CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/insert_vec_cpp_swig_swig_2d0df.cpp.o"

# External object files for target insert_vec_cpp_swig_swig_2d0df
insert_vec_cpp_swig_swig_2d0df_EXTERNAL_OBJECTS =

swig/insert_vec_cpp_swig_swig_2d0df: swig/CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/insert_vec_cpp_swig_swig_2d0df.cpp.o
swig/insert_vec_cpp_swig_swig_2d0df: swig/CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/build.make
swig/insert_vec_cpp_swig_swig_2d0df: swig/CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/andre/investigacao/OOT/gr-insert_vec_cpp/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Linking CXX executable insert_vec_cpp_swig_swig_2d0df"
	cd /home/andre/investigacao/OOT/gr-insert_vec_cpp/build/swig && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/link.txt --verbose=$(VERBOSE)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Swig source"
	cd /home/andre/investigacao/OOT/gr-insert_vec_cpp/build/swig && /usr/bin/cmake -E make_directory /home/andre/investigacao/OOT/gr-insert_vec_cpp/build/swig
	cd /home/andre/investigacao/OOT/gr-insert_vec_cpp/build/swig && /usr/bin/swig3.0 -python -fvirtual -modern -keyword -w511 -module insert_vec_cpp_swig -I/home/andre/investigacao/OOT/gr-insert_vec_cpp/build/swig -I/home/andre/investigacao/OOT/gr-insert_vec_cpp/swig -I/usr/local/include/gnuradio/swig -I/usr/include/python2.7 -I/usr/include/python2.7 -outdir /home/andre/investigacao/OOT/gr-insert_vec_cpp/build/swig -c++ -I/home/andre/investigacao/OOT/gr-insert_vec_cpp/lib -I/home/andre/investigacao/OOT/gr-insert_vec_cpp/include -I/home/andre/investigacao/OOT/gr-insert_vec_cpp/build/lib -I/home/andre/investigacao/OOT/gr-insert_vec_cpp/build/include -I/usr/include -I/usr/include -I/usr/local/include -I/home/andre/investigacao/OOT/gr-insert_vec_cpp/build/swig -I/home/andre/investigacao/OOT/gr-insert_vec_cpp/swig -I/usr/local/include/gnuradio/swig -I/usr/include/python2.7 -I/usr/include/python2.7 -o /home/andre/investigacao/OOT/gr-insert_vec_cpp/build/swig/insert_vec_cpp_swigPYTHON_wrap.cxx /home/andre/investigacao/OOT/gr-insert_vec_cpp/swig/insert_vec_cpp_swig.i

# Rule to build all files generated by this target.
swig/CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/build: swig/insert_vec_cpp_swig_swig_2d0df

.PHONY : swig/CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/build

swig/CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/requires: swig/CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/insert_vec_cpp_swig_swig_2d0df.cpp.o.requires

.PHONY : swig/CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/requires

swig/CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/clean:
	cd /home/andre/investigacao/OOT/gr-insert_vec_cpp/build/swig && $(CMAKE_COMMAND) -P CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/cmake_clean.cmake
.PHONY : swig/CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/clean

swig/CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/depend: swig/insert_vec_cpp_swig_swig_2d0df.cpp
swig/CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/depend: swig/insert_vec_cpp_swig_doc.i
swig/CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/depend: swig/insert_vec_cpp_swig.tag
swig/CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/depend: swig/insert_vec_cpp_swig_doc_swig_docs/xml/index.xml
	cd /home/andre/investigacao/OOT/gr-insert_vec_cpp/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/andre/investigacao/OOT/gr-insert_vec_cpp /home/andre/investigacao/OOT/gr-insert_vec_cpp/swig /home/andre/investigacao/OOT/gr-insert_vec_cpp/build /home/andre/investigacao/OOT/gr-insert_vec_cpp/build/swig /home/andre/investigacao/OOT/gr-insert_vec_cpp/build/swig/CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : swig/CMakeFiles/insert_vec_cpp_swig_swig_2d0df.dir/depend

