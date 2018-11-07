## Spring Framework

https://spring.io/projects/spring-framework#learn

| [Core](https://docs.spring.io/spring/docs/5.1.0.RELEASE/spring-framework-reference/core.html#spring-core) | IoC container, Events, Resources, i18n, Validation, Data Binding, Type Conversion, SpEL, AOP. |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [Testing](https://docs.spring.io/spring/docs/5.1.0.RELEASE/spring-framework-reference/testing.html#testing) | Mock objects, TestContext framework, Spring MVC Test, WebTestClient. |
| [Data Access](https://docs.spring.io/spring/docs/5.1.0.RELEASE/spring-framework-reference/data-access.html#spring-data-tier) | Transactions, DAO support, JDBC, ORM, Marshalling XML.       |
| [Web Servlet](https://docs.spring.io/spring/docs/5.1.0.RELEASE/spring-framework-reference/web.html#spring-web) | Spring MVC, WebSocket, SockJS, STOMP messaging.              |
| [Web Reactive](https://docs.spring.io/spring/docs/5.1.0.RELEASE/spring-framework-reference/web-reactive.html#spring-webflux) | Spring WebFlux, WebClient, WebSocket.                        |
| [Integration](https://docs.spring.io/spring/docs/5.1.0.RELEASE/spring-framework-reference/integration.html#spring-integration) | Remoting, JMS, JCA, JMX, Email, Tasks, Scheduling, Cache.    |
| [Languages](https://docs.spring.io/spring/docs/5.1.0.RELEASE/spring-framework-reference/languages.html#languages) | Kotlin, Groovy, Dynamic languages.                           |



- IoC container,

  - IOC （inverse of control)
    - 不关心组件的来源
    - 抄袭了JAVA EE的概念
  - DI (dependency injection)
    - 依赖查找
      - ID 别名、名称查找 : `getBean(String)`
      - 类型查找 ) `getBean(Class)`
      - 注解查找 `getBeanWIthAnotation()`
    - 依赖注入
      - 方法：
        - Spring @Autowired
        - JAVA @Resource
        - Java EE @Inject
      - 途径
        - 属性注入
        - 方法注入
        - 构造注入

  

-  Events, 

- Resources, 

- i18n, 

- Validation, 

- Data Binding, 

- Type Conversion, 

- SpEL,

-  AOP.