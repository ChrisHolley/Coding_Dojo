function psrl(tarr) {
    var sml = tarr[0]
    var lrg = tarr[0]
    for(var i = 0; i < tarr.length; i++){
        if(sml > tarr[i]){
            sml = tarr[i];
        }
        if(lrg < tarr[i]){
            lrg = tarr[i];
        }
    }
    
    console.log(sml);
    return lrg;
}
var arr = [8,3,2,5,7]
var large = psrl(arr)

console.log(large)