#### Error when executing `catkin_make_isolated --install --use-ninja -j1`

```bash
==> Processing catkin package: 'cartographer_ros'
==> Creating build directory: 'build_isolated/cartographer_ros'
==> Building with env: '/home/lin/ros/catkin_ws/install_isolated/env.sh'
==> cmake /home/lin/ros/catkin_ws/src/cartographer_ros/cartographer_ros -DCATKIN_DEVEL_PREFIX=/home/lin/ros/catkin_ws/devel_isolated/cartographer_ros -DCMAKE_INSTALL_PREFIX=/home/lin/ros/catkin_ws/install_isolated -G Ninja in '/home/lin/ros/catkin_ws/build_isolated/cartographer_ros'
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
-- Boost version: 1.66.0
-- Found the following Boost libraries:
--   system
--   iostreams
--   regex
-- Checking for module 'eigen3'
--   Found eigen3, version 3.3.7
-- Found eigen: /usr/include/eigen3  
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Looking for pthread_create
-- Looking for pthread_create - not found
-- Looking for pthread_create in pthreads
-- Looking for pthread_create in pthreads - not found
-- Looking for pthread_create in pthread
-- Looking for pthread_create in pthread - found
-- Found Threads: TRUE  
-- Boost version: 1.66.0
-- Found the following Boost libraries:
--   system
--   filesystem
--   thread
--   date_time
--   iostreams
--   serialization
--   chrono
--   atomic
--   regex
-- looking for PCL_COMMON
-- Found PCL_COMMON: /usr/lib64/libpcl_common.so  
-- Found PCL: /usr/lib64/libboost_system.so;/usr/lib64/libboost_filesystem.so;/usr/lib64/libboost_thread.so;-lpthread;/usr/lib64/libboost_date_time.so;/usr/lib64/libboost_iostreams.so;/usr/lib64/libboost_serialization.so;/usr/lib64/libboost_chrono.so;/usr/lib64/libboost_atomic.so;/usr/lib64/libboost_regex.so;optimized;/usr/lib64/libpcl_common.so;debug;/usr/lib64/libpcl_common.so;/usr/lib64/libboost_system.so;/usr/lib64/libboost_filesystem.so;/usr/lib64/libboost_thread.so;-lpthread;/usr/lib64/libboost_date_time.so;/usr/lib64/libboost_iostreams.so;/usr/lib64/libboost_serialization.so;/usr/lib64/libboost_chrono.so;/usr/lib64/libboost_atomic.so;/usr/lib64/libboost_regex.so  
CMake Error at CMakeLists.txt:47 (find_package):
  By not providing "Findcartographer.cmake" in CMAKE_MODULE_PATH this project
  has asked CMake to find a package configuration file provided by
  "cartographer", but CMake did not find one.

  Could not find a package configuration file provided by "cartographer" with
  any of the following names:

    cartographerConfig.cmake
    cartographer-config.cmake

  Add the installation prefix of "cartographer" to CMAKE_PREFIX_PATH or set
  "cartographer_DIR" to a directory containing one of the above files.  If
  "cartographer" provides a separate development package or SDK, be sure it
  has been installed.


-- Configuring incomplete, errors occurred!
See also "/home/lin/ros/catkin_ws/build_isolated/cartographer_ros/CMakeFiles/CMakeOutput.log".
See also "/home/lin/ros/catkin_ws/build_isolated/cartographer_ros/CMakeFiles/CMakeError.log".
<== Failed to process package 'cartographer_ros': 
  Command '['/home/lin/ros/catkin_ws/install_isolated/env.sh', 'cmake', '/home/lin/ros/catkin_ws/src/cartographer_ros/cartographer_ros', '-DCATKIN_DEVEL_PREFIX=/home/lin/ros/catkin_ws/devel_isolated/cartographer_ros', '-DCMAKE_INSTALL_PREFIX=/home/lin/ros/catkin_ws/install_isolated', '-G', 'Ninja']' returned non-zero exit status 1

Reproduce this error by running:
==> cd /home/lin/ros/catkin_ws/build_isolated/cartographer_ros && /home/lin/ros/catkin_ws/install_isolated/env.sh cmake /home/lin/ros/catkin_ws/src/cartographer_ros/cartographer_ros -DCATKIN_DEVEL_PREFIX=/home/lin/ros/catkin_ws/devel_isolated/cartographer_ros -DCMAKE_INSTALL_PREFIX=/home/lin/ros/catkin_ws/install_isolated -G Ninja

Command failed, exiting.
```
