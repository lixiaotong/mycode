# css 案例
    1） 缺少常规字体的研究
    


# css 编写顺序：

1 调整布局

2 调整间距

3 调整文本大小

4 增加图片

5 增加特效

# 基础组件：
1 cdn加速库：https://cdnjs.com/. 比如常用js css fontawesome 各种标准图标

2 毛玻璃效果：https://zxuqian.cn/glassmorphism-generator

3 Css最新的库：Tailwind CSS

4 卡片阴影效果： https://www.cssmatic.com/box-shadow

# 注意事项：
1 用css布局把页面先从手机版分辨率的布局，写到大屏幕的布局


# CSS 背景属性
- background              简写属性，将背景属性设置在一个声明中。
- background-attachment   背景图像是否固定或者随着页面的其余部分滚动。
- background-color        设置元素的背景颜色
- background-image        把图像设置为背景
- background-position     设置背景图像的起始位置
- background-repeat       设置背景图像是否及如何重复。

# CSS 文本属性
- color             设置文本颜色
- direction         设置文本方向
- letter-spacing    设置字符间距
- word-spacing      设置字间距   
- line-height       设置行高
- text-align        对齐元素中的文本
- text-decoration   向文本添加修饰
- text-indent       缩进元素中文本的首行
- text-shadow       设置文本阴影
- text-transform    控制元素中的字母
- unicode-bidi      设置或返回文本是否被重写
- vertical-align    设置元素的垂直对齐
- white-space       设置元素中空白的处理方式

# CSS 字体属性
- font              在一个声明中设置所有的字体属性
- font-family       指定文本的字体系列
- font-size         指定文本的字体大小
- font-style        指定文本的字体样式
- font-variant      以小型大写字体或者正常字体显示文本
- font-weight       指定字体的粗细

# CSS 列表属性
- list-style        简写属性。 用于把所有用于列表的属性设置于声明中
- list-style-image  将图像设置为列表项标志
- list-style-position   设置列表中列表项标志的位置
- list-style-type   设置列表项标志的类型

# CSS 边框属性
- border            简写属性，用于把针对四个边的属性设置在一个声明。
- border-style      用于设置元素所有边框样式，或者单独为各边设置边框样式。
- border-width      简写属性，用于为元素的所有边框设置宽度，或者单独地为各边边框设置宽度。
- border-color      简写属性，设置元素的所有边框中可见部分的颜色，或为四个边分别设置颜色。
- border-bottom     简写属性，用于把下边框的所有属性设置到一个声明中。
- border-bottom-color   设置元素的下边框的颜色
- border-bottom-style   设置元素的下边框的样式
- border-bottom-width   设置元素的下边框的宽度
- border-left       简写属性，用于把左边框的所有属性设置到一个声明中
- border-left-color 设置元素的左边框的颜色
- border-left-style 设置元素的左边框的样式
- border-left-width 设置元素的左边框的宽度
- border-right      简写属性，用于把右边框的所有属性设置到一个声明中。
- border-right-color 设置元素的右边框的颜色
- border-right-style    设置元素的右边框的样式
- border-right-width    设置元素的右边框的宽度
- border-top        简写属性，用于把上边框的所有属性设置到一个声明中。
- border-top-color  设置元素的上边框的颜色
- border-top-style  设置元素的上边框的样式
- border-top-width  设置元素的上边框的宽度
- border-radius     设置圆角的边框

# CSS 轮廓属性
- outline 在一个声明中设置所有的轮廓属性 outline-color
- outline-style
- outline-width
- inherit 2
- outline-color 设置轮廓的颜色 color-name
- hex-number
- rgb-number
- invert
- inherit 2
- outline-style 设置轮廓的样式 none
- dotted
- dashed
- solid
- double
- groove
- ridge
- inset
- outset
- inherit 2
- outline-width     设置轮廓的宽度 thin
- medium
- thick
- length
- inherit 2

# CSS 边距属性
- margin  简写属性。 在一个声明中设置所有外边距属性。
- margin-bottom   设置元素的下外边距
- margin-left     设置元素的左外边距
- margin-right    设置元素的右外边距
- margin-top      设置元素的上外边距

# CSS 填充属性
- padding 使用简写属性设置在一个声明中
- padding-bottom    设置元素的底部填充
- padding-left      设置元素的左部填充
- padding-right     设置元素的右边填充
- padding-top       设置元素的顶部填充

# CSS 尺寸属性
- height            设置元素的高度
- width             设置元素的宽度
- max-height        设置元素的最大高度
- min-height        设置元素的最小高度
- max-width         设置元素的最大宽度
- min-width         设置元素的最小宽度

# CSS 浮动属性
- clear 指定不允许元素周围有浮动元素。
  - left 
  - right
  - both
  - none
  - inherit
- float     指定一个盒子（元素）是否可以浮动
  - left
  - right
  - none
  - inherit

# CSS 伪类/元素
  选择器        示例      示例说明
- :link        a:link   选择所有未访问链接
- :visited    a:visited 选择所有访问过的链接
- :active     a:active  选择正在活动的链接
- :hover      a:hover   把鼠标放在链接上的状态
- :focus      input:focus   选择元素输入后具有焦点
- :first-letter   p:first-letter   选择每个<p>元素的第一个字母
- :first-line     p:first-line    选择每个<p>元素的第一行
- :first-child    p:first-child   选择器匹配属于任意元素的第一个子元素的<p>元素
- :before         p:before   在每个<p>元素之前插入内容
- :after          p:after     在每个<p>元素之后插入内容
- :lang(language) p:lang(it)  为<p>元素的lang属性选择一个开始值

# CSS 定位属性
- bottom    定义了定位元素下外边距边界与其包含块下边界之间的偏移。  auto
  - length
  - %
  - inherit 2
- clip    剪辑一个绝对定位的元素    shape
  - auto
  - inherit 2
- cursor  显示光标移动到指定的类型  url
  - auto
  - crosshair
  - default
  - pointer
  - move
  - e-resize
  - ne-resize
  - nw-resize
  - n-resize
  - se-resize
  - sw-resize
  - s-resize
  - w-resize
  - text
  - wait
  - help
- left  定义了定位元素左外边距边界与其包含块左边界之间的偏移  auto
  - length
  - %
  - inherit
- overflow  设置当元素的内容溢出其区域时发生的事情 auto
  - hidden
  - scroll
  - visible
  - inherit
- overflow-y 指定如何处理顶部/底部边缘的内容溢出元素的内容区域  auto
  - hidden
  - scroll
  - visible
  - no-display
  - no-content
- overflow-x  指定如何处理右边/左边边缘的内容溢出元素的内容区域 auto
  - hidden
  - scroll
  - visible
  - no-display
  - no-content
- position  指定元素的定位类型  absolute
  - fixed
  - relative
  - static
  - inherit
- right 定义了定位元素右外边距边界与其包含块右边界之间的偏移。  auto
  - length
  - %
  - inherit
- top 定义了一个定位元素的上外边距边界与其包含块上边界之间的偏移。  auto
  - length
  - %
  - inherit
- z-index 设置元素的堆叠顺序  number
  - auto
  - inherit
  - 