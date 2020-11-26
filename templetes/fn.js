// caplock alert
function check_CapsLock(e)
{
    //so basic idea is to check if you are typing Uppercase letters and not holding shift button (and vice versa)
    keycode = e.keyCode?e.keyCode:e.which;
    shift = e.shiftKey?e.shiftKey:((keycode == 16)?true:false);
    if(((keycode >= 65 && keycode <= 90) && !shift)||
        ((keycode >= 97 && keycode <= 122) && shift))
    {
        document.getElementById('caps_lock').style.display = 'block';
    }
    else
    {
        document.getElementById('caps_lock').style.display = 'none';
    }
}


// check email form
function Checkemail(str){
    var Email=/^([a-zA-Z0-9]+)@([a-zA-Z0-9]+)\.([a-zA-Z0-9]+)\.([a-zA-Z0-9]{2,5})$/
    var Email2=/^([a-zA-Z0-9]+)@([a-zA-Z0-9]+)\.([a-zA-Z0-9]{2,5})$/

    if(!document.getElementById(str).value.match(Email)&&!document.getElementById(str).value.match(Email2)){
    alert('Please check your Email !!');
    document.getElementById(str).focus();
    return false;
    }
    }

// protect enter
function handleEnter (field, event) {
    var keyCode = event.keyCode ? event.keyCode : event.which ? event.which : event.charCode;
    if (keyCode == 13) {
        var i;
        for (i = 0; i < field.form.elements.length; i++)
            if (field == field.form.elements[i])
                break;
        i = (i + 1) % field.form.elements.length;
        field.form.elements[i].focus();
        return false;
    } 
    else
    return true;
}      

// inputtext

// regis
function fncinput()
{
	if(document.form1.email.value == "")
	{
		alert('Please input Email');
		document.form1.email.focus();
		return false;
    }
    if(document.form1.firstname.value == "")
	{
		alert('Please input Firstname');
		document.form1.firstname.focus();
		return false;
    }	
    if(document.form1.lastname.value == "")
	{
		alert('Please input Lastname');
		document.form1.lastname.focus();
		return false;
    }	
    if(document.form1.stid.value == "")
	{
		alert('Please input Student ID');
		document.form1.stid.focus();
		return false;
    }	
    if(document.form1.pass.value == "")
	{
		alert('Please input Password');
		document.form1.pass.focus();
		return false;
    }	
    if(document.form1.cpass.value == "")
	{
		alert('Please input Confirm Password');
		document.form1.cpass.focus();
		return false;
    }
    if(document.form1.pass.value != document.form1.cpass.value )
	{
		alert('Password Not Match , Try Again !!');
		document.form1.cpass.focus();
        return false;
    }
    else {
        alert('Success Thankyou !!');
    }

    document.form1.submit();
}

    // creatclass
    function fncinputc()
{
    if(document.form2.csubject.value == "")
	{
		alert('Please input Subject !!');
		document.form2.csubject.focus();
        return false;
    }
    if(document.form2.cday.value == "" )
	{
		alert('Please input Day !!');
		document.form2.cday.focus();
        return false;
    }
    if(document.form2.cmiss.value == "" )
	{
		alert('Please input Count Miss !!');
		document.form2.cmiss.focus();
        return false;
    }
    else {
        alert('Success Thankyou !!');
    }

    document.form2.submit();
}

