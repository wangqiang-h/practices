> 生产器产生block --> filter(sub替换) --> rule(各种rule实例) --> 调用handler


# Rule 类：

1. 不同的Rule类可以有继承的关系。 Rule 的顺序很重要。
2. condition（判断是否走这个rule逻辑）  和 action(输出，并且有返回值，标识着是否继续其他Rule)


# HtmlHandler 类:

1. 整合输出格式
2. 供各种Rule类的action函数调用。
