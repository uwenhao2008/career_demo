//获取当前按钮的 name
function loadXMLDoc(e){
    console.log("标志进入xml函数，按钮id为-->"+e.id);
    ip = document.getElementById(e.id).parentNode.previousElementSibling.previousElementSibling.innerHTML;
    console.log("点击按钮这行的ip地址为："+ip)
    var xml;
    if (window.XMLHttpRequest){// code for IE7+, Firefox, Chrome, Opera, Safari
        xml=new XMLHttpRequest();
     }
    else{// code for IE6, IE5
        xml=new ActiveXObject("Microsoft.XMLHTTP");
     }
    var queryString = "../ajaxTot/";
    queryString = queryString + "?p=" + e.id + "&q="+ip;  //搞了半天，原来是这里的编码问题，而且还是？ 问号的缘故  英文和中文问号的区别
    // 英文 ?  encodeURIComponent  %3F  中文 ？  encodeURIComponent   %EF%BC%9F  三个字节
    // console.log(queryString)
    xml.onreadystatechange=function(){
        if (xml.readyState==4 && xml.status==200){
            console.log("点击的按钮id为"+e.id);
            console.log("服务器返回的内容为："+xml.responseText)  //高了半天控制台的输出是来自这里
        }
    }
    xml.open("GET",queryString,true);  //这里不要多此一举，写成"../templates/ajaxTot/"
    //xml.open("GET","../ajaxTot/?p="+e.id+"&q="+ip,true);  //这里不要多此一举，写成"../templates/ajaxTot/"
    //                ../ajaxTot/?p=del_id_7&q=192.168.1.127  只有这么对比才看出来细微区别....
    xml.send();
}