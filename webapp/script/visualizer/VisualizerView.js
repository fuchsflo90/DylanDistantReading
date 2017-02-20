Visualizer.VisualizerView = function(){

	var that = {};

	var parliamentview = null;
	var electionsview = null;
	var testcloud = null;
	var corporainfoview = null;
	var wordcloudview = null;
	var treemapview = null;
	var chartview = null;
	var datamanager = null;

	var barcolor = null;
	var anchor = null;

	var init = function(){
		initClickAndChangeEvents();
		initializeViewScripts();
		setupView();
	};

	var initClickAndChangeEvents = function(){

		$('#absolute_freq').click(function() {
    		$(this).addClass('active');
    		$('#menu_ngram').addClass('hide');
    		$('#posselector').removeClass('hide');
    		$('#freq_profiling').removeClass('active');
    		$('#ngrams').removeClass('active');
    		$(that).trigger("reload");
		});

		$('#freq_profiling').click(function() {
    		$(this).addClass('active');
    		$('#menu_ngram').addClass('hide');
    		$('#posselector').removeClass('hide');
    		$('#absolute_freq').removeClass('active');
    		$('#ngrams').removeClass('active');
   			$(that).trigger("reload");
		});

		$('#ngrams').click(function() {
    		$(this).addClass('active');
    		$('#menu_ngram').removeClass('hide');
    		$('#posselector').addClass('hide');
    		$('#absolute_freq').removeClass('active');
    		$('#freq_profiling').removeClass('active');
    		$(that).trigger("reload");
		});

		$("#partei_a").click(function() {
    		barcolor = '#1f77b4';
    		$('.button.active').removeClass("active");
    		$('#s3').removeClass("unable").css("pointer-events", "auto");
    		$('#s4').removeClass("unable").css("pointer-events", "auto");
    		$(this).addClass("active");
    		if($(".view.smallbutton.active").attr('id') == 's2'){
        		$('#contentwrapper').css("background", "rgba(0,43,97, 0.89)");
    		}
    		wordcloudview.init(100, 70);
   			$(that).trigger("reload");
		});

		$("#partei_b").click(function() {
    		barcolor = '#77b41f';
    		$('.button.active').removeClass("active");
    		$('#s3').removeClass("unable").css("pointer-events", "auto");
    		$('#s4').removeClass("unable").css("pointer-events", "auto");
    		$(this).addClass("active");
    		if($(".view.smallbutton.active").attr('id') == 's2'){
        		$('#contentwrapper').css("background", "rgba(0,97,43, 0.89)");
    		}
    		wordcloudview.init(100, 70);
    		$(that).trigger("reload");
		});

		$("#partei_both").click(function() {
    		$('#s3').addClass("unable").css("pointer-events", "none");
    		$('#s4').addClass("unable").css("pointer-events", "none");
    		$('.button.active').removeClass("active");
    		$(this).addClass("active");
    		if($(".view.smallbutton.active").attr('id') == 's2'){
        		$('#contentwrapper').css("background", "linear-gradient(to right, rgba(0,43,97, 0.89), rgba(0,97,43, 0.89))");
    		}
    		wordcloudview.init(49, 70);
   			$(that).trigger("reload");
		});

		$(".view.smallbutton").click(function() {
    		if ($(this).attr('id') == 's4'){
         		window.open(path);
        		return;
    		}
    		if ($(this).attr('id') == 's5'){
        		return;
    		}
    		if ($(this).attr('id') == 's2'){
         		id = $('.button.active').attr("id");

         		if (id == 'partei_a'){
            		$('#contentwrapper').css("background", "rgba(0,43,97, 0.89)");
         		}

         		if (id == 'partei_b'){
            		$('#contentwrapper').css("background", "rgba(0,97,43, 0.89)");
         		}

         		if (id == 'partei_both'){
            		$('#contentwrapper').css("background", "linear-gradient(to right, rgba(0,43,97, 0.89), rgba(0,97,43, 0.89))");
         		}
    		}
    		if ($(this).attr('id') == 's1' || $(this).attr('id') == 's3' || $(this).attr('id') == 's6'){
        		$('#contentwrapper').css("background", "none");
    		}

    		$(".view.smallbutton").removeClass('active');
    		$(this).addClass('active');
    		$(that).trigger("reload");
		});

		$("#methodselector").change(function() {
    		$(that).trigger("reload");
		});

		$("#lengthselector").change(function() {
    		$(that).trigger("reload");
		});

		$("#frequencyselector").change(function() {
    		$(that).trigger("reload");
		});

		$("#stopwordselector").change(function() {
    		$(that).trigger("reload");
		});

		$(".pos.smallbutton").click(function() {
    		$(".pos.smallbutton").removeClass('active');
    		$(this).addClass('active');
    		$(that).trigger("reload");
		});

		$('#s5').click(function() {

    		$('#png_img').attr("width", $('#chart0').width() + $('#chart1').width());
    		$('#png_img').attr("height", $('#chart0').height());

       		img2 = new Image();
    		if (document.getElementById('chart1').getElementsByTagName("svg")[0] !== undefined){
    			svgAsDataUri(document.getElementById('chart1').getElementsByTagName("svg")[0], {}, function(uri) {
        		img2.src = uri;
        		});
			}

     		img1 = new Image();
      		if (document.getElementById('chart0').getElementsByTagName("svg")[0] !== undefined){
    			svgAsDataUri(document.getElementById('chart0').getElementsByTagName("svg")[0], {}, function(uri) {
        		img1.src = uri;
        		});
			}

 
  			var canvas = document.querySelector("canvas");
  			var context = canvas.getContext("2d");

  			img1.onload = function() {
      			context.fillStyle = '#fff';
      			context.fillRect(0,0,canvas.width,canvas.height);
      			context.drawImage(img1, 0, 0);
      			context.drawImage(img2, $('#chart1').width(), 0);

      			var canvasdata = canvas.toDataURL("image/png");
      			var pngimg = '<img src="'+canvasdata+'">'; 
      			d3.select("#pngurl").html(pngimg);
      			var a = document.createElement("a");
      			a.href = canvasdata;
      			a.target = "_blank";
          		document.body.appendChild(a);
      			a.click();
    		};
			context.clearRect(0, 0, canvas.width, canvas.height);

		});

	};

	var initializeViewScripts = function(){
		parliamentview = DiscourseAnalysis.ParliamentView;
		parliamentview.init();
		parliamentview.generateParliament();

		electionsview = DiscourseAnalysis.ElectionsView;

    	testtable = DiscourseAnalysis.Table;

    	testcloud = DiscourseAnalysis.TestCloud;
    	testcloud.init(40, 40);

    	corporainfoview = DiscourseAnalysis.CorporaInfoView;
		corporainfoview.init("./meta/metainfo.json");

		chartview = DiscourseAnalysis.ChartView;
		chartview.init();

		wordcloudview = DiscourseAnalysis.WordcloudView;
		wordcloudview.init(100, 70);

		tableview = DiscourseAnalysis.Table;

		treemapview = DiscourseAnalysis.TreemapView;
		treemapview.init();

		$(that).trigger("ViewScriptsInitialized");
	};

	var setupView = function(){
		$('#b_start').addClass('selected');
    	$('#motivation').addClass('hide');
		$('#contentwrapper').addClass('start');
		$('.content').addClass('hide');
		$('#menu_ngram').addClass('hide');
		$('#partei_a').addClass('active');
		$('#absolute_freq').addClass('active');
		$("#s1").addClass('active');
		$("#w1").addClass('active');
		barcolor = '#1f77b4';
		anchor = '#chart0';
	};

	var readInputFiles = function(){

		datamanager = DiscourseAnalysis.Datamanager;
		datamanager.init(300);

		datamanager.readFile('../meta/nationalratswahlen.csv', function(data){ 
        	electionsview.init(datamanager.returnFile());
        	electionsview.generateElectionsChart();
    	});

    	datamanager.readFile('../meta/testwords.csv', function(data){ 
    		testtable.init(data, '#sampletable');
    	});

    	datamanager.readFile('../meta/testwords.csv', function(data){ 
        	testcloud.generateCloud(data, '#testcloud');
    	});
	};

	var generateView = function(path){

		datamanager = DiscourseAnalysis.Datamanager;
		datamanager.init(300);
		
		if (path.length == 2) {
        	for (var i = 0; i < path.length; i++) {
            	barcolor = '#1f77b4';
            	backgroundcolor= 'rgba(31,119,180, 0.05)';
            	if (i > 0) {
                	$('.chart').css('float', 'left');
                	anchor = '#chart' + i.toString();
                	barcolor = '#77b41f';
                	backgroundcolor = 'rgba(119,180,31, 0.05)';
            	}
            	generateView(path[i]);
        	}
        	return;
    	}
  
    	if ($(".view.smallbutton.active").attr('id') == 's1') {
        	datamanager.readFile(path, function(data){ 
            	chartview.generateChartView(anchor, barcolor, data);
        	});
    	}
    	if ($(".view.smallbutton.active").attr('id') == 's2') {
        	datamanager.readFile(path, function(data){ 
            	wordcloudview.generateCloud(data, anchor);
        	});
    	}
    	if ($(".view.smallbutton.active").attr('id') == 's6') {
        	$("#s5").addClass('unable').css("pointer-events", "none");
        	$(anchor).append('<h3 class="tableheading">Quelldatei: ' + path + '</h3>')
        	$(anchor).append('<table id="' + anchor.slice(1) + '_table' + '" class="valtable"><tr><th></th><th></th><th></th></tr></table>');
        	datamanager.readFile(path, function(data){ 
            	tableview.init(data, anchor + '_table');
        	});
        	return;
    	}
    	if ($(".view.smallbutton.active").attr('id') == 's3') {
        	$("#partei_both").addClass('unable').css("pointer-events", "none");
        	datamanager.readFile(path, function(data){ 
            	treemapview.generateTreemap(data, anchor);
        	});
        	return;
    	}
    	$("#s5").removeClass('unable').css("pointer-events", "auto");
    	$("#partei_both").removeClass('unable').css("pointer-events", "auto");
	};

	var clearChart = function(){
		$("#chart0").empty().removeAttr('class').removeAttr('style').attr('class', 'chart');
    	$("#chart1").empty().removeAttr('class').removeAttr('style').attr('class', 'chart');
    	anchor = '#chart0';
	};

	$( window ).resize(function() {
    	$(that).trigger("reload");
	});

	that.init = init;
	that.generateView = generateView;
	that.readInputFiles = readInputFiles;
	that.clearChart = clearChart;
	return that;
};