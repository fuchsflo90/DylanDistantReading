Visualizer.VisualizerController = function(){

	var that = {};

	var visualizerModel = null;
	var visualizerView = null;

	var filepath = "";

	var init = function(){

		visualizerModel = Visualizer.VisualizerModel();
		visualizerView = Visualizer.VisualizerView();

		selectFile();
		bindTriggers();

		visualizerView.init();
		visualizerModel.init();

		console.log("model and view initialized...");

	};

	var bindTriggers = function(){
		$(visualizerView).on("ViewScriptsInitialized", letViewReadInputFiles);
		$(visualizerView).on("reload", forceReload);
	};

	var letViewReadInputFiles = function(){
		visualizerView.readInputFiles();
	};

	var selectFile = function(){

		var filepath = "";

    	if ($('.button.active').attr('value') == "both") {
        	selectFiles();
    	}
   
    	if ($('.mbutton.active').attr('value') == "ngrams") {
        	filepath = "./ngram/" + $('#frequencyselector').val() + "/" + $('.button.active').attr('value') + "_XXV/" + $('#stopwordselector').val() + "/" + $('#methodselector').val() + "/" + $('#lengthselector').val() + ".csv";
        	path = filepath;
    	}
    
    	filepath = "./words/" + "dylan_rest/" + "stopwords_True" + "/" + $('.mbutton.active').attr('value') + "/" + $(".pos.smallbutton.active").attr('title') + ".csv";
    	console.log("datei geladen:" + filepath);
    	path = filepath;
	};

	var selectFiles = function(){

		var filepaths = new Array(2);

    	if ($('.mbutton.active').attr('value') == "ngrams") {
        	filepaths[0] = "./ngram/" + $('#frequencyselector').val() + "/" + "fpö" + "_XXV/" + $('#stopwordselector').val() + "/" + $('#methodselector').val() + "/" + $('#lengthselector').val() + ".csv";
        	filepaths[1] = "./ngram/" + $('#frequencyselector').val() + "/" + "grüne" + "_XXV/" + $('#stopwordselector').val() + "/" + $('#methodselector').val() + "/" + $('#lengthselector').val() + ".csv";
        	path = filepath;
    	}

        filepaths[0] = "./words/" + $('#partei_a').attr('value') + "_XXV/" + $('#stopwordselector').val() + "/" + $('.mbutton.active').attr('value') + "/" + $(".pos.smallbutton.active").attr('title') + ".csv";
        filepaths[1] = "./words/" + $('#partei_b').attr('value') + "_XXV/" + $('#stopwordselector').val() + "/" + $('.mbutton.active').attr('value') + "/" + $(".pos.smallbutton.active").attr('title') + ".csv";

    	path = filepath;
	};

	var forceReload = function(){

		visualizerView.clearChart();
		selectFile();
		visualizerView.generateView(path);

	};

	that.init = init;

	return that;
};