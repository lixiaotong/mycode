状态码 （Status Code）
HTTP 应答中，需要带⼀个很重要的字段：status code。它说明了请求的⼤致情况，是否正常完成、需要进⼀步处理、出现了什么错误，
对于客户端⾮常重要。状态码都是三位的整数，⼤概分成了⼏个区间：
2XX：请求正常处理并返回
3XX：重定向，请求的资源位置发⽣变化
4XX：客户端发送的请求有错误
5XX：服务器端错误

在 HTTP API 设计中，经常⽤到的状态码以及它们的意义如下表：
Status Code 语义 说明
200 OK  请求已成功
201 Created 请求已完成，并导致了⼀个或者多个资源被创建，最常⽤在 POST 创建资源的时候
202 Accepted    请求已经接收并开始处理，但是处理还没有完成。⼀般⽤在异步处理的情况，响应 body 中应该告诉客户端去哪⾥查看任务的状态
204 No Content  请求已经处理完成，但是没有信息要返回，经常⽤在 PUT 更新资源的时候（客户端提供资源的所有属性，因此不需要服务端返回）。如果
有重要的 metadata，可以放到头部返回

301 Moved Permanently 请求的资源已经永久性地移动到另外⼀个地⽅，后续所有的请求都应该直接访问新地址。服务端会把新地址写在 Location 头部字段，⽅便
客户端使⽤。允许客户端把 POST 请求修改为 GET。
302 Moved Temporarily 临时重定向
304 Not Modified 请求的资源和之前的版本⼀样，没有发⽣改变。⽤来缓存资源，和条件性请求（conditional request）⼀起出现
307 Temporary Redirect ⽬标资源暂时性地移动到新的地址，客户端需要去新地址进⾏操作，但是 不能 修改请求的⽅法。
308 Permanent Redirect 和 301 类似，除了客户端 不能 修改原请求的⽅法
400 Bad Request 1.语义有误，当前请求⽆法被服务器理解; 2. 请求参数有误。
401 Unauthorized 当前请求需要⾝份验证。
403 Forbidden 服务器已经理解请求，但是拒绝执⾏它。与401响应不同的是，⾝份验证并不能提供任何帮助，⽽且这个请求也不应该被重复提交。如果这
不是⼀个 HEAD 请求，⽽且服务器希望能够讲清楚为何请求不能被执⾏，那么就应该在实体内描述拒绝的原因。当然服务器也可以返回⼀
个404响应，假如它不希望让客户端获得任何信息。
404 Not Found 请求失败，请求所希望得到的资源未被在服务器上发现。
405 Method Not Allowed 请求⾏中指定的请求⽅法不能被⽤于请求相应的资源。该响应必须返回⼀个Allow 头信息⽤以表⽰出当前资源能够接受的请求⽅法的列表。 鉴于 PUT，DELETE ⽅法会对服务器上的资源进⾏写操作，因⽽绝⼤部分的⽹页服务器都不⽀持或者在默认配置下不允许上述请求⽅法，
对于此类请求均会返回405错误。
406 Not Acceptable 请求的资源的内容特性⽆法满⾜请求头中的条件，因⽽⽆法⽣成响应实体。
409 Conflict 由于和被请求的资源的当前状态之间存在冲突，请求⽆法完成。
429 Too Many Requests 资源配额不⾜或达到速率限制。
499 Client Closed Request 请求被客户端取消。
500 Internal Server Error 服务器内部错误
501 Not Implemented 服务器不⽀持当前请求所需要的某个功能。当服务器⽆法识别请求的⽅法，并且⽆法⽀持其对任何资源的请求。
502 Bad Gateway 作为⽹关或者代理⼯作的服务器尝试执⾏请求时，从上游服务器接收到⽆效的响应。
503 Service Unavailable 由于临时的服务器维护或者过载，服务器当前⽆法处理请求。这个状况是临时的，并且将在⼀段时间以后恢复。
504 Gateway Timeout 作为⽹关或者代理⼯作的服务器尝试执⾏请求时，未能及时从上游服务器（URI标识出的服务器，例如HTTP、FTP、LDAP）或者辅助服务
器（例如DNS）收到响应。
505 HTTP Version Not Supported 服务器不⽀持，或者拒绝⽀持在请求中使⽤的 HTTP 版本。


上⾯这些状态码覆盖了 API 设计中⼤部分的情况，如果对某个状态码不清楚或者希望查看更完整的列表，可以参考 HTTP Status Code[6]
、维基百科-状态码[7]或者 RFC7231 Response Status Codes[8] 的内容。



限流（RateLimit）
如果对访问的次数不加控制，很可能会造成 API 被滥⽤，甚⾄被 DDOS 攻击[12]。根据使⽤者不同的⾝份对其进⾏限流，可以防⽌这些情
况，减少服务器的压⼒。
对⽤户的请求限流之后，要有⽅法告诉⽤户它的请求使⽤情况，本⽂档推荐使⽤的三个相关的头部：
X-RateLimit-Limit: ⽤户每个⼩时允许发送请求的最⼤值
X-RateLimit-Remaining：当前时间窗⼝剩下的可⽤请求数⽬
X-RateLimit-Rest: 时间窗⼝重置的时候，到这个时间点可⽤的请求数量就会变成 X-RateLimit-Limit 的值
举例：
X-Ratelimit-Limit: 18000
X-Ratelimit-Remaining: 17995
X-Ratelimit-Reset: 1590570990
如果允许没有登录的⽤户使⽤ API（可以让⽤户试⽤），可以把 X-RateLimit-Limit 的值设置得很⼩，⽐如 60。没有登录的⽤户是按照请
求的 IP 来确定的，⽽登录的⽤户按照认证后的信息来确定⾝份。
对于超过流量的请求，可以返回 429 Too many requests[13] 状态码，并附带错误信息。


限流（RateLimit）
如果对访问的次数不加控制，很可能会造成 API 被滥⽤，甚⾄被 DDOS 攻击[12]。根据使⽤者不同的⾝份对其进⾏限流，可以防⽌这些情
况，减少服务器的压⼒。
对⽤户的请求限流之后，要有⽅法告诉⽤户它的请求使⽤情况，本⽂档推荐使⽤的三个相关的头部：
X-RateLimit-Limit: ⽤户每个⼩时允许发送请求的最⼤值
X-RateLimit-Remaining：当前时间窗⼝剩下的可⽤请求数⽬
X-RateLimit-Rest: 时间窗⼝重置的时候，到这个时间点可⽤的请求数量就会变成 X-RateLimit-Limit 的值
举例：
X-Ratelimit-Limit: 18000
X-Ratelimit-Remaining: 17995
X-Ratelimit-Reset: 1590570990
如果允许没有登录的⽤户使⽤ API（可以让⽤户试⽤），可以把 X-RateLimit-Limit 的值设置得很⼩，⽐如 60。没有登录的⽤户是按照请
求的 IP 来确定的，⽽登录的⽤户按照认证后的信息来确定⾝份。
对于超过流量的请求，可以返回 429 Too many requests[13] 状态码，并附带错误信息。


认证和授权（Authentication & Authorization）
⼀般来说，让任何⼈随意访问公开的 API 是不好的做法。验证和授权是两件事情：
验证（Authentication）是为了确定⽤户是其申明的⾝份，⽐如提供账户的密码。不然的话，任何⼈伪造成其他⾝份（⽐如其他⽤户或者管
理员）是⾮常危险的
授权（Authorization）是为了保证⽤户有对请求资源特定操作的权限。⽐如⽤户的私⼈信息只能⾃⼰能访问，其他⼈⽆法看到；有些特殊
的操作只能管理员可以操作，其他⽤户有只读的权限等等
如果没有通过验证（提供的⽤户名和密码不匹配，token 不正确等），需要返回 401 Unauthorized[9]状态码，并在 body 中说明具体的
错误信息；⽽没有被授权访问的资源操作，需要返回 403 Forbidden[10] 状态码，还有详细的错误信息。
NOTES: 借鉴于 Github，它对某些⽤户未被授权访问的资源操作返回 404 Not Found[11]，⽬的是为了防⽌私有资源的泄露（⽐如⿊客
可以⾃动化试探⽤户的私有资源，返回 403 的话，就等于告诉⿊客⽤户有这些私有的资源）。