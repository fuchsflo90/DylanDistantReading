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
        $(that).trigger("reload");
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


		$(".viewselectorbutton").click(function() {
            console.log("button wurde gedrückt");

    		if ($(this).attr('id') == 's4'){
                $(that).trigger("downloadcsv");
        		return;
    		}
    		if ($(this).attr('id') == 's5'){
        		return;
    		}
    		if ($(this).attr('id') == 's2'){
                $('#contentwrapper').css("background", "none");
    		}
    		if ($(this).attr('id') == 's1' || $(this).attr('id') == 's3' || $(this).attr('id') == 's6'){
        		$('#contentwrapper').css("background", "none");
    		}

    		$(".viewselectorbutton").removeClass('active');
    		$(this).addClass('active');
    		$(that).trigger("reload");
		});

		/*$("#methodselector").change(function() {
            if(wholedylancorpus){
                $("#referencecorpusselector option[value='_int']").attr('selected',true);
            }
            $(".mbutton").removeClass("active");
            $("#methodselector option:selected").addClass("active");

            if($("#methodselector option:selected").attr("value") == "significant_text_differences"){
                $(".viewselector2").addClass("hide");
                $(".posmenu").removeClass("hide");
                $("#corpusselector").removeClass("hide");
            }
            if($("#methodselector option:selected").attr("value") == "ngrams"){
                $(".viewselector2").removeClass("hide");
                $(".posmenu").addClass("hide");
                $("#corpusselector").addClass("hide");
            }

    		$(that).trigger("reload");
		});*/

        $("#methodselector").change(function() {
            
            $(".mbutton").removeClass("active");
            $("#methodselector option:selected").addClass("active");

            if($("#methodselector option:selected").attr("value") == "significant_text_differences"){
                $(".viewselector2").addClass("hide");
                $(".posmenu").removeClass("hide");
                $("#corpusselector2 button").prop("disabled",false);
            }

            if($("#timeselector option:selected").prop("value") == "1960-2019"){
                $("#corpusselector2 button").removeClass("active");
                $("#corpusselector2 button[value='_anc']").addClass("active");
                $("#corpusselector2 button").prop("disabled",true);
            }

            if($("#methodselector option:selected").attr("value") == "ngrams"){
                $(".viewselector2").removeClass("hide");
                $(".posmenu").addClass("hide");
                $("#corpusselector2 button").prop("disabled",true);
            }
            $('.selectpicker').selectpicker();
            $(that).trigger("reload");
        });

		$("#lengthselector").change(function() {
    		$(that).trigger("reload");
		});

		$("#frequencyselector").change(function() {
    		$(that).trigger("reload");
		});

        $("#testselector").change(function() {
            $(that).trigger("reload");
        });

		$("#stopwordselector").change(function() {
    		$(that).trigger("reload");
		});

		$("#posselector").change(function() {
    		$(that).trigger("reload");
		});

       /* $("#timeselector").change(function() {
            if($("#timeselector option:selected").prop("value") == "1960-2019"){
                wholedylancorpus = true;
                $("#referencecorpusselector option[value='_anc']").prop('selected',true);
                $("#referencecorpusselector").prop("disabled", true);
                $("#referencecorpusselector").css({ opacity: 0.8 });
                console.log("alles gewählt");

            }else{
                wholedylancorpus = false;
                $("#referencecorpusselector option[value='_int']").attr('selected',true);
                $("#referencecorpusselector").prop("disabled", false);
                $("#referencecorpusselector").css({ opacity: 1.0 });
                console.log("nicht alles gewählt");
            }

            $(that).trigger("reload");
        });*/

        $("#timeselector").change(function() {
            if($("#methodselector option:selected").attr("value") == "ngrams"){
                $(that).trigger("reload");
                return;
            }
            if($("#timeselector option:selected").prop("value") == "1960-2019"){
                $("#corpusselector2 button").removeClass("active");
                $("#corpusselector2 button[value='_anc']").addClass("active");
                $("#corpusselector2 button").prop("disabled",true);
                console.log("alles gewählt");

            }else{
                $("#corpusselector2 button").prop("disabled",false);
                console.log("nicht alles gewählt");
            }

            $(that).trigger("reload");
        });

        $("#authorselector").change(function() {
            $(that).trigger("reload");
        });

        $("#referencecorpusselector").change(function() {
            $(that).trigger("reload");
        });

        $("#corpusselector2 button").click(function() {
            $("#corpusselector2 button").removeClass("active");
            $(this).addClass("active");
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

    	testtable = DiscourseAnalysis.Table;

    	testcloud = DiscourseAnalysis.TestCloud;
    	testcloud.init(40, 40);

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
		$('#contentwrapper').addClass('start');
		$('#freq_profiling').addClass('active');

		$("#s1").addClass('active');
		$("#w1").addClass('active');
		barcolor = '#1f77b4';
		anchor = '#chart0';
	};

	var readInputFiles = function(){

		datamanager = DiscourseAnalysis.Datamanager;
		datamanager.init(300);

	};

	var generateView = function(path){

		datamanager = DiscourseAnalysis.Datamanager;
		datamanager.init(300);
    
    	if ($(".viewselectorbutton.active").attr('id') == 's1') {
        	datamanager.readFile(path, function(data){ 
            	chartview.generateChartView(anchor, barcolor, data);
        	});
    	}
    	if ($(".viewselectorbutton.active").attr('id') == 's2') {
        	datamanager.readFile(path, function(data){ 
            	wordcloudview.generateCloud(data, anchor);
        	});
    	}
    	if ($(".viewselectorbutton.active").attr('id') == 's6') {
        	$("#s5").addClass('unable').css("pointer-events", "none");
        	$(anchor).append('<h3 class="tableheading">Quelldatei: ' + path + '</h3>')
        	$(anchor).append('<table id="' + anchor.slice(1) + '_table' + '" class="table table-striped"><tr><th>Rang</th><th>Token</th><th>Wert</th></tr></table>');
        	datamanager.readFile(path, function(data){ 
            	tableview.init(data, anchor + '_table');
        	});
        	return;
    	}
    	if ($(".viewselectorbutton.active").attr('id') == 's3') {
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

	/*$( window ).resize(function() {
    	$(that).trigger("reload");
	});*/

	that.init = init;
	that.generateView = generateView;
	that.readInputFiles = readInputFiles;
	that.clearChart = clearChart;
	return that;
};