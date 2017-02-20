DiscourseAnalysis.CorporaInfoView = (function() {

var that = {},
metainfo,

init = function (path){

metainfo = jQuery.parseJSON(_readJSON(path));

/*$('#meta_gp').text(metainfo.general.gp);
$('#meta_start').text(metainfo.general.beginn);
$('#meta_tagger').text(metainfo.general.tagger);*/
$('#meta_name1').text(metainfo.partei_a.name);
$('#meta_sentences1').text(_trenner(metainfo.partei_a.sentences));
$('#meta_tokens1').text(_trenner(metainfo.partei_a.tokens));
$('#meta_name2').text(metainfo.partei_b.name);
$('#meta_sentences2').text(_trenner(metainfo.partei_b.sentences));
$('#meta_tokens2').text(_trenner(metainfo.partei_b.tokens));

},

//http://www.web-toolbox.net/webtoolbox/mathematik/tausender-trennzeichen.htm
_trenner = function (number) {
    number = '' + number;
    if (number.length > 3) {
        var mod = number.length % 3;
        var output = (mod > 0 ? (number.substring(0, mod)) : '');
        for (i = 0; i < Math.floor(number.length / 3); i++) {
            if ((mod == 0) && (i == 0))
                output += number.substring(mod + 3 * i, mod + 3 * i + 3);
            else
                output += '.' + number.substring(mod + 3 * i, mod + 3 * i + 3);
        }
        return (output);
    } else return number;
},

_readJSON = function (path) {
    var request = new XMLHttpRequest();
    request.open("GET", path, false);
    request.send(null);
    return request.responseText;
};

that.init = init;
//that.generateInfoView = generateInfoView;

return that;
}());