- 内存管理

  内存管理可以分为三个层次，自底向上分别是：

  - 操作系统内核的内存管理
  - glibc层使用系统调用维护的内存管理算法The GNU C Library project provides *the* core libraries for the GNU system and GNU/Linux systems, as well as many other systems that use Linux as the kernel. These libraries provide critical APIs including ISO C11, POSIX.1-2008, BSD, OS-specific APIs and more. These APIs include such foundational facilities as `open`, `read`, `write`, `malloc`, `printf`, `getaddrinfo`, `dlopen`, `pthread_create`, `crypt`, `login`, `exit` and more. 
  - 应用程序从glibc动态分配内存后，根据应用程序本身的程序特性进行优化， 比如使用引用计数std::shared_ptr，apache的内存池方式等等。

- 一个优秀的通用内存分配器应具有以下特性:

  - 额外的空间损耗尽量少
  - 分配速度尽可能快
  - 尽量避免内存碎片
  - 缓存本地化友好
  - 通用性，兼容性，可移植性，易调试

- 目前大部分服务端程序使用  https://blog.csdn.net/junlon2006/article/details/77854898  总体思路和redis的string类似，都是预先分配数据。

  - glibc提供的malloc/free系列函数，见 ptmalloc原理， ptmalloc内存管理讲解了数据结构和算法，直观感觉是使用了类似于散列表的数据结构，分配内存。

  - 而glibc使用的ptmalloc2在性能上远远弱后于google的tcmalloc和，按线程来组织内存
  - facebook的jemalloc。 而且后两者只需要使用LD_PRELOAD环境变量启动程序即可，甚至并不需要重新编译。 