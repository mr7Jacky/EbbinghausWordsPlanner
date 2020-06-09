###log error message
```bash
==> Processing plain cmake package: 'cartographer'
==> Creating build directory: 'build_isolated/cartographer/install'
==> Building with env: '/home/lin/ros/catkin_ws/install_isolated/env.sh'
==> cmake /home/lin/ros/catkin_ws/src/cartographer -DCMAKE_INSTALL_PREFIX=/home/lin/ros/catkin_ws/install_isolated -G Ninja in '/home/lin/ros/catkin_ws/build_isolated/cartographer/install'
-- The C compiler identification is GNU 8.3.1
-- The CXX compiler identification is GNU 8.3.1
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Build type: Release
Files /home/lin/ros/catkin_ws/build_isolated/cartographer/install/AllFiles.cmake and - differ
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Looking for pthread_create
-- Looking for pthread_create - not found
-- Looking for pthread_create in pthreads
-- Looking for pthread_create in pthreads - not found
-- Looking for pthread_create in pthread
-- Looking for pthread_create in pthread - found
-- Found Threads: TRUE  
-- Found GMock: /usr/lib64/libgmock_main.so;-lpthread  
-- Boost version: 1.66.0
-- Found the following Boost libraries:
--   iostreams
--   regex
-- Found required Ceres dependency: Eigen version 3.3.7 in /usr/include/eigen3
-- Found required Ceres dependency: glog
-- Found Ceres version: 1.12.0 installed in: /home/lin/ros/catkin_ws/install_isolated with components: [LAPACK, SuiteSparse, SparseLinearAlgebraLibrary, SchurSpecializations, OpenMP]
-- Found Lua: /usr/lib64/liblua-5.3.so;/usr/lib64/libm.so (found version "5.3.5") 
-- Found Protobuf: /usr/lib64/libprotobuf.so;-lpthread (found suitable version "3.5.0", minimum required is "3.0.0") 
-- Found PkgConfig: /usr/bin/pkg-config (found version "1.5.3") 
-- Checking for one of the modules 'cairo>=1.12.16'
-- Found Sphinx: /usr/libexec/python2-sphinx/sphinx-build  
-- Configuring done
-- Generating done
-- Build files have been written to: /home/lin/ros/catkin_ws/build_isolated/cartographer/install
==> ninja -j1 in '/home/lin/ros/catkin_ws/build_isolated/cartographer/install'
ninja: warning: multiple rules generate abseil/src/abseil-build/absl/synchronization/libabsl_synchronization.a. builds involving this target will not be correct; continuing anyway [-w dupbuild=warn]
[3/387] Performing download step (git clone) for 'abseil'
Cloning into 'abseil'...
Note: checking out '7b46e1d31a6b08b1c6da2a13e7b151a20446fa07'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by performing another checkout.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -b with the checkout command again. Example:

  git checkout -b <new-branch-name>

HEAD is now at 7b46e1d Export of internal Abseil changes. -- 07575526242a8e1275ac4223a3d2822795f46569 by CJ Johnson <johnsoncj@google.com>:
[6/387] Performing configure step for 'abseil'
loading initial cache file /home/lin/ros/catkin_ws/build_isolated/cartographer/install/abseil/tmp/abseil-cache-Release.cmake
-- The C compiler identification is GNU 8.3.1
-- The CXX compiler identification is GNU 8.3.1
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Looking for pthread_create
-- Looking for pthread_create - not found
-- Looking for pthread_create in pthreads
-- Looking for pthread_create in pthreads - not found
-- Looking for pthread_create in pthread
-- Looking for pthread_create in pthread - found
-- Found Threads: TRUE  
-- Configuring done
-- Generating done
-- Build files have been written to: /home/lin/ros/catkin_ws/build_isolated/cartographer/install/abseil/src/abseil-build
[7/387] Performing build step for 'abseil'
[1/121] Building CXX object absl/base/CMakeFiles/absl_base.dir/internal/cycleclock.cc.o
[2/121] Building CXX object absl/base/CMakeFiles/absl_base.dir/internal/raw_logging.cc.o
[3/121] Building CXX object absl/base/CMakeFiles/absl_internal_malloc_internal.dir/internal/low_level_alloc.cc.o
[4/121] Building CXX object absl/base/CMakeFiles/absl_base.dir/internal/spinlock.cc.o
[5/121] Building CXX object absl/base/CMakeFiles/absl_base.dir/internal/sysinfo.cc.o
[6/121] Building CXX object absl/base/CMakeFiles/absl_base.dir/internal/unscaledcycleclock.cc.o
[7/121] Building CXX object absl/base/CMakeFiles/absl_base.dir/internal/thread_identity.cc.o
[8/121] Building CXX object absl/base/CMakeFiles/absl_dynamic_annotations.dir/dynamic_annotations.cc.o
[9/121] Linking CXX static library absl/base/libabsl_dynamic_annotations.a
[10/121] Linking CXX static library absl/base/libabsl_internal_malloc_internal.a
[11/121] Building CXX object absl/base/CMakeFiles/absl_base.dir/internal/low_level_alloc.cc.o
[12/121] Building CXX object absl/base/CMakeFiles/absl_internal_throw_delegate.dir/internal/throw_delegate.cc.o
[13/121] Building CXX object absl/algorithm/CMakeFiles/absl_algorithm.dir/absl_algorithm_header_only_dummy.cc.o
[14/121] Linking CXX static library absl/algorithm/libabsl_algorithm.a
[15/121] Building CXX object absl/base/CMakeFiles/absl_internal_spinlock_wait.dir/internal/spinlock_wait.cc.o
[16/121] Linking CXX static library absl/base/libabsl_internal_spinlock_wait.a
[17/121] Linking CXX static library absl/base/libabsl_base.a
[18/121] Linking CXX static library absl/base/libabsl_internal_throw_delegate.a
[19/121] Building CXX object absl/container/CMakeFiles/test_instance_tracker_lib.dir/internal/test_instance_tracker.cc.o
[20/121] Building CXX object absl/container/CMakeFiles/absl_container.dir/internal/raw_hash_set.cc.o
[21/121] Building CXX object absl/debugging/CMakeFiles/absl_stack_consumption.dir/internal/stack_consumption.cc.o
[22/121] Linking CXX static library absl/container/libabsl_container.a
[23/121] Linking CXX static library absl/debugging/libabsl_stack_consumption.a
[24/121] Linking CXX static library absl/container/libtest_instance_tracker_lib.a
[25/121] Building CXX object absl/debugging/CMakeFiles/absl_symbolize.dir/internal/demangle.cc.o
[26/121] Building CXX object absl/debugging/CMakeFiles/absl_symbolize.dir/symbolize.cc.o
[27/121] Building CXX object absl/debugging/CMakeFiles/absl_symbolize.dir/internal/address_is_readable.cc.o
[28/121] Building CXX object absl/debugging/CMakeFiles/absl_symbolize.dir/internal/elf_mem_image.cc.o
[29/121] Building CXX object absl/debugging/CMakeFiles/absl_leak_check.dir/leak_check.cc.o
[30/121] Linking CXX static library absl/debugging/libabsl_leak_check.a
[31/121] Building CXX object absl/debugging/CMakeFiles/absl_symbolize.dir/internal/vdso_support.cc.o
[32/121] Linking CXX static library absl/debugging/libabsl_symbolize.a
[33/121] Building CXX object absl/debugging/CMakeFiles/absl_failure_signal_handler.dir/failure_signal_handler.cc.o
[34/121] Building CXX object absl/debugging/CMakeFiles/absl_stacktrace.dir/stacktrace.cc.o
[35/121] Building CXX object absl/debugging/CMakeFiles/absl_stacktrace.dir/internal/address_is_readable.cc.o
[36/121] Building CXX object absl/debugging/CMakeFiles/absl_stacktrace.dir/internal/elf_mem_image.cc.o
[37/121] Building CXX object absl/debugging/CMakeFiles/absl_debugging.dir/absl_debugging_header_only_dummy.cc.o
[38/121] Building CXX object absl/debugging/CMakeFiles/absl_stacktrace.dir/internal/vdso_support.cc.o
[39/121] Linking CXX static library absl/debugging/libabsl_stacktrace.a
[40/121] Linking CXX static library absl/debugging/libabsl_debugging.a
[41/121] Building CXX object absl/debugging/CMakeFiles/absl_examine_stack.dir/internal/examine_stack.cc.o
[42/121] Linking CXX static library absl/debugging/libabsl_examine_stack.a
[43/121] Building CXX object absl/hash/CMakeFiles/absl_hash.dir/internal/city.cc.o
[44/121] Building CXX object absl/memory/CMakeFiles/absl_memory.dir/absl_memory_header_only_dummy.cc.o
[45/121] Linking CXX static library absl/memory/libabsl_memory.a
[46/121] Building CXX object absl/meta/CMakeFiles/absl_meta.dir/absl_meta_header_only_dummy.cc.o
[47/121] Linking CXX static library absl/meta/libabsl_meta.a
[48/121] Building CXX object absl/hash/CMakeFiles/absl_hash.dir/internal/hash.cc.o
[49/121] Building CXX object absl/numeric/CMakeFiles/absl_numeric.dir/absl_numeric_header_only_dummy.cc.o
[50/121] Building CXX object absl/numeric/CMakeFiles/absl_int128.dir/int128.cc.o
[51/121] Linking CXX static library absl/numeric/libabsl_int128.a
[52/121] Linking CXX static library absl/numeric/libabsl_numeric.a
[53/121] Building CXX object absl/strings/CMakeFiles/str_format_extension_internal.dir/internal/str_format/extension.cc.o
[54/121] Building CXX object absl/strings/CMakeFiles/str_format_extension_internal.dir/internal/str_format/output.cc.o
[55/121] Building CXX object absl/strings/CMakeFiles/str_format_internal.dir/internal/str_format/arg.cc.o
[56/121] Building CXX object absl/strings/CMakeFiles/str_format_internal.dir/internal/str_format/bind.cc.o
[57/121] Building CXX object absl/strings/CMakeFiles/str_format_internal.dir/internal/str_format/extension.cc.o
[58/121] Building CXX object absl/strings/CMakeFiles/str_format_internal.dir/internal/str_format/output.cc.o
[59/121] Building CXX object absl/strings/CMakeFiles/str_format_internal.dir/internal/str_format/float_conversion.cc.o
[60/121] Building CXX object absl/strings/CMakeFiles/absl_strings.dir/ascii.cc.o
[61/121] Building CXX object absl/strings/CMakeFiles/str_format_internal.dir/internal/str_format/parser.cc.o
[62/121] Building CXX object absl/strings/CMakeFiles/absl_strings.dir/charconv.cc.o
[63/121] Building CXX object absl/strings/CMakeFiles/absl_strings.dir/escaping.cc.o
[64/121] Building CXX object absl/strings/CMakeFiles/absl_strings.dir/internal/charconv_parse.cc.o
[65/121] Building CXX object absl/strings/CMakeFiles/absl_strings.dir/internal/charconv_bigint.cc.o
[66/121] Building CXX object absl/strings/CMakeFiles/absl_strings.dir/internal/utf8.cc.o
[67/121] Building CXX object absl/strings/CMakeFiles/absl_strings.dir/internal/ostringstream.cc.o
[68/121] Building CXX object absl/strings/CMakeFiles/absl_strings.dir/internal/memutil.cc.o
[69/121] Building CXX object absl/strings/CMakeFiles/absl_strings.dir/match.cc.o
[70/121] Building CXX object absl/strings/CMakeFiles/absl_strings.dir/numbers.cc.o
[71/121] Building CXX object absl/strings/CMakeFiles/absl_strings.dir/str_cat.cc.o
[72/121] Building CXX object absl/strings/CMakeFiles/absl_strings.dir/str_replace.cc.o
[73/121] Building CXX object absl/strings/CMakeFiles/absl_strings.dir/str_split.cc.o
[74/121] Building CXX object absl/strings/CMakeFiles/absl_strings.dir/string_view.cc.o
[75/121] Building CXX object absl/strings/CMakeFiles/absl_str_format.dir/absl_str_format_header_only_dummy.cc.o
[76/121] Building CXX object absl/strings/CMakeFiles/absl_strings.dir/substitute.cc.o
[77/121] Linking CXX static library absl/strings/libabsl_strings.a
[78/121] Linking CXX static library absl/strings/libstr_format_extension_internal.a
[79/121] Building CXX object absl/synchronization/CMakeFiles/absl_synchronization.dir/barrier.cc.o
[80/121] Building CXX object absl/synchronization/CMakeFiles/absl_synchronization.dir/blocking_counter.cc.o
[81/121] Building CXX object absl/synchronization/CMakeFiles/absl_synchronization.dir/internal/create_thread_identity.cc.o
[82/121] Building CXX object absl/synchronization/CMakeFiles/absl_synchronization.dir/internal/per_thread_sem.cc.o
[83/121] Building CXX object absl/synchronization/CMakeFiles/absl_synchronization.dir/internal/waiter.cc.o
[84/121] Building CXX object absl/synchronization/CMakeFiles/absl_synchronization.dir/notification.cc.o
[85/121] Building CXX object absl/synchronization/CMakeFiles/absl_synchronization.dir/internal/graphcycles.cc.o
[86/121] Building CXX object absl/time/CMakeFiles/absl_time.dir/civil_time.cc.o
[87/121] Building CXX object absl/synchronization/CMakeFiles/absl_synchronization.dir/mutex.cc.o
[88/121] Building CXX object absl/time/CMakeFiles/absl_time.dir/clock.cc.o
[89/121] Building CXX object absl/time/CMakeFiles/absl_time.dir/time.cc.o
[90/121] Building CXX object absl/time/CMakeFiles/absl_time.dir/format.cc.o
[91/121] Building CXX object absl/time/CMakeFiles/absl_time.dir/duration.cc.o
[92/121] Building CXX object absl/time/CMakeFiles/absl_time.dir/internal/cctz/src/time_zone_fixed.cc.o
[93/121] Building CXX object absl/time/CMakeFiles/absl_time.dir/internal/cctz/src/civil_time_detail.cc.o
[94/121] Building CXX object absl/time/CMakeFiles/absl_time.dir/internal/cctz/src/time_zone_if.cc.o
[95/121] Building CXX object absl/time/CMakeFiles/absl_time.dir/internal/cctz/src/time_zone_format.cc.o
[96/121] Building CXX object absl/time/CMakeFiles/absl_time.dir/internal/cctz/src/time_zone_impl.cc.o
[97/121] Building CXX object absl/time/CMakeFiles/absl_time.dir/internal/cctz/src/time_zone_libc.cc.o
[98/121] Building CXX object absl/time/CMakeFiles/absl_time.dir/internal/cctz/src/time_zone_lookup.cc.o
[99/121] Building CXX object absl/time/CMakeFiles/absl_time.dir/internal/cctz/src/time_zone_posix.cc.o
[100/121] Building CXX object absl/time/CMakeFiles/absl_time.dir/internal/cctz/src/time_zone_info.cc.o
[101/121] Building CXX object absl/types/CMakeFiles/absl_span.dir/absl_span_header_only_dummy.cc.o
[102/121] Building CXX object absl/time/CMakeFiles/absl_time.dir/internal/cctz/src/zone_info_source.cc.o
[103/121] Building CXX object absl/types/CMakeFiles/absl_any.dir/absl_any_header_only_dummy.cc.o
[104/121] Linking CXX static library absl/time/libabsl_time.a
[105/121] Linking CXX static library absl/synchronization/libabsl_synchronization.a
[106/121] Linking CXX static library absl/debugging/libabsl_failure_signal_handler.a
[107/121] Building CXX object absl/types/CMakeFiles/absl_bad_any_cast.dir/bad_any_cast.cc.o
[108/121] Linking CXX static library absl/types/libabsl_bad_any_cast.a
[109/121] Building CXX object absl/types/CMakeFiles/absl_optional.dir/optional.cc.o
[110/121] Building CXX object absl/types/CMakeFiles/absl_bad_optional_access.dir/bad_optional_access.cc.o
[111/121] Linking CXX static library absl/types/libabsl_bad_optional_access.a
[112/121] Building CXX object absl/utility/CMakeFiles/absl_utility.dir/absl_utility_header_only_dummy.cc.o
[113/121] Linking CXX static library absl/utility/libabsl_utility.a
[114/121] Linking CXX static library absl/types/libabsl_span.a
[115/121] Linking CXX static library absl/strings/libstr_format_internal.a
[116/121] Building CXX object absl/types/CMakeFiles/absl_variant.dir/bad_variant_access.cc.o
[117/121] Linking CXX static library absl/strings/libabsl_str_format.a
[118/121] Linking CXX static library absl/types/libabsl_any.a
[119/121] Linking CXX static library absl/hash/libabsl_hash.a
[120/121] Linking CXX static library absl/types/libabsl_optional.a
[121/121] Linking CXX static library absl/types/libabsl_variant.a
[122/387] Building CXX object CMakeFil.../ground_truth/relations_text_file.cc.o^[288/387] Linking CXX executable carto...rm.transform_interpolation_buffer_test
FAILED: cartographer.transform.transform_interpolation_buffer_test 
: && /usr/bin/c++  -O2 -DNDEBUG  -rdynamic CMakeFiles/cartographer.transform.transform_interpolation_buffer_test.dir/cartographer/transform/transform_interpolation_buffer_test.cc.o  -o cartographer.transform.transform_interpolation_buffer_test  libcartographer.a -lgmock_main -lpthread libcartographer_test_library.a libcartographer.a /home/lin/ros/catkin_ws/install_isolated/lib64/libceres.a -lglog -lspqr -lcholmod -lccolamd -lcamd -lcolamd -lamd -llapack -lblas -lsuitesparseconfig -lrt -llapack -lblas -lsuitesparseconfig -lrt -lgomp -lpthread -llua-5.3 -lm -lboost_iostreams -lboost_regex -lglog -lgflags -lcairo -lprotobuf abseil/src/abseil-build/absl/synchronization/libabsl_synchronization.a abseil/src/abseil-build/absl/debugging/libabsl_symbolize.a abseil/src/abseil-build/absl/time/libabsl_time.a abseil/src/abseil-build/absl/strings/libstr_format_internal.a abseil/src/abseil-build/absl/strings/libstr_format_extension_internal.a abseil/src/abseil-build/absl/strings/libabsl_str_format.a abseil/src/abseil-build/absl/strings/libabsl_strings.a abseil/src/abseil-build/absl/hash/libabsl_hash.a abseil/src/abseil-build/absl/algorithm/libabsl_algorithm.a abseil/src/abseil-build/absl/base/libabsl_base.a abseil/src/abseil-build/absl/base/libabsl_dynamic_annotations.a abseil/src/abseil-build/absl/base/libabsl_internal_malloc_internal.a abseil/src/abseil-build/absl/base/libabsl_internal_spinlock_wait.a abseil/src/abseil-build/absl/base/libabsl_internal_throw_delegate.a abseil/src/abseil-build/absl/container/libabsl_container.a abseil/src/abseil-build/absl/container/libtest_instance_tracker_lib.a abseil/src/abseil-build/absl/debugging/libabsl_debugging.a abseil/src/abseil-build/absl/debugging/libabsl_examine_stack.a abseil/src/abseil-build/absl/debugging/libabsl_failure_signal_handler.a abseil/src/abseil-build/absl/debugging/libabsl_leak_check.a abseil/src/abseil-build/absl/debugging/libabsl_stack_consumption.a abseil/src/abseil-build/absl/debugging/libabsl_stacktrace.a abseil/src/abseil-build/absl/memory/libabsl_memory.a abseil/src/abseil-build/absl/meta/libabsl_meta.a abseil/src/abseil-build/absl/numeric/libabsl_int128.a abseil/src/abseil-build/absl/numeric/libabsl_numeric.a abseil/src/abseil-build/absl/synchronization/libabsl_synchronization.a abseil/src/abseil-build/absl/types/libabsl_any.a abseil/src/abseil-build/absl/types/libabsl_bad_any_cast.a abseil/src/abseil-build/absl/types/libabsl_bad_optional_access.a abseil/src/abseil-build/absl/types/libabsl_optional.a abseil/src/abseil-build/absl/types/libabsl_span.a abseil/src/abseil-build/absl/types/libabsl_variant.a abseil/src/abseil-build/absl/utility/libabsl_utility.a -lpthread && :
/usr/bin/ld: CMakeFiles/cartographer.transform.transform_interpolation_buffer_test.dir/cartographer/transform/transform_interpolation_buffer_test.cc.o: undefined reference to symbol '_ZN7testing8internal24FormatMatcherDescriptionEbPKcRKSt6vectorINSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEESaIS9_EE'
/usr/bin/ld: //usr/lib64/libgmock.so.1.8.1: error adding symbols: DSO missing from command line
collect2: error: ld returned 1 exit status
ninja: build stopped: subcommand failed.
<== Failed to process package 'cartographer': 
  Command '['/home/lin/ros/catkin_ws/install_isolated/env.sh', 'ninja', '-j1']' returned non-zero exit status 1

Reproduce this error by running:
==> cd /home/lin/ros/catkin_ws/build_isolated/cartographer && /home/lin/ros/catkin_ws/install_isolated/env.sh ninja -j1

Command failed, exiting.
```
