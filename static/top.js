document.writeln("<!DOCTYPE html>");
document.writeln("<html>");
document.writeln("    <head>");
document.writeln("        <title>协励行(厦门)绝缘科技有限公司</title>");
document.writeln("        <link rel=\'stylesheet\' href=\'static/style.css\'>");
document.writeln("        <meta charset=\'utf-8\' />");
document.writeln("    </head>");
document.writeln("<body>");
document.writeln("<p><center><h1>欢迎进入协励行(厦门)绝缘科技有限公司办公系统</h1></center></p>");
document.writeln("        <ul >");
document.writeln("            <li class=\'dropdown\'>");
document.writeln("                <a id=\'a\' href=\'javascript:void(0)\' class=\'dropbtn\' onclick=\'showList(this)\'>查询</a>");
document.writeln("                <div class=\'dropdown-content\' id=\'dropdown-a\'>");
document.writeln("                    <a href=\'/querystockexda\'>临近失效期库存查询</a>");
document.writeln("                    <a href=\'/querystock\'>库存查询</a>");
document.writeln("                    <a href=\'/currentstockdetail\'>库存重量明细汇总</a>");
document.writeln("		    <a href=\'/rqfrpr\'>运保查询</a>");
document.writeln("                    <a href=\'/rqdg\'>出货查询</a>");
document.writeln("                    <a href=\'/rqpi\'>进货查询</a>");
document.writeln("                    ");
document.writeln("                </div>");
document.writeln("            </li>");
document.writeln("            <li class=\'dropdown\'>");
document.writeln("                <a id=\'b\' href=\'javascript:void(0)\' class=\'dropbtn\' onclick=\'showList(this)\'>出货</a>");
document.writeln("                <div class=\'dropdown-content\' id=\'dropdown-b\'>");
document.writeln("                    <a href=\'/selectcustomer\'>出货文件号</a>");
document.writeln("                    <a href=\'/modifytobedealwith\'>待出货修改</a>");
document.writeln("                    <a href=\'/showdelieverydocument\'>生成出货单</a>");
document.writeln("                    <a href=\'/confirmdelievery\'>出货确认</a>");
document.writeln("                </div>");
document.writeln("            </li>");
document.writeln("            <li class=\'dropdown\'>");
document.writeln("                <a id=\'c\' href=\'javascript:void(0)\' class=\'dropbtn\' onclick=\'showList(this)\'>计算</a>");
document.writeln("                <div class=\'dropdown-content\' id=\'dropdown-c\'>");
document.writeln("                    <a href=\'/calculatefreight\'>运保费计算</a>");
document.writeln("                    <a href=\'/freightcalc\'>树脂运费计算器</a>");
document.writeln("			<a href=\'/changefp\'>树脂运保费更改</a>");
document.writeln("                </div>");
document.writeln("            </li>");
document.writeln("            <li class=\'dropdown\'>");
document.writeln("                <a id=\'d\' href=\'javascript:void(0)\' class=\'dropbtn\' onclick=\'showList(this)\'>入库</a>");
document.writeln("                <div class=\'dropdown-content\' id=\'dropdown-d\'>");
document.writeln("                    <a href=\'/putinwh\'>单条输入</a>");
document.writeln("                    <a href=\'/uploadfile\'>成批导入</a>");
document.writeln("                    <a href=\'/showinputdoc\'>生成进货单</a>");
document.writeln("                </div>");
document.writeln("            </li>");
document.writeln("            <li class=\'dropdown\'>");
document.writeln("                <a id=\'e\' href=\'javascript:void(0)\' class=\'dropbtn\' onclick=\'showList(this)\'>管理</a>");
document.writeln("                <div class=\'dropdown-content\' id=\'dropdown-e\'>");
document.writeln("                     <a href=\'/addnewuser\'>增加用户</a>");
document.writeln("                     <a href=\'/viewuser\'>用户浏览</a>");
document.writeln("                     <a href=\'/changepwd\'>更改密码</a>");
document.writeln("                     <a href=\'/deleteuser\'>删除用户</a>");
document.writeln("		<a href=\'/customerinfoinput\'>客户信息输入</a>");
document.writeln("                </div>");
document.writeln("            </li>");
document.writeln("        </ul>");
document.writeln("        <script src=\'static/script.js\'></script>  ");
document.writeln("");