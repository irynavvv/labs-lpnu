var n = 0;
var i = 0;
var s = 0;
document.write("Please enter value for N\n");
document.write("<br>");
n = prompt("Please enter value for N");
s = 0;
for (i = 1; i < n; i++) {
    if (i % 2 == 0) {
        s = s + i;
    }
    document.write("Current value i=" + i + " S=" + s + "\n");
    document.write("<br>");
}
document.write("Final result suma is S=" + s);
