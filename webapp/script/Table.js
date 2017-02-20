DiscourseAnalysis.Table = (function() {

var that = {},
data,
anchoring,


init = function(tdata, anchor){
	data = tdata;
	anchoring = anchor;
	//console.log(anchoring);
_fillTable();
},

_fillTable = function(){

for (var i = 1; i < data.length; i++){
	if (data[i][1] === undefined){
		return;
	}
  $(anchoring + ' tr:last').after('<tr><td class="rnk">' + i + '.' + '</td><td class="wrd">' + data[i][0] + '</td><td class="vl">' + data[i][1] + '</td></tr>');
}

};
that.init = init;
return that;
}());