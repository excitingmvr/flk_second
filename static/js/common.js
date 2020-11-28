// includeJs("./util.js")
// includeJs("./validation.js")

document.write("<script type='text/javascript' src='/static/js/constants.js?ver=0.0.1'></script>");
document.write("<script type='text/javascript' src='/static/js/util.js?ver=0.0.1'></script>");
document.write("<script type='text/javascript' src='/static/js/validation.js?ver=0.0.1'></script>"); 

// inputName = "";

commonTest = function() {
    alert("commonTest");
}


$(document).on("click", ".attachedButton", function() {
    inputSelector = "input[name=" + $(this).data("inputfilename") + "]";
    inputName = $(this).data("inputfilename");
    $(inputSelector).click();
});


$(document).on("change", "input[type=file]", function(e){
    var files = e.target.files;
    var arr = Array.prototype.slice.call(files)
    var i = 0;
    var totalFileSize = $("#boardAttachedSize_" + inputName).text();
    var attacehdFileNum;

    if($(this).data("type") == "image") {
        attacehdFileNum = $("div[id^=attached_" + inputName + "]").length;
    } else {
        attacehdFileNum = $("p[id^=attached_" + inputName + "]").length;
    }

    if($(this).data("maxfilenum") == "" || $(this).data("maxfilenum") == null){
        maxFileNum = _maxFileNum;
    } else { 
        maxFileNum = $(this).data("maxfilenum");
    }
                     
    if($(this).data("maximagefilesize") == "" || $(this).data("maximagefilesize") == null){
        maxImageFileSize = _maxImageFileSize;
    } else {
        maxImageFileSize = $(this).data("maximagefilesize");
    }

    if($(this).data("maxfilesize") == "" || $(this).data("maxfilesize") == null){
        maxFileSize = _maxFileSize;
    } else {
        maxFileSize = $(this).data("maxfilesize");
    }

    checkFileNum(Number(arr.length) + Number(attacehdFileNum));

    if($(this).data("type") == "image") {
        arr.forEach(function(f){
            var str = "";
            var reader = new FileReader(); 
            reader.onload = function (e) {
                totalFileSize = (Number(totalFileSize) + Number(bytesToMega($(inputSelector)[0].files[i].size))).toFixed(2);

                str += '<div id="attached_' + inputName + '_' + (Number(i) + Number(attacehdFileNum)) + '" style="width: 100px; float: left;">';
                str += '<img src="' + e.target.result + '" width="100px" height="100px"><p><span onclick="deleteAttached(\''+ inputName + '\',' + (Number(i) + Number(attacehdFileNum)) + ',' + bytesToMega($(inputSelector)[0].files[i].size) + ')" style="cursor:pointer">X</span> ' + reduceStirng(f.name, 5) + '</p>';
                str += '</div>'; 
                $(str).appendTo('#boardAttached_' + inputName);

                $("#boardAttachedSize_" + inputName).text(addComma(totalFileSize));
                i = i + 1;
            }
            reader.readAsDataURL(f);
        });
    } else {
        var str = "";
        for(i = 0 ; i < $(inputSelector)[0].files.length ; i++) {
            totalFileSize = (Number(totalFileSize) + Number(bytesToMega($(inputSelector)[0].files[i].size))).toFixed(2);

            str = '<p id="attached_' + inputName + '_' + (Number(i) + Number(attacehdFileNum)) + '"><span onclick="deleteAttached(\''+ inputName + '\',' + (Number(i) + Number(attacehdFileNum)) + ',' + bytesToMega($(inputSelector)[0].files[i].size) + ')" style=cursor:pointer>X</span> ' + $(inputSelector)[0].files[i].name + '</p>';
            $(str).appendTo('#boardAttached_' + inputName)

            $("#boardAttachedSize_" + inputName).text(addComma(totalFileSize));
        }
    }
});


deleteAttached = function(inputName, num, size) {
    var attachedId = "#attached_" + inputName + "_" + num;
    $(attachedId).remove();
    fileSize = Number($("#boardAttachedSize_" + inputName).text()) - Number(size);
    if ( fileSize < 0 ) {
        fileSize = 0;
    } else {
        // pass
    }
    $("#boardAttachedSize_" + inputName).text(fileSize.toFixed(2));
}


checkFileNum = function(num) {
    if(maxFileNum < num){
        alert("Max number of files allowed : " + maxFileNum);
        this.val("");
    } else { /* pass */ }
}


checkFileSize = function(attachedFileSize) {
    if(_maxImageFileSize > attachedFileSize) {
        alert("Max total file size allowed : " + _maxImageFileSize);
        this.val("");
    } else { /* pass */ }
}


addComma = function(str) {
    str = String(str);
    return str.replace(/(\d)(?=(?:\d{3})+(?!\d))/g, '$1,');
}


bytesToMega = function(num) {
    return (num / 1048576).toFixed(2);
}


datetimeClient = function() {
    var datetime = new Date();
    var year = datetime.getFullYear();
    var month = '' + (datetime.getMonth() + 1);
    var date = '' + datetime.getDate();
    var hour = '' + datetime.getHours();
    var minute = '' + datetime.getMinutes()
    var second = '' + datetime.getHours();

    if(month.length < 2) month = '0' + month;
    if(date.length < 2) date = '0' + date;
    if(hour.length < 2) hour = '0' + hour;
    if(minute.length < 2) minute = '0' + minute;
    if(second.length < 2) second = '0' + second;

    return year+"-"+month+"-"+date+" "+hour+":"+minute+":"+second;
}


offsetClient = function() {
    return -(new Date().getTimezoneOffset() / 60);
}
