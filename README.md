# hero_honour
django做的一个关于王者荣耀的小项目

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>轮播图</title>
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
    <img src="../images/1-1.jpg" alt="" width="500px" height="300px" style="display: block">
    <div id="div">
        <img src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1562685104160&di=f27a6b86a63c849c2c8789f3f9338d82&imgtype=0&src=http%3A%2F%2Fpic.87g.com%2Fupload%2F2017%2F0102%2F20170102085935367.jpg" alt="" width="70px" height="75px" >
        <img src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1562685104244&di=424e8eb60fd8752a9e53145c34eff764&imgtype=0&src=http%3A%2F%2Fimage.uczzd.cn%2F14357560211971134267.jpg" alt="" width="70px" height="75px" >
        <img src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1562685104244&di=c113767f171540f2bb4f5c461b3d55d3&imgtype=0&src=http%3A%2F%2Fimg1.famulei.com%2Fm%2F0%2Fp%2F178%2F1715462358279.jpg" alt="" width="70px" height="75px" >
        <img src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1562685104244&di=ef4d2fe6b5a1ed794e890a9d5ac076d2&imgtype=0&src=http%3A%2F%2Fi1.hdslb.com%2Fbfs%2Farchive%2Ffaa0aaa37898167dce8292961e42e4c28c685cc4.jpg" alt="" width="70px" height="75px" >
        <img src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1562685104244&di=23eed79767babca92a1a569016698dc5&imgtype=0&src=http%3A%2F%2Fwww.downxia.com%2Fuploadfiles%2F2017%2F0722%2F20170722042217658.jpg" alt="" width="70px" height="75px" >
        <img src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1562685104244&di=d195b197fa27f83b3914a59981faa5f4&imgtype=0&src=http%3A%2F%2Fwww.33lc.com%2Fuploadfile%2F2017%2F1015%2F20171015113647374.jpg" alt="" width="70px" height="75px" >
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
