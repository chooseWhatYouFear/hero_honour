# hero_honour
django做的一个关于王者荣耀的小项目
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>英雄头像</title>
    <style type="text/css">
        #div{
            width: 550px;
            height: 75px;
        }
        #div img{
            margin-top: 10px;
            margin-right: 11px;
        }
    </style>
</head>
<body>
    <img src="//game.gtimg.cn/images/yxzj/img201606/heroimg/503/503.jpg" alt="" width="500px" height="300px" style="display: block">
    <div id="div">
        <img src="//game.gtimg.cn/images/yxzj/img201606/heroimg/503/503.jpg" alt="" width="70px" height="75px" >
        <img src="//game.gtimg.cn/images/yxzj/img201606/heroimg/195/195.jpg" alt="" width="70px" height="75px" >
        <img src="//game.gtimg.cn/images/yxzj/img201606/heroimg/183/183.jpg" alt="" width="70px" height="75px" >
        <img src="//game.gtimg.cn/images/yxzj/img201606/heroimg/175/175.jpg" alt="" width="70px" height="75px" >
        <img src="//game.gtimg.cn/images/yxzj/img201606/heroimg/121/121.jpg" alt="" width="70px" height="75px" >
        <img src="//game.gtimg.cn/images/yxzj/img201606/heroimg/109/109.jpg" alt="" width="70px" height="75px" >
    </div>
</body>
</html>
<script type="text/javascript">
    var imgs = document.images;
//    console.log(imgs);
    var i = 2;
    function run() {
        t = setInterval(function () {
            imgs[0].src = imgs[i].src;
            for(var j=1;j<=6;j++){
                imgs[j].style.border='';
            }
            imgs[i].style.border='2px solid red';
            i++;
            if(i>6){
                i=1;
            }

        },800);
    }
    imgs[0].onmouseover = function () {
        clearInterval(t)
    };
    imgs[0].onmouseout = function () {
        run()
    };
    for(var k=1;k<=6;k++){
        imgs[k]['index']=k;
        imgs[k].onmouseover = function () {
            clearInterval(t);
            for(var j=1;j<=6;j++){
                imgs[j].style.border='';
            }
            this.style.border='2px solid red';
            imgs[0].src = this.src;
        };
        imgs[k].onmouseout = function () {
            if(this.index<6){
                i=this.index+1;
            }else{
                i=1;
            }

            run()
        };
    }
    run()
</script>
