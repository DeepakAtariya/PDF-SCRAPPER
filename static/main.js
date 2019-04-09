var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        console.log("server calling is done");
        document.getElementById("spinner").style.display="none";
        document.getElementById("header").innerHTML = this.responseText;

   }
};

xhttp.open("GET", "http://localhost:5000/", true);
xhttp.send(); 


function loadDoc() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("demo").innerHTML = this.responseText;
       }
    };

    var args = document.getElementById("in").value;
    // var url = "https://www.w3schools.com/js/js_htmldom_eventlistener.asp";
    xhttp.open("GET", "http://localhost:5000/test?text="+args, true);
    xhttp.send(); 
}

// document.getElementById("in").addEventListener("onkeypress", loadDoc);