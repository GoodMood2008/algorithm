

- 背景：底层通讯一般使用BIO、NIO，netty作为NIO框架，底层基于select、linux epoll，类似的通讯组件包有mina

- 优劣势：

  - netty相比于nio，进行了封装，可以更加方便的写出socket通讯，但是要用好需要把相关的参数搞明白。如果针对私有协议，用netty快速；但是如果用http等，还是用tomcat、jetty这些已经封装好的东西比较好，因为在http这个层次上封装的更加易用和工业级。
  - netty针对的是通用通讯底层通讯，而tomcat、jetty等是专用的某种协议的通讯，通讯只是其中的一部分，也可能会使用到netty。

- 场景：用于新发项目开发私有协议。一般情况下大的框架已经针对通讯封装好了，如spring、tomcat、jetty等。

  - 基于 netty框架的有Dubbo、RocketMQ

- 底层组成：

  - 《netty权威指南》20.1 分为三层
  - 高性能：性能是设计出来的，而不是测试出来的。
    - 异步非阻塞的I/O，基于reactor模式实现
    - zero copy， tcp接收和发送缓冲区使用直接内存代替堆内存
    - 内存池的方式循环利用Bytebuf
    - 可配置IO线程数、TCP参数
    - 引用计数？
  - 高可用：
    - 链路空闲监测机制
    - 通过引用计数对Netty的ByteBuf等内置对象，对非法对象引用进行检测和包含
    - 优雅停机
  - 可扩展
    - 责任链拦截
    - 应用层协议定制，这里更加说明各种协议的底层其实就是socket安全性

  - 安全性
    - SSL
    - netty黑名单，接入认证

- 底层原理和关键实现

  - NIO编程
  - 内存池

- 

- 

- 

- 

- 

- 





### 多线程模式Future Promise Callback

在并发编程中，我们通常会用到一组非阻塞的模型：Promise，Future 和 Callback。其中的 Future 表示一个可能还没有实际完成的异步任务的结果，针对这个结果可以添加 Callback 以便在任务执行成功或失败后做出对应的操作，而 Promise 交由任务执行者，任务执行者通过 Promise 可以标记任务完成或者失败。 可以说这一套模型是很多异步非阻塞架构的基础。 


这一套经典的模型在 Scala、C# 中得到了原生的支持，但 JDK 中暂时还只有无 Callback 的 Future 出现，当然也并非在 JAVA 界就没有发展了，比如 Guava 就提供了ListenableFuture 接口，而 Netty 4+ 更是提供了完整的 Promise、Future 和 Listener 机制，在 Netty 的官方文档 [Using as a generic library](http://netty.io/wiki/using-as-a-generic-library.html#wiki-h2-5) 中也介绍了将 Netty 作为一个 lib 包依赖，并且使用 Listenable futures 的示例。 







### TCP/IP

袁术网址：http://www.kohala.com/start/



















