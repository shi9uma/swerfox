# ~~【幼盾】~~【杉蔚狐】个性化图片徽章服务！

![](https://unv-shield.librian.net/api/unv_shield?txt=赞美莉沫酱！&scale=4&anime=3)

**这里再放三个徽章：斯达数、"代码质量：抽象"、"黄毛狐狸控：是"**

你还在因为 [Shanwer](https://github.com/Shanwer) 能量不足而感到难过吗？想要在自己的项目中插入 sw 徽章（语录）吗？快来使用 swerfox 个性化图片徽章服务吧！


## 使用方法！


```markdown
![](https://domain.com/api/swerfox?repo=你的名字/repo的名字)

例如：![](https://majo.im/api/swerfox?repo=shi9uma/swerfox)
```

把这行代码加入到你的 readme 中，就会显示成一个徽章，像是这样：

**这里放一个展示 repo 斯达数的徽章**

## 自定义！

通过向 url 传递不同的参数来自定义你的徽章，首先魔法起手式：`https://domain.com/api/swerfox?args`，后面接的 args 参数可以如下（使用 `&` 符来连接多个参数）！

- `url`：`url=https://avatars.githubusercontent.com/u/16631550`，换显示的图标！**这里放一个换了图标的徽章**
    
- `backcolor`：`backcolor=0000ff`，来设定背景颜色，默认的背景颜色会随图片改变，是自动生成的！**这里放一个换了背景颜色的徽章**
    
- `fontcolor`：`fontcolor=0000ff`，来设定文字的颜色，默认的文字颜色取决于背景颜色，通常使用白字，背景颜色的亮度高时使用黑字！**这里放一个换了字体颜色的徽章**
    
- `scale`：`scale=2`，来让你的徽章整个等比例放大！**这里放一个放大了的徽章**
    
- `text`：`text=草`，来显示徽章的文本！**这里放一个显示文本的徽章**
    
    > 样例: `txt=你好呀!`  
    > ![](https://unv-shield.librian.net/api/unv_shield?txt=你好呀!) 
    
    把字换掉。
    
- `border`：`border=4`，来设置徽章的边距和阴影扩散范围！**太麻烦了我不想写了**
    
- `barlen`：`barlen=10`，来设定徽章的文字条的长度，默认的长度是由文本决定的！
    
- `size`：`size=50`，设定徽章尺寸，但是字号不会变！
    
- `fontsize`：`frontsize=30`，可以设定字体大小了！
    
- `barradius`：`barradius=999`，设定文本条的援交！
    
- `anime`：`anime=5`，还可以设定文本条弹出的动画时间！
    
- `shadow`：`shadow=0.9`，设定背景阴影的浓度！

- `repo`：`repo=account_name/repo_name`，**特殊参数**，可以主动获得对应 repo 的名字和斯达数！


## 服务架构看不懂啦！

![./文档/q.png](./文档/q.png)

- 服务的核心是Azure上的一个Function App<sub>(FAAS)</sub>。
- 用cloudflare做了一层HTTP缓存，可以省钱。
- 通过GitHub访问时还会过一层Camo缓存。
- 活死人的呼声是一个定时触发器，用来防止unv-shield冷启动。


## ❤赞助❤

如果你觉得 swerfox 对你的工作或学习有所帮助，欢迎往作者：[RimoChan](https://github.com/RimoChan) 的邮箱 <[the@librian.net](mailto:the@librian.net)> 里发萝莉图片以表达谢意！**（不要发给我！）**
