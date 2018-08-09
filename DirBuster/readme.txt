不管是渗透还是拿一个网站，获取这个网站目录的一些信息，了解网站结构是很有用的。
像网站后台的地址，网站的一些文件上传地址，有时候也会获取到一些网站的源代码。
能实现以上功能等工具是就DirBuster，
DirBuster是用来探测web服务器上的目录和隐藏文件的。因为DirBuster是采用java编写的，所以运行前要安装上java的环境。

基本的使用：
①：TargetURL下输入要探测网站的地址，需要注意的是这个地址要加上协议，看网站是http还是https。
②：WorkMethod是选择工作方式，一个是get请求，一个是自动选择。一般选autoswitch的自动选择，它会自行判断是使用head方式或get方式。
③：NumberofThread是选择扫描线程数，一般为30。电脑配置好的可根据情况选择。
④：selectscanningtype是选择扫描类型。listbasedbruteforce是使用字典扫描的意思，勾选上。
随后browse选择字典文件，可用自己的，也可用dirbuster自己的。
⑤：selectstartingoptions选项一个是standardstartpoint（固定标准的名字去搜），一个是urlfuzz（相当于按关键字模糊搜索），
选择urlfuzz，随后在urltofuzz框中输入{dir}即可

配置好后点击start开始即可。有时候你可能看不到开始按钮，把鼠标放到软件边拖动一下大小，放下下界面就会显示出来。
DirBuster不仅可以暴力猜解目录，还可以进行蜘蛛爬行。

DirBuster官方网站 https://www.owasp.org/index.php/Category:OWASP_DirBuster_Project
