# Huatec 高校综合管理系统

基于 Flask 的高校综合管理平台，提供教务、人事、会务、资源等管理功能。

## 技术栈

| 类别 | 技术 |
|------|------|
| 框架 | Flask |
| ORM | SQLAlchemy |
| 数据库 | MySQL |
| 数据库迁移 | Flask-Migrate |
| 表单验证 | WTForms |
| 前端模板 | Jinja2 + Bootstrap |

## 项目结构

```
huatec/
├── app.py                 # 应用入口
├── models.py              # 数据模型
├── exts.py                # Flask扩展初始化
├── decorators.py          # 自定义装饰器
├── blueprints/            # 蓝图模块
│   ├── __init__.py
│   ├── login.py          # 登录/注册
│   ├── home.py           # 首页
│   ├── system.py         # 系统管理
│   ├── project.py        # 项目管理
│   ├── jiaowu.py         # 教务管理
│   ├── administration.py  # 行政管理
│   ├── affair.py         # 会务管理
│   └── resource.py       # 资源管理
├── templates/             # 前端模板
│   ├── login/           # 登录注册页面
│   ├── Home/            # 首页
│   ├── system/          # 系统管理页面
│   ├── project/         # 项目管理页面
│   ├── jiaowu/          # 教务管理页面
│   ├── administration/   # 行政管理页面
│   ├── affair/          # 会务管理页面
│   ├── resource/        # 资源管理页面
│   └── user/            # 用户个人页面
├── migrations/          # 数据库迁移文件
└── static/              # 静态资源
```

## 功能模块

### 1. 用户认证
- 用户注册
- 用户登录/登出
- 账户注销

### 2. 系统管理
- 用户管理
- 系统设置

### 3. 项目管理
- 基础信息管理
- 专业管理
- 学生管理
- 人员管理
- 资产管理
- 培训管理

### 4. 教务管理
- 成绩管理
- 考试管理
- 教学评价

### 5. 行政管理
- 入职办理
- 离职办理

### 6. 会务管理
- 会议管理
- 会务管理

### 7. 资源管理
- 学习资源
- 项目资源

## 快速开始

### 环境要求
- Python 3.7+
- MySQL 5.7+

### 安装依赖

```bash
pip install flask flask-sqlalchemy flask-migrate pymysql wtforms
```

### 配置

在项目根目录创建 `config.py`:

```python
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost:3306/huatec'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

### 初始化数据库

```bash
# 初始化迁移
flask db init

# 生成迁移脚本
flask db migrate -m "initial migration"

# 执行迁移
flask db upgrade
```

### 运行

```bash
python app.py
```

访问 `http://localhost:5000` 即可使用系统。

## 数据模型

### UserModel
用户表，存储用户基本信息。

| 字段 | 类型 | 说明 |
|------|------|------|
| id | Integer | 主键 |
| username | String(50) | 用户名(唯一) |
| password | String(200) | 密码 |
| sex | Integer | 性别 |
| join_time | DateTime | 注册时间 |
| modify_time | DateTime | 修改时间 |

### basicModel
基础信息表，存储学校/机构基础信息。

| 字段 | 类型 | 说明 |
|------|------|------|
| id | Integer | 主键 |
| name | String(200) | 名称 |
| school | String(200) | 学校/机构 |
| phone | String(200) | 电话 |
| email | String(200) | 邮箱 |
| zip | String(200) | 邮编 |
| address | String(200) | 地址 |
| creat_time | DateTime | 创建时间 |

## 路由清单

| 路由 | 功能 |
|------|------|
| `/` | 首页/登录页 |
| `/login` | 登录 |
| `/register` | 注册 |
| `/logoff` | 退出登录 |
| `/logout` | 注销账户 |
| `/home` | 首页 |
| `/system` | 系统管理 |
| `/s_user` | 用户管理 |
| `/project` | 项目管理 |
| `/p_basic` | 基础信息 |
| `/p_major` | 专业管理 |
| `/p_student` | 学生管理 |
| `/p_people` | 人员管理 |
| `/p_asset` | 资产管理 |
| `/p_training` | 培训管理 |
| `/jiaowu` | 教务管理 |
| `/j_score` | 成绩管理 |
| `/j_exam` | 考试管理 |
| `/j_evaluation` | 教学评价 |
| `/administration` | 行政管理 |
| `/a_entry` | 入职办理 |
| `/a_fire` | 离职办理 |
| `/affair` | 会务管理 |
| `/a_conference` | 会议管理 |
| `/a_huiwu` | 会务管理 |
| `/resource` | 资源管理 |
| `/r_study` | 学习资源 |
| `/r_project` | 项目资源 |

## API 接口

| 接口 | 方法 | 功能 |
|------|------|------|
| `/search_basic` | POST | 搜索基础信息 |
| `/add_basic` | POST | 添加基础信息 |

## 注意事项

1. 首次使用需配置数据库连接信息
2. 请在生产环境修改 `SECRET_KEY`
3. 建议使用虚拟环境隔离依赖
