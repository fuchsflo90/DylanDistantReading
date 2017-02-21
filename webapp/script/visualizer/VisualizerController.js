Visualizer.VisualizerController = function(){

	var that = {};

	var visualizerModel = null;
	var visualizerView = null;

	var filepath = "";

	var init = function(){

		visualizerModel = Visualizer.VisualizerModel();
		visualizerView = Visualizer.VisualizerView();

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

		filepath = "file not found";
   
    	if ($('.mbutton.active').attr('value') == "significant_text_differences") {
        	filepath = "./data/" + $('#timeselector option:selected').attr('value') + "/words/dylan_int/stopwords_True" + "/significant_text_differences/" + $('#posselector option:selected').attr('value') + ".csv";
    	}

    	if ($('.mbutton.active').attr('value') == "ngrams") {
        	filepath = "./data/" + $('#timeselector option:selected').attr('value') + "/ngram/min3/dylan_int/stopwords_True" + "/" + $('#testselector option:selected').attr('value')+ "/" + $("#lengthselector option:selected").attr("value") + ".csv";
    	}
        
        console.log("versuche datei zu laden:" + filepath);
	};

	var forceReload = function(){

		visualizerView.clearChart();
		selectFile();
		visualizerView.generateView(filepath);

	};

	that.init = init;

	return that;
};