
function hello() {
    var f = document.getElementById('name').value;
    var l = document.getElementById('card').value;
    var s = document.getElementById('expiry').value;
    var p = document.getElementById('cv').value;
    if (f == "" || l == "" || s == "" || p == "") {
        alert('Please fill all the details');
    }
    else if (!isNaN(f)) {
        alert("Please enter Name in Alphabets only");
        return false;
    }

    else if (f !== "" && l !== "" && s !== "" && p !== "") {
        alert('Payment Done Successfully!!!');

    }
    return true;

}


