# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

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
CMAKE_COMMAND = /usr/local/bin/cmake

# The command to remove a file.
RM = /usr/local/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The program to use to edit the cache.
CMAKE_EDIT_COMMAND = /usr/local/bin/ccmake

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/sandy/gr-wirlab

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/sandy/gr-wirlab/build

# Utility rule file for wirlab_swig_swig_doc.

# Include the progress variables for this target.
include swig/CMakeFiles/wirlab_swig_swig_doc.dir/progress.make

swig/CMakeFiles/wirlab_swig_swig_doc: swig/wirlab_swig_doc.i

swig/wirlab_swig_doc.i: swig/wirlab_swig_doc_swig_docs/xml/index.xml
	$(CMAKE_COMMAND) -E cmake_progress_report /home/sandy/gr-wirlab/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating python docstrings for wirlab_swig_doc"
	cd /home/sandy/gr-wirlab/docs/doxygen && /usr/bin/python2 -B /home/sandy/gr-wirlab/docs/doxygen/swig_doc.py /home/sandy/gr-wirlab/build/swig/wirlab_swig_doc_swig_docs/xml /home/sandy/gr-wirlab/build/swig/wirlab_swig_doc.i

swig/wirlab_swig_doc_swig_docs/xml/index.xml: swig/_wirlab_swig_doc_tag
	$(CMAKE_COMMAND) -E cmake_progress_report /home/sandy/gr-wirlab/build/CMakeFiles $(CMAKE_PROGRESS_2)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating doxygen xml for wirlab_swig_doc docs"
	cd /home/sandy/gr-wirlab/build/swig && ./_wirlab_swig_doc_tag
	cd /home/sandy/gr-wirlab/build/swig && /usr/bin/doxygen /home/sandy/gr-wirlab/build/swig/wirlab_swig_doc_swig_docs/Doxyfile

wirlab_swig_swig_doc: swig/CMakeFiles/wirlab_swig_swig_doc
wirlab_swig_swig_doc: swig/wirlab_swig_doc.i
wirlab_swig_swig_doc: swig/wirlab_swig_doc_swig_docs/xml/index.xml
wirlab_swig_swig_doc: swig/CMakeFiles/wirlab_swig_swig_doc.dir/build.make
.PHONY : wirlab_swig_swig_doc

# Rule to build all files generated by this target.
swig/CMakeFiles/wirlab_swig_swig_doc.dir/build: wirlab_swig_swig_doc
.PHONY : swig/CMakeFiles/wirlab_swig_swig_doc.dir/build

swig/CMakeFiles/wirlab_swig_swig_doc.dir/clean:
	cd /home/sandy/gr-wirlab/build/swig && $(CMAKE_COMMAND) -P CMakeFiles/wirlab_swig_swig_doc.dir/cmake_clean.cmake
.PHONY : swig/CMakeFiles/wirlab_swig_swig_doc.dir/clean

swig/CMakeFiles/wirlab_swig_swig_doc.dir/depend:
	cd /home/sandy/gr-wirlab/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/sandy/gr-wirlab /home/sandy/gr-wirlab/swig /home/sandy/gr-wirlab/build /home/sandy/gr-wirlab/build/swig /home/sandy/gr-wirlab/build/swig/CMakeFiles/wirlab_swig_swig_doc.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : swig/CMakeFiles/wirlab_swig_swig_doc.dir/depend

