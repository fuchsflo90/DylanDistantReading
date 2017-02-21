DiscourseAnalysis.Datamanager = (function() {

var that = {},
dataSlice = 50,
data,

init = function (dataSlice){
that.dataSlice = dataSlice;
},

readFile = function (path, handler){
    var xhr = new XMLHttpRequest();
    xhr.open("GET", path, true);
    xhr.onload = function (e) {
      if (xhr.readyState === 4) {
        if (xhr.status === 200) {
          if (handler != undefined){
          handler(_processCSVData(xhr.responseText));
          } else {
            _processCSVData(xhr.responseText);
          }
        } else {
          console.error(xhr.statusText);
        }
      }
    };
    xhr.onerror = function (e) {
      console.error(xhr.statusText);
    };
    xhr.send(null);
},

 _processCSVData = function (output) {
    Papa.parse(output, {
        complete: function(results) {
            data = results.data
        }
    });
    data = data.slice(0, dataSlice);
    return data;
}, 

returnFile = function (){
return data;
};

that.init = init;
that.readFile = readFile;
that.returnFile = returnFile;

return that;
}());