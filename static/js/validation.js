validationTest = function() {
    alert("validationTest");
}


checkNull = function(value, message) {
    if (value == "" || value == null) {
        alert(message);
        return false;
    } else {
        return true;
    }
}


checkPasswordAndRe = function(password, passwordRe, message){
    if(password == passwordRe){
        return true;
    } else {
        alert(message);
        return false;
    }
}


checkOnlyNumber = function(value) {
    var regExp = /^[0-9]+$/;
    if(regExp.test(value)) return true;
    else return false;
}


checkId = function(value) {
    var regExp = /^[A-Za-z0-9,_-]{4,20}$/ 
    if(regExp.test(value)) return true;
    else return false;
}


checkPassword = function(value) {
    var regExp = /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[!@#$%^&*]).{8,20}$/;
    if(regExp.test(value)) return true;
    else return false;
}


checkOnlyEnglish = function(value) {
    var regExp = /^[A-Za-z]+$/ 
    if(regExp.test(value)) return true;
    else return false;
}


checkDob = function(year, month, day, message) {
    if (Number(year) > 0 && Number(month) > 0 && Number(day) > 0){
        return true;
    } else {
        alert(message);
        return false;
    }
}


checkNullSelect = function(value, message) {
    if(Number(value) == 0){
        alert(message);
        return false;
    }
    else return true;
}