var iMaxFilesize = 2097152; //2M
    function imgPreview(fileDom){
        //判断是否支持FileReader
        if (window.FileReader) {
            var reader = new FileReader();
        } else {
            alert("您的设备不支持图片预览功能，如需该功能请升级您的设备！");
        }

        //获取文件
        var file = fileDom.files[0];
        var imageType = /^image\//;
        //是否是图片
        if (!imageType.test(file.type)) {
            alert("请选择图片！");
            return;
        }
        if (file .size > iMaxFilesize) {
            alert("图片大小不能超过2M");
            return;
        }
        //读取完成
        reader.onload = function(e) {
            //获取图片dom
            var img = document.getElementById("preview");
            //图片路径设置为读取的图片
            img.src = e.target.result;
        };
        reader.readAsDataURL(file);
        alert(document.getElementById("file"))
    }
//读取本地文件
// //读取本地文件
// var inputOne = document.getElementById('fileOne');
// inputOne.onchange = function () {
//     //1.获取选中的文件列表
//     var fileList = inputOne.files;
//     var file = fileList[0];
//     //读取文件内容
//     var reader = new FileReader();
//     reader.readAsDataURL(file);
//     reader.onload = function (e) {
//         //将结果显示到canvas
//         showCanvas(reader.result);
//     }
// }
// //指定图片内容显示
// function showCanvas(dataUrl) {
//     console.info(dataUrl);
//     var canvas = document.getElementById('canvasOne');
//     var ctx = canvas.getContext('2d');
//     //加载图片
//     var img = new Image();
//     img.onload = function () {
//         ctx.clearRect(0, 0, canvas.width, canvas.height);
//         ctx.drawImage(img, 0, 0, img.width, img.height);
//     }
//     img.src = dataUrl;
//     // document.body.appendChild(img);
// }