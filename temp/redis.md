https://redis.io/

http://redisdoc.com/ redis命令的翻译版

https://github.com/josiahcarlson/redis-in-action redis in action代码目录



<redis的设计与实现>

集群   sentinal

-------------------------------------------------------------------------------------------------------------------------

单机数据库                 订阅与发布      lua    事物

———————————————————————————————————————————

redis数据结构                   redisNIO、同步异步          控制逻辑            异常处理       







了Redis的内部机制（比如数据库实现、类型系统、事件模型），而且还介绍了大部分Redis单机特性（比如事务、持久化、Lua脚本、排序、二进制位操作），以及所有Redis多机特性（如复制、Sentinel和集群）。



Redis is an open source (BSD licensed), in-memory data structure store, used as a database, cache and message broker. 

It supports data structures such as strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperloglogs and geospatial indexes with radius queries. 

Redis has 

- built-in replication, 
- Lua scripting, 
- LRU eviction, transactions and 
- different levels of on-disk persistence, and provides high availability via Redis Sentinel and automatic partitioning with Redis Cluster. 



# data structure

- list adlist.h

  这是个最基本的list的实现

  

- list    quicklist.h

quicklist是双向链表 + ziplist的组合结构，既然这么设计，那么肯定是有这么做的道理，我没有看懂。ziplist压缩了数据，但是访问要频繁的操作内存，会不会很慢？

ziplist暂时放一下，但是quicklist本身应该是可以看懂的。



在这个底层就是一个双向链表，对于链表的操作。关键结构：

typedef struct quicklist {
    quicklistNode *head;
    quicklistNode *tail;
    unsigned long count;        /* total count of all entries in all ziplists */
    unsigned int len;           /* number of quicklistNodes */
    int fill : 16;              /* fill factor for individual nodes */
    unsigned int compress : 16; /* depth of end nodes not to compress;0=off */
} quicklist;

typedef struct quicklistNode {
    struct quicklistNode *prev;
    struct quicklistNode *next;
    unsigned char *zl;
    unsigned int sz;             /* ziplist size in bytes */
    unsigned int count : 16;     /* count of items in ziplist */
    unsigned int encoding : 2;   /* RAW==1 or LZF==2 */
    unsigned int container : 2;  /* NONE==1 or ZIPLIST==2 */
    unsigned int recompress : 1; /* was this node previous compressed? */
    unsigned int attempted_compress : 1; /* node can't compress; too small */
    unsigned int extra : 10; /* more bits to steal for future usage */
} quicklistNode;



在链表的本质上，增加了存储数据，压缩数据。



Redis的QuickList是个优化，双向链表 + 链表的每个节点是个字符数组（或者说一个内部协议），这样可以获取到更高的压缩率以及线性访问速度



- set的调用栈

redis_server!sdsnewlen+0x24 [c:\release\redis\src\sds.c @ 89]

redis_server!dbAdd+0x5e [c:\release\redis\src\db.c @ 162]

redis_server!setKey+0x3e [c:\release\redis\src\db.c @ 190]

redis_server!setGenericCommand+0x139 [c:\release\redis\src\t_string.c @ 87]

redis_server!setCommand+0x167 [c:\release\redis\src\t_string.c @ 140]

redis_server!call+0x90 [c:\release\redis\src\server.c @ 2282]

redis_server!processCommand+0x59d [c:\release\redis\src\server.c @ 2561]

redis_server!processInputBuffer+0x216 [c:\release\redis\src\networking.c @ 1438]

redis_server!readQueryFromClient+0x2da [c:\release\redis\src\networking.c @ 1503]

redis_server!redis_main+0x58c [c:\release\redis\src\server.c @ 4157]















