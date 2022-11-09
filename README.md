仓库地址：https://github.com/1223ol/team.git
# 项目描述
------------

-   项目名：基于微信的记账小程序开发
-   项目版本：2.0
-   项目功能简述：用户使用基于微信的记账小程序，使用“计划”功能配合用户自己输入的每天消费实现记录支出的作用。加上图表和公众号，方便用户的记录，查看和使用
-   代码仓库地址：
-   第一负责人：【hwl】

运行
------------
####    开发配置环境
-   Python环境，运行后端
-   微信开发小程序，做前端开发

####    开发&发布命令

```
  git clone https://gitee.com/SE-Tally/Tally.git
  cd server
  pip install -r requirement.txt
  python run .py
```

####    依赖库
- `certifi==2018.4.16`
- `chardet==3.0.4`
- `click==6.7`
- `Flask==1.0.2`
- `Flask-SQLAlchemy==2.3.2`
- `idna==2.6`
- `itsdangerous==0.24`
- `Jinja2==2.10`
- `MarkupSafe==1.0`
-  `requests==2.18.4`
- `SQLAlchemy==1.2.8`
- `urllib3==1.22`
- `Werkzeug==0.14.1`
####    发布
-   微信小程序端

####    相关人员

角色|人员
-|:-:
产品经理|cys
后端开发|hzy
前端开发|hjx
后端开发|hzh
测试|hzy


## CHANGELOG
### v2.0 (2018/6/1)
- 更改动态余额查看算法，更人性化
- UI重构，更美观
- 支持金钱燃尽图查看计划
- 图标展示部分进行重构
- 支持长按删除账单
- 新增公众号功能，支持通过语音或者文字增加账单
- 新增激活码机制

### v1.0 (2018/05/12)
- 支持动态余额计算
- 添加计划
- 修复背景图片不能查看bug
- 重构日历
- 支持查看账单明细

### v0.1.1 (2018/05/01)
- 日历
- 查看账单
- 添加账单
- 消费情况查看


## to do list
- [x] 支持公众号添加账单
- [ ] 公众号中的识别更加智能
- [ ] 数据展示增加多种展示 


