//针对log页定义一个对象
var log = {
    startdt: "2021-4-27",
    enddt: "2021-5-5",
    upatedt: "2021-4-27",
    anchor: "lidong"
}
//由对象派生业务逻辑
log.submit = {
    autohide: function (obj) {
        setTimeout(function () {
            obj.hide();
        }, 2000)
    },
}
function getByteLen(val) {
      var len = 0;
      for (var i = 0; i < val.length; i++) {
        var a = val.charAt(i);
        if (a.match(/[^\x00-\xff]/ig) != null) {
          len += 2;
        }
        else {
          len += 1;
        }
      }
      return len;
    }

function checkvalue() {
    //获取元素对象，并保存到变量中
    str = str.replace(/\s*/g,"");
    var $form = $("form");
    var $username = $("#username");
    var $password = $("#password");
    var $password2 = $("#password2");
    var $err1 = $("#err1");
    var $err2 = $("#err2");
    var $err3 = $("#err3");
    var reg = /^(?!(\d+)$)[\u4e00-\u9fffa-zA-Z\d\-_]{4,14}$/;
    var re=reg.test($username.val().replace(/\s*/g,""))
    var len= getByteLen($username.val().replace(/\s*/g,""))
    if ($username.val().replace(/\s*/g,"") == "") {
        $err1.text('请输入用户名')
        $err1.show();
        log.submit.autohide($err1);
        return false;
    } 
    else if (len>14){
        $err1.text('用户名不能超过7个汉字或14个字符')
        $err1.show();
        log.submit.autohide($err1);
        return false;
    }
    else if (! re) {
        $err1.text('用户名仅支持中英文、数字和下划线,且不能为纯数字')
        $err1.show();
        log.submit.autohide($err1);
        return false;
    }  
    
    else if ($password.val() == "") {
        $err2.show();
        log.submit.autohide($err2);
        return false;
    } 
    else if ($password.val() != $password2.val()) {
        $err3.show();
        log.submit.autohide($err3);
        return false;
    } 
    else {
        return true;
    }
}


